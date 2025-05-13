# Dollar ↔ Syrian Lira Gain Calculator&nbsp;&nbsp;💱

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.x-red)
![License](https://img.shields.io/badge/license-MIT-green)

A bilingual (English & Arabic) Streamlit app that shows your potential **profit or loss** when converting US Dollars (USD) to Syrian Lira (SYP) and back.  
Switching the language radio-button flips the whole interface between **LTR** and **RTL** on the fly.

---

## Table of Contents
1. [Demo](#demo)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Running Locally](#running-locally)
6. [Project Structure](#project-structure)
7. [Testing & Linting](#testing--linting)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

---

## Demo
<p align="center">
  <img src="docs/screenshot_en.png" alt="English UI" width="45%">
  &nbsp;&nbsp;
  <img src="docs/screenshot_ar.png" alt="Arabic UI (RTL)" width="45%">
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| **Bilingual UI** | One-click switch between **English** and **Arabic**. |
| **Direction-Aware Layout** | CSS injection sets `direction: ltr/rtl` and `text-align: left/right` for both the main page and the sidebar. |
| **Instant Profit Calculation** | Shows initial conversion, reconverted USD, and absolute/percentage profit or loss. |
| **Stateless & Lightweight** | Pure client-side math—no database or backend server needed. |
| **Hot-Reload Dev Experience** | Streamlit auto-reloads on file-save. |
| **Easy Deployment** | Ready for one-click deploy on **Streamlit Community Cloud** (or Docker). |

---

## Prerequisites

* **Python ≥ 3.8**
* **Git**
* (Optional) **virtualenv / venv** for isolation

---

## Installation

```bash
# 1 Clone the repository
git clone https://github.com/your-org/syp-gain-calculator.git
cd syp-gain-calculator

# 2 Create & activate a virtual environment
python -m venv .venv
# Windows:   .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3 Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
