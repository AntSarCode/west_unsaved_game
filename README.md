# WEST UNSAVED
An FPS experience forged in folklore, betrayal, and survival.

West Unsaved is a stylized, story-driven first-person shooter in active development. It serves as Part II of the West Unended Trilogy, continuing the mythic saga of survival across the haunted frontier.

# Overview
Set in a dark-fantasy Western universe, West Unsaved blends fast-paced FPS gameplay with unique team-up mechanics, a dynamic in-game economy, and deeply customizable character builds.

Players engage in chaotic Free-For-All skirmishes with temporary alliances, spiritual power-ups, and evolving objectives — all under the threat of collapse events that reshape the battlefield.

# Core Features
- 10-Player Free-for-All FPS Combat
- Temporary Alliance System
- In-Game Economy with Purchasable Perks & Gear
- Unique Character Loadouts, Abilities & Tradeoffs
- Game Phase Engine (Spawn → Explore → Objectives → Collapse → Final Showdown)
- Stylized Low-Poly World (600x600 frontier-inspired map)
- ELO, Reputation, and Streak Tracking (planned)
- Earnable & Purchasable Cosmetics (future stretch goal)

# Tech Stack
- Engine: Ursina Engine (Python-based)
- Language: Python 3.11
- Data Handling: SQLite (for persistent state, map logic, etc.)
- Models: .glb format (low-poly art style)
- Audio: Simpleaudio (voice lines, SFX)
- Version Control: Git + GitHub

# Project Structure
west_unsaved_game/
├── assets/               # 3D models, textures, audio
├── src/                  # Core engine logic, player control, perks
├── data/                 # Map layouts, game state files
├── shared/               # Interfaces, utilities
├── .venv/                # Virtual environment (gitignored)
└── requirements.txt      # Python dependencies

# 🚧 Current Progress
- ✅ Movement, Shooting, Reloading, HUD
- ✅ Character loadouts, abilities, perks
- ✅ Stylized asset integration
- ⏳ Health system & respawn logic (in progress)
- ⏳ Phase-based game state engine
- ⏳ Finalize alliance mechanics

# 📦 Setup

1. Clone the repo:
git clone https://github.com/AntStarCode/west_unsaved_game.git
cd west_unsaved_game

2. Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

# 🎯 Goals
- Build a fully playable demo by Month 3
- Implement online multiplayer and matchmaking by Month 6
- Reach beta release with full visual/audio polish by Month 9

# 👤 Credits
This project is independently developed by AntStarCode, written in Python, built with Ursina, and inspired by surreal, mythic Western storytelling.

# 📜 License
This project is currently closed-source and proprietary. Distribution, reproduction, or derivative projects are not permitted without explicit permission.

