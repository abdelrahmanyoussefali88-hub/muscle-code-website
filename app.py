import streamlit as st
from datetime import datetime

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Business Edition", page_icon="💪", layout="centered")

# --- تصميم النيون والواجهة ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: white; }
    h1 { color: #39FF14; text-align: center; text-shadow: 2px 2px 10px #39FF14; }
    .stButton>button { 
        background-color: #39FF14 !important; color: black !important; 
        font-weight: bold !important; width: 100%; border-radius: 10px;
    }
    .stTextInput>div>div>input { background-color: #222 !important; color: white !important; }
    .report-box { 
        background-color: #111; border: 1px solid #39FF14; padding: 20px; 
        border-radius: 10px; font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")
st.write("---")

# --- مدخلات البيانات ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الأسم الكامل")
    weight = st.number_input("الوزن (كيلو)", min_value=30, value=75)
    height = st.number_input("الطول (سم)", min_value=100, value=175)

with col2:
    age = st.number_input("العمر", min_value=10, value=25)
    gender = st.selectbox("الجنس", ["Male", "Female"])
    whatsapp = st.text_input("رقم الواتساب (لإرسال التقرير والخصومات)")

# --- زر التنفيذ ---
if st.button("إصدار التقرير الصحي مجاناً"):
    if not name or not whatsapp:
        st.error("يرجى إدخال الاسم ورقم الواتساب لاستلام تقريرك!")
    else:
        # الحسابات
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        gender_factor = 1 if gender == "Male" else 0
        body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * gender_factor) - 5.4
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender_factor else -161)
        tdee = bmr * 1.55
        calories = round(tdee - 500)
        
        # عرض التقرير
        st.success(f"أهلاً كابتن {name}! تم تجهيز تقريرك بنجاح ✅")
        
        report = f"""
        [ تحليل الجسم ]
        - مؤشر كتلة الجسم: {bmi:.1f}
        - نسبة الدهون التقريبية: {max(0, body_fat):.1f}%
        
        [ الخطة الغذائية ]
        - السعرات المستهدفة: {calories} سعرة
        - البروتين اليومي: {round(weight * 2)} جرام
        
        [ ملاحظة الكابتن ]
        تم حفظ بياناتك.. سنتواصل معك عبر واتساب ({whatsapp}) 
        لإرسال جدول تمارين مجاني مخصص لك!
        """
        
        st.markdown("### 📋 التقرير المبدئي")
        st.code(report, language="text")
        
        # هنا يمكنك إضافة تنبيه لنفسك (برمجياً) أو ببساطة جمع البيانات
        st.balloons()
        st.info("سيتم التواصل معك خلال 24 ساعة لتقديم استشارة مجانية.")

st.write("---")
st.caption("Powered by Muscle Code Business System")
