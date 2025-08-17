<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# PROJECT5-CERTIFICATION-GETAROUND

<em>Transforming Data into Smarter Rental Decisions</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/mmatthieu1290/Project5-Certification-Getaround?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/mmatthieu1290/Project5-Certification-Getaround?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/mmatthieu1290/Project5-Certification-Getaround?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikitlearn">
<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat&logo=Gunicorn&logoColor=white" alt="Gunicorn">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
<br>
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)

---

## Overview

Project5-Certification-Getaround is a versatile developer toolset for rent price estimation, delay analysis, and operational insights within the car rental ecosystem. It combines interactive dashboards, scalable APIs, and pre-trained models to streamline data analysis and deployment.

**Why Project5-Certification-Getaround?**

This project aims to simplify complex rent and delay analytics, enabling data-driven decisions. The core features include:

- **🧩** **Data Visualization:** Interactive dashboards for exploring rental delays, causes, and their operational impacts.
- **🚀** **Real-Time API:** Seamless integration for dynamic rent price predictions based on vehicle features.
- **🛠️** **Pre-Trained Models:** Advanced calculations for inverse rent proportion and rent loss estimations.
- **🐳** **Containerized Deployment:** Docker and Heroku configurations ensure reliable, scalable hosting.
- **🔧** **Environment Management:** Clear dependency setup for consistent development and deployment.
- **📊** **Data Analysis Notebooks:** Tools for data exploration, cleaning, and insight generation.

---

**Dashboard with streamlit:** https://mmatthieu1290-bloc-5-dashboard-streamlit-jgmoaw.streamlit.app/

**API for estimation of the price of cars:** https://my-api-bloc5.herokuapp.com/

## Description of the files.

**dashboard_streamlit.py:** contain the dashbord code in streamlit.

**requirements.txt:** a file listing all the dependencies for the dashboard on streamlit.

**db_deployment.db:** database which contains the data required for the dashboard on streamlit.

**estimator_problems_inverse.pkl:** linear regression for the inverse of proportion of rent with problem according to the threshold.

**time_losse.pkl:** cuadratic regression for the time of rent lossed according to the threshold.

**Folder APIcode:** all the file for making the API on production on heroku. The API estimates the daily price on rent thanks to a linear regression.

**Folder Notebooks:** the two notebooks that I use in order to prepare the database and to fit the models.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker

### Installation

Build Project5-Certification-Getaround from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/mmatthieu1290/Project5-Certification-Getaround
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Project5-Certification-Getaround
    ```

3. **Install the dependencies:**

**Using [docker](https://www.docker.com/):**

```sh
❯ docker build -t mmatthieu1290/Project5-Certification-Getaround .
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt, APIcode/requirements.txt
```

### Usage

Run the project with:

**Using [docker](https://www.docker.com/):**

```sh
docker run -it {image_name}
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
python {entrypoint}
```

### Testing

Project5-certification-getaround uses the {__test_framework__} test framework. Run the test suite with:

**Using [docker](https://www.docker.com/):**

```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
pytest
```

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
