from users.status_effects import status_effect_types

CHARACTERS = {
    # All character definitions remain unchanged...
}

# --- Step 1: Validate abilities against status_effect_types ---
def validate_status_effects():
    invalid_references = []
    for name, data in CHARACTERS.items():
        for ability_key in ["ability_1", "ability_2", "passive", "ultimate"]:
            ability = data.get(ability_key, {})
            for key, value in ability.items():
                if isinstance(value, str) and value.lower() in status_effect_types:
                    continue
                if key in ["applies", "inflicts", "effect"] and isinstance(value, str):
                    if value.lower() not in status_effect_types:
                        invalid_references.append((name, ability_key, value))
    return invalid_references

# --- Step 2: Nickname Index ---
NICKNAME_INDEX = {
    # Format: "Nickname": "Full Character Key"
    "Mama B": "Braizie 'Mama B' Stack",
    "The Kid": "Bonnie 'The Kid' Mathers",
    "Princess": "Jillian 'Princess' Reese",
    "Trailblazer": "Edwin 'Trailblazer' Horton",
    "Banished": "Clogade the Banished",
    "Forsaken": "Forsaken Cain",
    "Chief": "Rowan 'Chief' WhiteCloud",
    "BloodChug": "Zeke-Ray 'BloodChug' Coffin",
    "E-12": "Eli 'E-12' Revenant",
    "Frosty": "Taydon 'Frosty' Stack",
    "Brother Dave": "Brother Dave",
    "Siren Serpent": "Alaina 'Siren Serpent' Mavinidis",
    "Pyro": "Pico The Pyro",
    "Trey Card": "Willy 'Trey Card' Monty",
    "Prophet": "Olexsian Prophet",
    "Beast Tamer": "Xiao 'Beast Tamer' Chen",
    "Thumping Heart": "Thumping Heart",
    "Reverend Piper": "Reverend Piper",
    "Full Moon": "Harmony 'Full Moon' King",
    "The Kid's Sidekick": "Bonnie Pistols",
    "Baby Jack": "Jillian 'Peach' Reese's sidekick",
    "Winry": "Braizie 'Mama B' Stack's sidekick",
    "Liam": "Harmony 'Full Moon' King's sidekick",
    "Jack": "Jillian 'Peach' Reese's sidekick"
}


# Character Stats
BASE_HEALTH = 150
BASE_SPEED = 5

