import streamlit as st
import pandas as pd

# --- MOBİL ÖNCELİKLİ AYARLAR ---
st.set_page_config(page_title="Tahmin Ligi", layout="centered")

# --- MİNİMALİST YEŞİL TEMALI DÜNYA KUPASI TASARIMI ---
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(180deg, #06260f 0%, #000000 100%); 
        color: #FFFFFF; font-family: sans-serif;
    }
    .title-text { 
        text-align: center; font-size: 26px; font-weight: 800; 
        margin-top: 20px; margin-bottom: 40px; color: #76FF7B;
        text-shadow: 0 0 10px rgba(118, 255, 123, 0.3);
    }
    /* Butonlar için merkezli ve büyük tasarım */
    .stButton { display: flex; justify-content: center; }
    .stButton>button {
        width: 85% !important; height: 75px !important; 
        border-radius: 20px !important; border: 1px solid #333;
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important; font-size: 18px !important; font-weight: 600 !important;
        margin-bottom: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ANA SAYFA MANTIĞI ---
if 'page' not in st.session_state: st.session_state.page = 'home'

if st.session_state.page == 'home':
    st.markdown('<div class="title-text">DÜNYA KUPASI TAHMİN LİGİ</div>', unsafe_allow_html=True)
    
    # Butonlara tıklandığında session_state anında güncellenir
    if st.button("🥇 Genel Puan Durumu"): st.session_state.page = 'genel'; st.rerun()
    if st.button("⚡ Günlük Hesaplamalar"): st.session_state.page = 'gunluk'; st.rerun()
    if st.button("📅 Gelecek Program"): st.session_state.page = 'program'; st.rerun()
    if st.button("⚽ Canlı Skorlar"): st.session_state.page = 'canli'; st.rerun()

else:
    # Geri dön butonu
    if st.button("⬅ ANA MENÜ"): st.session_state.page = 'home'; st.rerun()
    
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
        st.write("27. Gün: Fransa vs Fas")
        st.write("28. Gün: İspanya vs Belçika")
        st.write("29. Gün: Norveç-İngiltere & Arjantin-Kolombiya")
        st.write("30-33. Gün: Yarı Finaller, 3.lük & FİNAL")
        
    elif st.session_state.page == 'canli':
        st.subheader("⚽ Canlı Skorlar")
        st.link_button("CANLI MAÇLARI GÖR", "https://www.flashscore.com.tr/", use_container_width=True)
