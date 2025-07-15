# 🌵 WEST UNSAVED — Part II of the *West Unended* Trilogy

**West Unsaved** is the second chapter of the *West Unended* saga — a stylized low-poly first-person shooter rooted in Western dark fantasy, alliance mechanics, spirit-world warfare, and narrative-driven chaos.

Built in **Python + Ursina**, *West Unsaved* offers a surreal blend of objective-based combat, player betrayal, and evolving alliances in a world haunted by possession, decay, and mythic resurrection.

> _“This land don’t forgive. It remembers.”_

---

## 🚩 Current Dev Status

| Month | Theme                         | Status     |
|-------|-------------------------------|------------|
| 1     | Core Systems & Controller     | ✅ Complete |
| 2     | Weapons, FX, Health/Respawn   | ✅ Complete |
| 3     | Multiplayer (P2P), Map Logic  | 🚧 In Progress |
| 4     | AI + Spirit Possession System | 🔜 Upcoming |
| 5     | Questline & Ritual Engine     | 🔜 Upcoming |
| 6     | ELO System + Cosmetics        | 🔜 Upcoming |

---

## 🔥 Key Game Features

### 🎮 Gameplay Systems
- **FPS Combat**: Sprinting, crouching, ADS, reloads, multi-weapon support.
- **Stylized Combat Effects**: Low-poly muzzle flash, bullet trails, and reload FX.
- **Health & Respawn Logic**: Lives tied to player “vessel” status.
- **Dynamic Alliances**: Temporary team-ups, betrayals, shifting player allegiances.
- **Game Phases**: Spawn → Exploration → Objectives → Collapse → Final Duel.

### ⚔️ Character Kits & Spirit Powers
- Build custom characters with:
  - Active and passive abilities
  - Tradeoff perks (e.g. longer sprint vs. no ADS)
  - Spirit-form ultimates
- Unlock **Vessel Form**, becoming vulnerable to possession — or a host for ancient spirits.

### 🌍 World & Lore
- Explore mythic ruins, ghost towns, scorched earths, and frozen temples.
- Every map reflects themes of decay, memory, and ritual — part of the *West Unended* cosmology.
- Seasons of lore-driven content, each expanding the spirit-economy storyline.

---

## 🧱 Tech Stack

| Component     | Tool/Framework         |
|---------------|------------------------|
| Engine        | 🐍 Python + Ursina     |
| Database      | SQLite (player stats, cosmetics) |
| Sound         | Custom FX via FFmpeg   |
| Multiplayer   | P2P (custom socket layer) |
| Art Style     | Stylized Low-Poly (Blender + Unity assets converted to `.glb`) |

---

## 📁 Project Structure (WIP)
west_unsaved/
├── assets/
│ ├── models/
│ ├── audio/
│ └── textures/
├── src/
│ ├── main.py
│ ├── combat/
│ ├── player/
│ ├── map/
│ ├── perks/
│ └── utils/
├── shared/
├── README.md
└── requirements.txt

---

## 👣 Development Goals (Q3–Q4 2025)

- [ ] Finalize multiplayer testing (P2P room creation + sync)
- [ ] Implement alliance/traitor detection logic
- [ ] Launch first Spirit Possession Ritual mechanic
- [ ] Complete map transitions and endgame scoring logic
- [ ] Begin Season I content narrative for Part II: *The Hollow Siege*

---

## 👻 Join the Development

Want to contribute? Reach out or submit a PR!
We welcome:
- Art assets (GLB, low-poly, eerie Western)
- Sound design (ambient, dark, ritualistic)
- Playtesters with interest in FPS + surreal storytelling
- Lorekeepers — help us expand *West Unended*’s cosmology!

---

## 🎭 Part of the *West Unended* Trilogy

1. **West Uncanny** *(TV series + script — [GitHub link or Notion link])*  
2. **West Unsaved** *(This game — WIP)*  
3. **West Unbroken** *(TBD — final entry)*

---

## 📜 License

MIT License. Assets used from third-party creators are credited in `/assets/LICENSES.md`.

---

## 🐎 Final Word

> *"When the frontier collapsed, the spirits came first — and the guns followed after."*

West Unsaved is not just a game — it's a reckoning.

---
