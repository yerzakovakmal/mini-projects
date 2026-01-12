# Asteroids Game (Python + Pygame)

A simple **Asteroids‑style arcade game** built using **Python** and **Pygame**. In this game, you control a spaceship that can rotate and shoot bullets to destroy drifting asteroids. Asteroids break into smaller pieces when shot, and the game ends if your ship collides with one.

---

## 🎮 Gameplay Features

- 🛰️ **Player control**
  - Rotate left/right
  - Shoot bullets in the direction the player is facing

- 🌑 **Asteroids**
  - Move in straight lines with constant velocity
  - Split into smaller pieces when shot
  - Destroyed entirely when they are below a minimum radius

- 💥 **Collisions**
  - Player collides with asteroids → **Game Over**
  - Bullets collide with asteroids → both are removed and the asteroid splits

- ⏱️ **Frame‑rate independent movement**
  - Delta time (`dt`) is used so movement stays consistent regardless of FPS.

---

## 🧠 Key Technologies Used

This project is built with:

- **Python 3**
- **Pygame** — for graphics, game loop, input handling, and rendering
- **OOP (Object‑Oriented Programming)**
  - Classes like `Player`, `Asteroid`, `Shot`, and `CircleShape`
  - Uses class inheritance and method overriding

### Coding Concepts Included

- Game loop with **update** and **draw** methods  
- Delta time (`dt`) for smooth movement  
- Collision detection using `pygame.Vector2.distance_to()`  
- Use of `pygame.sprite.Group` for managing updatable and drawable objects  
- Simple event logging and game‑over screen  

---

## 📁 Project Structure
```
asteroidsgame/
├── main.py
├── player.py
├── asteroid.py
├── shot.py
├── circleshape.py
├── constants.py
├── assets/ (optional background/image assets)
└── README.md
```
---

## 🚀 How to Run

### 1. Install dependencies

Make sure you have Python 3 installed. Then install Pygame:

```bash
#Install pygame
pip install pygame
#Clone Repo
git clone https://github.com/yerzakovakmal/mini-projects.git
#Navigate
cd mini-projects/python-projects/asteroidsgame
# Run the Game
python3 main.py
```

## 🎯 How to Play

- **Rotate ship:** `A` and `D`  
- **Shoot bullets:** `Spacebar`  
- **Avoid hitting asteroids**  
- **Destroy asteroids to survive longer**

> If you hit an asteroid, the game will display a **Game Over** message.