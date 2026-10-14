# 🤖 Artificial Intelligence Practicals — Academic Repository

> **Department of Computer Engineering & Department of AI & Data Science**  
> **Course:** Artificial Intelligence Laboratory | Savitribai Phule Pune University (SPPU)

![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-blue?logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange?logo=matplotlib&logoColor=white)
![ipywidgets](https://img.shields.io/badge/ipywidgets-8.x-purple)
![NetworkX](https://img.shields.io/badge/NetworkX-3.x-informational?logo=networkx&logoColor=white)
![Status](https://img.shields.io/badge/Status-Verified%20%26%20Active-brightgreen)

---

## 📌 Repository Overview

This repository hosts a comprehensive, verified, and interactive collection of **Artificial Intelligence Laboratory Practicals**, organized into two dedicated academic tracks:

1. **[Computer Science Engineering (CS Branch)](#-track-1-computer-science-engineering-cs-branch)**:
   - **Visualized Suite** (`AI for CS Branch/Visualized/`): 9 premium, highly visual, interactive Jupyter Notebooks featuring dynamic `matplotlib` plots, real-time `ipywidgets` steppers/sliders, and automated verification test suites.
   - **Standard Suite** (`AI for CS Branch/Normal/`): Baseline implementations and HTML archives.
2. **[AI & Data Science (AI & DS Branch)](#-track-2-artificial-intelligence--data-science-ai--ds-branch)**:
   - Practicals 01 through 06 with dual **Basic** and **Advance** implementations in both modular Python scripts and Jupyter Notebooks.

---

## 📁 Repository Structure

```text
Artificial_Intelligence/
├── README.md                          ← Main repository guide (You are here)
├── requirements.txt                   ← Core Python dependencies
│
├── AI for CS Branch/                  ← Computer Science Engineering Curriculum
│   ├── Visualized/                    ← Upgraded interactive & visualized notebooks (Recommended)
│   │   ├── 01_vacuum_cleaner_agent.ipynb
│   │   ├── 02_astar_8_puzzle.ipynb
│   │   ├── 03_alpha_beta_pruning.ipynb
│   │   ├── 04_tower_of_hanoi.ipynb
│   │   ├── 05_bfs_path_planning.ipynb
│   │   ├── 06_eight_queens.ipynb
│   │   ├── 07_number_guessing_agent.ipynb
│   │   ├── 08_minimax_tic_tac_toe.ipynb
│   │   ├── 09_rule_based_recommendation.ipynb
│   │   └── README.md                  ← Detailed CS Branch guide & audit metrics
│   │
│   └── Normal/                        ← Original baseline notebooks (Protected)
│       ├── 01_vacuum_cleaner_agent.ipynb
│       ├── 02_astar_8_puzzle.ipynb
│       ├── ...
│       └── README.md
│
├── Practical_01/                      ← Expert System (Rule-based decision engine)
│   ├── Basic/
│   └── Advance/
├── Practical_02/                      ← BFS & DFS Maze Solver (Graph search)
│   ├── Basic/
│   └── Advance/
├── Practical_03/                      ← A* Heuristic Search (Shortest path planning)
│   ├── Basic/
│   └── Advance/
├── Practical_04/                      ← CSP Map Coloring (Backtracking algorithm)
│   ├── Basic/
│   └── Advance/
├── Practical_05/                      ← Minimax Game Engine (Tic-Tac-Toe AI)
│   ├── Basic/
│   └── Advance/
└── Practical_06/                      ← Alpha-Beta Pruning (Optimized adversarial search)
    ├── Basic/
    └── Advance/
```

---

## 🚀 Track 1: Computer Science Engineering (CS Branch)

A collection of **9 self-contained practicals** designed for intuitive visual learning, algorithmic transparency, and seamless live examination demonstrations.

| # | Topic | Algorithm | Visual & Interactive Features | Status |
|---|---|---|---|---|
| **01** | **[Vacuum Cleaner Agent](AI%20for%20CS%20Branch/Visualized/01_vacuum_cleaner_agent.ipynb)** | Reflex Agent & Percept Loop | Dual-room visual schematic, dirt status badges, sprite motion, step-by-step playback stepper. | ✅ Verified |
| **02** | **[A* Search for 8-Puzzle](AI%20for%20CS%20Branch/Visualized/02_astar_8_puzzle.ipynb)** | A\* with Manhattan Distance | 3×3 grid tiles, highlighted blank tile, $g/h/f$ costs, inversion parity check, move stepper. | ✅ Verified |
| **03** | **[Alpha-Beta Pruning](AI%20for%20CS%20Branch/Visualized/03_alpha_beta_pruning.ipynb)** | Adversarial Game Tree Search | 4-tier tree diagram with MAX/MIN layers, pruned branch cutoff flags ($\beta \le \alpha$), mode toggle. | ✅ Verified |
| **04** | **[Tower of Hanoi](AI%20for%20CS%20Branch/Visualized/04_tower_of_hanoi.ipynb)** | BFS State-Space Planning | 3 peg visualization with size-scaled disks, invariant stack checks, optimal 7-move trajectory slider. | ✅ Verified |
| **05** | **[BFS Path Planning](AI%20for%20CS%20Branch/Visualized/05_bfs_path_planning.ipynb)** | Uniform-Cost Grid Wavefront | 6×6 coordinate grid, obstacle barrier walls, explored wavefront markers, green optimal path trace. | ✅ Verified |
| **06** | **[Eight Queens Problem](AI%20for%20CS%20Branch/Visualized/06_eight_queens.ipynb)** | Backtracking CSP Solver | 8×8 tournament chessboard, golden queen crowns, conflict-free row/col/diagonal placement inspector. | ✅ Verified |
| **07** | **[Number Guessing Agent](AI%20for%20CS%20Branch/Visualized/07_number_guessing_agent.ipynb)** | Binary Search Policy | Search interval shrinkage bars ($[low, high]$), guess history trace, custom target slider. | ✅ Verified |
| **08** | **[Minimax Tic-Tac-Toe](AI%20for%20CS%20Branch/Visualized/08_minimax_tic_tac_toe.ipynb)** | Zero-Loss Minimax with Depth Discount | 3×3 game board, candidate move valuations, zero-loss theoretical guarantee, click move engine. | ✅ Verified |
| **09** | **[Rule-Based Recommender](AI%20for%20CS%20Branch/Visualized/09_rule_based_recommendation.ipynb)** | IF–THEN Expert System | 5-stage inference flowchart, styled recommendation dossier cards, multi-dropdown preference dashboard. | ✅ Verified |

👉 For full details on the Visualized suite, see the **[Visualized README](AI%20for%20CS%20Branch/Visualized/README.md)**.

---

## 📊 Track 2: Artificial Intelligence & Data Science (AI & DS Branch)

Modular implementations covering standard SPPU AI practical topics with **Basic** and **Advance** tiers:

| # | Practical | Description | Key Algorithms & Tools |
|---|---|---|---|
| **01** | **[Expert System](Practical_01/)** | Knowledge-based diagnosis and recommendation | Forward-chaining rule engine |
| **02** | **[BFS & DFS Solver](Practical_02/)** | Maze traversal and state-space exploration | Breadth-First & Depth-First Search |
| **03** | **[A* Algorithm](Practical_03/)** | Shortest pathfinding on weighted graphs | Heuristic search ($f = g + h$), NetworkX |
| **04** | **[CSP Map Coloring](Practical_04/)** | Constraint Satisfaction Problem on region maps | Backtracking search with forward checking |
| **05** | **[Minimax Tic-Tac-Toe](Practical_05/)** | Two-player adversarial game agent | Recursive Minimax decision tree |
| **06** | **[Alpha-Beta Pruning](Practical_06/)** | Optimized game-tree pruning | Minimax with $\alpha$ and $\beta$ threshold cutoffs |

---

## 🛠️ Installation & Environment Setup

### 1. Prerequisites
Ensure you have **Python 3.10 or higher** installed.

### 2. Clone the Repository
```bash
git clone https://github.com/himanshu-jadhav108/College_Practicals.git
cd College_Practicals/Artificial_Intelligence
```

### 3. Create & Activate Virtual Environment
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 How to Run the Practicals

### Launching Jupyter Notebooks (Recommended for CS Branch)
```bash
# Launch the Jupyter Notebook dashboard
jupyter notebook
```
Navigate to `AI for CS Branch/Visualized/` and open any practical. Select **Cell → Run All** to view all diagrams, metric cards, and interactive widgets.

### Running AI & DS Branch Scripts
```bash
# Run Basic CLI script
python Practical_02/Basic/practical_02_basic.py

# Run Advanced script with graphical plot
python Practical_02/Advance/practical_02_advance.py

# Or launch its dedicated notebook
jupyter notebook Practical_02/Advance/practical_02_advance.ipynb
```

---

## 📦 Required Dependencies

All packages are standard, lightweight, and installable via `pip`:
* **`matplotlib`** (v3.9.0+) — 2D graphics, chessboards, grid worlds, and tree diagrams
* **`ipywidgets`** (v8.0.6+) — Interactive sliders, buttons, steppers, and dashboard controls
* **`networkx`** (v3.1+) — Graph structure modeling and state-space visualization
* **`numpy`** (v1.26.0+) — Coordinate grids and numerical utilities
* **`jupyter`** / **`notebook`** — Interactive execution environment

---

## 👨‍💻 Maintainer & Author

**Himanshu Jadhav**  
Computer Engineering / AI & Data Science | Savitribai Phule Pune University (SPPU)

[![GitHub](https://img.shields.io/badge/GitHub-himanshu--jadhav108-black?logo=github)](https://github.com/himanshu-jadhav108)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Himanshu%20Jadhav-blue?logo=linkedin)](https://www.linkedin.com/in/himanshu-jadhav-328082339)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blueviolet?logo=vercel)](https://himanshu-jadhav-portfolio.vercel.app/)

---

> ✅ All practicals are self-contained, mathematically verified, fully executed, and ready for lab evaluations and viva demonstrations.
