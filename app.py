import streamlit as st
from datetime import datetime

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="Muscle Code | Health Calculator",
    page_icon="💪",
    layout="centered"
)

# --- إضافة لمسات جمالية بالـ CSS (نيون وتصميم مظلم) ---
st.markdown("""
    <style>
    .main {
        background-color: #000000;
    }
    .stApp {
        background-color: #000000;
    }
    h1 {
        color: #39FF14;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 10px #39FF14;
    }
    label {
        color: white !important;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #39FF14 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 3em !important;
        width: 100% !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px #39FF14;
    }
    .report-text {
        color: #39FF14;
        background-color: #111;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        border: 1px solid #333;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")
st.write("---")

# --- واجهة المدخلات ---
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("الأسم (Name)", placeholder="مثال: أحمد")
    weight = st.number_input("الوزن (Weight - KG)", min_value=30.0, max_value=250.0, value=75.0, step=0.1)
    height = st.number_input("الطول (Height - CM)", min_value=100.0, max_value=250.0, value=175.0, step=0.1)

with col2:
    age = st.number_input("العمر (Age)", min_value=10, max_value=100, value=25, step=1)
    gender = st.selectbox("الجنس (Gender)", ["Male", "Female"])
    submit_btn = st.button("إصدار التقرير الصحي")

# --- العمليات الحسابية والنتائج ---
if submit_btn:
    if name.strip() == "":
        st.error("يرجى إدخال الاسم أولاً!")
    else:
        # الحسابات العلمية
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        gender_factor = 1 if gender == "Male" else 0
        
        # نسبة الدهون (معادلة تقريبية)
        body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * gender_factor) - 5.4
        ideal_weight = 22.5 * (height_m ** 2)
        
        # السعرات (Mifflin-St Jeor)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender_factor else -161)
        tdee = bmr * 1.55 # نشاط متوسط
        target_calories = round(tdee - 500) # عجز للتنشيف
        
        # الماكروز
        protein = round(weight * 2.0)
        carbs = round((target_calories * 0.4) / 4)
        fats = round((target_calories * 0.25) / 9)
        water = round((weight * 0.04) + 0.5, 1)

        # تجهيز نص التقرير
        report_output = f"""
==========================
 MUSCLE CODE HEALTH REPORT
==========================
 DATE: {datetime.now().strftime('%Y-%m-%d')}
 NAME: {name.upper()}
 --------------------------
 [ BODY ANALYSIS ]
 - BMI        : {bmi:.1f}
 - BODY FAT % : {max(0, body_fat):.1f}%
 - WEIGHT     : {weight} kg
 - IDEAL WT   : {round(ideal_weight)} kg
    
 [ NUTRITION PLAN ]
 - CALORIES   : {target_calories} kcal
 - PROTEIN    : {protein} g
 - CARBS      : {carbs} g
 - FATS       : {fats} g
    
 [ DAILY HABITS ]
 - WATER      : {water} L
 - CREATINE   : 5g Daily
 - TRAINING   : 4-5 Days/Wk
==========================
   DISCIPLINE IS THE KEY
=========================="""

        # عرض التقرير
        st.markdown("### 📋 تقريرك الجاهز")
        st.code(report_output, language="text")
        
        # ميزة النسخ
        st.success("تم حساب بياناتك بنجاح! انسخ التقرير أعلاه.")
        st.info("نصيحة: الانضباط هو مفتاح النتيجة!")

# تذييل الصفحة
st.write("---")
st.caption("Muscle Code App v2.0 - Built for Champions")