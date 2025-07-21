# 🎯 Parabolic Motion Animation using Manim

This project visualizes the motion of a projectile (gerak parabola) using the [Manim](https://www.manim.community/) animation engine. It includes a ball following a parabolic path, velocity vector visualizations at different points in time, and formulas explaining the physics behind the motion.

---

## 📽️ Features

✅ Simulates projectile motion based on initial velocity and launch angle  
✅ Highlights:
- Before maximum height  
- At maximum height  
- After maximum height  

✅ Displays velocity vectors at each of those points  
✅ Animates relevant physics formulas like:
- Maximum height  
- Time of flight  
- Range  
- Velocity vector:  
  \[
  \vec{v} = \left( v_0 \cos\theta,\ v_0 \sin\theta - g t \right)
  \]

---

## 📦 Requirements

| Tool      | Version       |
|-----------|---------------|
| Python    | 3.10 or 3.11  |
| Manim CE  | ≥ 0.18.0      |
| NumPy     | ≥ 1.22        |

---

## 🛠️ Installation and Run the Animation

### 1. Clone or download this repository

```bash
git clone https://github.com/yourusername/parabolic-motion-manim.git
cd parabolic-motion-manim
```
### 2: (Optional but Recommended) Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
### 3: Install Required Packages
```bash
pip install manim numpy
```
### 4: How to Run the Animation
```bash
manim -pql parabola.py GerakParabola
```
