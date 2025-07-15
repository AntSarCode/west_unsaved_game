from abc import ABC, abstractmethod
from typing import Protocol, Tuple, List
from enum import Enum

# For systems that rely on lifecycle hooks: update(), apply(), etc.
class Updatable(Protocol):
    def update(self, delta_time: float) -> None:
        ...

class Damageable(ABC):
    @abstractmethod
    def take_damage(self, amount: float, source: str = "") -> None:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass

class HasPosition(ABC):
    @abstractmethod
    def get_position(self) -> Tuple[float, float, float]:
        pass

class StatusEffectApplier(Protocol):
    def apply_effect(self, effect_type: Enum, duration: float, source: str = "") -> None:
        ...

class EffectHost(ABC):
    active_effects: List[Enum]

    @abstractmethod
    def clear_expired_effects(self) -> None:
        pass

    @abstractmethod
    def has_effect(self, effect: Enum) -> bool:
        pass

    @abstractmethod
    def remove_effect(self, effect: Enum) -> None:
        pass
