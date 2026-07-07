import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Tahmin Ligi PRO", layout="wide", page_icon="🏆")

# --- 3D / PREMIUM CSS TASARIMI ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .css-1r6slb0, .css-18e3th9, .css-1d391kg {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    }
    h1, h2, h3 {
        text-transform: uppercase;
        background: -webkit-linear-gradient(#ffdd00, #fbb034);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        font-weight: 900 !important;
    }
    div[data-testid="stDataFrame"] {
        background: rgba(0, 0, 0, 0.5);
        border-radius: 15px;
        padding: 10px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- BAŞLIK ---
st.title("🏆 TAHMİN LİGİ PRO")
st.markdown("---")

# --- SEKMELER (TABS) ---
tab1, tab2, tab3 = st.tabs(["🥇 GENEL PUAN DURUMU", "⚡ GÜNLÜK SONUÇLAR", "⚽ CANLI SKORLAR"])

# 1. SEKME: GENEL PUAN DURUMU
with tab1:
    st.subheader("Güncel Sıralama")
    try:
        df_genel = pd.read_csv("genel_durum.csv")
        st.dataframe(df_genel, use_container_width=True, hide_index=True)
    except FileNotFoundError:
        st.info("Genel durum verisi henüz yüklenmedi.")

# 2. SEKME: GÜNLÜK SONUÇLAR
with tab2:
    st.subheader("Geçmiş Günlerin Analizi")
    try:
        df_gunluk = pd.read_csv("gunluk_sonuclar.csv")
        gunler = df_gunluk['Gün'].unique()
        gun_secimi = st.selectbox("Sonuçlarını görmek istediğiniz günü seçin:", gunler)
        df_secilen = df_gunluk[df_gunluk['Gün'] == gun_secimi]
        df_goster = df_secilen.drop(columns=['Gün'])
        st.dataframe(df_goster, use_container_width=True, hide_index=True)
    except FileNotFoundError:
        st.info("Günlük veriler (CSV) henüz yüklenmedi.")

# 3. SEKME: DÜNYA KUPASI CANLI SKOR
with tab3:
    st.subheader("Dünya Kupası Canlı Maç Sonuçları")
    components.html(
        """
        <iframe src="https://www.scorebat.com/embed/livescore/" frameborder="0" width="100%" height="600" allowfullscreen allow="autoplay; fullscreen" style="width:100%;height:600px;overflow:hidden;border-radius:15px;box-shadow: 0 4px 15px rgba(0,0,0,0.5);"></iframe>
        """,
        height=600,
    )
