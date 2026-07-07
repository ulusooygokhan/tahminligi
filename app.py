import streamlit as st
import pandas as pd

# =====================================================
# SAYFA AYARLARI
# =====================================================
st.set_page_config(page_title="Dünya Kupası Tahmin Ligi", page_icon="🏆", layout="centered", initial_sidebar_state="collapsed")

# =====================================================
# PREMIUM TASARIM (CSS)
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp {
    background: linear-gradient(rgba(5,10,20,.88), rgba(0,0,0,.95)), url("https://images.unsplash.com/photo-1508098682722-e99c43a406b2");
    background-size: cover; background-position: center; background-attachment: fixed; color: white;
}
.title { text-align:center; font-size:36px; font-weight:800; color:white; margin-top:20px; }
.subtitle { text-align:center; font-size:14px; letter-spacing:3px; color:#D4AF37; margin-bottom:30px; }
.card { background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.15); border-radius:20px; padding:20px; margin:10px 0; text-align:center; backdrop-filter:blur(10px); }
.stButton button { width:100%; height:60px; border-radius:20px; font-weight:600; }
</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION VE FONKSİYONLAR
# =====================================================
if "page" not in st.session_state: st.session_state.page = "home"

def go(page): st.session_state.page = page; st.rerun()

def header(title, subtitle):
    st.markdown(f'<div class="title">{title}</div><div class="subtitle">{subtitle}</div>', unsafe_allow_html=True)

def back():
    if st.button("⬅ ANA MENÜ"): go("home")

# =====================================================
# SAYFALAR
# =====================================================
def home():
    header("🏆 DÜNYA KUPASI<br>TAHMİN LİGİ", "FIFA 2026 EXPERIENCE")
    if st.button("🥇 GENEL PUAN DURUMU"): go("genel")
    if st.button("⚡ GÜNLÜK SONUÇLAR"): go("gunluk")
    if st.button("📅 MAÇ PROGRAMI"): go("program")
    if st.button("⚽ CANLI SKORLAR"): go("canli")

def genel():
    header("🏆 GENEL SIRALAMA", "LİDERLİK TABLOSU")
    back()
    try:
        df = pd.read_csv("genel_durum.csv")
        st.dataframe(df, use_container_width=True, hide_index=True)
    except: st.warning("genel_durum.csv bulunamadı.")

def gunluk():
    header("⚡ GÜNLÜK SONUÇLAR", "PERFORMANS TAKİBİ")
    back()
    try:
        df = pd.read_csv("gunluk_sonuclar.csv")
        secim = st.selectbox("📅 Gün Seç:", df["Gün"].unique())
        st.dataframe(df[df["Gün"] == secim].drop(columns=["Gün"]), use_container_width=True, hide_index=True)
    except: st.warning("gunluk_sonuclar.csv bulunamadı.")

def program():
    header("📅 MAÇ PROGRAMI", "FİNAL YOLU")
    back()
    st.markdown('<div class="card"><b>27. Gün:</b> Fransa vs Fas<br><b>28. Gün:</b> İspanya vs Belçika<br><b>29. Gün:</b> Norveç-İngiltere & Arjantin-Kolombiya<br><b>30-33. Gün:</b> Yarı Finaller, 3.lük & FİNAL</div>', unsafe_allow_html=True)

def canli():
    header("⚽ CANLI SKORLAR", "MAÇ TAKİP MERKEZİ")
    back()
    st.link_button("🌐 DETAYLI SKORLAR (FLASHSCORE)", "https://www.flashscore.com.tr/", use_container_width=True)

# =====================================================
# YÖNLENDİRME
# =====================================================
if st.session_state.page == "home": home()
elif st.session_state.page == "genel": genel()
elif st.session_state.page == "gunluk": gunluk()
elif st.session_state.page == "program": program()
elif st.session_state.page == "canli": canli()
