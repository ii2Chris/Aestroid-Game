# 🪐 Asteroid Game (Pygame)

A modern, object-oriented clone of the classic *Asteroids* arcade game — built with **Python** and **Pygame**.  
This project demonstrates OOP principles, delta-time–based movement, collision detection, and sprite management.

---

## 🚀 Features

- **Player Ship** — Rotates, moves forward/backward, and shoots bullets  
- **Asteroids** — Spawn randomly, drift across the screen, and split into smaller fragments when hit  
- **Bullets / Shots** — Travel in the direction fired, with a cooldown to prevent spamming  
- **Collisions** — Fully implemented circular collision detection via a shared `CircleShape` base class  
- **Modular Codebase** — Organized into logical files for reusability and clarity:
  - `main.py` — main loop, groups, and game orchestration  
  - `player.py` — player control, shooting, and rotation  
  - `asteroid.py` — asteroid logic and splitting  
  - `asteroidfield.py` — automatic asteroid spawning  
  - `shoot.py` — bullet (shot) logic  
  - `circleshape.py` — shared physics & collision base class  
  - `constants.py` — all tunable game constants  

---

## 🧩 How It Works

Each entity in the game inherits from a common `CircleShape` class, which provides:
- Position (`pygame.Vector2`)
- Velocity
- Radius
- Collision helper (`collides_with()`)

The game loop:
1. Updates all objects (`.update(dt)`) through sprite groups  
2. Checks collisions between **shots** and **asteroids**  
3. Draws all objects to the screen each frame  

Asteroids are spawned dynamically by an `AsteroidField` class.  
When a bullet hits an asteroid, it **splits into two smaller pieces**, unless it’s already at the minimum radius.

---

## 🕹️ Controls

| Key | Action |
|-----|---------|
| **W** | Move forward |
| **S** | Move backward |
| **A** | Rotate left |
| **D** | Rotate right |
| **Space** | Shoot (0.3-second cooldown) |
| **Esc / X** | Quit window |

---

## ⚙️ Requirements

- Python 3.10+  
- Pygame 2.6+

### Installation

```bash
pip install pygame
```

### Run the Game

```python main.py```

