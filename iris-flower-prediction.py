import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load and train
iris = load_iris()
X, y = iris.data, iris.target
clf = RandomForestClassifier()
clf.fit(X, y)

# Streamlit app
st.title("🌸 Iris Flower Classifier")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

features = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = clf.predict(features)
pred_name = iris.target_names[prediction[0]]

if st.button("🔮 Predict Flower"):
    st.success(f"🌼 It's a {pred_name} Flower!")
