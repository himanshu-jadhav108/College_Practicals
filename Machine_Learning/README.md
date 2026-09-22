# 🧠 Machine Learning (ML) Practicals – SPPU 2024

> **Third-Year / Final-Year Engineering | Artificial Intelligence & Data Science | Savitribai Phule Pune University**  
> **Author:** Himanshu Jadhav (Roll No: TE-32)

![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-v1.3%2B-orange?logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-v1.24%2B-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-v2.x-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-v1.10%2B-8CAAE6?logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-v3.7%2B-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-v0.12%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed%20(100%25)-brightgreen)
![SPPU](https://img.shields.io/badge/University-SPPU%202024-orange)

---

## 📌 Repository Overview

This repository houses a comprehensive, dual-tiered laboratory suite for **Machine Learning (ML)**, engineered strictly in alignment with the **Savitribai Phule Pune University (SPPU)** Artificial Intelligence and Data Science curriculum.

Every experiment has been designed with a dual-track implementation pedagogy:

- **🟢 Basic Implementation:** Clean, self-contained conceptual notebooks emphasizing mathematical foundations, foundational workflows, algorithmic mechanics, and standard Scikit-Learn / NumPy APIs.
- **🚀 Advance Implementation:** Production-grade, mathematically rigorous notebooks featuring LaTeX theoretical formulations, custom algorithmic implementations from scratch, multi-dimensional ablation studies, extensive hyperparameter optimization (`GridSearchCV`), publication-quality diagnostic visualizations (residual analysis, learning curves, ROC-AUC, Voronoi tessellations, decision boundaries, Q-value surface plots), and modular Object-Oriented (OOP) pipelines.

All notebooks are pre-executed with cell outputs, evaluation tables, and figures preserved for evaluation and offline review.

---

## 📁 Repository Directory Structure

```
Machine_Learning/
├── README.md                                          ← Comprehensive repository guide & syllabus mapping
├── requirements.txt                                   ← Categorized dependencies with version pins
│
├── Practical_01/                                      ← Feature Engineering (Imputation, Encoding & Scaling)
│   ├── Basic/
│   │   └── Practical_01.ipynb
│   └── Advance/
│       └── Practical_01_Advance.ipynb
│
├── Practical_02/                                      ← Dimensionality Reduction & Manifold Learning (PCA & LDA)
│   ├── Basic/
│   │   └── Practical_02.ipynb
│   └── Advance/
│       └── Practical_02.ipynb
│
├── Practical_03/                                      ← Multiple Linear Regression & Regularization (OLS, VIF)
│   ├── Basic/
│   │   └── Practical_03.ipynb
│   └── Advance/
│       └── Practical_03_Advance.ipynb
│
├── Practical_04/                                      ← Polynomial Regression & Bias-Variance Diagnostics
│   ├── Basic/
│   │   └── Practical_04.ipynb
│   └── Advance/
│       └── Practical_04.ipynb
│
├── Practical_05/                                      ← Regularized Regression (Ridge, Lasso & ElasticNet Dynamics)
│   ├── Basic/
│   │   └── Practical_05.ipynb
│   └── Advance/
│       └── Practical_05_Advance.ipynb
│
├── Practical_06/                                      ← Logistic Regression & Classification Diagnostics
│   ├── Basic/
│   │   └── Practical_06.ipynb
│   └── Advance/
│       └── Practical_06_Advance.ipynb
│
├── Practical_07/                                      ← Support Vector Machines (Linear, RBF & Kernel Geometry)
│   ├── Basic/
│   │   └── Practical_07.ipynb
│   └── Advance/
│       └── Practial_07_Advance.ipynb
│
├── Practical_08/                                      ← K-Means Clustering & Validation Metrics (Elbow, Silhouette)
│   ├── Basic/
│   │   ├── Practical_08.ipynb
│   │   └── Practical_08_extra.ipynb
│   └── Advance/
│       ├── Practical_08_Advance.ipynb
│       └── Practical_08_Advance_Extra.ipynb
│
├── Practical_09/                                      ← Density-Based Spatial Clustering (DBSCAN & k-Distance)
│   ├── Basic/
│   │   ├── Practical_09_Basic.ipynb
│   │   ├── Practical_09_Basic_Extra.ipynb
│   │   └── wildlife_gps_tracking.csv
│   └── Advance/
│       ├── Practical_09_Advanced.ipynb
│       ├── Practical_09_Advance_Extra.ipynb
│       └── wildlife_gps_tracking.csv
│
├── Practical_10/                                      ← Ensemble Learning (Bagging, Boosting, Stacking & Voting)
│   ├── Basic/
│   │   ├── Practical_10.ipynb
│   │   └── anime_success_dataset.csv
│   └── Advance/
│       ├── Practical_10_Advance.ipynb
│       └── anime_success_dataset.csv
│
└── Practical_11/                                      ← Reinforcement Learning (Q-Learning vs SARSA on Grid World)
    ├── Basic/
    │   └── Practical_11_Basic.ipynb
    └── Advance/
        └── Practical_11_Advanced.ipynb
```

---

## 📚 Practical Curriculum & Syllabus Mapping

| # | Curriculum Topic & Focus | Basic Implementation | Advance Implementation | Key Algorithms, Formulations & Theoretical Scope | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **01** | **Feature Engineering for Machine Learning** | [`Practical_01.ipynb`](./Practical_01/Basic/Practical_01.ipynb) | [`Practical_01_Advance.ipynb`](./Practical_01/Advance/Practical_01_Advance.ipynb) | Missing value imputation strategies, categorical encoding (One-Hot, Ordinal), numerical scaling (StandardScaler, MinMaxScaler, RobustScaler), outlier detection via IQR, Auto MPG dataset. | `Completed` |
| **02** | **Dimensionality Reduction & Manifold Learning** | [`Practical_02.ipynb`](./Practical_02/Basic/Practical_02.ipynb) | [`Practical_02.ipynb`](./Practical_02/Advance/Practical_02.ipynb) | Principal Component Analysis (PCA), Incremental PCA (IPCA), Kernel PCA (RBF/poly), Linear Discriminant Analysis (LDA), t-SNE projection, TruncatedSVD, Scree variance ratio plots, 64-feature Digits dataset. | `Completed` |
| **03** | **Multiple Linear Regression & Diagnostics** | [`Practical_03.ipynb`](./Practical_03/Basic/Practical_03.ipynb) | [`Practical_03_Advance.ipynb`](./Practical_03/Advance/Practical_03_Advance.ipynb) | Ordinary Least Squares (OLS), Multicollinearity Diagnostics via Variance Inflation Factor (VIF), residual homoscedasticity & normality tests (Q-Q plot), Cross-Validation, MSE/RMSE/MAE/$R^2$, Diabetes dataset. | `Completed` |
| **04** | **Polynomial Regression & Bias-Variance Diagnostics** | [`Practical_04.ipynb`](./Practical_04/Basic/Practical_04.ipynb) | [`Practical_04.ipynb`](./Practical_04/Advance/Practical_04.ipynb) | Non-linear polynomial feature transformations ($d=1 \dots 15$), Bias-Variance decomposition, underfitting vs. overfitting trade-offs, learning curves, train vs. validation loss divergence, L2 Ridge dampening. | `Completed` |
| **05** | **Regularized Linear Models (Ridge, Lasso & ElasticNet)** | [`Practical_05.ipynb`](./Practical_05/Basic/Practical_05.ipynb) | [`Practical_05_Advance.ipynb`](./Practical_05/Advance/Practical_05_Advance.ipynb) | L1 sparsity vs. L2 weight shrinkage dynamics, ElasticNet compromise ($\alpha, l_1\text{ ratio}$), coefficient trace paths, $k$-fold cross-validation grid search (`GridSearchCV`), multicollinearity mitigation. | `Completed` |
| **06** | **Logistic Regression & Classification Metrics** | [`Practical_06.ipynb`](./Practical_06/Basic/Practical_06.ipynb) | [`Practical_06_Advance.ipynb`](./Practical_06/Advance/Practical_06_Advance.ipynb) | Sigmoid function geometry, binary & multiclass (OvR vs. Multinomial) classification, L1/L2 penalties, Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC curves, Breast Cancer Diagnostic dataset. | `Completed` |
| **07** | **Support Vector Machines & Kernel Geometry** | [`Practical_07.ipynb`](./Practical_07/Basic/Practical_07.ipynb) | [`Practial_07_Advance.ipynb`](./Practical_07/Advance/Practial_07_Advance.ipynb) | Maximal margin hyperplanes, Kernel Trick geometry (Linear, Polynomial, RBF, Sigmoid), support vector extraction, dual hyperparameter grid search ($C, \gamma$), multiclass decision boundaries, Wine Recognition dataset. | `Completed` |
| **08** | **K-Means Clustering & Cluster Validation** | [`Practical_08.ipynb`](./Practical_08/Basic/Practical_08.ipynb)<br>[`Practical_08_extra.ipynb`](./Practical_08/Basic/Practical_08_extra.ipynb) | [`Practical_08_Advance.ipynb`](./Practical_08/Advance/Practical_08_Advance.ipynb)<br>[`Practical_08_Advance_Extra.ipynb`](./Practical_08/Advance/Practical_08_Advance_Extra.ipynb) | K-Means++ vs. Random initialization stability, Within-Cluster Sum of Squares (WCSS) Elbow curve, Silhouette coefficient plots, Calinski-Harabasz & Davies-Bouldin metrics, Voronoi tessellations, 2D PCA cluster centroids. | `Completed` |
| **09** | **Density-Based Spatial Clustering (DBSCAN)** | [`Practical_09_Basic.ipynb`](./Practical_09/Basic/Practical_09_Basic.ipynb)<br>[`Practical_09_Basic_Extra.ipynb`](./Practical_09/Basic/Practical_09_Basic_Extra.ipynb) | [`Practical_09_Advanced.ipynb`](./Practical_09/Advance/Practical_09_Advanced.ipynb)<br>[`Practical_09_Advance_Extra.ipynb`](./Practical_09/Advance/Practical_09_Advance_Extra.ipynb) | $k$-Distance plot for heuristic optimal $\varepsilon$, joint $(\varepsilon, \text{MinPts})$ grid search, Core / Border / Noise classification, non-spherical arbitrary density discovery, Wildlife GPS tracking & Geospatial datasets. | `Completed` |
| **10** | **Ensemble Learning (Bagging, Boosting & Stacking)** | [`Practical_10.ipynb`](./Practical_10/Basic/Practical_10.ipynb) | [`Practical_10_Advance.ipynb`](./Practical_10/Advance/Practical_10_Advance.ipynb) | Baseline Decision Tree, Random Forest with Out-of-Bag (OOB) scoring, AdaBoost with adaptive weights, Gradient Boosting with residual fitting, Soft/Hard Voting classifiers, Stacking meta-learners, Anime Success dataset. | `Completed` |
| **11** | **Reinforcement Learning on Grid World** | [`Practical_11_Basic.ipynb`](./Practical_11/Basic/Practical_11_Basic.ipynb) | [`Practical_11_Advanced.ipynb`](./Practical_11/Advance/Practical_11_Advanced.ipynb) | Model-free Temporal Difference (TD) control, Q-Learning (Off-Policy Bellman optimality) vs. SARSA (On-Policy TD update), Custom 2D Grid World ("The Shrine Trial"), $\varepsilon$-greedy exploration-exploitation decay, 3D Value Function surface plots. | `Completed` |

---

## 🔬 In-Depth Practical Walkthroughs

### 🟢 Practical 01: Feature Engineering for Machine Learning

- **Objective:** Master foundational data preprocessing techniques including missing value handling, categorical feature encoding, numerical feature scaling, and distribution analysis on tabular datasets.
- **Implementations:**
  - **Basic:** Univariate analysis, identifying missing values in the Auto MPG dataset, imputing numerical attributes with statistical metrics (mean/median), One-Hot and Ordinal encoding, and comparing `StandardScaler` vs. `MinMaxScaler`.
  - **Advance:** Comprehensive feature engineering pipeline:
    - Advanced multivariate and KNN-based missing value imputation.
    - Robust outlier detection using Interquartile Range (IQR) and Z-score gating.
    - Comparative feature transformation benchmarking across `StandardScaler`, `MinMaxScaler`, and `RobustScaler` on skewed distributions.
    - End-to-end scikit-learn `Pipeline` and `ColumnTransformer` integration preventing data leakage.

### 🟢 Practical 02: Dimensionality Reduction & Manifold Learning

- **Objective:** Mitigate the curse of dimensionality, preserve explained variance, and project high-dimensional data into lower-dimensional manifolds for visualization and classification.
- **Implementations:**
  - **Basic:** Unsupervised dimensionality reduction using Principal Component Analysis (PCA) and supervised reduction using Linear Discriminant Analysis (LDA) on the 64-pixel handwritten digits dataset; 2D projection scatter plots and variance ratio scree analysis.
  - **Advance:** Multi-algorithm dimensionality reduction and manifold benchmarking suite:
    - Standard Batch PCA vs. Incremental PCA (IPCA) for memory-efficient out-of-core learning.
    - Non-linear manifold learning with Kernel PCA (RBF, Polynomial, and Cosine kernels).
    - t-Distributed Stochastic Neighbor Embedding (t-SNE) for local neighborhood preservation.
    - TruncatedSVD for sparse matrix decomposition.
    - Downstream classification benchmarking across varying component counts ($k \in [2, 10, 20, 30, 40]$).

### 🟢 Practical 03: Multiple Linear Regression & Diagnostics

- **Objective:** Formulate multiple linear regression models, evaluate goodness-of-fit metrics, diagnose multicollinearity, and validate classical linear regression assumptions.
- **Implementations:**
  - **Basic:** Ordinary Least Squares (OLS) regression on the open-access Diabetes dataset, evaluating Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and Coefficient of Determination ($R^2$).
  - **Advance:** Comprehensive econometric and statistical regression diagnostics:
    - Multicollinearity detection using the Variance Inflation Factor (VIF) and correlation matrices.
    - Gauss-Markov assumption validation: residual normality via Q-Q plots, homoscedasticity via Breusch-Pagan / Residuals vs. Fitted plots.
    - Direct performance benchmarking of OLS vs. Ridge, Lasso, and ElasticNet under high multicollinearity.
    - $k$-fold cross-validated performance bounds.

### 🟢 Practical 04: Polynomial Regression & Model Complexity Diagnostics

- **Objective:** Analyze non-linear response surfaces using polynomial basis expansions and empirically study the Bias-Variance trade-off across varying model complexities.
- **Implementations:**
  - **Basic:** Polynomial regression across degrees $d \in \{1, 2, 3, 5, 9\}$ on a non-linear dataset, demonstrating underfitting at low degrees and overfitting oscillations at higher degrees.
  - **Advance:** In-depth bias-variance decomposition and diagnostic suite:
    - Extended polynomial expansion spanning degrees $d = 1$ to $d = 15$.
    - Training vs. Validation learning curves illustrating sample size scaling behavior and variance degradation.
    - Regularization dampening: applying L2 Ridge regression to high-degree polynomials to suppress coefficient explosion while retaining non-linear expressiveness.
    - Generalization gap analysis across cross-validation folds.

### 🟢 Practical 05: Regularized Linear Models (Ridge, Lasso & ElasticNet)

- **Objective:** Implement penalization dynamics to control model variance, induce feature sparsity, and stabilize ill-conditioned regression matrices.
- **Implementations:**
  - **Basic:** Comparing standard Linear Regression against Ridge (L2 penalty) and Lasso (L1 penalty) on synthetic multicollinear polynomial features; tracking coefficient shrinkage.
  - **Advance:** Rigorous regularization dynamic exploration:
    - Mathematical formulation and comparison of $L_1$ norm (Manhattan) diamond geometry vs. $L_2$ norm (Euclidean) spherical geometry.
    - ElasticNet hybridization combining both penalties ($\alpha \cdot l_1\text{ ratio} + \frac{\alpha (1 - l_1\text{ ratio})}{2}$).
    - Continuous coefficient path trajectories as regularization strength $\lambda$ varies over decades ($10^{-4}$ to $10^{4}$).
    - Exhaustive hyperparameter grid search (`RidgeCV`, `LassoCV`, `ElasticNetCV`) with automated optimal penalty selection.

### 🟢 Practical 06: Logistic Regression & Classification Diagnostics

- **Objective:** Implement probabilistic binary and multiclass classification, construct decision thresholds, and compute comprehensive performance metrics.
- **Implementations:**
  - **Basic:** Binary classification on the Wisconsin Diagnostic Breast Cancer (WDBC) dataset; sigmoid activation, log-loss convergence, confusion matrix, classification report (Precision, Recall, F1-Score), and ROC curve.
  - **Advance:** Production-grade classification diagnostic suite:
    - One-vs-Rest (OvR) vs. Multinomial Softmax cross-entropy comparison for multi-category targets.
    - Regularized logistic classification exploring $L_1$ (sparse feature selection) and $L_2$ penalties with liblinear and lbfgs solvers.
    - Decision boundary contour visualization across 2D reduced feature spaces.
    - Precision-Recall (PR) curves, ROC-AUC metric benchmarking, and decision threshold calibration curves.

### 🟢 Practical 07: Support Vector Machines & Kernel Geometry

- **Objective:** Understand maximal margin hyperplanes, the dual optimization problem, support vector identification, and the non-linear Kernel Trick.
- **Implementations:**
  - **Basic:** Support Vector Classifier (SVC) training on the Wine Recognition multiclass dataset; comparative evaluation of Linear, Polynomial, and Radial Basis Function (RBF) kernels.
  - **Advance:** Deep mathematical kernel diagnostics and geometry:
    - Support vector extraction, counting, and boundary distance distribution analysis.
    - Kernel Trick exploration: Linear, Polynomial ($d \in \{2, 3, 5\}$), RBF ($\gamma$), and Sigmoid kernels.
    - Dual hyperparameter optimization grid search over cost parameter $C \in [0.1, 1000]$ and kernel bandwidth $\gamma \in [0.001, 1]$.
    - Multiclass Decision boundary surface contour plots and macro/micro-averaged ROC-AUC analysis.

### 🟢 Practical 08: K-Means Clustering & Cluster Validation Diagnostics

- **Objective:** Segment unlabeled feature spaces into coherent partitions and quantitatively evaluate cluster compactness and separation.
- **Implementations:**
  - **Basic:** K-Means clustering on synthetic datasets and handwritten digits; Within-Cluster Sum of Squares (WCSS) Elbow Method and average Silhouette score computation.
  - **Advance:** Comprehensive cluster validation diagnostic suite:
    - Algorithmic initialization stability: K-Means++ distance-weighted sampling vs. standard Random initialization.
    - Multi-metric validation: WCSS Elbow Curve, Per-Sample Silhouette Analysis diagrams with silhouette thickness profiling.
    - Internal clustering quality metrics: Calinski-Harabasz Index (variance ratio) and Davies-Bouldin Index.
    - Voronoi tessellation decision regions and 2D PCA cluster centroid scatter plots on high-dimensional digits data.

### 🟢 Practical 09: Density-Based Spatial Clustering (DBSCAN)

- **Objective:** Discover clusters of arbitrary non-spherical shapes, handle noise and outliers effectively, and evaluate density-reachability algorithms.
- **Implementations:**
  - **Basic:** DBSCAN clustering on simulated non-spherical urban ride-pickup locations; finding optimal neighborhood radius $\varepsilon$ via the sorted $k$-distance nearest-neighbor graph; core vs. noise point identification.
  - **Advance:** Advanced spatial density analysis on simulated geospatial data and custom Wildlife GPS tracking datasets:
    - Sorted $k$-Distance plot for heuristic optimal $\varepsilon$ knee-point detection.
    - Joint 2D grid search over neighborhood radius $\varepsilon$ and `min_samples` parameter pairs evaluated by Silhouette score.
    - Point-type classification: Core points ($\ge \text{MinPts}$ within $\varepsilon$), Border points, and Noise outliers ($-1$).
    - Direct head-to-head comparison: DBSCAN vs. K-Means on complex non-convex manifold geometries.

### 🟢 Practical 10: Ensemble Learning (Bagging, Boosting & Stacking)

- **Objective:** Leverage collective intelligence by combining diverse weak learners to minimize bias and variance through Bagging, Boosting, and Stacking meta-architectures.
- **Implementations:**
  - **Basic:** Single Decision Tree baseline vs. Random Forest Classifier and AdaBoost on tabular datasets; performance evaluation and comparison of classification metrics.
  - **Advance:** Production-grade meta-ensemble benchmarking workstation:
    - Baseline: Unpruned Single Decision Tree diagnostics.
    - Bagging: Random Forest with bootstrap aggregation and Out-of-Bag (OOB) error estimation.
    - Boosting: AdaBoost with sequential sample weight updating vs. Gradient Boosting with gradient residual minimization.
    - Ensemble Fusion: Hard Voting (majority rule), Soft Voting (weighted class probabilities), and Stacking Classifiers with Logistic Regression blender.
    - Gini impurity-based feature importance ranking and learning curve comparison on a custom Anime Success dataset (`anime_success_dataset.csv`).

### 🟢 Practical 11: Reinforcement Learning on Custom Grid World

- **Objective:** Implement model-free Temporal Difference (TD) reinforcement learning algorithms to train autonomous agents navigating complex stochastic grid worlds.
- **Implementations:**
  - **Basic:** Implementation of the classic Off-Policy Q-Learning algorithm on a custom Grid World environment ("The Shrine Trial"); defining state spaces, discrete action sets, transition dynamics, reward structures, and Q-table updates.
  - **Advance:** Advanced Reinforcement Learning comparison and diagnostic suite:
    - Custom Grid World ("The Shrine Trial") featuring obstacles, deadly pits/hazards, goal rewards, and blessed bonus tiles.
    - Off-Policy Q-Learning (Bellman Optimality equation: $Q(s, a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s,a)]$) vs. On-Policy SARSA ($Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma Q(s', a') - Q(s,a)]$).
    - Adaptive $\varepsilon$-greedy exploration-exploitation decay schedules ($\varepsilon_{\text{decay}}$).
    - Cumulative episode reward convergence curves and rolling mean trend analysis.
    - 3D Value Function surface plots ($V(s) = \max_a Q(s,a)$) and heatmaps showing optimal navigational vector policies.

