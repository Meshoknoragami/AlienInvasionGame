# 👾 Alien Invasion

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern Python remake of the classic arcade shooter **Alien Invasion**, built with [Pygame](https://www.pygame.org/). 
Defend Earth from descending alien fleets, rack up points, and survive increasingly difficult waves!

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/9c0c69cf-96a4-486b-b17e-ff9d2d5e2073" />

---

## Features

- **Dynamic Difficulty**: Enemy speed & point values scale with each level
- **Score & High-Score Tracking**: Persistent high scores saved to `records.txt`
- **Fullscreen Mode**: Immersive gameplay with automatic screen scaling
- **Play Button UI**: Mouse-driven start/restart interface
- **Lives System**: Multiple ships per game with visual HUD feedback
- **Object-Oriented Architecture**: Clean, modular code using Pygame's `Sprite` system

---

## Controls

| Key / Action      | Function                          |
|-------------------|-----------------------------------|
| `A` / `D`         | Move ship left / right            |
| `Space`           | Fire projectile                   |
| `Q`               | Quit game & save high score       |


---

## 🚀 Installation & Setup

### Prerequisites
- Python `3.8` or higher
- `pip` package manager

### Step-by-Step
```bash
# 1. Clone the repository
git clone https://github.com/Meshoknoragami/AlienInvasionGame.git
cd alien-invasion

# 2. Install dependencies
pip install pygame

# 3. Run the game
python alien_invasion.py
