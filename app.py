import streamlit as st
import urllib.parse

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Muscle Code | Direct Connect", page_icon="💬")

# --- رقم واتسابك الخاص (اكتبه هنا بدقة) ---
# ملاحظة: اكتب الرقم بكود الدولة بدون أصفار أو علامة + (مثال لمصر: 2010xxxxxxxx)
MY_PHONE_NUMBER = "201013099096" 

st.markdown("""
    <style>
    .stApp { background-color: #000; color: white; }
    h1 { color: #39FF14; text-align: center; }
    .stButton>button { 
        background-color: #39FF14 !important; color: black !important; 
        font-weight: bold !important; width: 100%; border-radius: 10px;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("MUSCLE CODE ⚡")
st.write("احسب سعراتك واحصل على استشارة مجانية فوراً")

# --- المدخلات ---
name = st.text_input("الأسم الكامل")
weight = st.number_input("الوزن (كيلو)", min_value=30, value=75)
height = st.number_input("الطول (سم)", min_value=100, value=175)
age = st.number_input("العمر", min_value=10, value=25)

# --- زر التنفيذ ---
if st.button("إصدار التقرير والاتصال بالكابتن"):
    if name:
        # 1. الحسابات السريعة
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        # 2. تجهيز نص الرسالة التي ستصلك على الواتساب
        message = f"""أهلاً كابتن، أنا استخدمت موقع Muscle Code ودي بياناتي:
- الاسم: {name}
- الوزن: {weight} كجم
- الطول: {height} سم
- العمر: {age} سنة
- BMI: {bmi:.1f}
محتاج أعرف نظامي الغذائي والتدريبي المناسب."""

        # تحويل النص لصيغة روابط الإنترنت
        encoded_message = urllib.parse.quote(message)
        
        # رابط الواتساب المباشر
        whatsapp_url = f"https://wa.me/{MY_PHONE_NUMBER}?text={encoded_message}"
        
        # 3. عرض النتيجة وزر التحويل للواتساب
        st.success(f"تم حساب بياناتك يا {name}!")
        st.info("اضغط على الزر بالأسفل لاستلام تقريرك الكامل وجدول التمارين على واتسابك")
        
        # إنشاء رابط يفتح الواتساب
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    background-color: #25D366;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    display: inline-block;
                    font-size: 16px;
                    width: 100%;
                    border-radius: 10px;
                    border: none;
                    cursor: pointer;
                    font-weight: bold;">
                    اضغط هنا لاستلام التقرير على WhatsApp ✅
                </button>
            </a>
            """, unsafe_allow_html=True)
    else:
        st.error("من فضلك اكتب اسمك أولاً")

st.write("---")
st.caption("Muscle Code v3.0 - Direct WhatsApp System")
