import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Advanced Report", page_icon="🏋️‍♂️")

# --- رقم واتسابك (عدله لرقمك الحقيقي) ---
MY_PHONE_NUMBER = "201013099096" 

st.markdown("""
    <style>
    .stApp { background-color: #000; color: white; }
    h1 { color: #39FF14; text-align: center; text-shadow: 2px 2px 10px #39FF14; }
    .stButton>button { 
        background-color: #39FF14 !important; color: black !important; 
        font-weight: bold !important; width: 100%; border-radius: 10px;
    }
    .report-card {
        background-color: #111; border: 1px solid #333; padding: 15px; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")
st.write("احصل على نظامك الغذائي والمكملات الموصى بها")

# --- المدخلات ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الأسم الكامل")
    weight = st.number_input("الوزن الحالي (كيلو)", min_value=30, value=75)
    height = st.number_input("الطول (سم)", min_value=100, value=175)
with col2:
    age = st.number_input("العمر", min_value=10, value=25)
    gender = st.selectbox("الجنس", ["Male", "Female"])
    goal = st.selectbox("هدفك الحالي", ["تنشيف وحرق دهون", "تضخيم وبناء عضلات", "تحسين اللياقة"])

# --- العمليات الحسابية ---
if st.button("إصدار التقرير الشامل"):
    if name:
        # 1. حساب الوزن المثالي (معادلة Devine)
        height_m = height / 100
        if gender == "Male":
            target_weight = round(50 + 2.3 * ((height / 2.54) - 60))
        else:
            target_weight = round(45.5 + 2.3 * ((height / 2.54) - 60))
            
        # 2. حساب السعرات (Mifflin-St Jeor)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
        tdee = bmr * 1.55 # نشاط متوسط
        
        if goal == "تنشيف وحرق دهون":
            target_calories = round(tdee - 500)
            system_name = "Low Carb / High Protein"
        elif goal == "تضخيم وبناء عضلات":
            target_calories = round(tdee + 300)
            system_name = "Lean Bulk"
        else:
            target_calories = round(tdee)
            system_name = "Balanced Maintenance"

        # 3. حساب الماكروز (Macros)
        protein = round(weight * 2.2) # 2.2 جرام لكل كيلو
        fats = round((target_calories * 0.25) / 9) # 25% من السعرات دهون صحية
        carbs = round((target_calories - (protein * 4) - (fats * 9)) / 4)
        
        # 4. المكملات الموصى بها
        supplements = "Whey Protein, Creatine Monohydrate, Multi-Vitamin"
        if goal == "تنشيف وحرق دهون":
            supplements += ", Omega-3, Caffeine"

        # تجهيز نص الرسالة للواتساب
        summary_msg = f"""أهلاً كابتن، بياناتي من موقعك:
- الاسم: {name}
- الوزن المستهدف: {target_weight} كجم
- النظام: {system_name}
- السعرات: {target_calories} سعرة
- البروتين: {protein} جم
- الكارب: {carbs} جم
- الدهون الصحية: {fats} جم
- المكملات: {supplements}
اريد البدء معك!"""

        # عرض النتائج في الموقع
        st.success("تم تحليل بياناتك بنجاح!")
        st.markdown(f"""
        <div class="report-card">
        <h3>📋 تقريرك الصحي:</h3>
        <p><b>الوزن المثالي المستهدف:</b> {target_weight} كجم</p>
        <p><b>النظام الموصى به:</b> {system_name}</p>
        <p><b>السعرات اليومية:</b> {target_calories} Kcal</p>
        <hr>
        <h4>توزيع الماكروز:</h4>
        <p>🍗 بروتين: {protein} جم</p>
        <p>🍚 كاربوهيدرات: {carbs} جم</p>
        <p>🥑 دهون صحية: {fats} جم</p>
        <hr>
        <h4>💊 المكملات الموصى بها:</h4>
        <p>{supplements}</p>
        </div>
        """, unsafe_allow_html=True)

        # زر الواتساب
        encoded_msg = urllib.parse.quote(summary_msg)
        whatsapp_url = f"https://wa.me/{MY_PHONE_NUMBER}?text={encoded_msg}"
        
        st.write("---")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; border: none; width: 100%; font-weight: bold; cursor: pointer;">
                    استلم التقرير PDF وتواصل مع الكابتن ✅
                </button>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.error("الرجاء إدخال اسمك")
