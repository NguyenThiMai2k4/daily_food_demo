import streamlit as st
from streamlit_option_menu import option_menu
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
    protein = st.number_input("Protein (g)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
    carbs = st.number_input("Carbohydrates (g)", min_value=0.0, max_value=200.0, value=30.0, step=0.5)
    fat = st.number_input("Fat (g)", min_value=0.0, max_value=100.0, value=5.0, step=0.5)

    # Selectbox cho Category
    categories = ['Beverages', 'Dairy', 'Fruits', 'Grains', 'Meat', 'Snacks', 'Vegetables']
    category = st.selectbox("Category", categories)

    # Selectbox cho Meal_Type
    meal_types = ['Breakfast', 'Dinner', 'Lunch', 'Snack']
    meal_type = st.selectbox("Meal Type", meal_types)

    # Selectbox cho Food_Item
    food_items = [
        'Apple', 'Banana', 'Beef Steak', 'Bread', 'Broccoli', 'Butter', 'Carrot',
        'Cheese', 'Chicken Breast', 'Chips', 'Chocolate', 'Coffee', 'Cookies',
        'Eggs', 'Grapes', 'Green Tea', 'Milk', 'Milkshake', 'Nuts', 'Oats',
        'Orange', 'Orange Juice', 'Paneer', 'Pasta', 'Popcorn', 'Pork Chop',
        'Potato', 'Quinoa', 'Rice', 'Salmon', 'Spinach', 'Strawberry', 'Tomato',
        'Water', 'Yogurt'
    ]
    food_item = st.selectbox("Food Item", food_items)

    # Button xác nhận
    if st.button("🔍 Phân tích dữ liệu"):
        st.session_state["input_data"] = {
            "Protein": protein,
            "Carbohydrates": carbs,
            "Fat": fat,
            "Category": category,
            "Meal_Type": meal_type,
            "Food_Item": food_item
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

        # Placeholder: sau này bạn sẽ thêm model.predict vào đây
        st.write("### 🔮 Dự đoán (demo)")
        st.success(f"Món ăn **{data['Food_Item']}** thuộc nhóm **{data['Category']}**, thường được ăn vào **{data['Meal_Type']}**.")

# =============================
# Footer
# =============================
st.markdown('<div class="footer">© 2025 Food Nutrition ML Demo | Built with ❤️ by Streamlit</div>', unsafe_allow_html=True)
