import streamlit as st
import pandas as pd
import os


# -----------------------------
# SAYFA AYARLARI
# -----------------------------

st.set_page_config(
    page_title="Dünya Kupası Tahmin Ligi",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# -----------------------------
# PREMIUM CSS
# -----------------------------

st.markdown("""
<style>

/* Genel */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');


html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* Ana arka plan */

.stApp {

    background:
    linear-gradient(
        rgba(3,8,18,0.88),
        rgba(3,8,18,0.95)
    ),
    url("https://images.unsplash.com/photo-1508098682722-e99c43a406b2");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;

    color:white;
}


/* Streamlit üst boşluk */

.block-container {

    padding-top:2rem;
    max-width:900px;

}



/* Başlık */

.main-title {

    text-align:center;

    font-size:42px;

    font-weight:800;

    letter-spacing:3px;

    margin-top:40px;

    color:white;

}


.sub-title {

    text-align:center;

    color:#D4AF37;

    font-size:18px;

    letter-spacing:5px;

    margin-bottom:50px;

}



/* Kart sistemi */


.menu-card {

    background:
    rgba(255,255,255,0.06);

    backdrop-filter:
    blur(15px);


    border:

    1px solid rgba(255,255,255,0.12);


    border-radius:25px;


    padding:25px;


    margin:18px 0;


    text-align:center;


    transition:0.35s;


}


.menu-card:hover {

    transform:
    translateY(-8px);


    border:

    1px solid #D4AF37;


    box-shadow:

    0 0 35px rgba(212,175,55,.25);

}



.card-icon {

    font-size:45px;

}



.card-title {

    font-size:22px;

    font-weight:700;

    margin-top:10px;

}



.card-desc {

    color:#bbbbbb;

    font-size:14px;

}



/* Butonları gizli kart yap */

div.stButton > button {


    width:100%;

    height:100%;

    position:absolute;

    opacity:0;

    cursor:pointer;

}


div.stButton {


    height:0;

}



/* Geri butonu */

.back button {


    background:

    rgba(255,255,255,.08)!important;


    color:white!important;


    border-radius:20px!important;


    border:1px solid rgba(255,255,255,.15)!important;

}



/* Tablo */

[data-testid="stDataFrame"] {


    background:

    rgba(255,255,255,.05);

    border-radius:20px;

}


/* Altın yazı */


.gold {

color:#D4AF37;

}


/* Mobil */

@media(max-width:600px){

.main-title{

font-size:30px;

}


.menu-card{

padding:20px;

}


}


</style>

""", unsafe_allow_html=True)



# -----------------------------
# SESSION
# -----------------------------


if "page" not in st.session_state:

    st.session_state.page="home"



# -----------------------------
# SAYFA DEĞİŞTİRME
# -----------------------------


def change_page(page):

    st.session_state.page=page

    st.rerun()



# -----------------------------
# BAŞLIK
# -----------------------------


def header():

    st.markdown(
    """
    <div class="main-title">

    🏆<br>
    DÜNYA KUPASI<br>
    TAHMİN LİGİ

    </div>

    <div class="sub-title">

    FIFA 2026 EXPERIENCE

    </div>

    """,
    unsafe_allow_html=True
    )



# -----------------------------
# KART OLUŞTURUCU
# -----------------------------


def card(icon,title,desc,page):


    st.markdown(
    f"""

    <div class="menu-card">

    <div class="card-icon">
    {icon}
    </div>


    <div class="card-title">
    {title}
    </div>


    <div class="card-desc">
    {desc}
    </div>


    </div>

    """,
    unsafe_allow_html=True
    )


    if st.button(
        title,
        key=page
    ):

        change_page(page)
# -----------------------------
# GENEL PUAN TABLOSU
# -----------------------------


def genel_siralama():

    st.markdown(
    """
    <div class="main-title">
    🏆 GENEL SIRALAMA
    </div>

    <div class="sub-title">
    LİDERLİK TABLOSU
    </div>
    """,
    unsafe_allow_html=True
    )


    if st.button("⬅ ANA MENÜ", key="back_general"):

        change_page("home")



    try:

        df = pd.read_csv("genel_durum.csv")


        # İlk 3 oyuncu özel gösterim

        if len(df) >= 3:


            ilk_uc = df.head(3)


            cols = st.columns(3)


            madalyalar = [
                "🥇",
                "🥈",
                "🥉"
            ]


            for i,row in ilk_uc.iterrows():

                with cols[i]:


                    st.markdown(
                    f"""

                    <div class="menu-card">

                    <div class="card-icon">
                    {madalyalar[i]}
                    </div>


                    <div class="card-title">
                    {row.iloc[1]}
                    </div>


                    <div class="card-desc">

                    {row.iloc[-1]} PUAN

                    </div>

                    </div>


                    """,
                    unsafe_allow_html=True
                    )



        st.markdown(
        """
        <br>
        """,
        unsafe_allow_html=True
        )



        # Tablo


        st.dataframe(

            df,

            use_container_width=True,

            hide_index=True

        )



    except Exception:


        st.warning(
            "Henüz puan verisi yüklenmedi."
        )



# -----------------------------
# ANA MENÜ
# -----------------------------


def home():


    header()


    card(

        "🥇",

        "GENEL PUAN",

        "Turnuva sıralaması ve liderlik tablosu",

        "genel"

    )


    card(

        "⚡",

        "GÜNLÜK SONUÇLAR",

        "Gün gün puan değişimleri",

        "gunluk"

    )


    card(

        "📅",

        "MAÇ PROGRAMI",

        "Final yolundaki tüm karşılaşmalar",

        "program"

    )


    card(

        "⚽",

        "CANLI SKOR",

        "Anlık maç sonuçlarını takip et",

        "canli"

    )



# -----------------------------
# SAYFA YÖNLENDİRME
# -----------------------------


if st.session_state.page=="home":

    home()



elif st.session_state.page=="genel":

    genel_siralama()
# -----------------------------
# GÜNLÜK SONUÇLAR
# -----------------------------


def gunluk_sonuclar():


    st.markdown(
    """
    <div class="main-title">
    ⚡ GÜNLÜK SONUÇLAR
    </div>

    <div class="sub-title">
    GÜN GÜN PUAN DEĞİŞİMLERİ
    </div>

    """,
    unsafe_allow_html=True
    )


    if st.button("⬅ ANA MENÜ", key="back_daily"):

        change_page("home")



    try:


        df = pd.read_csv(
            "gunluk_sonuclar.csv"
        )


        gunler = df["Gün"].unique()


        secilen_gun = st.selectbox(

            "📅 Gün Seç",

            gunler

        )



        sonuc = df[
            df["Gün"] == secilen_gun
        ]



        st.markdown(

        f"""

        <div class="menu-card">

        <div class="card-icon">
        ⚡
        </div>


        <div class="card-title">

        {secilen_gun}

        </div>


        <div class="card-desc">

        Günlük performans sonuçları

        </div>

        </div>

        """,

        unsafe_allow_html=True

        )



        st.dataframe(

            sonuc.drop(
                columns=["Gün"]
            ),

            use_container_width=True,

            hide_index=True

        )



    except:


        st.warning(

            "Günlük sonuç dosyası bulunamadı."

        )





# -----------------------------
# MAÇ PROGRAMI
# -----------------------------


def program():



    st.markdown(

    """

    <div class="main-title">

    📅 MAÇ PROGRAMI

    </div>


    <div class="sub-title">

    FİNAL YOLU

    </div>

    """,

    unsafe_allow_html=True

    )



    if st.button(
        "⬅ ANA MENÜ",
        key="back_program"
    ):

        change_page("home")



    maclar = [

        (
        "27. Gün",
        "🇫🇷 Fransa",
        "🇲🇦 Fas",
        "Çeyrek Final"
        ),


        (
        "28. Gün",
        "🇪🇸 İspanya",
        "🇧🇪 Belçika",
        "Çeyrek Final"
        ),


        (
        "29. Gün",
        "🇳🇴 Norveç",
        "🏴 İngiltere",
        "Yarı Final"
        ),


        (
        "30. Gün",
        "🇦🇷 Arjantin",
        "🇨🇴 Kolombiya",
        "Yarı Final"
        ),


        (
        "33. Gün",
        "🏆 Final",
        "🌎 Dünya Şampiyonu",
        "Final"
        )

    ]



    for gun,ev,dep, tur in maclar:



        st.markdown(

        f"""

        <div class="menu-card">


        <div class="card-title">

        {gun}

        </div>


        <br>


        <div style="font-size:22px;font-weight:700">

        {ev}

        <br>

        ⚔️

        <br>

        {dep}

        </div>



        <br>


        <div class="card-desc">

        {tur}

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )





# -----------------------------
# YÖNLENDİRME GÜNCELLEME
# -----------------------------

elif st.session_state.page=="program":

    program()
# -----------------------------
# CANLI SKOR SAYFASI
# -----------------------------


def canli_skor():


    st.markdown(

    """

    <div class="main-title">

    ⚽ CANLI SKOR

    </div>


    <div class="sub-title">

    MAÇ TAKİP MERKEZİ

    </div>

    """,

    unsafe_allow_html=True

    )



    if st.button(
        "⬅ ANA MENÜ",
        key="back_live"
    ):

        change_page("home")



    # İstatistik kartları


    col1, col2 = st.columns(2)



    with col1:

        st.markdown(

        """

        <div class="menu-card">

        <div class="card-icon">
        🔥
        </div>

        <div class="card-title">
        AKTİF MAÇLAR
        </div>

        <div class="card-desc">
        Güncel karşılaşmalar
        </div>

        </div>

        """,

        unsafe_allow_html=True

        )



    with col2:

        st.markdown(

        """

        <div class="menu-card">

        <div class="card-icon">
        🏆
        </div>

        <div class="card-title">
        TURNUVA
        </div>

        <div class="card-desc">
        FIFA 2026
        </div>

        </div>

        """,

        unsafe_allow_html=True

        )




    st.markdown("<br>", unsafe_allow_html=True)



    # Canlı maç kartları


    canli_maclar = [

        (
        "🇧🇷 Brezilya",
        "🇯🇵 Japonya",
        "65'",
        "2 - 1"
        ),


        (
        "🇵🇹 Portekiz",
        "🇭🇷 Hırvatistan",
        "23'",
        "0 - 0"
        ),


        (
        "🇩🇪 Almanya",
        "🇦🇷 Arjantin",
        "Başlamadı",
        "-"
        )

    ]



    for ev,dep,dakika,skor in canli_maclar:


        st.markdown(

        f"""

        <div class="menu-card">


        <div class="card-title">

        🔴 CANLI

        </div>


        <br>


        <div style="
        font-size:20px;
        font-weight:700;
        ">


        {ev}


        <br>

        ⚔️

        <br>


        {dep}


        </div>


        <br>


        <div style="
        font-size:28px;
        color:#D4AF37;
        font-weight:800;
        ">

        {skor}

        </div>


        <div class="card-desc">

        {dakika}

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )



    st.markdown("<br>",unsafe_allow_html=True)



    st.link_button(

        "🌐 DETAYLI SKORLAR",

        "https://www.flashscore.com.tr/",

        use_container_width=True

    )

# -----------------------------
# FOOTER
# -----------------------------


def footer():

    st.markdown(

    """

    <br><br>


    <div style="

    text-align:center;

    color:rgba(255,255,255,.45);

    font-size:13px;

    padding:20px;

    ">


    ━━━━━━━━━━━━━━━


    <br>


    🏆 Dünya Kupası Tahmin Ligi


    <br>


    FIFA 2026 Experience


    <br><br>


    © 2026


    </div>


    """,

    unsafe_allow_html=True

    )





# -----------------------------
# ANİMASYON EFEKTLERİ
# -----------------------------


st.markdown(

"""

<style>


@keyframes fadeIn {


from {

opacity:0;

transform:translateY(20px);

}


to {


opacity:1;

transform:translateY(0);


}


}



.menu-card {


animation:

fadeIn .6s ease;


}



.stSelectbox label {


color:white!important;

font-weight:600;

}



.stSelectbox div[data-baseweb="select"] {


background:

rgba(255,255,255,.08);


border-radius:15px;


}



button:hover {


border-color:#D4AF37!important;


}



</style>


""",

unsafe_allow_html=True

)



# Footer bütün sayfalarda

footer()
# -----------------------------
# SAYFA YÖNLENDİRME
# -----------------------------

if st.session_state.page == "home":

    home()


elif st.session_state.page == "genel":

    genel_siralama()


elif st.session_state.page == "gunluk":

    gunluk_sonuclar()


elif st.session_state.page == "program":

    program()


elif st.session_state.page == "canli":

    canli_skor()


footer()
