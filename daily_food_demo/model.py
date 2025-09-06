import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dữ liệu và train model
iris = load_iris()
X, y = iris.data, iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

st.title("🌸 Demo ML với Streamlit - Iris Classification")

# Input từ người dùng
sepal_length = st.slider("Sepal length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal width", 0.1, 2.5, 1.0)

# Dự đoán
if st.button("Dự đoán"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success(f"Kết quả dự đoán: {iris.target_names[prediction[0]]}")
