import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Direct System", page_icon="💪")

# --- رقم واتسابك (تأكد من كتابته بكود الدولة بدون أصفار: مثال 2010xxxxxxxx) ---
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
    .instruction-box {
        background-color: #111; padding: 20px; border-radius: 10px;
        border: 1px solid #333; text-align: center; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")

with st.container():
    st.markdown('<div class="instruction-box">أدخل بياناتك بالأسفل للحصول على تقريرك الصحي الشامل وجدول المكملات عبر الواتساب مباشرة</div>', unsafe_allow_html=True)

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

# --- معالجة البيانات وإرسالها ---
if st.button("إرسال التقرير إلى الواتساب الخاص بي ✅"):
    if name:
        # 1. حساب الوزن المثالي
        if gender == "Male":
            target_weight = round(50 + 2.3 * ((height / 2.54) - 60))
        else:
            target_weight = round(45.5 + 2.3 * ((height / 2.54) - 60))
            
        # 2. حساب السعرات (Mifflin-St Jeor)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
        tdee = bmr * 1.55 
        
        if goal == "تنشيف وحرق دهون":
            target_calories = round(tdee - 500)
            system_name = "Low Carb / High Protein"
        elif goal == "تضخيم وبناء عضلات":
            target_calories = round(tdee + 300)
            system_name = "Lean Bulk"
        else:
            target_calories = round(tdee)
            system_name = "Balanced Maintenance"

        # 3. حساب الماكروز
        protein = round(weight * 2.2)
        fats = round((target_calories * 0.25) / 9)
        carbs = round((target_calories - (protein * 4) - (fats * 9)) / 4)
        
        # 4. المكملات الموصى بها
        supplements = "Whey Protein, Creatine, Multi-Vitamin"
        if goal == "تنشيف وحرق دهون":
            supplements += ", Omega-3, L-Carnitine"

        # 5. تجهيز الرسالة "الاحترافية" اللي هتوصلك
        summary_msg = f"""🔥 تقرير MUSCLE CODE الجديد 🔥
------------------------------
👤 العميل: {name}
🎯 الهدف: {goal}
------------------------------
📊 التحليل الرقمي:
- الوزن الحالي: {weight} كجم
- الوزن المستهدف: {target_weight} كجم
- السعرات المطلوبة: {target_calories} سعرة
- النظام المقترح: {system_name}
------------------------------
🥩 الماكروز اليومية:
- البروتين: {protein} جم
- الكارب: {carbs} جم
- الدهون الصحية: {fats} جم
------------------------------
💊 المكملات الموصى بها:
{supplements}
------------------------------
رقم الواتساب للعميل تم استلامه أوتوماتيكياً."""

        # تحويل الرسالة لرابط
        encoded_msg = urllib.parse.quote(summary_msg)
        whatsapp_url = f"https://wa.me/{MY_PHONE_NUMBER}?text={encoded_msg}"
        
        # رسالة نجاح للمستخدم مع زر التحويل
        st.success("تم تحليل بياناتك! اضغط على الزر بالأسفل لفتح الواتساب واستلام التقرير كاملاً.")
        
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; border: none; width: 100%; font-weight: bold; font-size: 20px; cursor: pointer;">
                    فتح محادثة واتساب واستلام التقرير 📩
                </button>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.error("يرجى إدخال اسمك أولاً.")

st.write("---")
st.caption("Muscle Code System v4.0 - Direct Private Report")
