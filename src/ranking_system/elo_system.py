from typing import Dict, List

# Constants
BASE_ELO = 1000
K_FACTOR = 32
IN_GAME_WEIGHT = 0.8
PLACEMENT_WEIGHT = 0.15
SOLO_BONUS = 0.05  # Extra value added if player is solo (not in an alliance)

def expected_score(player_elo: float, opponent_avg_elo: float) -> float:
    return 1 / (1 + 10 ** ((opponent_avg_elo - player_elo) / 400))

def update_elo(current_elo: int, expected: float, actual: float) -> int:
    return round(current_elo + K_FACTOR * (actual - expected))

def apply_individual_match_results(
    player_team_map: Dict[str, int],  # player_id -> team number (e.g., 1 or 2)
    team_elos: Dict[int, float],      # team number -> average team Elo
    elos: Dict[str, int],
    winning_team: int,
    in_game_scores: Dict[str, int],
    placements: Dict[str, int],
    solo_players: List[str]
) -> Dict[str, int]:
    """
    Updates Elo ratings for all individual players based on match performance.
    Adds a slight bonus for solo players not in any alliance.
    """
    max_score = max(in_game_scores.values()) if in_game_scores else 1

    for player, current_elo in elos.items():
        team = player_team_map.get(player)
        opponent_teams = [t for t in team_elos if t != team]
        opponent_avg_elo = sum([team_elos[t] for t in opponent_teams]) / len(opponent_teams)

        expected = expected_score(current_elo, opponent_avg_elo)

        placement_rank = placements.get(player, 10)
        score_value = in_game_scores.get(player, 0) / max_score
        placement_value = 1 / placement_rank if placement_rank > 0 else 0

        weighted_score = (
            score_value * IN_GAME_WEIGHT +
            placement_value * PLACEMENT_WEIGHT
        )

        if player in solo_players:
            weighted_score *= 1 + SOLO_BONUS

        actual_result = 1.0 if team == winning_team else 0.0
        if winning_team == 0:
            actual_result = 0.5

        combined_actual = (weighted_score + actual_result) / 2
        elos[player] = update_elo(current_elo, expected, combined_actual)

    return elos
