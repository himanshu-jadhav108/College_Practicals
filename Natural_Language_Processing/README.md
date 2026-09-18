# 🗣️ Natural Language Processing (NLP) Practicals – SPPU 2024

> **Third-Year / Final-Year Engineering | Artificial Intelligence & Data Science | Savitribai Phule Pune University**  
> **Author:** Himanshu Jadhav (Roll No: TE-32)

![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-v3.x-green?logo=python&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-v3.x-blue?logo=spacy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-v1.3%2B-orange?logo=scikit-learn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.x-red?logo=pytorch&logoColor=white)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface&logoColor=white)
![Status](<https://img.shields.io/badge/Status-Completed%20(100%25)-brightgreen>)
![SPPU](https://img.shields.io/badge/University-SPPU%202024-orange)

---

## 📌 Repository Overview

This repository houses a comprehensive, dual-tiered laboratory suite for **Natural Language Processing (NLP)**, engineered strictly in alignment with the **Savitribai Phule Pune University (SPPU)** Artificial Intelligence and Data Science curriculum.

Every experiment has been designed with a dual-track implementation pedagogy:

- **🟢 Basic Implementation:** Clean, self-contained conceptual notebooks emphasizing linguistic fundamentals, foundational algorithms, and standard library APIs.
- **🚀 Advance Implementation:** Production-grade, mathematically rigorous notebooks featuring LaTeX theoretical formulations, custom algorithms built from scratch without black-box abstractions, multi-domain benchmark corpora, empirical ablation studies, publication-quality visualizations, and modular Object-Oriented (OOP) pipelines.

All notebooks are pre-executed with cell outputs, evaluation tables, and figures preserved for evaluation and offline review.

---

## 📁 Repository Directory Structure

```
Natural_Language_Processing/
├── README.md                                          ← Comprehensive repository guide & syllabus mapping
├── requirements.txt                                   ← Categorized dependencies with version pins
│
├── Practical_01/                                      ← Text Preprocessing, Linguistic Pipelines & POS Tagging
│   ├── Basic/
│   │   └── Practical_01.ipynb
│   └── Advance/
│       └── Practical_01_advance.ipynb
│
├── Practical_02/                                      ← Regular Expressions, Lexical Analysis & Finite Automata
│   ├── Basic/
│   │   └── Practical_02.ipynb
│   └── Advance/
│       └── Practical_02_Advance.ipynb
│
├── Practical_03/                                      ← Minimum Edit Distance, Noisy Channel & Spelling Correction
│   ├── Basic/
│   │   └── Practical_03.ipynb
│   └── Advance/
│       └── Practical_03_Advance.ipynb
│
├── Practical_04/                                      ← Feature Extraction & Vector Space Modeling (BoW, TF-IDF)
│   ├── Basic/
│   │   └── Practical_04.ipynb
│   └── Advance/
│       └── Practical_04_Advance.ipynb
│
├── Practical_05/                                      ← Text Classification (Naive Bayes & Logistic Regression)
│   ├── Basic/
│   │   └── Practical_05.ipynb
│   └── Advance/
│       └── Practical_05_Advance.ipynb
│
├── Practical_06/                                      ← N-gram Language Modeling, Smoothing Paradigms & Perplexity
│   ├── Basic/
│   │   └── Practical_06.ipynb
│   └── Advance/
│       └── Practical_06_Advance.ipynb
│
├── Practical_07/                                      ← Named Entity Recognition (NER) & Sequence Labeling
│   ├── Basic/
│   │   └── Practical_07.ipynb
│   └── Advance/
│       └── Practical_07_Advance.ipynb
│
├── Practical_08/                                      ← Dependency Parsing, SVO Extraction & Syntactic Ambiguity
│   ├── Basic/
│   │   └── Practical_08.ipynb
│   └── Advance/
│       └── Practical_08_Advance.ipynb
│
├── Practical_09/                                      ← Extractive & Abstractive Summarization (Transformers)
│   ├── Basic/
│   │   ├── Practical_09_Basic_Easy.ipynb
│   │   └── Practical_09_Basic_Moderate.ipynb
│   └── Advance/
│       └── Practical_09_Advance.ipynb
│
├── Practical_10/                                      ← Capstone Practical: Multi-Domain AI News Summarizer
│   ├── Basic/
│   │   ├── Practical_10_Easy.ipynb
│   │   └── Practical_10_Moderate.ipynb
│   └── Advance/
│       └── Practical_10_Advance.ipynb
│
└── MiniProject_AniSense/                              ← 🎌 Capstone NLP Project: Anime Sentiment & Recommendation
    ├── data/
    │   ├── anime_meta.json
    │   └── anime_reviews.json
    └── AniSense_Anime_Sentiment_Recommendation.ipynb
```

---

## 📚 Syllabus Mapping & Experiment Matrix

|   #    | Practical Title                                | Basic Notebook(s)                                                                                                                                                                      | Advance Notebook                                                                                                        | Key Concepts & Implementations                                                                                                                                                        |   Status    |
| :----: | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------: |
| **01** | **Linguistic Preprocessing & POS Tagging**     | [`Practical_01.ipynb`](./Practical_01/Basic/Practical_01.ipynb)                                                                                                                        | [`Practical_01_advance.ipynb`](./Practical_01/Advance/Practical_01_advance.ipynb)                                       | Sentence/word tokenization, stop-word elimination, Porter/Snowball stemming, WordNet lemmatization, NLTK vs spaCy benchmark, dependency SVO extraction.                               | `Completed` |
| **02** | **Regular Expressions & Finite Automata**      | [`Practical_02.ipynb`](./Practical_02/Basic/Practical_02.ipynb)                                                                                                                        | [`Practical_02_Advance.ipynb`](./Practical_02/Advance/Practical_02_Advance.ipynb)                                       | Regex pattern matching, email/phone/date extraction, custom tokenizing compiler lexer, PII redaction engine, visual DFA state-machine transition simulation.                          | `Completed` |
| **03** | **Edit Distance & Spelling Correction**        | [`Practical_03.ipynb`](./Practical_03/Basic/Practical_03.ipynb)                                                                                                                        | [`Practical_03_Advance.ipynb`](./Practical_03/Advance/Practical_03_Advance.ipynb)                                       | Levenshtein dynamic programming distance matrix, optimal alignment backtracing, Peter Norvig noisy channel candidate model, Soundex phonetic hashing.                                 | `Completed` |
| **04** | **Vector Space Models (BoW & TF-IDF)**         | [`Practical_04.ipynb`](./Practical_04/Basic/Practical_04.ipynb)                                                                                                                        | [`Practical_04_Advance.ipynb`](./Practical_04/Advance/Practical_04_Advance.ipynb)                                       | One-Hot encoding, Document-Term Matrix (DTM), from-scratch TF-IDF with sublinear scaling ablation, LSA (Truncated SVD) latent semantics, Cosine similarity.                           | `Completed` |
| **05** | **Text Classification (Spam vs. Ham)**         | [`Practical_05.ipynb`](./Practical_05/Basic/Practical_05.ipynb)                                                                                                                        | [`Practical_05_Advance.ipynb`](./Practical_05/Advance/Practical_05_Advance.ipynb)                                       | Multinomial Naive Bayes from scratch, Complement Naive Bayes for imbalanced text, Logistic Regression with L2 penalty, log-odds feature importance, ROC-AUC / PR curves.              | `Completed` |
| **06** | **N-gram Language Modeling & Smoothing**       | [`Practical_06.ipynb`](./Practical_06/Basic/Practical_06.ipynb)                                                                                                                        | [`Practical_06_Advance.ipynb`](./Practical_06/Advance/Practical_06_Advance.ipynb)                                       | Unigram/Bigram/Trigram models, 5 smoothing regimes (MLE, Add-$k$, Good-Turing, Jelinek-Mercer interpolation, Kneser-Ney), Perplexity scoring, Zipf's law analysis, text generation.   | `Completed` |
| **07** | **Named Entity Recognition (NER)**             | [`Practical_07.ipynb`](./Practical_07/Basic/Practical_07.ipynb)                                                                                                                        | [`Practical_07_Advance.ipynb`](./Practical_07/Advance/Practical_07_Advance.ipynb)                                       | Rule-based gazetteer matching, 4 NER paradigms (Regex, Contextual Window Classifier, Neural spaCy, Hybrid Ensemble), CoNLL strict vs. partial evaluation, Knowledge Graph triples.    | `Completed` |
| **08** | **Dependency Parsing & Syntactic Ambiguity**   | [`Practical_08.ipynb`](./Practical_08/Basic/Practical_08.ipynb)                                                                                                                        | [`Practical_08_Advance.ipynb`](./Practical_08/Advance/Practical_08_Advance.ipynb)                                       | spaCy dependency parser, displaCy rendering, ASCII syntax tree hierarchy, tree topometry (depth, branching, MDD), voice-normalized SVO extraction, PP-attachment arbiter.             | `Completed` |
| **09** | **Extractive & Abstractive Summarization**     | [`Practical_09_Basic_Easy.ipynb`](./Practical_09/Basic/Practical_09_Basic_Easy.ipynb)<br>[`Practical_09_Basic_Moderate.ipynb`](./Practical_09/Basic/Practical_09_Basic_Moderate.ipynb) | [`Practical_09_Advance.ipynb`](./Practical_09/Advance/Practical_09_Advance.ipynb)                                       | 4 custom extractive algorithms (TF-IDF, TextRank Graph PageRank, Position-Biased, MMR redundancy elimination), Seq2Seq DistilBART neural summarizer, ROUGE-1/2/L benchmarking.        | `Completed` |
| **10** | **Multi-Domain Article Summarization**         | [`Practical_10_Easy.ipynb`](./Practical_10/Basic/Practical_10_Easy.ipynb)<br>[`Practical_10_Moderate.ipynb`](./Practical_10/Basic/Practical_10_Moderate.ipynb)                         | [`Practical_10_Advance.ipynb`](./Practical_10/Advance/Practical_10_Advance.ipynb)                                       | Multi-article news intelligence pipeline, RAKE keyphrase extraction, Flesch Reading Ease scoring, Compression Ratio analysis, dual extractive vs abstractive comparative radar chart. | `Completed` |
| **🎌** | **AniSense: Anime Sentiment & Recommendation** | —                                                                                                                                                                                      | [`AniSense_Anime_Sentiment_Recommendation.ipynb`](./MiniProject_AniSense/AniSense_Anime_Sentiment_Recommendation.ipynb) | Multi-class review sentiment classification, metadata feature fusion, TF-IDF + Cosine similarity anime recommendation engine, interactive search inference.                           | `Completed` |

---

## 🔬 In-Depth Practical Walkthroughs

### 🟢 Practical 01: Linguistic Preprocessing & POS Tagging

- **Objective:** Master text normalization, tokenization hierarchies, stemming vs. lemmatization trade-offs, and part-of-speech tagging.
- **Implementations:**
  - Tokenization at word, sentence, and regex level.
  - Comparative analysis: Porter Stemmer vs. Lancaster Stemmer vs. WordNet Lemmatizer with POS tag mapping.
  - NLTK Penn Treebank POS tagger vs. spaCy statistical tagger.
  - **Advance:** SVO (Subject-Verb-Object) triplet extraction from dependency relations, morphological ambiguity profiling, and an end-to-end OOP `LinguisticPipeline`.

### 🟢 Practical 02: Regular Expressions, Lexical Analysis & Finite Automata

- **Objective:** Construct lexical analysis tools, regex pattern extractors, and simulate deterministic finite automata (DFA).
- **Implementations:**
  - Robust regex patterns for email addresses, international phone numbers, ISO dates, and URLs.
  - Custom tokenizing compiler lexer transforming source strings into typed token streams (`IDENTIFIER`, `KEYWORD`, `OPERATOR`, `LITERAL`).
  - Automated Personally Identifiable Information (PII) redaction system (emails, phone numbers, credit cards).
  - **Advance:** Formal DFA state-machine simulator verifying regular language membership with state transition visualizer.

### 🟢 Practical 03: Minimum Edit Distance & Spelling Correction

- **Objective:** Implement dynamic programming string metrics and statistical noisy channel spelling correction.
- **Implementations:**
  - Wagner-Fischer dynamic programming algorithm for Levenshtein Distance.
  - Backtracing algorithm computing optimal alignment string operations (Insert, Delete, Substitute, Match).
  - Peter Norvig Noisy Channel Bayesian spelling corrector with candidate word generation ($\text{Edit}_1, \text{Edit}_2$).
  - **Advance:** Soundex and Metaphone phonetic hashing integration to capture phonological spelling mistakes.

### 🟢 Practical 04: Vector Space Modeling (BoW & TF-IDF)

- **Objective:** Transform unstructured text into high-dimensional vector spaces and analyze semantic similarity.
- **Implementations:**
  - One-Hot vector representations and Vocabulary Indexer.
  - Document-Term Matrix (DTM) construction with term frequency counting.
  - From-scratch TF-IDF vectorizer adhering to standard smoothing ($1 + \log \frac{1+N}{1+df}$) and L2 normalization.
  - **Advance:** Latent Semantic Analysis (LSA via Truncated SVD), sublinear term-frequency scaling ($1 + \log(tf)$) ablation study, and Cosine similarity information retrieval engine.

### 🟢 Practical 05: Text Classification (Spam vs. Ham)

- **Objective:** Construct probabilistic and linear classifiers for text categorization with class imbalance handling.
- **Implementations:**
  - SMS Spam Collection dataset preprocessing and vectorization.
  - Custom from-scratch Multinomial Naive Bayes classifier with Laplace ($+1$) smoothing and log-space probability calculations.
  - Scikit-Learn MultinomialNB and Complement Naive Bayes (CNB) designed specifically for severe class imbalance.
  - **Advance:** L2-regularized Logistic Regression, log-odds feature importance analysis identifying top predictive spam/ham tokens, Precision-Recall curves, and Confusion Matrices.

### 🟢 Practical 06: N-gram Language Modeling & Smoothing Paradigms

- **Objective:** Estimate probability distributions over word sequences, evaluate perplexity, and resolve zero-probability hazards.
- **Implementations:**
  - Maximum Likelihood Estimation (MLE) unigram, bigram, and trigram counting with Laplace Add-1 smoothing.
  - Autoregressive text generation with greedy decoding and temperature-scaled probabilistic sampling.
  - **Advance:** 5 smoothing paradigms benchmarked side-by-side:
    1. Maximum Likelihood Estimation (MLE)
    2. Add-$k$ (Lidstone) Smoothing
    3. Good-Turing Frequency Estimation
    4. Jelinek-Mercer Linear Interpolation ($\lambda_1, \lambda_2, \lambda_3$)
    5. Kneser-Ney Absolute Discounting with continuation probabilities
  - Empirical validation of Zipf's Law ($\log(\text{Rank})$ vs. $\log(\text{Frequency})$) with regression fitting.

### 🟢 Practical 07: Named Entity Recognition (NER) & Sequence Labeling

- **Objective:** Extract and categorize domain entities from unstructured narrative text across multi-token spans.
- **Implementations:**
  - Rule-based gazetteer and regex-driven entity extraction.
  - spaCy statistical entity recognizer across standard OntoNotes categories (`PERSON`, `ORG`, `GPE`, `DATE`, `MONEY`).
  - **Advance:** Multi-domain gold standard dataset across 4 technological and geopolitical domains.
  - Evaluation of 4 NER paradigms: Regex/Gazetteer, Sliding-Window Feature Classifier, Neural Pipeline, and Hybrid Ensemble.
  - Strict vs. Relaxed CoNLL span evaluation metrics ($P$, $R$, $F_1$) and Knowledge Graph triplet generator.

### 🟢 Practical 08: Dependency Parsing & Syntactic Ambiguity

- **Objective:** Parse grammatical structures, analyze syntactic dependencies, and disambiguate structural ambiguity.
- **Implementations:**
  - Dependency parsing using spaCy's transition-based neural parser.
  - Identification of root verbs, grammatical subjects (`nsubj`), direct objects (`dobj`), and prepositional phrases (`prep`).
  - **Advance:** Custom ASCII tree visualizer rendering hierarchical dependency trees in stdout/notebook.
  - Syntactic topometry metrics: Tree Depth, Max Branching Factor, and Mean Dependency Distance (MDD).
  - SVO event extraction with automatic passive-to-active voice normalization (`agent` by-phrase handling).
  - Prepositional Phrase (PP) attachment ambiguity classifier determining verb vs. noun attachment.

### 🟢 Practical 09: Extractive & Abstractive Summarization

- **Objective:** Synthesize long documents using extractive graph algorithms and deep Seq2Seq transformer models.
- **Implementations:**
  - **Basic Easy:** TF-IDF sentence centrality scoring and Seq2Seq abstractive summarization.
  - **Basic Moderate:** Extended multi-document comparison with ROUGE-1, ROUGE-2, and ROUGE-L evaluation.
  - **Advance:** 4 from-scratch extractive algorithms:
    1. TF-IDF Centroid Sentence Scoring
    2. TextRank Graph Algorithm (Sentence similarity graph with PageRank power iteration)
    3. Position-Biased Sentence Scoring (Lead-sentence academic weighting)
    4. Maximal Marginal Relevance (MMR) for dynamic redundancy elimination
  - Direct Hugging Face `AutoModelForSeq2SeqLM` loading `sshleifer/distilbart-cnn-12-6` with beam search and `forced_bos_token_id=0`.

### 🟢 Practical 10: Multi-Domain AI News Article Summarizer

- **Objective:** Build an end-to-end intelligent summarization and text analytics workstation for multi-domain news corpora.
- **Implementations:**
  - **Basic Easy & Moderate:** Production-ready multi-article summarizer comparing extractive vs. transformer summaries with compression ratio metrics.
  - **Advance:** Comprehensive AI News Intelligence Pipeline:
    - Multi-domain corpus ingestion (Generative AI, Quantum Computing, Climate Science).
    - Rapid Automatic Keyword Extraction (RAKE) algorithm.
    - Readability profiling using the Flesch Reading Ease Index.
    - Dual extractive vs. abstractive comparative analysis evaluated on ROUGE and compression efficiency.
    - Visual radar chart and comparative distribution plots.

### 🎌 Mini Project: AniSense – Anime Sentiment & Hybrid Recommendation System

- **Objective:** Build a capstone NLP recommendation and sentiment analysis application on real-world anime review data.
- **Implementations:**
  - Sentiment classification on user reviews using TF-IDF feature representations and multi-class classifiers (Logistic Regression, Linear SVC, Multinomial Naive Bayes).
  - Feature fusion combining review sentiment scores with structured anime metadata (genres, studios, ratings, synopsis).
  - Content-based recommendation engine utilizing Cosine similarity over fused TF-IDF synopsis and genre vectors.
  - Interactive search and prediction interface demonstrating end-to-end inference on user queries.

---

## 🚀 Installation & Quickstart Guide

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/himanshu-jadhav108/College_Practicals.git
cd College_Practicals/Natural_Language_Processing
```

### Step 2: Set Up Python Virtual Environment

It is strongly recommended to use Python **3.10**, **3.11**, or **3.12**:

```bash
# Create the virtual environment
python -m venv nlp_env

# Activate on Windows (PowerShell)
.\nlp_env\Scripts\Activate.ps1

# Activate on Windows (Command Prompt)
.\nlp_env\Scripts\activate.bat

# Activate on Linux / macOS
source nlp_env/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Download Essential NLP Corpora & Models

Run the following commands to download the spaCy English pipeline and all required NLTK linguistic corpora:

```bash
# spaCy small English pipeline
python -m spacy download en_core_web_sm

# Essential NLTK corpora
python -c "import nltk; nltk.download(['punkt', 'punkt_tab', 'stopwords', 'wordnet', 'gutenberg', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng'])"
```

### Step 5: Register the Virtual Environment Kernel in Jupyter

```bash
python -m ipykernel install --user --name=nlp_env --display-name="Python (nlp_env)"
```

### Step 6: Launch Jupyter Notebook or JupyterLab

```bash
jupyter notebook
```

> In Jupyter, select the **Python (nlp_env)** kernel from the top-right kernel dropdown when opening any notebook.

---

## 🛠️ Technology Stack & Dependencies

| Category                   | Primary Libraries                    | Version Range                     | Purpose                                                                 |
| :------------------------- | :----------------------------------- | :-------------------------------- | :---------------------------------------------------------------------- |
| **Core Computing**         | `numpy`, `pandas`, `scipy`           | `>=1.24.0`, `>=2.0.0`, `>=1.10.0` | Numerical arrays, matrix operations, tabular manipulation               |
| **Classical NLP**          | `nltk`, `spacy`                      | `>=3.8.1`, `>=3.7.0`              | Tokenization, POS tagging, WordNet, Lemmatization, Dependency Parsing   |
| **Linguistic Assets**      | `en_core_web_sm`                     | `3.8.0`                           | spaCy statistical model for English syntax and NER                      |
| **Machine Learning**       | `scikit-learn`                       | `>=1.3.0`                         | CountVectorizer, TfidfVectorizer, Naive Bayes, Logistic Regression, SVD |
| **Deep Learning**          | `torch`, `transformers`              | `>=2.0.0`, `>=4.36.0`             | Seq2Seq neural summarization (`sshleifer/distilbart-cnn-12-6`)          |
| **Visualization**          | `matplotlib`, `seaborn`, `wordcloud` | `>=3.7.0`, `>=0.12.0`, `>=1.9.0`  | Confusion matrices, loss curves, radar plots, word clouds               |
| **Formatting & Utilities** | `tabulate`, `tqdm`                   | `>=0.9.0`, `>=4.66.0`             | Publication-style markdown/ASCII grid tables, progress bars             |
| **Evaluation Metrics**     | `rouge_score`                        | `>=0.1.2`                         | Summarization evaluation (ROUGE-1, ROUGE-2, ROUGE-L)                    |
| **Interactive Runtime**    | `jupyter`, `ipykernel`, `nbconvert`  | `>=1.0.0`, `>=6.25.0`, `>=7.10.0` | Interactive notebook execution and export                               |

---

## ⚙️ Technical Design Notes & Best Practices

1. **Hugging Face Transformers Architecture:**
   In `transformers >= 4.36.0` / `5.x`, Seq2Seq abstractive summarization is executed using explicit `AutoTokenizer` and `AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")`. Generation includes `forced_bos_token_id=0` and `no_repeat_ngram_size=3` to ensure grammatically fluent, coherent summaries without repetition.
2. **Deterministic Reproducibility:**
   All random seeds across Scikit-Learn (`random_state=42`) and PyTorch (`torch.manual_seed(42)`) are explicitly pinned to guarantee reproducible splits, embeddings, and classification results.
3. **Cross-Platform Compatibility:**
   All text processing operations specify UTF-8 encoding explicitly, ensuring seamless execution across Windows, Linux, and macOS environments without character map decode errors.
4. **Zero-Dependency Fallbacks:**
   Advanced notebooks implement custom fallback logic for optional dependencies (e.g., SVD co-occurrence matrix fallback for word embeddings), ensuring all notebooks execute from end to end even in constrained environments.

---

## 👨‍💻 Author & Academic Information

- **Student:** Himanshu Jadhav
- **Roll Number:** TE-32
- **Degree Program:** Bachelor of Engineering (B.E.)
- **Specialization:** Artificial Intelligence & Data Science (AI & DS)
- **Institution:** Savitribai Phule Pune University (SPPU)
- **Academic Year:** 2024 – 2028
