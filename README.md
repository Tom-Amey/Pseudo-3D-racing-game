# Turbo 90 🏎️💨

A retro 90s-inspired arcade racing game built from scratch in **Python** using **Pygame**, **Tkinter**, and **SQLite**—featuring a custom **pseudo-3D rendering engine** without external 3D libraries.

## 🎮 Gameplay Preview
*(Drag or paste your curved-road gameplay screenshot here!)*

## Gameplay
<img width="443" height="250" alt="image" src="https://github.com/user-attachments/assets/b3c1a1dd-cd98-4448-9a49-69e85f8069da" />
<img width="591" height="332" alt="image" src="https://github.com/user-attachments/assets/2d8e4775-31ef-4dbc-b196-6c6f5b7505a9" />


## ✨ Key Features
- **Custom Pseudo-3D Projection Engine:** Translates 3D world coordinates (`x_world`, `y_world`, `z_world`) into 2D screen space using field-of-view trigonometry, depth scaling, and cumulative road curvature for dynamic left and right corners.
- **2D & Pseudo-3D Levels:** Includes 4 distinct levels spanning classic top-down 2D arcade tracks (Levels 1–2) and high-speed pseudo-3D highways with checkpoints (Levels 3–4).
- **Dynamic Sprite & Traffic Scaling:** Real-time depth scaling and lane-based collision detection for oncoming traffic, billboards, and roadside scenery.
- **User Accounts & GDPR-Compliant Database:** Built-in Tkinter login/registration system backed by SQLite (`Turbo90.db`), featuring hashed password storage (`hashlib`), persistent coin tracking, and full account deletion ("Right to be Forgotten").
- **Modular OOP Architecture:** Structured across 15+ object-oriented modules (`PsuedoLevelLogic`, `Polygon`, `SpriteManager`, `DataBaseMethods`, `Menu`, `Button`) for clean maintainability and low resource overhead (~3 MB total footprint).

## 🛠️ Tech Stack
- **Language:** Python 3
- **Graphics & Audio:** Pygame
- **Login GUI:** Tkinter
- **Database & Security:** SQLite3, Hashlib

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the main game loop:
   ```bash
   python Main.py
   ```

## 🏗️ Architecture Overview
- `Main.py` & `GameAssets.py` – Core game loop, OS compatibility verification, and pre-loading manager.
- `Pseudo3DPolygon.py` & `PseudoRoadCreator.py` – Perspective math and procedural straight/curved road segment generation.
- `PseudoLogic.py` & `PseudoManager.py` – 3D rendering pipeline, camera tracking, and checkpoint progression.
- `SpriteManager.py` & `collisionDetection.py` – Depth-scaled traffic/scenery and 2D/3D hit detection.
- `LoginPage.py`, `SQLMethods.py` & `Hashing.py` – Tkinter authentication GUI and SQLite persistence.
