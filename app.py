import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- MOBİL VE KOYU TEMA AYARLARI ---
st.set_page_config(page_title="Dünya Kupası Tahmin Ligi", layout="centered", page_icon="⚽")

# --- ÖZGÜN TASARIM (DÜNYA KUPASI HAVASI) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                    url('https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-attachment: fixed;
        color: #FFFFFF;
    }
    .program-box { 
        background-color: rgba(255, 255, 255, 0.1); 
        border-radius: 15px; 
        padding: 20px; 
        border-left: 5px solid #FFD700;
        margin-bottom: 20px; 
        backdrop-filter: blur(15px);
    }
    h1 { color: #FFD700 !important; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); }
    .stDataFrame { background: rgba(0,0,0,0.3) !important; }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ DÜNYA KUPASI LİGİ")

# --- GELECEK PROGRAM ---
st.subheader("🗓️ Gelecek Maç Programı")
st.markdown("""
<div class="program-box">
    <b>27. Gün:</b> Fransa vs Fas | <b>28. Gün:</b> İspanya vs Belçika<br>
    <b>29. Gün:</b> Norveç vs İngiltere & Arjantin vs Kolombiya/İsviçre<br>
    <b>30-31. Gün:</b> Yarı Finaller | <b>32. Gün:</b> 3.lük | <b>33. Gün:</b> FİNAL
</div>
""", unsafe_allow_html=True)

# --- SEKMELER ---
tab1, tab2, tab3 = st.tabs(["GENEL", "SONUÇLAR", "CANLI"])

with tab1:
    st.subheader("🏆 Puan Durumu")
    try:
        df_genel = pd.read_csv("genel_durum.csv")
        st.dataframe(df_genel, use_container_width=True, hide_index=True)
    except:
        st.write("Veriler yükleniyor...")

with tab2:
    st.subheader("⚡ Günlük Seçim")
    try:
        df_gunluk = pd.read_csv("gunluk_sonuclar.csv")
        secim = st.selectbox("Günü Seçin:", df_gunluk['Gün'].unique())
        df_secilen = df_gunluk[df_gunluk['Gün'] == secim].drop(columns=['Gün'])
        st.dataframe(df_secilen, use_container_width=True, hide_index=True)
    except:
        st.write("Veriler yükleniyor...")

with tab3:
    st.subheader("⚽ Canlı Maçlar")
    # Mobil uyumluluğu yüksek bir alternatif skor widget'ı (Flashscore entegrasyonu gibi)
    components.html(
        """
        <div style="width:100%; height:500px; overflow-y:scroll; border-radius:15px;">
            <script type="text/javascript" src="https://www.flashscore.com/res/_fs/js/widget.js?v=2"></script>
            <script type="text/javascript">
                flashscore_widget("fls-widget", "livescore", {"width":"100%","height":"500","theme":"dark"});
            </script>
        </div>
        """,
        height=500,
    )
