from ursina import Entity, color, held_keys, Vec3, time
from users.characters import character_kits
from users.perks import PERKS
from users.status_effects import status_effect_types
from weapons.weapon_loader import weapon_library

class Player(Entity):
    def __init__(self, name, character_key, perk_key, game_state, use_cowboy_model=False):
        super().__init__()

        self.name = name
        self.character_key = character_key
        self.perk_key = perk_key
        self.character = character_kits[character_key]
        self.perk = PERKS[perk_key]
        self.game_state = game_state

        # Base stats
        self.base_health = self.character['base_health']
        self.max_health = self.base_health  # Can be modified later by perks, consumables, etc.
        self.health = self.max_health
        self.speed = self.character['speed']
        self.jump_height = 0.35
        self.gravity = 1.2
        self.vertical_velocity = 0
        self.grounded = True
        self.score = 0
        self.loadout = self.character['loadout']
        self.active_status_effects = {}

        # Sprint and crouch modifiers
        self.sprint_multiplier = 1.5
        self.crouch_multiplier = 0.5
        self.is_crouching = False

        # Weapon inventory and selection
        self.weapon_inventory = [weapon_library.get(w, weapon_library['pistol']) for w in self.loadout]
        self.active_weapon_index = 0
        self.weapon = self.weapon_inventory[self.active_weapon_index]

        # Default perk-related attributes
        self.can_repair = False
        self.can_steal = False
        self.can_heal_self = False
        self.can_heal_others = False
        self.weapon_restriction = None
        self.economy_bonus = 0
        self.loot_bonus = 0
        self.weapon_range_bonus = 0
        self.weapon_ammo_bonus = 0
        self.combat_penalty = 0

        self.apply_perk_effects()

        # Respawn tracking
        self.is_respawning = False
        self.respawn_time_remaining = 0
        self.respawn_delay = 5

        # Cowboy model override
        if use_cowboy_model:
            self.model = 'models/cowboy_lowpoly'
            self.color = color.orange
            self.scale = 1
            self.position = (0, 0, 0)

        try:
            self.model = 'models/cowboy_lowpoly'
        except Exception as e:
            print(f"Failed to load cowboy model: {e}, using cube instead.")
            self.model = 'cube'
            self.color = color.orange

    def switch_weapon(self, index):
        if 0 <= index < len(self.weapon_inventory):
            self.active_weapon_index = index
            self.weapon = self.weapon_inventory[index]
            print(f"{self.name} switched to {self.weapon.name}")

    def apply_perk_effects(self):
        if 'health_bonus' in self.perk:
            self.max_health += self.perk['health_bonus']
        if 'health_penalty' in self.perk:
            self.max_health -= self.perk['health_penalty']

        # Clamp current health to new max
        self.health = min(self.health, self.max_health)

        if 'speed_bonus' in self.perk:
            self.speed += self.perk['speed_bonus']
        if 'speed_penalty' in self.perk:
            self.speed -= self.perk['speed_penalty']

        self.can_repair = self.perk.get('can_repair', False)
        self.can_steal = self.perk.get('can_steal', False)
        self.can_heal_self = self.perk.get('can_heal_self', False)
        self.can_heal_others = self.perk.get('can_heal_others', False)
        self.weapon_restriction = self.perk.get('weapon_restriction', None)

        self.economy_bonus = self.perk.get('economy_bonus', 0)
        self.loot_bonus = self.perk.get('loot_bonus', 0)
        self.weapon_range_bonus = self.perk.get('weapon_range_bonus', 0)
        self.weapon_ammo_bonus = self.perk.get('weapon_ammo_bonus', 0)
        self.combat_penalty = self.perk.get('combat_penalty', 0)

    def apply_status_effect(self, effect_key):
        if effect_key not in status_effect_types:
            print(f"Unknown status effect: {effect_key}")
            return
        effect = status_effect_types[effect_key]
        self.active_status_effects[effect_key] = effect['duration']
        print(f"{self.name} afflicted with {effect['name']} for {effect['duration']}s")

    def update_status_effects(self, dt):
        expired = []
        for effect_key in self.active_status_effects:
            self.active_status_effects[effect_key] -= dt
            if self.active_status_effects[effect_key] <= 0:
                expired.append(effect_key)
        for key in expired:
            del self.active_status_effects[key]
            print(f"{self.name} no longer affected by {status_effect_types[key]['name']}")

    def take_damage(self, amount, source=None):
        if self.is_respawning or self.health <= 0:
            return

        self.health -= amount
        self.last_damaged_by = source.name if source else "Unknown"
        print(f"{self.name} took {amount} damage from {self.last_damaged_by}. Health now {self.health}.")

        if self.health <= 0:
            print(f"{self.name} is down. Respawn in {self.respawn_delay}s.")
            self.is_respawning = True
            self.respawn_time_remaining = self.respawn_delay

    def respawn(self):
        print(f"{self.name} has respawned.")
        self.health = self.max_health
        self.position = Vec3(0, 0, 0)  # Replace with spawn logic
        for weapon in self.weapon_inventory:
            weapon.ammo = weapon.ammo_capacity
        self.is_respawning = False
        self.last_damaged_by = None

    def update(self):
        if self.is_respawning:
            self.respawn_time_remaining -= time.dt
            if self.respawn_time_remaining <= 0:
                self.respawn()
            return

        # Fire weapon on left click
        if held_keys['left mouse']:
            self.weapon.fire()

        # Start reload on 'R'
        if held_keys['r']:
            self.weapon.start_reload()

        # Process reload timer
        self.weapon.update_reload()