character_kits = {
    'The Kid': {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Bonnie Pistols', 'Flash Grenades', 'Hunting Knife'],
        'ability_1': 'Quick Draw',
            'ability_1_desc': 'The Kid\'s first shot after reloading deals 25% more damage. If the shot is a headshot, it deals 50% more damage.',
            'ability_1_cooldown': 0, # passive
        'ability_2': 'Snake In The Grass',
            'ability_2_desc': 'When in an alliance at least one other player, The Kid gains life-steal equal to 10% of damage dealt to enemy players. This ability can only be activated when The Kid is not the last player alive on his team.',
            'ability_2_cooldown': 15, # seconds
        'ultimate': 'Revenge',
            'ultimate_voice_line': "Es demasiado tarde para ti.",
            'ultimate_desc': 'The Kid\'s weapon speed is increased by 50%, and he does not lose ammo or need to reload.',
            'ultimate_duration': 7,
            'ultimate_cooldown': 80
    },
    "Jillian 'Peach' Reese": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Repeater Rifle', 'Throwing Knife','Baby Jack (sidekick)'],
        'ability_1': 'Quick Slide',
            'ability_1_desc': 'Jillian can slide for a short distance in any direction, dodging incoming fire and gaining a speed boost for 3 seconds.',
            'ability_1_cooldown': 15,
        'ability_2': 'Jack\'s Call',
            'ability_2_desc': 'Jillian can assume control of Baby Jack. When Baby Jack detects an enemy, they are marked for 5 seconds. Jillian can see the marked enemies through walls.',
            'ability_2_duration': 6,
            'ability_2_cooldown': 30,
        'ultimate': 'Jack and Jillian',
            'ultimate_voice_line': "No more games, Jack!",
            'ultimate_desc': 'Jillian summons Baby Jack, who automatically fires at all enemies within 20 feet. Jack fires one shot every half second, and deals 10 damage per hit. Jillian gains a 20% damage boost while Jack is active.',
            'ultimate_cooldown': 90
    },
    'Forsaken Cain': {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Betrayer', 'Buckshot', 'Hammerfist'],
        'ability_1': 'Obliterate',
            'ability_1_desc': 'Cain can rapidly thrust forward 10 feet. He is invulnerable while thrusting. If his thrust hits an enemy player, they are stunned for 3 seconds. After thrusting, Cain can only melee (HammerFist) for 3 seconds.',
            'ability_1_cooldown': 15,
        'ability_2': 'Betrayer\'s Mark',
            'ability_2_desc': 'If Cain\'s alliance is broken, he has 3 seconds to activate this ability. If he does, he gains a 25% damage boost. For every enemy player Cain kills while ability is active, he gains an additional 10% health for the remainder of that life.',
            'ability_2_duration': 10,
            'ability_2_cooldown': 30,
        'ultimate': 'Twisting The Knife',
            'ultimate_voice_line': "Loyalty was always your weakness.",
            'ultimate_desc': 'Cain absorbs 50 health from all players in enemy alliances within 25 feet. All absorbed health is converted to over-health.',
            'ultimate_duration': 10,
            'ultimate_cooldown': 90
    },
    "Rowan 'Chief' WhiteCloud": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Spirit Rifle', 'Totem of Wind', 'Dreamcatcher'],
        'ability_1': 'Totemic Uplift',
            'ability_1_desc': 'Places a totem that heals himself and all allies in its radius.',
            'ability_1_duration': 6,
            'ability_1_cooldown': 22,
        'ability_2': 'Wind Step',
            'ability_2_desc': 'Rowan leaps high into the air, and can glide to an area within 30 feet. Dreamcatcher absorbs all damage taken while airborne, and grants Rowan over-health equal 20% of the damage absorbed.',
            'ability_2_cooldown': 20,
        'ultimate': 'Calling the Sky',
            'ultimate_voice_line': "The spirits lay you to rest.",
            'ultimate_desc': 'Player selects an area. An eagle-shaped energy storm rains down, dealing 50 AoE dps to any enemies.',
            'ultimate_duration': 8,
            'ultimate_cooldown': 90
    },
    "Zeke-Ray 'BloodChug' Coffin": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Poison Revolver', 'Poison Drone Mine', 'Sledge Clouder'],
        'ability_1': 'Chug',
            'ability_1_desc': "Zeke drinks from canteen and gains a 'poison damage stack'. For each stack gained, poison effects on enemy players increase by 4% (20 stacks maximum). This ability can be used while moving, but Zeke cannot shoot or use abilities while drinking. Stacks are reset upon respawn.",
            'ability_1_cooldown': 8,
        'ability_2': 'Mine Heist',
            'ability_2_desc': 'If Zeke uses this ability while controlling on a Poison Drone Mine, instead of dealing the damage the drone will steal an enemy player primary weapon. Zeke can use the stolen weapon while the ability is active. The stolen weapon will be returned to the enemy player if Zeke dies or the ability ends.',
            'ability_2_duration': 15,
            'ability_2_cooldown': 26,
        'ultimate': 'Clouder Rage Shout',
            'ultimate_voice_line': "FUCK YOU!",
            'ultimate_desc': 'Zeke slams the ground with his Sledge Clouder creating a spiraling 25 meter shockwave in the direction Zeke is facing. Any character hit by the wave takes 125 damage and a 20 meter knock-back.',
            'ultimate_duration': 5,
            'ultimate_cooldown': 90
    },
    "Eli 'E-12' Revenant": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Chain Harpoon, Dual Rapiers, Recall Knife'],
        'ability_1': 'Agile Anger',
        'ability_1_desc': "Eli flickers forward and backward rapidly, avoiding all bullets and projectiles. Afterwards, his Rapiers gain a temporary 30% damage boost. Eli cannot use weapons while in flicker.",
        'ability_1_flicker_duration': 1.5,
        'ability_1_rapier_boost_duration': 3,
        'ability_1_cooldown': 12,
        'ability_2': 'Age Old Curse',
        'ability_2_desc': "Eli activates his watch triggering the 'Slow' status effect on all enemies withing 10 meters. Enemies in alliances within 10 meters are affected 150%.",
        'ability_2_duration': 3,
        'ability_2_cooldown': 25,
        'ultimate': 'Immortal Patience',
        'ultimate_voice_line': "I've got all the time in the world.",
        'ultimate_desc': 'Eli becomes invulnerable, and gains a 100% damage boost. While ultimate is active, Eli can only use his Recall Knife, but without cooldowns.',
        'ultimate_duration': 7,
        'ultimate_cooldown': 90
    },
    "Taydon 'Frosty' Stack":{
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Frostbite Rifle', 'Subzero Shotgun', 'Ice Pick'],
        'ability_1': 'Cold and Calculated',
            'ability_1_desc': "Taydon gains a 15% speed increase and does not lose ammo or need to reload. Damage to enemies while the ability is active applies the 'Marked' effect.",
            'ability_1_duration': 3,
            'ability_1_cooldown': 13,
        'ability_2': 'Chill Out',
            'ability_2_desc': 'Taydon can fluidly slide up to 7 meters (including on walls) in the direction he aims, applying the "Freeze" status effect to all enemies he contacts. Taydon is invulnerable to weapons, but not abilities, while sliding.',
            'ability_2_cooldown': 23,
        'ultimate': 'Blizzard',
            'ultimate_voice_line': "My only wish is I die real.",
            'ultimate_desc': "Taydon creates a blizzard in a 10 meter radius around himself. The blizzard applies the 'Freeze' status effect to all enemies and an additional 10 dps. If Taydon is killed while ultimate is active, he is revived with 100% health and a temporary 20% damage boost.",
            'ultimate_duration': 5,
            'ultimate_damage_boost_duration': 5,
            'ultimate_cooldown': 90
    },
    "Braizie 'Mama B' Stack": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Bouquet Staff', 'Spinning Kick', "'Winry' Voodoo Doll (sidekick)"],
        'ability_1': 'Flower Flame',
            'ability_1_desc': "Braizie fires the entire bouquet from the tip of her staff. Bouquet explodes on impact, dealing 50 damage and applying the 'Fear' status effect to all enemies within 5 meters. The explosion also heals Braizie for 20% of the damage dealt.",
            'ability_1_cooldown': 12,
        'ability_2': 'Winry\'s Trap',
            'ability_2_desc': "Braizie can place Winry on the ground. If an enemy player steps on Winry, it applies the 'Stun' status effect and deals 50 damage. Braizie can also activate Winry to heal herself for 30 health. Winry returns to Braizie after ability deactivates.",
            'ability_2_duration': 5,
            'ability_2_cooldown': 5,
        'ultimate': 'Winry\'s World',
            'ultimate_voice_line': "Get 'em baby!",
            'ultimate_desc': "Braizie summons 5 Winry dolls that automatically seek out the nearest enemy players and explode. Each Winry deals 40 damage and applies the 'Fear' status effect.",
            'ultimate_duration': 10,
            'ultimate_cooldown': 90
    },
    "Brother Dave": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Cursed Shotgun', 'Jolly Roger Hat', 'Gallows Blade'],
        'ability_1': 'Medal of Valor',
            'ability_1_desc': "While wearing the Jolly Roger Hat, Brother Dave can throw his Medal of Valor up to 25 meters at an enemy player. If the enemy player is hit, the player takes 25 damage the 'Stun' status effect is applied. If the enemy player is not hit, the medal returns to Brother Dave.",
            'ability_1_cooldown': 9,
        'ability_2': 'Down Bad Dave',
            'ability_2_desc': "Brother Dave loses his Cursed Shotgun while ability is active. In exchange, his Gallows Blade gains a 25% damage boost and he gains a 10% speed boost. For every player Brother Dave kills while ability is active, he gains an additional 10% health.",
            'ability_2_duration': 9,
            'ability_2_cooldown': 4,
        'ultimate': 'Davy Jones\'s Locker',
            'ultimate_voice_line': "To the depths...",
            'ultimate_desc': "If within 3 meters of an enemy player, Brother Dave can activate his ultimate to become invulnerable while pulling the enemy player into a ghostly locker. Invulnerability ends when the enemy is closed into the locker. While inside the locker, enemy player takes 25 dps. If enemy player is in an alliance, his teammates can free them by killing Brother Dave.",
            'ultimate_duration': 20,
            'ultimate_cooldown': 80
    },
    "Alaina 'Siren Serpent' Mavinidis":{
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Serpent Rifle','Siren Harp', 'Siren\'s Call'],
        'ability_1': 'Dreadful Melody',
            'ability_1_desc': "Alaina plays a haunting melody with her Siren Harp that applies the 'Poison' status effect to all enemies within 10 meters. The 'Slow' status effect is also applied to enemy players in alliances.",
            'ability_1_duration': 4,
            'ability_1_cooldown': 16,
        'ability_2': 'Serpent Strike',
            'ability_2_desc': "Alaina coils her body then lunges forward 10 meters. Upon landing, she creates a 5 meter radius poison cloud that deals 25 damage applies the 'Poison' status effect to all enemies in radius. Enemy players hit are also knocked back 3 meters. Teammates in radius are cleansed of all status effects.",
            'ability_2_duration': 3,
            'ability_2_cooldown': 20,
        'ultimate': "The Depths\' Calling",
            'ultimate_voice_line': "Do, re, mi, fa, so, down, you, go.",
            'ultimate_desc': "While moving at 50% BASE_SPEED, Alaina can activate a siren call covering a 25 meter radius around her. All enemy players within the radius are pulled towards Alaina and take the 'Stun' status effect. Alaina's teammates are cleansed of all status effects, granted 20% over-health and 15% speed boost while ability is active.",
            'ultimate_duration': 6,
            'ultimate_cooldown': 90
    },
    "Pico The Pyro":{
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Flame Shotgun','Blast Boots', 'Molotov Cocktail'],
        'ability_1': 'Tasmanian Devil',
            'ability_1_desc': "Pico rapidly dashes backwards 10 meters leaving a trail of fire which applies the 'Burn' status effect if touched by an enemy. After dashing, he gains a 15% speed boost. If Pico collides with an enemy player while dashing, the 'Burn' status effect is applied.",
            'ability_1_duration': 2.5,
            'ability_1_speed_boost_duration': 3,
            'ability_1_cooldown': 22,
        'ability_2': 'Whirling Dervish',
            'ability_2_desc': "Pico spins around rapidly, creating a fiery whirlwind that applies the 'Burn' status effect and 20 damage to all enemies within 5 meters. The whirlwind also knocks back enemies and cleanses teammates of all status effects.",
            'ability_2_duration': 3,
            'ability_2_cooldown': 24,
        'ultimate': "Fireball Focus",
            'ultimate_voice_line': "Let's step it up a notch!",
            'ultimate_desc': "Pico drinks a shot of Fireball Whiskey, giving unlimited energy to his blast boots for the duration and 5 additional Molotov Cocktails. Pico's speed is increased by 20% for the duration.",
            'ultimate_duration': 7,
            'ultimate_cooldown': 90
    },
    "Willy 'Trey Card' Monty": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Card Gun', 'Smoke Shot', 'Willy\'s Lasso'],
        'ability_1': 'Card Trick',
            'ability_1_desc': "Willy throws a projectile card that applies the 'Bleed' status effect to all enemies hit. The card applies the 'Stun' status effect to the first enemy player hit. If the card hits a teammate, they are granted a temporary 15% speed boost.",
            'ability_1_duration': 4,
            'ability_1_speed_boost_duration': 3,
            'ability_1_cooldown': 14,
        'ability_2': 'Sleight of Hand',
            'ability_2_desc': "Willy's Card gun does not lose ammo or need to reload, and fire rate is increased by 25% while ability is active.",
            'ability_2_duration': 6,
            'ability_2_cooldown': 23,
        'ultimate': 'Deck of Fate',
            'ultimate_voice_line': "Let\'s see what fate has in store for you.",
            'ultimate_desc': "Willy draws a card from his Deck of Cards. The card can either heal Willy to full health, apply the 'Marked' status effect to all enemy players within a 20 meter radius, or deal 75 damage to all enemies within a 10 meter radius.",
            'ultimate_duration': 5,
            'ultimate_cooldown': 90
    },
    "Olexsian Prophet":{
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Prophet\'s Cane Gun', 'Hypno-mirror', 'Glass Eye'],
        'ability_1': 'Candy Cane',
            'ability_1_desc': "Olexsa swings cane in a wide arc, dealing 30 damage to all enemies and 15 healing to all teammates within 5 meters in front of him. If an enemy player is hit, they are knocked back 3 meters and apply the 'Bleed' status effect.",
            'ability_1_cooldown': 13,
        'ability_2': 'Mirror Madness',
            'ability_2_desc': "This ability can be activated when Olexsa has >= 50 'Hypno-mirror stacks'. While ability is active, the Hypno-mirror absorbs and reflects all damage from an enemy alliance to every player within that alliance.",
            'ability_2_duration': 4,
            'ability_2_cooldown': 29,
        'ultimate': 'Primordial Vision',
            'ultimate_voice_line': "Your future is my past.",
            'ultimate_desc': "The Prophet gains a vision of all enemy players' locations for 10 seconds. The 'Marked' status effect is applied to all enemy players within a 20 meter radius of Olexsa.",
            'ultimate_vision_duration': 7,
            'ultimate_cooldown': 90
    },
    "Xiao 'Beast Tamer' Chen": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Dragon Revolver', 'Great Wall', 'Fan of Blades'],
        'ability_1': 'Fortify',
            'ability_1_desc': "While standing near or on her 'Great Wall', Xiao can activate this ability to cleanse all status effects and gain 30% damage resistance. Teammates gain 10% damage while on or near the Great Wall.",
            'ability_1_duration': 15,
            'ability_1_cooldown': 18, # may need adjustment
        'ability_2': 'Reverse Revolver',
            'ability_2_desc': "Xiao's revolver heals teammates for 25 health per shot while ability is active. She also gains 20% health for every shot landed on a teammate. If she has no teammates, activating this ability will heal her for 50 health. She does not lose ammo or need to reload while ability is active.",
            'ability_2_duration': 7,
            'ability_2_cooldown': 27,
        'ultimate': 'Dragon\'s Fury',
            'ultimate_voice_line': "Feel the flames of fury!", # Chinese translation needed
            'ultimate_desc': "Xiao summons a dragon spirit that ignites a 15-meter radius area around her. The flame radius moves does not move once placed. All enemies within the area take 45 dps and are set ablaze, applying the 'Burn' status effect. The dragon spirit also grants Xiao 20% damage resistance for the duration.",
            'ultimate_vision_duration': 7,
            'ultimate_cooldown': 90
    },
    "Thumping Heart": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Heartbreaker Rifle', 'Dreamy Drone', 'Heart Dagger'],
        'ability_1': 'Heart Pulse',
            'ability_1_desc': "Thumping Heart sends out a pulse that reveals all enemy players within 20 meters and heals all allies within 10 meters for 40 health.",
            'ability_1_duration': 2.5,
            'ability_1_cooldown': 18,
        'ability_2': 'Love Hurts',
            'ability_2_desc': "If ability is activated while using Dreamy Drone, the drone can place two mines which, if triggered, apply the 'Allure' status effect to all enemies within a 3 meter radius. Enemies are lured to the mine which then explodes, dealing 80 damage and applying the 'Marked' status effect.",
            'ability_2_mine_duration': 45,
            'ability_2_cooldown': 20,
        'ultimate': 'No Heart of Gold',
            'ultimate_voice_line': "You knew what this was, honey.",
            'ultimate_desc': "If Thumping Heart's alliance breaks for any reason, she has 3 seconds to activate her ultimate. If she does, all enemies within a 15 meter radius are allured and take 50 damage. Thumping Heart gains a 25% damage boost for the duration.",
            'ultimate_duration': 3.5,
            'ultimate_cooldown': 90
    },
    "Reverend Piper": {
        'base_health': BASE_HEALTH,
        'base_speed': BASE_SPEED,
        'loadout': ['Testament Rifle', 'Crucible Crucifix', 'Scripture'],

        'ability_1': 'Verse of Dread',
        'ability_1_desc': "Piper opens the Book of Spirits and chants a verse granting his Creed rifle a 20% increased fire rate. While ability is active, bullets fired by the Creed Rifle apply the 'Fear' status effect; bullets that hit teammates heal 25 health.",
        'ability_1_duration': 5,
        'ability_1_cooldown': 17,

        'ability_2': 'False Salvation',
        'ability_2_desc': "When a teammate breaks an alliance with Piper, he has 3 seconds to activate this ability. If he does, he gains 40 over-health and his Crucifix gains a 25% damage boost and has immediate recall for the duration.",
        'ability_2_option_duration': 3,
        'ability_2_duration': 6,
        'ability_2_cooldown': 29,

        'passive_1': 'Blood of The Lamb',
        'passive_1_desc': "All enemies affected by Fear or Allure effects are automatically marked for Piper for 6 seconds.",

        'ultimate': 'Exorcism Sermon',
        'ultimate_voice_line': "The everlasting CAGE!",
        'ultimate_desc': "Piper's health bar surges to 175%, but he cannot directionally move. He can only turn for the duration. Piper begins a fiery sermon that damages and echoes a 15 meter area he initially faces. Players within 5 meters are dealt 80 damage and are knocked back 10 meters. At the end of his ultimate, the 'Stun' effect is applied to all players within the 15 meter area after duration.",
        'ultimate_duration': 6,
        'ultimate_cooldown': 95
    },
    "Harmony 'Full Moon' King": {
        'base_health': BASE_HEALTH,
        'speed': 6,
        'loadout': ['Moonlight Bow', 'Lunar Shield', 'Liam (sidekick)'],
        'ability_1': 'Lunar Dash',
            'ability_1_desc': "Harmony or Liam can teleport behind the nearest enemy within 30 meters. If Harmony teleports, she remains silent if she does not damage enemies and must teleport back after duration. If Liam teleports, he gains a 15% damage boost for 5 seconds, but there is a sound cue.",
            'ability_1_duration': 12,
            'ability_1_cooldown': 13,
        'ability_2': 'Shield Bash',
            'ability_2_desc': "Harmony's Lunar Shield moves with her as she dashes forward 10 meters. If she hits an enemy player, they are knocked back 5 meters the 'Stun' effect is applied. If the shield touches a teammate, they are cleansed of all status effects and receive 20 temporary over-health. If Harmony's shield stuns an enemy while Liam is active, Liam gains 20% damage and speed boost for 5 seconds.",
            'ability_2_duration': 5,
            'ability_2_cooldown': 27,
        'ultimate': 'Lunar Harmony',
            'ultimate_voice_line': "*Wolf howl*",
            'ultimate_desc': "Harmony fires a powerful arrow that creates a 15 meter radius moonlight field. All enemies within the field take 30 dps and are slowed by 50%. Allies within the field gain a 20% speed boost and are cleansed of all status effects. While the field is active, Harmony's weapon speed is increased by 25%.",
            'ultimate_duration': 8,
            'ultimate_cooldown': 90
    },
    "Theo 'Prospector' Clayborne": {
        'base_health': BASE_HEALTH,
        'speed': BASE_SPEED,
        'loadout': ['Schematics', 'Prospector\'s Lantern', 'Prospector\'s Dynamite'],
        'ability_1': 'Prospector\'s Insight',
            'ability_1_desc': "Theo can place a Prospector's Lantern that reveals all enemy players within a 20 meter radius. The lantern also heals all allies within the radius for 30 health.",
            'ability_1_duration': 3,
            'ability_1_cooldown': 20,
        'ability_2': 'Dynamite Toss',
            'ability_2_desc': "Theo throws a stick of dynamite that explodes after 3 seconds, dealing 50 damage and applying the 'Burn' status effect to all enemies within a 7 meter radius. If the dynamite hits an enemy player, they are knocked back 5 meters. The dynamite can also destroy most enemy defenses.",
            'ability_2_duration': 3,
            'ability_2_cooldown': 14,
        'ultimate': 'Prospector\'s Bounty',
            'ultimate_voice_line': "There's gold in them there hills!",
            'ultimate_desc': "Theo can place a Prospector's Bounty that reveals all enemy players within a 30 meter radius. For every enemy player revealed, Theo receives 500 currency. The bounty also grants all allies within the radius a 20% damage boost and cleanses them of all status effects.",
            'ultimate_duration': 7,
            'ultimate_cooldown': 90
    },
    "Glorp Glapper": {
        'base_health': BASE_HEALTH + 40,  # More health
        'base_speed': BASE_SPEED - 1.25,  # Slower
        'loadout': ['Glapper Gun', 'Glorp Shield', 'Belly Buster'],
        'ability_1': 'Blowfish',
            'ability_1_desc': "Upon activation, Glorp flashes red for 3 seconds before inflating himself, becoming a large target but gaining 80% damage resistance for 5 seconds and invulnerability to any incoming status effects. While inflated, Glorp cannot use weapons or abilities, but can roll to move at 40% base speed. Glorp can roll into an enemy player dealing 150 damage. If Glorp dies while inflated, he explodes, applying the 'stun' effect to all enemies within a 7 meter radius.",
            'ability_1_duration': 5,
            'ability_1_cooldown': 28,
        'ability_2': 'Glorp Shield',
            'ability_2_desc': "Glorp deploys a large plasma shield that blocks all incoming damage and status effects. The shield can absorb up to 750 damage before breaking. Allies within 5 meters of the shield gain a 20% damage resistance boost while ability is active.",
            'ability_2_duration': 6,
            'ability_2_cooldown': 14,
        'ultimate': 'Belly Flop',
            'ultimate_voice_line': "Glorp smash! *During slam* Wheeeeeeee!",
            'ultimate_desc': "Upon activation if Glorp has teammates, he consumes them and they become invulnerable for the duration. Glorp then leaps high into the air, expands and slams down, creating a shockwave that deals 100 damage and applies the 'stun' effect to all enemies within a 10 meter radius. If Glorp is killed while his ultimate is active, his teammates are released and gain a 50% damage boost for 5 seconds.",
            'ultimate_duration': 6,
            'ultimate_cooldown': 90
    },
    "Anteus 'Puzzle' Ramble": {
        'base_health': BASE_HEALTH,
        'base_speed': BASE_SPEED,
        'loadout': ['Puzzler Gun', 'Rubix Cube', 'Trustfall'], # Trustfall is an assassination animation
        'ability_1': "Lame Ducks",
            'ability_1_desc': "Anteus can quickly teleport to a selected area up to a distance of 20 meters. Once teleported, he radiates a shockwave that applies the 'Confusion' status effect to all enemies within a 10 meter radius. He teleports back to previous location after duration.",
            'ability_1_duration': 4,
            'ability_1_cooldown': 24,
        'ability_2': 'Hand of Friendship',
            'ability_2_desc': "Anteus always appears to enemy players as a solo player. If Anteus is already in an alliance, he can still use his handshake. If an unsuspecting enemy accepts the handshake, the 'Confusion' status effect and 40 damage is applied.",
            'ability_2_duration': 7,
            'ability_2_cooldown': 13,
        'ultimate': 'Bullshit Squared',
            'ultimate_voice_line': "Don't bullshit a bullshitter, youngster...",
            'ultimate_desc': "If any alliance is broken within 10 meters of Anteus, he has 3 seconds to activate his ultimate. If he does, 75 damage and the 'stun' effect are applied to the alliance breaker. Additionally, all loot from the alliance breaker is transferred to Anteus.",
            'ultimate_duration': 3,
            'ultimate_cooldown': 90
    },
    "Clogade the Banished": {
        'base_health': BASE_HEALTH + 50,
        'base_speed': BASE_SPEED - 0.75,
        'loadout': ['Griefbreaker', 'Echo Shard', 'Giant\'s Canteen'],

        'ability_1': 'Echo Slam',
        'ability_1_desc': "Clogade slams the ground with Griefbreaker, sending out a seismic pulse. The 'Slow' status effect is applied to all enemies within 7 meters. Clogade and his teammates gain a 15% damage boost for 3 seconds after the slam.",
        'ability_1_duration': 3,
        'ability_1_cooldown': 18,

        'ability_2': 'Forsaken Might',
        'ability_2_desc': "Clogade channels his inner Giant, increasing 25% in size and gaining a 20% damage boost and immunity to incoming status effects. While ability is active, enemies within 5 meters are inflicted with 'Weaken', reducing their damage by 15%.",
        'ability_2_duration': 6,
        'ability_2_cooldown': 28,

        'passive_1': 'Canteen of Giants',
        'passive_1_desc': "When Clogade drinks from his Giant's Canteen, he gains a 'Giant Stack' increasing his size and melee damage by 2%. Stacks reset upon death. Maximum of 150 stacks.",

        'ultimate': 'Spirit Reclamation',
        'ultimate_voice_line': "My wrath is eternal.",
        'ultimate_desc': "Clogade temporarily manifests his true Giant form. He quadruples in size, gains 50% damage resistance, 100% increased melee range, and each strike applies a stacking 'Crush' debuff (-10% armor, max 3 stacks). After duration, he unleashes a roar that applies the 'Stun' status effect enemies he is facing within 10 meters.",
        'ultimate_duration': 8,
        'ultimate_cooldown': 100
    },
    "Edwin 'Trailblazer' Horton": {
        'base_health': BASE_HEALTH + 25,
        'base_speed': BASE_SPEED,

        'loadout': ['Surveyor’s Lance Rifle', 'Black Ember Compass', 'Native Arcanist Kit'],

        'ability_1': 'Fearmarked Territory',
        'ability_1_desc': "Edwin plants the Black Ember Compass in the ground, claiming a 15-meter radius as 'Trailblazer’s Domain' for 8 seconds. Enemies inside are gradually slowed (up to 25%) and receive the 'Fear' status if they remain for 4+ seconds. Allies inside the domain gain +10 armor and +10% movement speed.",
        'ability_1_duration': 8,
        'ability_1_cooldown': 22,

        'ability_2': 'Forged Salvation',
        'ability_2_desc': "Using salvaged parts and native rituals, Edwin instantly builds a temporary, auto-firing defense construct with AoE flame rounds and suppressive fear effects. Lasts 5 seconds or until destroyed. Placement within 10 meters.",
        'ability_2_duration': 5,
        'ability_2_cooldown': 30,

        'passive_1': 'Landowner’s Influence',
        'passive_1_desc': "When Edwin is in a Fog or Collapse Zone, his minimap reveals enemy locations every 3 seconds. Additionally, any enemy affected by 'Fear' within 20 meters drops 20% more loot when eliminated.",

        'ultimate': 'Frontier Pact',
        'ultimate_voice_line': "Let ‘em come. This land fights back.",
        'ultimate_desc': "Edwin calls upon his homestead defenses. For 9 seconds, automated flame turrets rise from the ground and target enemies within 25 meters. All enemies affected by Fear are highlighted and take 20% increased damage from allies. A spectral stampede charges at the end, dealing 80 damage in a straight line and knocking down all enemies hit.",
        'ultimate_duration': 9,
        'ultimate_cooldown': 95
    }
}