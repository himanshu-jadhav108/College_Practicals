# Artificial Intelligence Laboratory — Visualized Practicals Suite

> **Department of Computer Science & Engineering**  
> **Course:** Artificial Intelligence Laboratory  
> **Target Audience:** Undergraduate Computer Science Students & Practical Examiners

---

## 1. Project Overview

The **Visualized Practicals Suite** transforms the standard undergraduate Artificial Intelligence lab curriculum into a visually rich, interactive, mathematically grounded, and rigorously verified educational collection of Jupyter Notebooks.

Every practical in this collection contains:
* **Academic Theory & Formal Formulation**: Problem definition, state representation, search space characteristics, and optimality bounds.
* **Pure Python Implementation**: Core algorithms implemented cleanly without black-box library wrappers so students can study every decision step.
* **Dual-Layer Visualization Engine**:
  * **Static Graphical Diagrams (`matplotlib`)**: Production-ready, publication-style visual representations showing initial states, state transitions, explored wavefronts, and final solutions.
  * **Interactive Exploration Widgets (`ipywidgets`)**: Live sliders, previous/next steppers, and mode selectors allowing students to inspect algorithms step-by-step or test interactive scenarios live during practical exams.
* **Automated Verification Suites**: Rigorous inline test cells running boundary assertions, parity checks, constraint solvers, and optimality verifications.
* **Responsive Metric Cards (HTML/CSS)**: Clean summary dashboards displaying state space sizes, expanded nodes, pruning ratios, and solution optimality.

---

## 2. The Nine Practicals Overview

| # | Practical Filename | Topic / Algorithm | Key Visualization Features | Interactive Controls |
|---|---|---|---|---|
| **01** | `01_vacuum_cleaner_agent.ipynb` | **Reflex Agent Environment** | Dual-room visual schematic (Room A & B), dirty/clean status badges, agent sprite position, pre/post execution comparison. | Step-by-step room transition stepper, reset environment button. |
| **02** | `02_astar_8_puzzle.ipynb` | **A\* Search with Manhattan Heuristic** | 3×3 grid tiles, highlighted blank tile, tile displacement vectors, Manhattan distance breakdowns ($g, h, f$). | Move-by-move solution stepper slider, step navigation buttons. |
| **03** | `03_alpha_beta_pruning.ipynb` | **Adversarial Search & Alpha-Beta Cutoffs** | Complete 4-tier game tree diagram with MAX/MIN level badges, cutoff dashed edges, and cutoff condition banners ($\beta \le \alpha$). | Search mode toggle: Full Minimax vs. Alpha-Beta Pruning. |
| **04** | `04_tower_of_hanoi.ipynb` | **BFS State-Space Planning** | Scaled colored disks on 3 vertical pegs with base platform, legal disk order constraints, and step counters. | Disk movement stepper slider, previous/next move buttons. |
| **05** | `05_bfs_path_planning.ipynb` | **Grid Robot Path Planning** | 6×6 discrete grid map, obstacle barriers, BFS wavefront exploration markers, and optimal green path trace. | Grid inspection stepper, path coordinate waypoint tracker. |
| **06** | `06_eight_queens.ipynb` | **Backtracking CSP** | 8×8 light/dark chessboard, golden queen crowns, conflict-free row/column/diagonal arrangement. | Interactive queen row placement inspector, board reset. |
| **07** | `07_number_guessing_agent.ipynb` | **Binary Search Reflex Agent** | Logarithmic search interval convergence bars, candidate range shrinkage, and guess-by-guess percept history. | Custom target number slider, search speed controller. |
| **08** | `08_minimax_tic_tac_toe.ipynb` | **Zero-Loss Minimax Game Engine** | 3×3 game board with color-coded marks (Human 'X' vs. AI 'O'), winning line indicator, terminal outcome overlay. | Interactive move coordinate selector, game reset button. |
| **09** | `09_rule_based_recommendation.ipynb` | **Rule-Based Expert System** | 5-stage inference pipeline flowchart, styled recommendation cards, rule matching trace and domain filters. | Multi-dropdown dashboard (Domain, Experience, Difficulty, Interest). |

---

## 3. Recommended Execution Order

To maximize conceptual clarity, execute the notebooks in their natural pedagogical sequence:

1. **Foundations of AI Agents**:
   - `01_vacuum_cleaner_agent.ipynb` (Simple Reflex Agent & Percept-Action Loop)
2. **Informed Heuristic Search**:
   - `02_astar_8_puzzle.ipynb` (A\* Search, Admissible Heuristics, State-Space Trees)
3. **Adversarial Decision Making**:
   - `03_alpha_beta_pruning.ipynb` (Game Trees, Minimax, $\alpha\text{–}\beta$ Pruning Optimization)
