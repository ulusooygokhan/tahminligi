import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Tahmin Ligi PRO", layout="wide", page_icon="🏆")

# --- 3D / PREMIUM CSS TASARIMI ---
st.markdown("""
    <style>
    /* Arka Plan ve Genel Tema */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    
    /* 3D Kart Efekti (Glassmorphism) */
    .css-1r6slb0, .css-18e3th9, .css-1d391kg {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    }
    
    /* Başlıklar için İddialı Neon Efekti */
    h1, h2, h3 {
        text-transform: uppercase;
        background: -webkit-linear-gradient(#ffdd00, #fbb034);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        font-weight: 900 !important;
    }
    
    /* Tablo Tasarımı */
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
        # GitHub'daki csv dosyas
