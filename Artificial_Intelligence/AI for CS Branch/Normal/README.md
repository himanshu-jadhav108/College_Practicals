# AI Practicals and Mini-Project — CS Branch

## Overview
This repository folder contains a complete, verified collection of eight Artificial Intelligence undergraduate practical notebooks and one rule-based recommendation mini-project notebook tailored for Computer Science engineering students. Each notebook adheres to a clean college practical submission format featuring the practical title, concise aim, numbered code cells, and pre-computed, fully verified execution outputs.

## Folder Contents

| Filename | Description |
| :--- | :--- |
| `01_vacuum_cleaner_agent.ipynb` | Design and implementation of a simple reflex agent for the two-room Vacuum Cleaner World. |
| `02_astar_8_puzzle.ipynb` | Optimal state-space pathfinding for the 8-Puzzle using the A* search algorithm and Manhattan distance heuristic. |
| `03_alpha_beta_pruning.ipynb` | Adversarial game-tree search comparing standard Minimax against Alpha-Beta pruning with branch cutoff tracking. |
| `04_tower_of_hanoi.ipynb` | State-space representation and Breadth-First Search (BFS) solver for the 3-disk Tower of Hanoi problem. |
| `05_bfs_path_planning.ipynb` | Robot grid path planning with obstacle avoidance using Breadth-First Search (BFS). |
| `06_eight_queens.ipynb` | Constraint Satisfaction Problem (CSP) solver for the 8-Queens problem using recursive backtracking. |
| `07_number_guessing_agent.ipynb` | Intelligent agent using binary search strategy with higher/lower feedback to guess secret numbers. |
| `08_minimax_tic_tac_toe.ipynb` | Game-playing intelligent agent selecting optimal and blocking moves in Tic-Tac-Toe using Minimax. |
| `09_rule_based_recommendation.ipynb` | Rule-based recommendation expert system matching user profiles with suitable programming languages and project ideas. |
| `README.md` | Documentation, practical index, execution instructions, and verification report. |

## Requirements
The practical implementations rely primarily on Python's built-in standard library (`heapq`, `collections.deque`, `json`, etc.), ensuring deterministic and offline execution without external APIs or heavy dependencies.

* **Python**: Version 3.10+ (tested and verified on Python 3.13)
* **Jupyter Environment**: Jupyter Notebook, JupyterLab, or VS Code / Antigravity Notebook Viewer
* **Jupyter Kernel**: Standard `ipykernel`

## How to Run
1. Open the project directory in your terminal or IDE:
   ```bash
   cd "AI for CS Branch"
   ```
2. Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   # or
   jupyter lab
   ```
3. Open any of the `.ipynb` files from the notebook browser.
4. The notebooks already contain verified execution outputs. To re-execute cells from scratch:
   * Click **Kernel** $\rightarrow$ **Restart & Run All** (or **Run All Cells** in VS Code).
   * All cells run automatically without requiring manual keyboard input or external network connections.

## Practical Index

1. **Practical 1: Vacuum Cleaner Agent**
   * *Title*: Design and Implement a Simple Reflex Agent for the Vacuum Cleaner World and Analyze Rational Behavior
   * *Core Concepts*: Reflex agents, condition-action rules, percept-action cycle, rational behavior.
2. **Practical 2: A\* Search for 8-Puzzle**
   * *Title*: Implement the A* Search Algorithm to Solve the 8-Puzzle Problem
   * *Core Concepts*: State-space search, priority queue (`heapq`), Manhattan distance heuristic, inversion solvability.
3. **Practical 3: Adversarial Search with Alpha-Beta Pruning**
   * *Title*: Implement Adversarial Search with Alpha-Beta Pruning for Game Playing
   * *Core Concepts*: Zero-sum game trees, minimax evaluation, alpha-beta cutoff bounds, search tree optimization.
4. **Practical 4: Tower of Hanoi using State-Space Search**
   * *Title*: Implement the Tower of Hanoi Problem Using State-Space Search
   * *Core Concepts*: State representations, legal transition graphs, Breadth-First Search (BFS), shortest path reconstruction.
5. **Practical 5: BFS for Path Planning**
   * *Title*: Implement Breadth-First Search for a Planning Problem
   * *Core Concepts*: Grid environments, 4-connected movements, obstacle avoidance, grid rendering, unreachable destination handling.
6. **Practical 6: 8-Queens CSP using Backtracking**
   * *Title*: Implement Backtracking to Solve the 8-Queens Constraint Satisfaction Problem
   * *Core Concepts*: Constraint satisfaction problems (CSP), backtracking search, row/column/diagonal conflict prevention.
7. **Practical 7: Intelligent Number-Guessing Agent**
   * *Title*: Design an Intelligent Agent to Guess a Number Using Higher/Lower Feedback
   * *Core Concepts*: Binary search agents, percept feedback, logarithmic time complexity, boundary convergence.
8. **Practical 8: Minimax Game-Playing Agent**
   * *Title*: Implement a Game-Playing Agent Using the Minimax Algorithm
   * *Core Concepts*: Tic-Tac-Toe representation, adversarial decision-making, terminal utility scoring, automated simulation.
9. **Mini-Project: Rule-Based Recommendation System**
   * *Title*: Rule-Based Programming Language and Project Recommendation System
   * *Core Concepts*: Expert systems, structured IF–THEN knowledge rules, multi-attribute profile matching, validation, and fallback mechanisms.

## Verification Status

All 9 notebooks have been executed from beginning to end in the dedicated Python virtual environment (`ai_cs_venv`). Every cell ran to completion without errors and produced complete, verified output traces that are persisted directly within the `.ipynb` files.

| Notebook | Execution Status | Automated Checks | Verification Result |
| :--- | :---: | :---: | :---: |
| `01_vacuum_cleaner_agent.ipynb` | **Executed** | Multi-scenario test, clean verification | **VERIFIED** |
| `02_astar_8_puzzle.ipynb` | **Executed** | Optimal path, solvability check, goal match | **VERIFIED** |
| `03_alpha_beta_pruning.ipynb` | **Executed** | Minimax match, leaf savings, prune trace | **VERIFIED** |
| `04_tower_of_hanoi.ipynb` | **Executed** | 7-move optimal bound, legal transitions | **VERIFIED** |
| `05_bfs_path_planning.ipynb` | **Executed** | Obstacle-free path, blocked case handling | **VERIFIED** |
| `06_eight_queens.ipynb` | **Executed** | 8 queens placed, zero attacks verified | **VERIFIED** |
| `07_number_guessing_agent.ipynb` | **Executed** | Boundary tests, $\le 7$ guesses verified | **VERIFIED** |
| `08_minimax_tic_tac_toe.ipynb` | **Executed** | Win/block detection, full game simulation | **VERIFIED** |
| `09_rule_based_recommendation.ipynb` | **Executed** | Multi-profile evaluation, fallback tests | **VERIFIED** |

*Verification Summary: 9 / 9 notebooks executed, tested, and verified successfully.*
