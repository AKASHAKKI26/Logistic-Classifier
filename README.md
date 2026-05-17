# Logistic-Classifier
# Wine Classification using Logistic Regression

This project is a Machine Learning web application built using Streamlit and Logistic Regression.

The model predicts the type of wine based on important wine properties.

## Wine Classes

| Class | Wine Type |
|------|--------------------------|
| 0 | Barolo-type wine |
| 1 | Grignolino-type wine |
| 2 | Barbera-type wine |

---

## Features Used

- Alcohol
- Color Intensity
- Magnesium
- Proline
- Hue

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pickle

---

## Machine Learning Algorithm

- Logistic Regression Classifier

---

## Project Structure

```text
WineClassification/
│
├── classapp.py
├── wine_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run classapp.py
```

---

## Model Accuracy

The model gives approximately:

```text
95% to 100% Accuracy
```

---

## Output Example

```text
Predicted Wine Class: 0
Wine Type: Barolo-type wine
```

---

## Author

Machine Learning Mini Project
