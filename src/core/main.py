from ursina import *
from src.users.player import Player
from src.core.engine.game_state import GameState
from src.core.engine.phases import PhaseState
from src.utils.debug_overlay import DebugOverlay
from src.utils.match_logger import log_game_state_event
from src.config.metrics.constants import MAX_PLAYERS
from ui.overlays import OverlayManager
from ui.HUD import HUD
from src.core.engine.combat import apply_damage, calculate_damage, apply_on_hit_effects

app = Ursina()
game_state = GameState()
phase_state = PhaseState()
debug_overlay = DebugOverlay()
overlay_manager = OverlayManager()

# Basic environment setup
Entity(model='assets/models/dirt_floor_tile.glb',
    scale=10,  # adjust to match world size
    position=(0, -1, 0),
    collider='mesh'
)

Entity(
    model='wireframe_cube',
    color=color.white,
    position=(0, 0, 0), scale=1.5)

DirectionalLight().look_at(Vec3(1, -1, -1))

# Add cowboy player with model fallback
cowboy_player = Player(
    name="Frosty",
    character_key="Taydon 'Frosty' Stack",
    perk_key="Deadeye",
    game_state=game_state,
    use_cowboy_model=True
)

players = [cowboy_player] + [
    Player(f'Player{i+1}', 'Frosty', 'Deadeye', game_state, use_cowboy_model=True)
    for i in range(MAX_PLAYERS - 1)
]

# HUD instance for main player
hud = HUD()
hud.show()

# Optional: Camera positioning
camera.position = (0, 10, -30)
camera.look_at(cowboy_player)

# Optional: Movement controller (1st-person style)
editor_camera = EditorCamera(rotation_speed=100, panning_speed=5)

def update():
    for player in players:
        player.update()

    # Detect and process downed players
    for victim in players:
        if victim.health <= 0 and not victim.is_respawning:
            killer_name = getattr(victim, 'last_damaged_by', 'Unknown')
            overlay_manager.add_kill_feed(killer_name, victim.name)
            victim.is_respawning = True
            victim.respawn_time_remaining = victim.respawn_delay

    overlay_manager.update_kill_feed_positions()

    # Phase and UI updates
    phase_state.tick()
    current_phase = phase_state.describe_current_phase()
    debug_overlay.update(players=len(players), phase=current_phase)

    # HUD ammo & weapon update
    if cowboy_player.weapon:
        hud.update_ammo(
            cowboy_player.weapon.ammo,
            cowboy_player.weapon.ammo_capacity,
            cowboy_player.weapon.reserve_ammo
        )
        hud.update_weapon_name(cowboy_player.weapon.name)

    # End match if only one non-respawning player remains
    alive_players = [p for p in players if p.health > 0 and not p.is_respawning]
    if len(alive_players) == 1:
        print(f'{alive_players[0].name} wins!')
        log_game_state_event("match_end", {"winner": alive_players[0].name})
        application.quit()

def handle_input(key):
    if key == 'f1':
        debug_overlay.toggle()
    elif key in ('1', '2', '3'):
        cowboy_player.switch_weapon(int(key) - 1)
        hud.update_weapon_name(cowboy_player.weapon.name)
    elif key == 't':
        # Simulate damage test
        target = players[1] if len(players) > 1 else None
        if target:
            damage = calculate_damage(cowboy_player, target, cowboy_player.weapon.name.lower())
            apply_damage(cowboy_player, target, damage)
            apply_on_hit_effects(target, cowboy_player.weapon.name.lower())

window.input = handle_input

camera.position = (0, 2, -5)
camera.look_at((0, 1, 0))

app.run()
