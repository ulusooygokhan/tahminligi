import streamlit as st
import pandas as pd

# --- MOBİL ÖNCELİKLİ AYARLAR ---
st.set_page_config(page_title="Tahmin Ligi", layout="wide", page_icon="⚽")

# --- ÖZGÜN DÜNYA KUPASI TEMASI VE MOBİL SABİTLEME ---
st.markdown("""
    <style>
    /* Sabit arka plan ve görsel */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=2000');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    /* Tabloların sağa sola kaymasını engelle */
    .stDataFrame { width: 100% !important; overflow-x: hidden !important; }
    
    /* İçeriklerin birbirine girmesini engelle */
    .block-container { padding: 10px !important; }
    
    /* Gelecek Program Kutusu */
    .program-box { 
        background: rgba(255, 255, 255, 0.1); padding: 15px; 
        border-radius: 10px; border-left: 5px solid #FFD700;
        font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ DÜNYA KUPASI LİGİ")

# --- GELECEK PROGRAM ---
st.markdown("""
<div class="program-box">
    <b>📅 GELECEK PROGRAM</b><br>
    27. Gün: Fransa vs Fas<br>
    28. Gün: İspanya vs Belçika<br>
    29. Gün: Norveç-İngiltere & Arjantin-Kolombiya/İsviçre<br>
    30-33. Gün: Yarı Finaller, 3.lük & FİNAL
</div>
""", unsafe_allow_html=True)

# --- SEKMELER ---
tab1, tab2, tab3 = st.tabs(["GENEL", "SONUÇLAR", "CANLI SKOR"])

with tab1:
    st.subheader("🏆 GENEL PUAN")
    try:
        df_genel = pd.read_csv("genel_durum.csv")
        st.dataframe(df_genel, use_container_width=True, hide_index=True)
    except:
        st.write("Veri bekleniyor.")

with tab2:
    st.subheader("⚡ GÜNLÜK SONUÇLAR")
    try:
        df_gunluk = pd.read_csv("gunluk_sonuclar.csv")
        secim = st.selectbox("Günü Seç:", df_gunluk['Gün'].unique())
        df_secilen = df_gunluk[df_gunluk['Gün'] == secim].drop(columns=['Gün'])
        st.dataframe(df_secilen, use_container_width=True, hide_index=True)
    except:
        st.write("Veri bekleniyor.")

with tab3:
    st.subheader("⚽ CANLI SKORLAR")
    st.markdown("Canlı skorları görüntülemek için aşağıdaki butona tıklayın:")
    st.link_button("CANLI MAÇLARI GÖR", "https://www.flashscore.com.tr/", use_container_width=True)
