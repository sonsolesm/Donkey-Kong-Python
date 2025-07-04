# 🎮 Donkey Kong – Python Game with Pyxel

This project is a recreation of the classic Donkey Kong game, developed in Python using the [Pyxel](https://github.com/kitao/pyxel) game engine. It was created as the final project for the Programming course in the first year of the Dual Degree in Computer Science and Business Administration at UC3M.

Developed by **Sonsoles Molina Abad** and **Lorenzo Largacha Sanz**.

---

## 🕹️ Game Summary

In this game, Mario must climb platforms and avoid barrels thrown by Donkey Kong to rescue Pauline. Mario can move, climb, jump, and dodge barrels, and has three lives per game.

The game includes:
- Character animations and interaction logic
- Collisions and fall detection via pixel-based map matrix
- Score and life counters
- Start and game-over screens
- Sound and visual effects
- Debug shortcut to win (`T`) and quit (`Q`)

---

## 🧱 Project Structure

```
lls-sma-TrabajoFinal/
├── donkeyKong/             # Main game package
│   ├── escenario/          # Platforms, ladders, barrels, counters
│   ├── personajes/         # Mario, Pauline, Donkey Kong
│   ├── assets/             # Sprite sheets and images
│   ├── constantes.py       # Game constants
│   ├── donkeyKong.py       # Main game class
│   ├── inicio.py           # Start screen
│   ├── game_over.py        # End screen
│   └── test.py             # Entry point to run the game
```

---

## 🛠 Technologies

- Python 3
- Pyxel (pixel-based retro game engine)
- GIMP (for sprite size & optimization)
- Git and Teletype (for real-time collaborative coding)

---

## 🚀 How to Run

1. Install [Pyxel](https://github.com/kitao/pyxel):
```bash
pip install pyxel
```

2. Navigate to the project folder:
```bash
cd donkeyKong
```

3. Run the game:
```bash
python test.py
```

---

## 🎯 Game Features

- Mario can walk, climb ladders, and jump over barrels
- Randomized barrel drops and movement logic
- Escalating difficulty with multiple barrels
- Pixel-precision movement based on matrix mapping
- Score increases when jumping barrels
- Lives displayed via mini-Mario icons
- Optional cheat key (`T`) to auto-win and `Q` to quit
- Start and game over screens with animation

---

## 📌 Development Notes

We split the work into sprints, starting with object modeling and GUI, then movement, physics, logic, and polishing. The game's core is a matrix that defines walkable, climbable, and fall zones. All logic (collision, movement, animation) reacts to that map.

---

## 👥 Authors

- **Sonsoles Molina Abad**  
- **Lorenzo Largacha Sanz**

---

## 🧠 Reflection

This project was a fun and challenging introduction to game development and team collaboration. We used Git and Teletype to work simultaneously, explored Pyxel’s capabilities beyond class content, and designed every aspect of the game from scratch.

---

## 📄 License

For academic and educational purposes only. UC3M.

