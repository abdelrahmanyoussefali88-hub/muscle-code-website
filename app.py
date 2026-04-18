import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Professional System", page_icon="🔥")

# --- رقم واتسابك المحدث ---
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
    .main-text { text-align: center; font-size: 1.2rem; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")
st.markdown('<p class="main-text">حدد هدفك واحصل على تقرير السعرات والأنظمة الغذائية المقترحة</p>', unsafe_allow_html=True)

# --- مدخلات البيانات ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("الأسم الكامل")
    weight = st.number_input("الوزن الحالي (كيلو)", min_value=30, value=75)
    height = st.number_input("الطول (سم)", min_value=100, value=175)
with col2:
    age = st.number_input("العمر", min_value=10, value=25)
    gender = st.selectbox("الجنس", ["Male", "Female"])
    goal = st.selectbox("هدفك الحالي", ["تنشيف وحرق دهون", "تضخيم وبناء عضلات", "تحسين اللياقة"])

# --- معالجة البيانات ---
if st.button("إصدار التقرير وإرساله للواتساب ✅"):
    if name:
        # حساب السعرات (Mifflin-St Jeor)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
        tdee = bmr * 1.55 # نشاط متوسط
        
        # تخصيص السعرات والنسب حسب الهدف
        if goal == "تنشيف وحرق دهون":
            target_calories = round(tdee - 500)
            p_ratio, c_ratio, f_ratio = 2.4, 1.8, 0.7 # بروتين عالي للتنشيف
        elif goal == "تضخيم وبناء عضلات":
            target_calories = round(tdee + 400)
            p_ratio, c_ratio, f_ratio = 2.0, 4.5, 0.9 # كارب عالي للتضخيم
        else:
            target_calories = round(tdee)
            p_ratio, c_ratio, f_ratio = 2.0, 3.0, 0.8

        # حساب الماكروز بالجرام
        protein = round(weight * p_ratio)
        fats = round(weight * f_ratio)
        carbs = round((target_calories - (protein * 4) - (fats * 9)) / 4)

        # تجهيز الرسالة "الزتونة" للواتساب
        summary_msg = f"""🚀 *تقرير MUSCLE CODE الاحترافي* 🚀
------------------------------
👤 *العميل:* {name}
🎯 *الهدف:* {goal}
------------------------------
📊 *السعرات المستهدفة:*
👈 *{target_calories} سعرة حرارية/يوم*

🥩 *الماكروز اليومية المطلوبة:*
- *البروتين:* {protein} جم
- *الكربوهيدرات:* {carbs} جم
- *الدهون الصحية:* {fats} جم
------------------------------
🍱 *أنواع الأكل المقترحة:*
✅ *بروتين:* صدور دجاج، بياض بيض، سمك ماكريل، جبنة قريش.
✅ *كارب:* أرز بسمتي، بطاطس مسلوقة، شوفان، فاصوليا حمراء.
✅ *دهون:* زيت زيتون، مكسرات نيئة، زبدة فول سوداني، أفوكادو.
------------------------------
💊 *المكملات الأساسية:*
(Whey Protein, Creatine, Omega-3)
------------------------------
*يا كابتن، أنا جاهز أبدأ البرنامج معاك، محتاج تفاصيل الاشتراك!*"""

        # تحويل النص لرابط واتساب
        encoded_msg = urllib.parse.quote(summary_msg)
        whatsapp_url = f"https://wa.me/{MY_PHONE_NUMBER}?text={encoded_msg}"
        
        st.success(f"ممتاز يا {name}! تم حساب خطتك.")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; border: none; width: 100%; font-weight: bold; font-size: 20px; cursor: pointer;">
                    اضغط هنا لاستلام السعرات والأنظمة (WhatsApp) ✅
                </button>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.error("يرجى إدخال الاسم أولاً")

st.write("---")
st.caption("Muscle Code System v5.1 - Private Coaching Tool")
