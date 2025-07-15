from .weapons import Weapon, weapon_types
from .weapon_loader import weapon_library
from src.core.engine.combat import (
    calculate_damage,
    apply_damage,
    apply_on_hit_effects
)

__all__ = [
    "Weapon",
    "weapon_types",
    "weapon_library",
    "calculate_damage",
    "apply_damage",
    "apply_on_hit_effects"
]