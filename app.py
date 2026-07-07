import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- MOBİL VE KOYU TEMA AYARLARI ---
st.set_page_config(page_title="Tahmin Ligi", layout="centered", page_icon="🏆")

# --- KOYU TEMA VE SADE TASARIM ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .stDataFrame { font-size: 16px !important; }
    div[data-baseweb="select"] { font-size: 18px !important; }
    h1, h2, h3 { color: #FFFFFF !important; text-align: center; }
    .program-box { 
        background-color: #161B22; border-radius: 10px; 
        padding: 15px; border-left: 5px solid #FFDD00;
        margin-bottom: 20px; font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 TAHMİN LİGİ")

# --- GELECEK PROGRAMLAR (Yeni Eklenen Bölüm) ---
st.subheader("🗓️ Gelecek Maç Programı")
st.markdown("""
<div class="program-box">
    <b>27. Gün:</b> Fransa vs Fas<br>
    <b>28. Gün:</b> İspanya vs Belçika<br>
    <b>29. Gün:</b> Norveç vs İngiltere & Arjantin vs Kolombiya/İsviçre<br>
    <b>30. Gün:</b> Yarı Final 1. Maç<br>
    <b>31. Gün:</b> Yarı Final 2. Maç<br>
    <b>32. Gün:</b> 3.lük Maçı<br>
    <b>33. Gün:</b> Final Maçı
</div>
""", unsafe_allow_html=True)

# --- SEKMELER ---
tab1, tab2, tab3 = st.tabs(["GENEL", "SONUÇLAR", "CANLI"])

with tab1:
    st.subheader("Puan Durumu")
    try:
        df_genel = pd.read_csv("genel_durum.csv")
        st.dataframe(df_genel, use_container_width=True, hide_index=True)
    except:
        st.write("Veri yükleniyor...")

with tab2:
    st.subheader("Günlük Seçim")
    try:
        df_gunluk = pd.read_csv("gunluk_sonuclar.csv")
        gunler = df_gunluk['Gün'].unique()
        secim = st.selectbox("Günü Seçin:", gunler)
        df_secilen = df_gunluk[df_gunluk['Gün'] == secim].drop(columns=['Gün'])
        st.dataframe(df_secilen, use_container_width=True, hide_index=True)
    except:
        st.write("Veri yükleniyor...")

with tab3:
    st.subheader("Canlı Maçlar")
    components.html(
        """
        <iframe src="https://www.scorebat.com/embed/livescore/" frameborder="0" width="100%" height="500" allowfullscreen allow="autoplay; fullscreen" style="border-radius:10px;"></iframe>
        """,
        height=500,
    )
