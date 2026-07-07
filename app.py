import streamlit as st
import pandas as pd

# --- MOBİL ÖNCELİKLİ AYARLAR ---
st.set_page_config(page_title="Tahmin Ligi", layout="centered")

# --- MİNİMALİST INSTAGRAM TARZI TASARIM ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    
    /* Başlık */
    .title-text { text-align: center; font-size: 24px; font-weight: 700; margin-top: 50px; margin-bottom: 40px; color: #FFFFFF; }
    
    /* 3D Buton Stili */
    .stButton>button {
        width: 100%; height: 60px; border-radius: 15px; border: none;
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        color: white; font-size: 16px; font-weight: 600;
        box-shadow: 5px 5px 10px #000000, -2px -2px 5px #262626;
        margin-bottom: 15px; transition: 0.3s;
    }
    .stButton>button:active { transform: scale(0.98); box-shadow: inset 2px 2px 5px #000000; }
    
    /* Genel Ayarlar */
    .stDataFrame { width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

# --- ANA SAYFA MANTIĞI ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_home(): st.session_state.page = 'home'

if st.session_state.page == 'home':
    st.markdown('<div class="title-text">⚽ DÜNYA KUPASI TAHMİN LİGİ</div>', unsafe_allow_html=True)
    
    if st.button("🥇 Genel Puan Durumu"): st.session_state.page = 'genel'
    if st.button("⚡ Günlük Hesaplamalar"): st.session_state.page = 'gunluk'
    if st.button("📅 Gelecek Program"): st.session_state.page = 'program'
    if st.button("⚽ Canlı Skorlar"): st.session_state.page = 'canli'

# --- ALT SAYFALAR ---
else:
    if st.button("← Ana Menüye Dön"): go_home()
    
    if st.session_state.page == 'genel':
        st.subheader("🏆 Genel Sıralama")
        try: st.dataframe(pd.read_csv("genel_durum.csv"), use_container_width=True, hide_index=True)
        except: st.write("Veri yükleniyor...")
        
    elif st.session_state.page == 'gunluk':
        st.subheader("⚡ Günlük Sonuçlar")
        try:
            df = pd.read_csv("gunluk_sonuclar.csv")
            secim = st.selectbox("Günü Seç:", df['Gün'].unique())
            st.dataframe(df[df['Gün'] == secim].drop(columns=['Gün']), use_container_width=True, hide_index=True)
        except: st.write("Veri yükleniyor...")
            
    elif st.session_state.page == 'program':
        st.subheader("📅 Gelecek Program")
        st.markdown("""
        - **27. Gün:** Fransa vs Fas
        - **28. Gün:** İspanya vs Belçika
        - **29. Gün:** Norveç-İngiltere & Arjantin-Kolombiya/İsviçre
        - **30-33. Gün:** Yarı Finaller, 3.lük & FİNAL
        """)
        
    elif st.session_state.page == 'canli':
        st.subheader("⚽ Canlı Skorlar")
        st.link_button("CANLI MAÇLARI GÖR", "https://www.flashscore.com.tr/", use_container_width=True)