---

## 🚀 Installation & Quickstart Guide

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/himanshu-jadhav108/College_Practicals.git
cd College_Practicals/Machine_Learning
```

### Step 2: Set Up Python Virtual Environment

It is strongly recommended to use Python **3.10**, **3.11**, or **3.12**:

```bash
# Create the virtual environment
python -m venv ml_env

# Activate on Windows (PowerShell)
.\ml_env\Scripts\Activate.ps1

# Activate on Windows (Command Prompt)
.\ml_env\Scripts\activate.bat

# Activate on Linux / macOS
source ml_env/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Environment & Core Libraries

Run a quick verification command to check the installation of key scientific libraries:

```bash
python -c "import numpy, pandas, sklearn, matplotlib, seaborn, scipy, statsmodels; print('All ML dependencies successfully imported!')"
```

### Step 5: Register the Virtual Environment Kernel in Jupyter

```bash
python -m ipykernel install --user --name=ml_env --display-name="Python (ml_env)"
```

### Step 6: Launch Jupyter Notebook or JupyterLab

```bash
jupyter notebook
```

> In Jupyter, select the **Python (ml_env)** kernel from the top-right kernel dropdown when opening any notebook.

---

## 🛠️ Technology Stack & Dependencies

| Category | Primary Libraries | Version Range | Purpose |
| :--- | :--- | :--- | :--- |
| **Core Computing** | `numpy`, `pandas`, `scipy` | `>=1.24.0`, `>=2.0.0`, `>=1.10.0` | High-performance numerical arrays, linear algebra, tabular manipulation |
| **Machine Learning** | `scikit-learn` | `>=1.3.0` | Preprocessing, regressions, SVM, clustering, ensemble models, model evaluation |
| **Statistical Diagnostics** | `statsmodels` | `>=0.14.0` | OLS summary statistics, Variance Inflation Factor (VIF), hypothesis testing |
| **Visualization** | `matplotlib`, `seaborn` | `>=3.7.0`, `>=0.12.0` | Decision boundaries, ROC curves, Voronoi tessellations, residual plots |
| **Formatting & Utilities** | `tabulate`, `tqdm` | `>=0.9.0`, `>=4.66.0` | Publication-style markdown/ASCII comparison tables, iteration progress bars |
| **Interactive Runtime** | `jupyter`, `notebook`, `ipykernel`, `nbconvert` | `>=1.0.0`, `>=7.0.0`, `>=6.25.0`, `>=7.10.0` | Interactive notebook execution, rendering, and markdown/HTML export |

