# ☁️ Cloud Computing Practicals & Case Studies – SPPU 2024

> **Third-Year / Final-Year Engineering | Artificial Intelligence & Data Science | Savitribai Phule Pune University**  
> **Course:** Cloud Computing Laboratory (SPPU Curriculum)  
> **Author:** [Himanshu Jadhav](https://github.com/himanshu-jadhav108) (Roll No: TE-32)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Cloud-AWS](https://img.shields.io/badge/Cloud-AWS%20%7C%20Azure%20%7C%20GCP-orange?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Security](https://img.shields.io/badge/Security-Zero--Trust%20%7C%20IAM-red?logo=auth0&logoColor=white)](#)
[![Cryptography](https://img.shields.io/badge/Crypto-RSA--2048%20%7C%20SHA--256%20%7C%20JWT-yellow?logo=letsencrypt&logoColor=white)](#)
[![SciPy](https://img.shields.io/badge/SciPy-Signal%20Processing-blue?logo=scipy&logoColor=white)](https://scipy.org/)
[![Status](<https://img.shields.io/badge/Status-Completed%20(100%25)-brightgreen>)](#)
[![University](https://img.shields.io/badge/University-SPPU%202024-orange)](http://www.unipune.ac.in/)

---

## 📌 Repository Overview

This repository houses the complete practical package and case study portfolio for **Cloud Computing**, engineered specifically in accordance with the **Savitribai Phule Pune University (SPPU)** curriculum for Artificial Intelligence and Data Science Engineering.

The laboratory package covers two foundational units through a rigorous two-pronged methodology:

1. **Applied Computational Case Studies & Demonstrations:** Interactive, reproducible Python and Jupyter Notebook implementations evaluating core algorithmic workloads (Bioinformatics sequence alignment, lattice protein folding, biomedical signal telemetry, cryptographic JWT authentication, and default-deny IAM policy engines).
2. **Official Academic Master Reports:** Comprehensive, publication-quality PDF submission reports articulating enterprise cloud architectures, multi-cloud provider mappings (AWS, Microsoft Azure, Google Cloud Platform), regulatory compliance frameworks (HIPAA, GDPR), and Zero-Trust identity engineering.

---

## 📁 Directory Structure

```text
Cloud_Computing/
├── README.md                                                          ← Main laboratory guide & documentation (You are here)
├── README_CC.md                                                       ← Navigation alias & quick reference
│
├── Case_Study_Unit_3/                                                 ← Case Study 1: Healthcare & Biology in the Cloud
│   ├── Healthcare_Biology_Demo.ipynb                                  ← Interactive Python/Jupyter demonstration notebook
│   └── Report1_Healthcare_Biology_Cloud_CC.pdf                        ← Official master submission report (PDF)
│
└── Case_Study_Unit_4/                                                 ← Case Study 2: Cloud Identity, Authentication & Authorization
    ├── Cloud_Identity_Security_Demo.ipynb                             ← Interactive Python/Jupyter demonstration notebook
    └── Report2_Cloud_Identity_Authentication_Authorization_CC.pdf     ← Official master submission report (PDF)
```

---

## 📚 Case Studies & Curriculum Breakdown

| Unit / Module | Title                                              | Primary Technologies                                                       | Artifacts & Links                                                                                                                                               |   Status    |
| :------------ | :------------------------------------------------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------: |
| **Unit 3**    | **Healthcare & Biology in the Cloud**              | Python, NumPy, SciPy (`butter`, `filtfilt`), Pandas, Matplotlib            | [Notebook](Case_Study_Unit_3/Healthcare_Biology_Demo.ipynb) • [Report (PDF)](Case_Study_Unit_3/Report1_Healthcare_Biology_Cloud_CC.pdf)                         | `Completed` |
| **Unit 4**    | **Cloud Identity, Authentication & Authorization** | Python, `cryptography` (RSA-2048, PKCS#1 v1.5, SHA-256), Base64URL, Pandas | [Notebook](Case_Study_Unit_4/Cloud_Identity_Security_Demo.ipynb) • [Report (PDF)](Case_Study_Unit_4/Report2_Cloud_Identity_Authentication_Authorization_CC.pdf) | `Completed` |

---

## 🔬 In-Depth Case Study Analysis

### 🧬 Unit 3: Healthcare & Biology in the Cloud

#### 1. Context & Computational Workloads

High-throughput biomedical data (genomic sequencing, protein structure folding, and continuous patient telemetry) generates petabyte-scale datasets characterized by bursty computational demands. This case study demonstrates the underlying computational algorithms and details how enterprise cloud architectures support these pipelines at production scale.

#### 2. Key Demonstrations in [Healthcare_Biology_Demo.ipynb](Case_Study_Unit_3/Healthcare_Biology_Demo.ipynb)

- **Global DNA Sequence Alignment (Needleman–Wunsch Algorithm):**
  - Implements dynamic programming alignment for nucleotide sequences with parameterizable match ($+1$), mismatch ($-1$), and gap penalties ($-2$).
  - Evaluates toy read and reference sequences, generates the optimal alignment score matrix, and visualizes dynamic programming matrices via heatmaps.
  - Computes GC content fractions and $k$-mer distribution histograms to emulate preprocessing in Next-Generation Sequencing (NGS).
- **Protein Folding Concept (2D Hydrophobic–Polar Lattice Model):**
  - Models primary sequence folding on a 2D square lattice using Self-Avoiding Walks (SAW) where non-covalent hydrophobic ($H-H$) topological contacts contribute $-1$ to free energy.
  - Explores combinatorial explosion through exhaustive walk enumeration across chain lengths $N \in [4, 16]$, visualizing exponential state-space scaling on a logarithmic scale.
  - Scores all $30,073$ conformations for a 12-residue sequence (`HPHPPHHPHPPH`) to identify the minimum-energy fold ($E = -5$).
- **Biomedical Telemetry & ECG Signal Processing:**
  - Synthesizes multi-component electrocardiogram (ECG) waveforms with realistic baseline wander ($0.3\text{ Hz}$ respiration artifact), $50\text{ Hz}$ powerline interference, and Gaussian noise.
  - Constructs a digital signal processing pipeline: 2nd-order bandpass Butterworth filter ($5 - 15\text{ Hz}$ passband), non-linear squared derivative energy operator, and moving-window integration (MWI).
  - Implements adaptive thresholding to detect cardiac R-peaks, reporting **$100\%$ Sensitivity** and **$100\%$ Precision** on synthetic traces.
  - Executes noise-robustness stress testing across increasing noise standard deviations ($\sigma \in [0.1, 1.0]$).

#### 3. Cloud Architecture & Enterprise Provider Mapping

As documented in [Report1_Healthcare_Biology_Cloud_CC.pdf](Case_Study_Unit_3/Report1_Healthcare_Biology_Cloud_CC.pdf):

- **Genomic Pipeline Orchestration:** Workflow automation via Nextflow / WDL mapped to **AWS Batch** and **AWS HealthOmics**, or **Azure Batch** and **Google Cloud Life Sciences**.
- **Data Lake Storage:** Raw sequence files (`FASTQ`, `BAM`, `CRAM`, `VCF`) stored on object stores with tiering lifecycle policies (Amazon S3 Standard $\rightarrow$ S3 Glacier Flexible / Deep Archive; Azure Blob Cold/Archive).
- **Regulatory Compliance & Security:** Enforcing HIPAA, GDPR, and HITECH requirements through hardware-level AES-256 encryption at rest (AWS KMS / Azure Key Vault), TLS 1.3 in transit, and immutable audit logging (AWS CloudTrail, Azure Monitor).

---

### 🛡️ Unit 4: Cloud Identity, Authentication & Authorization

#### 1. Context & Zero-Trust Architecture

In modern multi-tenant cloud environments, network perimeter-based security is obsolete. Identity serves as the primary security perimeter. This case study operationalizes the dual pillars of cloud access control: cryptographic authentication (validating identity claims) and default-deny authorization (enforcing least-privilege policies under dynamic context).

#### 2. Key Demonstrations in [Cloud_Identity_Security_Demo.ipynb](Case_Study_Unit_4/Cloud_Identity_Security_Demo.ipynb)

- **Ephemeral Asymmetric Key Generation & RS256 Cryptography:**
  - Generates 2048-bit RSA key pairs on demand using Python's `cryptography` primitives.
  - Adheres strictly to cryptographically sound signing using SHA-256 with PKCS#1 v1.5 padding, preventing insecure legacy algorithms.
- **Strict JSON Web Token (JWT) Security Validation:**
  - Token construction adhering to RFC 7519 with standard claims: `iss` (issuer), `sub` (subject), `aud` (audience), `exp` (expiration), and `scope`.
  - Comprehensive 8-point validation pipeline:
    1. Base64URL structural format verification (Header, Payload, Signature).
    2. Strict algorithm whitelisting (enforces `RS256`, rejects `alg: none` exploit vectors).
    3. Known Key ID (`kid`) resolution.
    4. Cryptographic public-key signature verification.
    5. Issuer validation (`https://idp.example.com`).
    6. Audience restriction (`api://orders`).
    7. Expiration (`exp`) and temporal freshness checks.
    8. Required permission scope verification (`orders.read`).
  - Automated test suite validating $8$ distinct security vectors (Valid token, Expired token, Audience mismatch, Issuer spoofing, Scope insufficiency, `alg: none` evasion, Foreign key signature, and Payload bit-flipping/tampering).
- **Default-Deny Zero-Trust IAM Policy Evaluation Engine:**
  - Evaluates incoming action requests against declarative permission policies using a 4-tier decision priority hierarchy:
    1. **Explicit Deny Precedence:** Any matching Deny rule terminates evaluation and rejects access immediately.
    2. **Resource Guardrails / Service Control Policies (SCPs):** Requests targeting resources outside defined organizational boundaries are blocked.
    3. **Explicit Allow with Contextual Enforcement:** Requests matching allowed actions and resources proceed only if contextual predicates (e.g., `mfa == True`) are satisfied.
    4. **Default Deny (Implicit Deny):** Unmatched requests default to a Deny response.
  - Automated test matrix evaluating $6$ cloud enterprise request scenarios (MFA-gated reporting, non-MFA reporting, destructive production database deletion, deployment pipeline controls, and unlisted service access).

#### 3. Cloud Provider IAM Mapping

As documented in [Report2_Cloud_Identity_Authentication_Authorization_CC.pdf](Case_Study_Unit_4/Report2_Cloud_Identity_Authentication_Authorization_CC.pdf):

- **AWS IAM:** Organizations Service Control Policies (SCPs) acting as guardrails, IAM Policies with JSON syntax (`Effect`, `Action`, `Resource`, `Condition`), STS AssumeRole temporary credentials, and Permission Boundaries.
- **Microsoft Entra ID (Azure AD):** OAuth 2.0 / OpenID Connect (OIDC) token issuance, Conditional Access policies (enforcing MFA and device compliance), and Role-Based Access Control (RBAC).
- **Google Cloud Platform (GCP) IAM:** Workload Identity Federation for keyless machine authentication, Context-Aware Access, and IAM Conditions.

---

## 📊 Verification Test Matrices & Benchmarks

### 🔑 Unit 4: JWT Authentication Test Suite

| Test Case | Scenario / Attack Vector                      | Expected Decision | Actual Decision | Verification Reason             | Status |
| :-------- | :-------------------------------------------- | :---------------: | :-------------: | :------------------------------ | :----: |
| **01**    | Valid Well-Formed Token                       |     `Accept`      |    `Accept`     | Valid signature & claims (`ok`) | `PASS` |
| **02**    | Expired Token ($t > \text{exp}$)              |     `Reject`      |    `Reject`     | `expired or missing expiry`     | `PASS` |
| **03**    | Audience Mismatch (`aud` spoof)               |     `Reject`      |    `Reject`     | `wrong audience`                | `PASS` |
| **04**    | Issuer Spoofing (`iss` mismatch)              |     `Reject`      |    `Reject`     | `wrong issuer`                  | `PASS` |
| **05**    | Scope Insufficiency (missing `orders.read`)   |     `Reject`      |    `Reject`     | `missing scope`                 | `PASS` |
| **06**    | Algorithm Substitution (`alg = none`)         |     `Reject`      |    `Reject`     | `algorithm not allowed`         | `PASS` |
| **07**    | Foreign Key Signature (untrusted private key) |     `Reject`      |    `Reject`     | `bad signature`                 | `PASS` |
| **08**    | Payload Bit-Flipping / Tampering              |     `Reject`      |    `Reject`     | `bad signature`                 | `PASS` |

_Result:_ **8 / 8 Tests Passed ($100\%$ Accuracy)**

---

### 🛡️ Unit 4: Authorization Policy Engine Test Suite

| Test Scenario                        | Request Context                                  | Policy Guardrail      | Expected Decision | Actual Decision | Evaluation Reason                   | Status |
| :----------------------------------- | :----------------------------------------------- | :-------------------- | :---------------: | :-------------: | :---------------------------------- | :----: |
| **Analyst Reads Report with MFA**    | `s3:GetObject` on `reports/q3.csv`, `mfa: true`  | Inside guardrail      |      `ALLOW`      |     `ALLOW`     | Explicit allow condition met        | `PASS` |
| **Analyst Reads Report without MFA** | `s3:GetObject` on `reports/q3.csv`, `mfa: false` | Inside guardrail      |      `DENY`       |     `DENY`      | Implicit deny (condition unmet)     | `PASS` |
| **Developer Deletes Production DB**  | `db:Delete` on `prod-db`                         | Inside guardrail      |      `DENY`       |     `DENY`      | Explicit deny overrides all         | `PASS` |
| **Pipeline Deploys to Test Account** | `deploy` on `acct-test`                          | Inside guardrail      |      `ALLOW`      |     `ALLOW`     | Explicit allow rule matched         | `PASS` |
| **Pipeline Deploys to Production**   | `deploy` on `acct-prod`                          | Inside guardrail      |      `DENY`       |     `DENY`      | Implicit deny (unauthorized env)    | `PASS` |
| **Request to Unlisted Service**      | `s3:GetObject` on `hr-data/x`                    | **Outside guardrail** |      `DENY`       |     `DENY`      | Resource guardrail boundary blocked | `PASS` |

_Result:_ **6 / 6 Tests Passed ($100\%$ Accuracy)**

---

### 🫀 Unit 3: ECG R-Peak Detection & Telemetry Benchmark

| Metric                         | Target / Benchmark |    Measured Value    | Unit  |
| :----------------------------- | :----------------: | :------------------: | :---: |
| **Generated Beats**            |         12         |          12          | Beats |
| **Detected Beats**             |         12         |          12          | Beats |
| **True Positives (TP)**        |         12         |          12          | Beats |
| **False Positives (FP)**       |         0          |          0           | Beats |
| **False Negatives (FN)**       |         0          |          0           | Beats |
| **Detection Sensitivity**      |       $1.00$       | **$1.00$ ($100\%$)** | Ratio |
| **Detection Precision**        |       $1.00$       | **$1.00$ ($100\%$)** | Ratio |
| **Mean Heart Rate (Detected)** |      $72.91$       |     **$72.93$**      |  BPM  |

---

## 🚀 Setup & Execution Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/himanshu-jadhav108/College_Practicals.git
cd College_Practicals/Cloud_Computing
```

### 2️⃣ Environment Configuration

Create and activate an isolated Python virtual environment (Python 3.10+ recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Linux / macOS
source venv/bin/activate

# Install required numerical, cryptographic, and visualization dependencies
pip install --upgrade pip
pip install numpy pandas scipy matplotlib cryptography
```

### 3️⃣ Running the Demonstration Notebooks

#### Option A: Local Jupyter Environment

```bash
# Launch Case Study 1 (Healthcare & Biology in the Cloud)
jupyter notebook Case_Study_Unit_3/Healthcare_Biology_Demo.ipynb

# Launch Case Study 2 (Cloud Identity, Authentication & Authorization)
jupyter notebook Case_Study_Unit_4/Cloud_Identity_Security_Demo.ipynb
```

#### Option B: Google Colab

Both notebooks are self-contained and pre-configured for **Google Colab**:

1. Open [Google Colab](https://colab.research.google.com/).
2. Select **Upload** and upload `Healthcare_Biology_Demo.ipynb` or `Cloud_Identity_Security_Demo.ipynb`.
3. Execute via **Runtime → Run all**.

---

## 🛠️ Technology Stack & Libraries

<div align="left">

| Category                           | Tools & Libraries                                               | Description / Usage                                                       |
| :--------------------------------- | :-------------------------------------------------------------- | :------------------------------------------------------------------------ |
| **Cloud Computing Platforms**      | `AWS`, `Microsoft Azure`, `Google Cloud (GCP)`                  | Enterprise reference architectures, storage lifecycle, batch computing    |
| **Identity & Access Management**   | `AWS IAM`, `Microsoft Entra ID`, `GCP Cloud IAM`                | Zero-Trust architecture, SCPs, RBAC, ABAC, OIDC, STS                      |
| **Cryptography & Security**        | `cryptography` (hazmat RSA, PKCS#1 v1.5, SHA-256), `JWT`        | Ephemeral asymmetric key generation, Base64URL encoding, token validation |
| **Scientific & Signal Processing** | `NumPy`, `SciPy` (`butter`, `filtfilt`, `find_peaks`), `Pandas` | Dynamic programming, combinatorial walk modeling, ECG digital filtering   |
| **Visualization & Reporting**      | `Matplotlib`                                                    | Score matrix heatmaps, conformation growth curves, R-peak detection plots |
| **Interactive Environments**       | `Jupyter Notebook`, `Google Colab`, `VS Code`                   | Reproducible execution, test result validation                            |

</div>

---

## 👤 Maintainer & Academic Information

<br>

<p align="center">
  <table align="center" style="border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; background: rgba(30, 41, 59, 0.4); backdrop-filter: blur(8px); padding: 24px; max-width: 550px; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);">
    <tr>
      <td align="center">
        <h3 style="margin: 0; color: #38bdf8; font-size: 1.7em; font-weight: 800; letter-spacing: -0.5px;">Himanshu Jadhav</h3>
        <p style="color: #38bdf8; font-weight: 600; margin: 4px 0 2px 0;">Roll Number: TE-32</p>
        <p style="color: #94a3b8; font-weight: 500; margin: 2px 0 15px 0;">Artificial Intelligence & Data Science Engineer | SPPU (2024 – 2028)</p>
        <p style="color: #cbd5e1; font-size: 0.95em; max-width: 440px; line-height: 1.5; margin-bottom: 20px;">
          Focused on distributed cloud computing, cryptographic identity systems, scalable bioinformatic workflows, and enterprise Zero-Trust architectures.
        </p>
        <div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap;">
          <a href="https://github.com/himanshu-jadhav108" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
          <a href="https://www.linkedin.com/in/himanshu-jadhav-328082339" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
          <a href="https://himanshu-jadhav-portfolio.vercel.app/" target="_blank"><img src="https://img.shields.io/badge/Portfolio-FFD700?style=for-the-badge&logo=google-chrome&logoColor=black" alt="Portfolio"></a>
          <a href="https://www.instagram.com/himanshu_jadhav_108?igsh=MWYxamppcTBlY3Rl" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
        </div>
      </td>
    </tr>
  </table>
</p>

<br>

---

<div align="center">

**⭐ If you find this Cloud Computing case study repository valuable, please consider starring it!**

[⬅️ Back to Main Repository](../README.md)

</div>
