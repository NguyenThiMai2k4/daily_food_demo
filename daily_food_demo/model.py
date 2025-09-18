# ================= THÊM MÔ HÌNH ML Ở COLAB VÀO
import os

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("df_final_resampled_fixed.csv")
X = df.drop("label", axis=1)
y = df["label"]

# 2. Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,   # 20% cho test
    random_state=42, # để kết quả cố định
    stratify=y   # giữ tỉ lệ nhãn đồng đều
)
# 3. Train model
model = RandomForestClassifier(random_state=42, class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("📊 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📌 Classification report:")
print(classification_report(y_test, y_pred))

print("\n📌 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 4. Lưu model ra file .pkl
BASE_DIR = os.path.dirname(__file__)   # thư mục hiện tại (page/)
model_path = os.path.join(BASE_DIR, "model.pkl")
# with open("model.pkl", "wb") as f:
#     pickle.dump(model, f)














# import streamlit as st
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
#
# # Load dữ liệu và train model
# iris = load_iris()
# X, y = iris.data, iris.target
# model = LogisticRegression(max_iter=200)
# model.fit(X, y)
#
# st.title("🌸 Demo ML với Streamlit - Iris Classification")
#
# # Input từ người dùng
# sepal_length = st.slider("Sepal length", 4.0, 8.0, 5.0)
# sepal_width = st.slider("Sepal width", 2.0, 4.5, 3.0)
# petal_length = st.slider("Petal length", 1.0, 7.0, 4.0)
# petal_width = st.slider("Petal width", 0.1, 2.5, 1.0)
#
# # Dự đoán
# if st.button("Dự đoán"):
#     prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
#     st.success(f"Kết quả dự đoán: {iris.target_names[prediction[0]]}")
