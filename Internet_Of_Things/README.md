# 🌐 Internet of Things (IoT) Practicals – SPPU 2026–2027

> **Third-Year / Final-Year Engineering | Savitribai Phule Pune University**  
> **Repository:** Final Practical Submission Package & Laboratory Codebase  
> **Final Submission Report:** [IoT_Practical_Submission_Report.pdf](IoT_Practical_Submission_Report.pdf) | [Markdown Version](IoT_Practical_Submission_Report.md)

![IoT](https://img.shields.io/badge/IoT-Sensors%20%26%20Actuators-blue?logo=internetofthings&logoColor=white)
![Arduino](https://img.shields.io/badge/Hardware-Arduino%20UNO-00979D?logo=arduino&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Repository Overview

This repository contains the complete, verified, and officially organized **Internet of Things (IoT)** laboratory submission aligned with the **SPPU Course Curriculum**. It covers embedded sensor interfacing, digital actuation, serial telemetry, IoT communications protocols, edge preprocessing, privacy-by-design, and machine learning models.

---

## 📁 Submission Folder Structure

```
Internet_Of_Things/
├── IoT_Practical_Submission_Report.pdf   ← Master 22-page print-ready submission report
├── IoT_Practical_Submission_Report.md    ← Markdown version of the submission report
├── IoT Lab Manual.docx                   ← Official university lab manual reference
├── README.md                             ← Repository guide and documentation
│
├── Practical_01/                         ← Temperature Sensor Interfacing (TMP36)
│   ├── Circuit_Diagram/Practical_01_Circuit.png
│   ├── Code/Practical_01.ino, Practical_01_Reader.py
│   └── Output/Practical_01_Output.txt
│
├── Practical_02/                         ← Proximity & Obstacle Detection (IR + LED)
│   ├── Circuit_Diagram/Practical_02_Circuit.png
│   ├── Code/Practical_02.ino
│   └── Output/Practical_02_Output.txt
│
├── Practical_03/                         ← Physical Design & Device Actuation (GPIO LED)
│   ├── Circuit_Diagram/Practical_03_Circuit.png
│   ├── Code/Practical_03.ino
│   └── Output/Practical_03_Output.txt
│
├── Practical_04/                         ← Gas Leakage Detection System (MQ-2 + Buzzer)
│   ├── Circuit_Diagram/Practical_04_Circuit.png
│   ├── Code/Practical_04.ino
│   └── Output/Practical_04_Output.txt
│
├── Practical_05/                         ← RFID Identification System (MFRC522 SPI)
│   ├── Circuit_Diagram/Practical_05_Circuit.png
│   ├── Code/Practical_05.ino
│   └── Output/Practical_05_Output.txt
│
├── Practical_06/                         ← IoT Device-to-Server Protocol (UART / HTTP REST)
│   ├── Circuit_Diagram/Practical_06_Circuit.png, Practical_06_System_Diagram.png
│   ├── Code/Practical_06_Sender.ino, Practical_06_Receiver.ino, Practical_06_Server.py, Practical_06_Client.py
│   └── Output/Practical_06_Output.txt
│
├── Practical_07/                         ← Data Cleaning, Normalization & Visualization
│   ├── Practical_07_Submission.ipynb     ← Interactive Jupyter Notebook
│   ├── Code/Practical_07_Data_Cleaning.py
│   └── Output/Practical_07_Plot.png
│
├── Practical_08/                         ← Real-Time Sensor ML Temperature Forecasting
│   ├── Practical_08_Submission.ipynb     ← Interactive Jupyter Notebook
│   ├── Code/Practical_08_Temp_ML.py
│   └── Output/Practical_08_Plot.png
│
├── Practical_09/                         ← Password-Protected Smart Sensor Security (SHA-256)
│   ├── Practical_09_Submission.ipynb     ← Interactive Jupyter Notebook
│   ├── Circuit_Diagram/Practical_09_Circuit.png
│   ├── Code/Practical_09_Auth.py
│   └── Output/Practical_09_Output.txt
│
├── Practical_10/                         ← Case Study: Privacy-by-Design Data Minimization
│   ├── Practical_10_Submission.ipynb     ← Interactive Jupyter Notebook
│   ├── Circuit_Diagram/Practical_10_Circuit.png
│   ├── Code/Practical_10_Smart_Threshold.py
│   └── Output/Practical_10_Plot.png, Practical_10_Output.txt
│
└── Practical_11/                         ← 🚀 Capstone IoT Mini Project: Privacy-Aware Intelligent AIoT System
    ├── Practical_11_Submission.ipynb     ← Interactive Jupyter Notebook (Mini Project Pipeline)
    ├── Circuit_Diagram/Practical_11_Circuit.png
    ├── Code/Practical_11_Privacy_AIoT.py
    └── Output/Practical_11_Output.txt
```

---

## 📚 Complete Practical Index

| # | Official Title | Tech Stack | Status |
|---|---|---|---|
| **01** | Develop an Application for the Connectivity of the Arduino UNO/Raspberry Pi Circuit with Sensors | Arduino C++, Python pySerial | `Completed` |
| **02** | Implement an Application to Detect Obstacles and Notify Users Using LEDs to Understand the Connectivity of Raspberry Pi/Arduino with IR Sensor | Arduino C++ (GPIO 7, 13) | `Completed` |
| **03** | Implement a Simple IoT Application Using an Arduino Board to Control an LED Through GPIO Pins to Understand the Physical Design of IoT Devices and Device Actuation | Arduino C++ (GPIO 13) | `Completed` |
| **04** | Develop a Program to Detect Gas Leakage in the Surrounding Environment | Arduino C++ (MQ-2, Piezo Buzzer) | `Completed` |
| **05** | Design an RFID-Based Identification System that Reads Tag Information and Displays the ID on a Monitoring System to Demonstrate Short-Range Communication Technologies in IoT | Arduino C++ (MFRC522, SPI) | `Completed` |
| **06** | Develop an IoT Application that Uses a Communication Protocol to Transmit Sensor Data Between an IoT Device and a Server | Dual Arduino Serial / Python HTTP REST | `Completed` |
| **07** | Perform Data Cleaning, Normalization, and Visualization on an IoT Sensor Dataset | Python (Pandas, NumPy, Matplotlib) | `Completed` |
| **08** | Implement an IoT Application to Collect Real-Time Temperature Data Using an IoT Sensor and Apply a Machine Learning Model to Predict Future Temperature Values | Python (Scikit-Learn Linear Regression) | `Completed` |
| **09** | Design and Implement a Password-Protected Smart Sensor System that Allows Access to Sensor Data Only After Successful Authentication, Demonstrating Basic IoT Security Concepts | Python (Cryptographic SHA-256 Hashing) | `Completed` |
| **10** | Case Study for Data Minimization Using Smart Threshold Alert by Providing Privacy-by-Design | Python (Smart Thresholding, 86.7% reduction) | `Completed` |
| **11** | **[IoT Mini Project]** Develop a Privacy-Aware Intelligent Smart IoT Application: Design and Implementation of an AIoT-Based Smart Sensor System with Cloud-Based Data Preprocessing and Intelligent Decision-Making | Python (AIoT, AES Fernet, Random Forest) | `Completed (Mini Project)` |

---

## 🛠️ Verification & Audit Checklist

- [x] **CHECK 1:** Every practical from official lab manual represented (11 / 11)
- [x] **CHECK 2:** Practical numbering strictly matches official syllabus (1 to 11)
- [x] **CHECK 3:** Official titles and aims faithfully preserved from lab manual
- [x] **CHECK 4:** User's newly created circuit diagrams inserted (`01-iot.png` through `06-iot.png`)
- [x] **CHECK 5:** Reconstructed `.ino` files for Practical 02 and Practical 05 matching hardware pinouts
- [x] **CHECK 6:** Jupyter Notebooks (`.ipynb`) created and validated for data science & AIoT practicals (07, 08, 09, 10, 11)
- [x] **CHECK 7:** White-background, printer-friendly outputs and high-resolution plots generated
- [x] **CHECK 8:** Strictly maximum 2 pages per practical (Report length: exactly 22 pages)
- [x] **CHECK 9:** No cropped circuits, no broken references, no blank pages