---

## ⚙️ Technical Design Notes & Best Practices

1. **Deterministic Reproducibility:**  
   All random seeds across NumPy (`np.random.seed(42)`) and Scikit-Learn estimators (`random_state=42`) are explicitly pinned across all notebooks to guarantee 100% reproducible splits, synthetic clusters, and model evaluations.
2. **Data Leakage Prevention:**  
   All preprocessing operations (imputation, scaling, encoding) are strictly fitted on the training split only (`fit_transform`) and applied to the test split (`transform`), utilizing scikit-learn `Pipeline` and `ColumnTransformer` constructs.
3. **Rigorous Statistical Diagnostics:**  
   Models are validated beyond simple accuracy; regression tasks evaluate $R^2$, RMSE, MAE, VIF, and residual homoscedasticity; classification tasks evaluate precision-recall trade-offs, confusion matrices, and ROC-AUC curves; clustering tasks evaluate Silhouette, Calinski-Harabasz, and Davies-Bouldin indices.
4. **Cross-Platform Compatibility:**  
   All dataset file paths and operations utilize relative paths with cross-platform formatting (`os.path` / `pathlib`), ensuring immediate out-of-the-box execution across Windows, Linux, and macOS environments.
5. **Pre-Executed Artifact Integrity:**  
   Every notebook contains saved execution outputs, diagnostic graphs, and convergence plots, facilitating immediate assessment and offline review.

---

## 👨‍💻 Author & Academic Information

- **Student:** Himanshu Jadhav
- **Roll Number:** TE-32
- **Degree Program:** Bachelor of Engineering (B.E.)
- **Specialization:** Artificial Intelligence & Data Science (AI & DS)
- **Institution:** Savitribai Phule Pune University (SPPU)
- **Academic Year:** 2024 – 2028

---

[⬅️ Back to Main Repository](../README.md)
