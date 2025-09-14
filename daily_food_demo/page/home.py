import os

import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import pandas as pd

# =============================
# Load model
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # thư mục daily_food_demo
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# =============================
# Cấu hình page
# =============================
st.set_page_config(
    page_title="Food Nutrition Demo",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# Sidebar (menu)
# =============================
with st.sidebar:
    selected = option_menu(
        "Menu",                               # Tiêu đề menu
        ["Trang chủ", "Nhập dữ liệu", "Kết quả"],     # Các trang
        icons=['house', 'cloud-upload', 'bar-chart'],# Icon cho từng mục
        menu_icon="menu-app",                                # Icon của menu chính
        default_index=0,                              # Mặc định mở trang đầu tiên
    )

# =============================
# Header
# =============================
st.markdown("""
    <style>
    .header {
        background-color: #4CAF50;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    .footer {
        margin-top: 50px;
        padding: 10px;
        text-align: center;
        color: gray;
        font-size: 14px;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">🥗 Food Nutrition ML Demo</div>', unsafe_allow_html=True)

# =============================
# Nội dung chính theo menu
# =============================
if selected == "Trang chủ":
    st.subheader("Giới thiệu")
    st.write("""
    Đây là demo ứng dụng Machine Learning dự đoán mức năng lượng từ dữ liệu dinh dưỡng.  
    Bạn có thể nhập các thông số về Protein, Carbohydrates, Fat cùng các thông tin liên quan để xem kết quả phân loại.
    """)

elif selected == "Nhập dữ liệu":
    st.subheader("📥 Nhập thông tin món ăn")

    # Input số (với ngưỡng hợp lý)
    calories = st.number_input("Calories (kcal)", min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
    protein = st.number_input("Protein (g)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
    carbs = st.number_input("Carbohydrates (g)", min_value=0.0, max_value=200.0, value=30.0, step=0.5)
    fat = st.number_input("Fat (g)", min_value=0.0, max_value=100.0, value=5.0, step=0.5)
    fiber = st.number_input("Fiber (g)", min_value=0.0, max_value=50.0, value=5.0, step=0.5)
    sugars = st.number_input("Sugars (g)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
    sodium = st.number_input("Sodium (mg)", min_value=0.0, max_value=5000.0, value=300.0, step=10.0)

    # Button xác nhận
    if st.button("🔍 Phân tích dữ liệu"):
        st.session_state["input_data"] = {
            "Calories (kcal)": calories,
            "Protein (g)": protein,
            "Carbohydrates (g)": carbs,
            "Fat (g)": fat,
            "Fiber (g)": fiber,
            "Sugars (g)": sugars,
            "Sodium (mg)": sodium
        }
        st.success("✅ Dữ liệu đã được ghi nhận! Chuyển sang tab **Kết quả** để xem.")

elif selected == "Kết quả":
    st.subheader("📊 Kết quả phân tích")

    if "input_data" not in st.session_state:
        st.warning("⚠️ Vui lòng nhập dữ liệu trước trong tab **Nhập dữ liệu**.")
    else:
        data = st.session_state["input_data"]

        st.write("### Thông tin đã nhập:")
        st.json(data)

        # Chuẩn bị dữ liệu cho model
        input_df = pd.DataFrame([data])

        # Gọi model để dự đoán
        prediction = model.predict(input_df)[0]

        st.write("### 🔮 Dự đoán")
        st.success(f"Kết quả dự đoán: **{prediction}**")

        # ================= Thống kê biểu đồ =================
        st.write("### 📊 Đánh giá thành phần dinh dưỡng")

        # Ngưỡng tham khảo (có thể chỉnh lại cho hợp lý)
        thresholds = {
            "Calories (kcal)": (400, 700),
            "Protein (g)": (10, 35),  # %
            "Carbohydrates (g)": (45, 65),  # %
            "Fat (g)": (20, 35),  # %
            "Fiber (g)": (8, 10),  # g
            "Sugars (g)": (0, 25),  # g < 25
            "Sodium (mg)": (0, 2000)  # mg < 2000
        }

        nutrients = list(data.keys())
        values = list(data.values())
        colors = []

        for nut, val in data.items():
            low, high = thresholds.get(nut, (0, float("inf")))
            if low <= val <= high:
                colors.append("dodgerblue")  # đạt
            else:
                colors.append("red")  # không đạt

        fig, ax = plt.subplots()
        ax.bar(nutrients, values, color=colors)
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Giá trị")
        plt.title("Đánh giá thành phần dinh dưỡng")
        st.pyplot(fig)

# =============================
# Footer
# =============================
st.markdown('<div class="footer">© 2025 Food Nutrition ML Demo | Built with ❤️ by Streamlit</div>', unsafe_allow_html=True)
