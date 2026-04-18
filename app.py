import streamlit as st
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Business Edition", page_icon="💪", layout="centered")

# --- تصميم النيون ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: white; }
    h1 { color: #39FF14; text-align: center; text-shadow: 2px 2px 10px #39FF14; }
    .stButton>button { 
        background-color: #39FF14 !important; color: black !important; 
        font-weight: bold !important; width: 100%; border-radius: 10px;
    }
    .stTextInput>div>div>input { background-color: #222 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")
st.write("---")

# ربط الشيت (إعداد الاتصال)
conn = st.connection("gsheets", type=GSheetsConnection)

# --- مدخلات البيانات ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الأسم الكامل")
    weight = st.number_input("الوزن (كيلو)", min_value=30, value=75)
    height = st.number_input("الطول (سم)", min_value=100, value=175)

with col2:
    age = st.number_input("العمر", min_value=10, value=25)
    gender = st.selectbox("الجنس", ["Male", "Female"])
    whatsapp = st.text_input("رقم الواتساب")

# --- زر التنفيذ ---
if st.button("إصدار التقرير الصحي مجاناً"):
    if not name or not whatsapp:
        st.error("يرجى إدخال الاسم ورقم الواتساب!")
    else:
        # 1. حساب البيانات (نفس حساباتك)
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        gender_factor = 1 if gender == "Male" else 0
        body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * gender_factor) - 5.4
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender_factor else -161)
        calories = round((bmr * 1.55) - 500)

        # 2. حفظ البيانات في جوجل شيت أوتوماتيك
        new_data = pd.DataFrame([{
            "Name": name,
            "Weight": weight,
            "WhatsApp": whatsapp,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
        
        # قراءة البيانات القديمة وإضافة الجديدة
        try:
            existing_data = conn.read(worksheet="Sheet1")
            updated_df = pd.concat([existing_data, new_data], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
        except:
            # لو الشيت فاضي خالص
            conn.update(worksheet="Sheet1", data=new_data)

        # 3. عرض التقرير للعميل
        st.success(f"تم تجهيز تقريرك يا كابتن {name}! تم حفظ بياناتك وسنتواصل معك ✅")
        st.code(f"السعرات: {calories} kcal\nنسبة الدهون: {max(0, body_fat):.1f}%", language="text")
        st.balloons()
