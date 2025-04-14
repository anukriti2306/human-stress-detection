
# Human Stress Detection in and through Sleep

## Project Overview

This project aims to detect **stress levels** in humans during their sleep by analyzing **physiological data** collected through **IoT-based devices**. The system uses a model trained on a dataset with various sleep-related features such as **snoring rate**, **respiration rate**, **body temperature**, and **heart rate** to predict stress levels during sleep.

The dataset used for this project is sourced from Kaggle and the **SaYoPillow project**, an IoT-based device designed to monitor sleep and detect stress. The goal is to provide a tool for better understanding and managing stress, specifically during sleep, which can improve overall **health and well-being**.

---

## Problem Description

This project aims to predict **stress levels** during sleep based on physiological data collected during sleep cycles. Stress is detected using several features, including **heart rate**, **limb movement**, and **snoring rate**, and it can be categorized into five levels (from low to high).

By accurately predicting stress levels during sleep, this system can contribute to improving sleep quality and overall stress management.

---

## Dataset

The dataset used for this project includes the following features:

| Feature Name         | Description                                        |
|----------------------|----------------------------------------------------|
| **Snoring Rate**      | Intensity of snoring during sleep.                 |
| **Respiration Rate**  | Frequency of breathing during sleep.               |
| **Body Temperature**  | Body temperature while sleeping.                   |
| **Limb Movement**     | Frequency of limb movements during sleep.          |
| **Blood Oxygen**      | Blood oxygen levels during sleep.                  |
| **Eye Movement**      | Ocular activity during sleep.                      |
| **Sleeping Hours**    | Total number of hours of sleep.                    |
| **Heart Rate**        | Heart rate during sleep.                           |
| **Stress Level**      | Detected stress level during sleep (0 - 4 scale).  |

**Stress Level** categories:
- **0**: Low/Normal
- **1**: Medium-Low
- **2**: Medium
- **3**: Medium-High
- **4**: High

---

## Getting Started

This guide will help you set up the project locally, train the model, and create a **Flask API** to serve the model. Additionally, we will use **Streamlit** to create an interactive frontend for users to input data and get stress predictions.

### Prerequisites

You will need the following to run this project:

- **Python 3.x**
- **Pipenv** (for dependency management, optional but recommended)
- **Flask** (for backend API)
- **Streamlit** (for frontend interface)
- **Scikit-learn**, **pandas**, **numpy** (for machine learning and data manipulation)

---

### Installing Dependencies

First, create a virtual environment and install the necessary libraries. You can use pipenv or pip depending on your preference.

1. **Using pipenv**:

   If you don't have **pipenv** installed, install it with:

   ```bash
   pip install pipenv
   ```

   Then, install the dependencies:

   ```bash
   pipenv install
   pipenv shell
   ```

2. **Using pip**:

   Alternatively, you can install the dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

---

### Building the Model

To train the model, run the `train.py` script, which will:

- Load and preprocess the data.
- Train the **Logistic Regression** model.
- Save the trained model and scaler for future use.

Run the following command to train the model:

```bash
python train.py
```

This will:

1. Preprocess the dataset.
2. Train the model using **Logistic Regression**.
3. Save the trained model and scaler to disk as `trained_model.pkl` and `scaler.pkl`.

---

### Serving the Model with Flask

We will serve the trained model using **Flask**. This will create an API endpoint that accepts input data, processes it, and returns the predicted stress level.

#### Flask API Setup:

In the `backend/` folder, you will find the **Flask app** (`app.py`). This file loads the trained model and scaler, then listens for incoming requests to make predictions.

Here's how to run the Flask app:

```bash
python backend/app.py
```

By default, Flask will run on **localhost:5000**.

#### Flask API Endpoint:

The Flask app provides a **POST** endpoint `/predict` that accepts data in **JSON** format and returns the predicted stress level.

Example request:

```json
{
  "features": [30, 15, 36.6, 10, 98, 5, 7, 75]
}
```

The `features` array contains the input data in the same order as the dataset's features (e.g., snoring rate, respiration rate, etc.).

Example response:

```json
{
  "prediction": 2
}
```

---

### Creating the Streamlit Frontend

**Streamlit** will be used to create an interactive user interface where users can input their sleep data and receive predictions from the Flask API.

#### Streamlit App Setup:

In the `frontend/` folder, you will find the **Streamlit app** (`stress_app.py`). This app allows users to enter their data and displays the predicted stress level.

#### Running the Streamlit App:

To run the Streamlit app, simply execute the following command:

```bash
streamlit run frontend/stress_app.py
```

Streamlit will launch a local web server, usually at **http://localhost:8501**, where you can interact with the app.

---

### Testing the Model

To test the model with some sample data:

1. **Flask Backend**: Ensure the Flask backend is running (`python backend/app.py`).
2. **Streamlit Frontend**: Run the Streamlit app (`streamlit run frontend/stress_app.py`).
3. Input sample data in the Streamlit interface, and the predicted stress level will be displayed.

---

## Citation

If you'd like to cite the research behind the dataset and the IoT-based stress detection system, you can reference the following papers:

- L. Rachakonda, A. K. Bapatla, S. P. Mohanty, and E. Kougianos, “SaYoPillow: Blockchain-Integrated Privacy-Assured IoMT Framework for Stress Management Considering Sleeping Habits”, *IEEE Transactions on Consumer Electronics (TCE)*, Vol. 67, No. 1, Feb 2021, pp. 20-29.
- L. Rachakonda, S. P. Mohanty, E. Kougianos, K. Karunakaran, and M. Ganapathiraju, “Smart-Pillow: An IoT-based Device for Stress Detection Considering Sleeping Habits”, in *Proceedings of the 4th IEEE International Symposium on Smart Electronic Systems (iSES)*, 2018, pp. 161–166.

---

