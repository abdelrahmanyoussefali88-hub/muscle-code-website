import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Smart Logic", page_icon="🧬")

# --- رقم واتسابك الخاص ---
MY_PHONE_NUMBER = "201013099096" 

st.markdown("""
    <style>
    .stApp { background-color: #000; color: white; }
    h1 { color: #39FF14; text-align: center; text-shadow: 2px 2px 10px #39FF14; }
    .stButton>button { 
        background-color: #39FF14 !important; color: black !important; 
        font-weight: bold !important; width: 100%; border-radius: 12px;
        height: 3.5em; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")

# --- مدخلات البيانات ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الأسم الكامل")
    weight = st.number_input("الوزن الحالي (كيلو)", min_value=30, value=75)
    height = st.number_input("الطول (سم)", min_value=100, value=175)
with col2:
    age = st.number_input("العمر", min_value=10, value=25)
    gender = st.selectbox("الجنس", ["Male", "Female"])
    is_experienced = st.radio("مستوى الخبرة الرياضية:", ["مبتدئ (كتلة عضلية منخفضة)", "رياضي +1 سنة (كتلة عضلية عالية)"])

goal = st.selectbox("هدفك الحالي", ["تنشيف وحرق دهون", "تضخيم وبناء عضلات", "تحسين اللياقة"])

# --- معالجة البيانات بالمعادلات الذكية ---
if st.button("إصدار التقرير الذكي ✅"):
    if name:
        # 1. حساب الوزن المستهدف (المثالي)
        target_weight = round(height - 100) if gender == "Male" else round(height - 105)
        weight_diff = weight - target_weight

        # 2. تطبيق منطق الفرق بين المبتدئ والرياضي
        # BMR ثابت (Mifflin-St Jeor)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
        
        if is_experienced == "رياضي +1 سنة (كتلة عضلية عالية)":
            # الرياضي عنده حرق أعلى (Activity Factor أعلى)
            tdee = bmr * 1.6 
            # يحتاج بروتين أعلى للحفاظ على العضلات
            p_ratio = 2.4 if goal == "تنشيف وحرق دهون" else 2.2
            deficit = 500 if goal == "تنشيف وحرق دهون" else -400 # عجز أكبر لأنه يتحمل
        else:
            # المبتدئ حرق أبطأ (Activity Factor أقل)
            tdee = bmr * 1.35 
            # بروتين معتدل لبناء العضلات لأول مرة
            p_ratio = 1.8 if goal == "تنشيف وحرق دهون" else 1.6
            # عجز طفيف للمبتدئ عشان ميفقدش طاقته
            deficit = 300 if goal == "تنشيف وحرق دهون" else -250

        target_calories = round(tdee - deficit)
        
        # حساب الماكروز
        protein = round(weight * p_ratio)
        fats = round(weight * 0.8)
        carbs = round((target_calories - (protein * 4) - (fats * 9)) / 4)

        # تجهيز الرسالة
        summary_msg = f"""🧬 *تحليل MUSCLE CODE الذكي* 🧬
------------------------------
👤 *العميل:* {name}
🏅 *المستوى:* {is_experienced}
🎯 *الهدف:* {goal}
------------------------------
📊 *مقارنة الوزن:*
- الحالي: {weight} كجم | المستهدف: {target_weight} كجم
⚠️ *الفرق:* {weight_diff} كجم
------------------------------
🔥 *الخطة الغذائية (مخصصة لمستواك):*
👈 *السعرات:* {target_calories} سعرة
- *البروتين:* {protein} جم (عالي لضمان البناء العضلي)
- *الكارب:* {carbs} جم
- *الدهون:* {fats} جم
------------------------------
💡 *نصيحة الكابتن:*
بما أنك {is_experienced}، تم ضبط السعرات لضمان {"أقصى حرق للدهون مع حماية العضلات" if is_experienced.startswith("رياضي") else "تحسين شكل الجسم وبناء عضلات جديدة"}.
------------------------------
*أريد البدء في خطة التحول معك يا كابتن!*"""

        encoded_msg = urllib.parse.quote(summary_msg)
        whatsapp_url = f"https://wa.me/{MY_PHONE_NUMBER}?text={encoded_msg}"
        
        st.success("تم تخصيص المعادلات بناءً على كتلتك العضلية المتوقعة!")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; border: none; width: 100%; font-weight: bold; font-size: 20px; cursor: pointer;">
                    استلم التقرير المخصص لمستواك (WhatsApp) ✅
                </button>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.error("يرجى إدخال الاسم")

st.write("---")
st.caption("Muscle Code System v7.0 - Body Composition Logic")