4. **Uninformed State-Space Search**:
   - `04_tower_of_hanoi.ipynb` (Graph Search Formulation, BFS Shortest Path)
   - `05_bfs_path_planning.ipynb` (Grid Navigation, 4-Connected Movement, Wavefront Expansion)
5. **Constraint Satisfaction Problems (CSP)**:
   - `06_eight_queens.ipynb` (Variables, Domains, Backtracking Search, Diagonal Pruning)
6. **Agent Strategy & Game Theory**:
   - `07_number_guessing_agent.ipynb` (Logarithmic Convergence, Binary Search Policy)
   - `08_minimax_tic_tac_toe.ipynb` (Two-Player Zero-Sum Game, Terminal Utilities, Zero-Loss Policy)
7. **Expert Knowledge Systems**:
   - `09_rule_based_recommendation.ipynb` (Rule-Based Expert System, IF–THEN Inference, Domain Filtering)

---

## 4. Setup Instructions & Dependencies

### Python Environment
* **Python Version**: Python 3.10, 3.11, 3.12, or 3.13
* **Virtual Environment**: Recommended to avoid conflicts with system packages.

### Required Dependencies
The suite uses standard, lightweight scientific Python packages:
```bash
pip install matplotlib ipywidgets notebook
```
*(Optional for headless testing: `nbclient`, `nbformat`)*

### Quick Start
1. Open PowerShell or Terminal in the repository root:
   ```powershell
   cd "D:\College Practicals\Artificial_Intelligence\AI for CS Branch\Visualized"
   ```
2. Activate your virtual environment (if using one):
   ```powershell
   ..\..\venv\Scripts\Activate.ps1
   ```
3. Launch Jupyter Notebook or JupyterLab:
   ```powershell
   jupyter notebook
   ```
4. In the browser interface, click on any notebook (e.g., `01_vacuum_cleaner_agent.ipynb`) to open it.

---

## 5. How to Run a Practical & Interact

### Standard Execution
* In the Jupyter menu, select **Cell** $\rightarrow$ **Run All** (or press `Shift + Enter` to execute cell-by-cell).
* Every notebook executes completely from top to bottom with zero external setup required.

### Interacting with Visualizations
1. **Static Visualizations**: Rendered immediately below the *Static Demonstration* code cell using `matplotlib`. These provide clean, static diagrams suitable for lab record submissions and screenshot documentation.
2. **Interactive Widgets**: Rendered in the *Interactive Demonstration* cell. Use the controls:
   * **Sliders**: Drag to scrub back and forth through algorithm iterations (e.g., puzzle moves, search bounds, disk placements).
   * **Buttons (`◀ Prev`, `Next ▶`, `Reset ↺`)**: Step through state transitions one step at a time.
   * **Dropdowns / Radios**: Select input parameters (e.g., career domain, search modes) to see dynamic re-computation.

---

## 6. Verification and Quality Audit Status

All 9 notebooks have been executed from a fresh kernel using automated test harnesses.

| Notebook | Code Cells | Test Suite Status | Plots Rendered | HTML Cards | Audit Result |
|---|---|---|---|---|---|
| `01_vacuum_cleaner_agent.ipynb` | 7 | 100% Passed (4 Environment Tests) | 2 | 1 | **VERIFIED** |
| `02_astar_8_puzzle.ipynb` | 7 | 100% Passed (Solvability Parity & Optimal A\*) | 1 | 1 | **VERIFIED** |
| `03_alpha_beta_pruning.ipynb` | 7 | 100% Passed (Minimax Equivalence & 37.5% Pruning) | 2 | 1 | **VERIFIED** |
| `04_tower_of_hanoi.ipynb` | 7 | 100% Passed (Disk Invariant & 7-Move Optimality) | 1 | 1 | **VERIFIED** |
| `05_bfs_path_planning.ipynb` | 7 | 100% Passed (10-Step Optimal Path & Barrier Check) | 2 | 1 | **VERIFIED** |
| `06_eight_queens.ipynb` | 7 | 100% Passed (All CSP Constraints Verified) | 1 | 1 | **VERIFIED** |
| `07_number_guessing_agent.ipynb` | 7 | 100% Passed (Boundaries 1, 100 & Random Targets $\le$ 7 Guesses) | 2 | 1 | **VERIFIED** |
| `08_minimax_tic_tac_toe.ipynb` | 7 | 100% Passed (Zero-Loss Guarantee & Full Match Simulation) | 2 | 1 | **VERIFIED** |
| `09_rule_based_recommendation.ipynb` | 7 | 100% Passed (Multi-Domain Inferences & Schema Error Handling) | 1 | 3 | **VERIFIED** |

*Integrity Check:* The original folder `AI for CS Branch\Normal` remains 100% protected, intact, and unmodified.
