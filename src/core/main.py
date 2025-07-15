from ursina import *
from users.player import Player
from core.engine.game_state import GameState
from core.engine.phases import PhaseState
from utils.debug_overlay import DebugOverlay
from utils.match_logger import log_game_state_event
from config.metrics.constants import MAX_PLAYERS
from config.metrics.map_loader import MAP_NODES
from ui.overlays import OverlayManager
from ui.HUD import HUD
from dotenv import load_dotenv
load_dotenv()

# Combat imports moved below to avoid circular import

def run_game():
    from panda3d.core import loadPrcFileData
    loadPrcFileData('', 'win-size 1152 720')

    # Engine Launch
    app = Ursina()

    # UI Cleanup
    mouse.locked = True
    window.fps_counter.enabled = False

    game_state = GameState()
    phase_state = PhaseState()
    debug_overlay = DebugOverlay()
    overlay_manager = OverlayManager()

    ### --- Basic environment setup --- ###

    # Grid debug toggleable helpers
    grid_entities = []
    show_debug_grid = [False]  # mutable toggle wrapper

    def toggle_debug_grid():
        if show_debug_grid[0]:
            for g in grid_entities:
                destroy(g)
            grid_entities.clear()
        else:
            for x in range(-60, 61, 5):
                for z in range(-60, 61, 5):
                    marker = Entity(
                        model='cube',
                        scale=(0.25, 0.25, 0.25),
                        position=(x, 0.01, z),
                        color=color.white33,
                        enabled=True
                    )
                    grid_entities.append(marker)
        show_debug_grid[0] = not show_debug_grid[0]

    # Load map configuration & nodes (zone titles)
    for node in MAP_NODES:
        color_map = {
            'control': color.azure,
            'boss': color.red,
            'loot': color.orange,
            'objective': color.green
        }

        Entity(
            model='cube',
            scale=(3, 1, 3),
            position=(node['x'], 0, node['y']),
            color=color_map.get(node['type'], color.gray),
            collider='box'
        )
        Text(
            text=node['name'],
            position=(node['x'], 3.5, node['y']),
            origin=(0, 0),
            scale=1.25,
            color=color.white
        )

    # Skybox
    Sky()

    # Ground
    Entity(
        model='plane',
        scale=(120, 1, 120),
        color=color.brown,
        collider='box'
    )

    ## -- Basic structures -- ##
    # Saloon
    Entity(
        model='assets/models/map/saloon.glb',
        scale=1.6,
        position=(12, 0, -6),
        collider='mesh'
    )
    # Ruins
    Entity(
        model='assets/models/map/ruins.glb',
        scale=1.3,
        position=(-18, 0, 6),
        collider='mesh'
    )
    # AI User Entities
    Entity(
        model='assets/models/ai_users/ghoul.glb',
        position=(0, 0, 0),
        scale=1.8,
        collider='mesh'
    )

    # Lighting
    AmbientLight(color=color.rgba(200, 200, 200, 0.5))
    DirectionalLight().look_at(Vec3(1, -1, -1))

    # Player Models
    cowboy_player = Player(
        name="Frosty",
        character_key="Taydon 'Frosty' Stack",
        perk_key="Deadeye",
        game_state=game_state,
        use_cowboy_model=True,
        position=(0, 1, 0)
    )

    players = [cowboy_player] + [
        Player(f'Player{i+1}', "Taydon 'Frosty' Stack",
               'Deadeye',
               game_state,
               use_cowboy_model=True,
               position=(i * 2, 1, -5)
        )
        for i in range(MAX_PLAYERS - 1)
    ]

    # HUD instance for main player
    hud = HUD()
    hud.show()

    # Disable dev camera unless toggled
    editor_camera = EditorCamera(rotation_speed=100, panning_speed=5)
    editor_camera.enabled = False

    # Player Camera
    camera.parent = cowboy_player
    camera.position = Vec3(0, 1.6, 0)
    camera.rotation = (0, 0, 0)

    # Main game loop update function
    def update():
        for player in players:
            player.update()

        for victim in players:
            if victim.health <= 0 and not victim.is_respawning:
                killer_name = getattr(victim, 'last_damaged_by', 'Unknown')
                overlay_manager.add_kill_feed(killer_name, victim.name)
                victim.is_respawning = True
                victim.respawn_time_remaining = victim.respawn_delay

        overlay_manager.update_kill_feed_positions()
        phase_state.tick()
        current_phase = phase_state.describe_current_phase()
        debug_overlay.update(players=len(players), phase=current_phase)

        if cowboy_player.weapon:
            hud.update_ammo(
                cowboy_player.weapon.ammo,
                cowboy_player.weapon.ammo_capacity,
                cowboy_player.weapon.reserve_ammo
            )
            hud.update_weapon_name(cowboy_player.weapon.name)

        alive_players = [p for p in players if p.health > 0 and not p.is_respawning]
        if len(alive_players) == 1:
            print(f'{alive_players[0].name} wins!')
            log_game_state_event("match_end", {"winner": alive_players[0].name})
            application.quit()

    window.update = update

    def handle_input(key):
        from utils.combat_utils import apply_damage, calculate_damage, apply_on_hit_effects
        if key == 'f1':
            debug_overlay.toggle()
        elif key in ('1', '2', '3'):
            cowboy_player.switch_weapon(int(key) - 1)
            hud.update_weapon_name(cowboy_player.weapon.name)
        elif key == 't':
            target = players[1] if len(players) > 1 else None
            if target:
                damage = calculate_damage(cowboy_player, target, cowboy_player.weapon.name.lower())
                apply_damage(cowboy_player, target, damage)
                apply_on_hit_effects(target, cowboy_player.weapon.name.lower())
        elif key == 'v':
            toggle_debug_grid()
            editor_camera.enabled = not editor_camera.enabled
            if editor_camera.enabled:
                camera.parent = scene
            else:
                camera.parent = cowboy_player
                camera.position = Vec3(0, 1.6, 0)
                camera.rotation = (0, 0, 0)

    window.input = handle_input

    app.run()
