import streamlit as st

# Беттің баптаулары
st.set_page_config(
    page_title="Ерекше Бонус Алыңыз!",
    page_icon="🚀",
    layout="centered"
)

# Өзгертуге болатын негізгі деректер
TELEGRAM_CHANNEL_LINK = "https://t.me/yours_channel_name"  # Өз арнаңыздың сілтемесі
BONUS_TITLE = "🎁 Тегін Чек-лист / Бағыт-бағдар алу"

# Дизайн стилін баптау (баған ортасы, түстер)
st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #2AABEE;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. САТУ ХУКЫ (Hook / Басқы тақырып)
st.title("🔥 Сарапшыдан Тәжірибелік Нұсқаулық")
st.subheader("Жүйелі түрде табысты арттырудың 3 қадамы")

st.divider()

# 2. МӘСЕЛЕ ЖӘНЕ ШЕШІМ (Pain & Solution / Воронканың екінші бөлігі)
st.write("""
Сіз де өз ісіңізде жүйесіздіктен шаршадыңыз ба? 
Біз сіз үшін арнайы тегін материал дайындадық. Оны алу үшін Telegram арнамызға жазылсаңыз болғаны!
""")

# Көрнекілік үшін сурет немесе белгі (міндетті емес)
st.info(f"📌 **Сыйлық:** {BONUS_TITLE}")

# 3. ӘРЕКЕТКЕ ШАҚЫРУ (Call to Action)
st.write("Төмендегі батырманы басып, Telegram арнаға өтіңіз де, **'БОНУС'** деп жазыңыз:")

# Тікелей Telegram арнаға жіберетін батырма
st.link_button("👉 Бонусты алу (Telegram-ға өту)", https://t.me/tuman_muzz)

st.divider()

# 4. СЕНІМДІЛІК (Social Proof / Қосымша ақпарат)
st.caption("🔒 Спамсыз. Кез келген уақытта шығып кетуге болады.")
