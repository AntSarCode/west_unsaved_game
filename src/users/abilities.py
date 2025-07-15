from users.status_effects import status_effect_types

def use_ability_effect(player, ability_name):
    character = player.character
    ability_key = character.get(ability_name)
    if not ability_key:
        print(f"No {ability_name} defined for {player.name}")
        return

    # Simple switchboard for known abilities
    if ability_key == "Echo Slam":
        echo_slam(player)
    elif ability_key == "Forsaken Might":
        forsaken_might(player)
    elif ability_key == "Spirit Reclamation":
        spirit_reclamation(player)
    else:
        print(f"{player.name} used {ability_key}, but no handler is defined.")


def echo_slam(player):
    print(f"{player.name} slams the ground! Applying 'Slow' to nearby enemies.")
    for target in player.game_state.get_nearby_players(player, radius=7):
        target.apply_status_effect("slow")
    player.game_state.apply_team_buff(player, buff_type="damage", value=0.15, duration=3)


def forsaken_might(player):
    print(f"{player.name} channels Forsaken Might!")
    player.apply_status_effect("weaken")  # Assuming self-risks
    player.speed *= 0.9
    player.health += 25


def spirit_reclamation(player):
    print(f"{player.name} transforms into GIANT FORM!")
    player.scale *= 4
    player.health += 100
    player.apply_status_effect("stun")  # AoE exit effect
