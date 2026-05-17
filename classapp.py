import streamlit as st
import pickle
import numpy as np

with open("wine_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

st.set_page_config(
    page_title="Wine Classification",
    layout="centered"
)

st.title("Wine Classification App")

st.write("Enter the wine properties below")

input_data = []

for feature in features:

    value = st.number_input(
        feature,
        min_value=0.0,
        value=1.0,
        format="%.4f"
    )

    input_data.append(value)

if st.button("Predict Wine Class"):

    input_array = np.array([input_data])

    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)

    probability = model.predict_proba(input_scaled)

    st.success(
        f"Predicted Wine Class: {prediction[0]}"
    )


    if prediction[0] == 0:
        st.success("Wine Type: Barolo-type wine")

    elif prediction[0] == 1:
        st.success("Wine Type: Grignolino-type wine")

    else:
        st.success("Wine Type: Barbera-type wine")