import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Expert System", page_icon="💪")

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
    is_experienced = st.radio("هل تتمرن منذ أكثر من سنة؟", ["نعم (جسم رياضي)", "لا (مبتدئ)"])

goal = st.selectbox("هدفك الحالي", ["تنشيف وحرق دهون", "تضخيم وبناء عضلات", "تحسين اللياقة"])

# --- معالجة البيانات ---
if st.button("إصدار التقرير والتحليل المقارن ✅"):
    if name:
        # 1. حساب الوزن المستهدف (المثالي)
        if gender == "Male":
            target_weight = round(50 + 2.3 * ((height / 2.54) - 60))
        else:
            target_weight = round(45.5 + 2.3 * ((height / 2.54) - 60))
        
        weight_diff = weight - target_weight
        diff_text = f"تحتاج خسارة {weight_diff} كجم" if weight_diff > 0 else f"تحتاج زيادة {abs(weight_diff)} كجم"

        # 2. حساب السعرات (مع مراعاة الخبرة الرياضية)
        # إذا كان رياضياً، نضرب في معامل نشاط أعلى قليلاً لأن كتلته العضلية تحرق أكثر
        activity_factor = 1.65 if is_experienced == "نعم (جسم رياضي)" else 1.4
        
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
        tdee = bmr * activity_factor
        
        if goal == "تنشيف وحرق دهون":
            target_calories = round(tdee - 500)
            p_ratio = 2.5 if is_experienced == "نعم (جسم رياضي)" else 2.0
        elif goal == "تضخيم وبناء عضلات":
            target_calories = round(tdee + 400)
            p_ratio = 2.2 if is_experienced == "نعم (جسم رياضي)" else 1.8
        else:
            target_calories = round(tdee)
            p_ratio = 2.0

        # حساب الماكروز
        protein = round(weight * p_ratio)
        fats = round(weight * 0.8)
        carbs = round((target_calories - (protein * 4) - (fats * 9)) / 4)

        # 3. تجهيز الرسالة للواتساب
        summary_msg = f"""🚀 *تقرير MUSCLE CODE المتقدم* 🚀
------------------------------
👤 *العميل:* {name}
🏅 *المستوى:* {is_experienced}
🎯 *الهدف:* {goal}
------------------------------
📏 *مقارنة الوزن:*
- الوزن الحالي: {weight} كجم
- الوزن المستهدف: {target_weight} كجم
⚠️ *الحالة:* {diff_text}
------------------------------
📊 *خطة السعرات والماكروز:*
👈 *السعرات:* {target_calories} سعرة
- البروتين: {protein} جم
- الكربوهيدرات: {carbs} جم
- الدهون الصحية: {fats} جم
------------------------------
🍱 *أمثلة للأكل المقترح:*
✅ صدور دجاج، سمك تونة، بيض، جبن قريش.
✅ أرز بسمتي، شوفان، بطاطس، كينوا.
✅ زيت زيتون، مكسرات، زبدة فول سوداني.
------------------------------
*أنا جاهز يا كابتن لبدء التحدي معك!*"""

        encoded_msg = urllib.parse.quote(summary_msg)
        whatsapp_url = f"https://wa.me/{MY_PHONE_NUMBER}?text={encoded_msg}"
        
        st.success(f"تم تحليل بياناتك بنجاح يا كابتن {name}!")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; border: none; width: 100%; font-weight: bold; font-size: 20px; cursor: pointer;">
                    استلم مقارنة الوزن وتفاصيل النظام (WhatsApp) ✅
                </button>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.error("يرجى إدخال الاسم")

st.write("---")
st.caption("Muscle Code System v6.0 - Advanced Body Analysis")
