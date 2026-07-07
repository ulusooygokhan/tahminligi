import streamlit as st
import pandas as pd


# =====================================================
# SAYFA AYARLARI
# =====================================================

st.set_page_config(
    page_title="Dünya Kupası Tahmin Ligi",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =====================================================
# PREMIUM TASARIM
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');


* {
    font-family: 'Poppins', sans-serif;
}


.stApp {

background:
linear-gradient(
rgba(5,10,20,.88),
rgba(0,0,0,.95)
),
url("https://images.unsplash.com/photo-1508098682722-e99c43a406b2");

background-size:cover;
background-position:center;
background-attachment:fixed;

color:white;

}



.block-container {

max-width:900px;
padding-top:30px;

}




.title {

text-align:center;

font-size:42px;

font-weight:800;

letter-spacing:3px;

color:white;

margin-top:30px;

}



.subtitle {

text-align:center;

font-size:16px;

letter-spacing:5px;

color:#D4AF37;

margin-bottom:45px;

}





.card {


background:

rgba(255,255,255,.07);


border:

1px solid rgba(255,255,255,.15);


border-radius:25px;


padding:25px;


margin:15px 0;


text-align:center;


backdrop-filter:blur(15px);


transition:.3s;


}



.card:hover {


transform:translateY(-8px);


border-color:#D4AF37;


box-shadow:

0 0 35px rgba(212,175,55,.25);


}



.icon {

font-size:45px;

}



.card-title {

font-size:22px;

font-weight:700;

margin-top:10px;

}



.card-text {

font-size:14px;

color:#bbbbbb;

}




.stButton button {


width:100%;


height:60px;


border-radius:25px;


background:transparent;


border:none;


color:transparent;


position:absolute;


margin-top:-90px;


cursor:pointer;


}



.stButton {


height:0;

}




div[data-testid="stDataFrame"] {


border-radius:20px;


overflow:hidden;

}



.back button {


color:white!important;

}



@media(max-width:600px){


.title {

font-size:30px;

}


.card {

padding:20px;

}


}


</style>

""", unsafe_allow_html=True)



# =====================================================
# SESSION
# =====================================================


if "page" not in st.session_state:

    st.session_state.page="home"



def go(page):

    st.session_state.page=page

    st.rerun()



# =====================================================
# ORTAK BİLEŞENLER
# =====================================================


def header(title, subtitle):

    st.markdown(
    f"""

    <div class="title">

    {title}

    </div>


    <div class="subtitle">

    {subtitle}

    </div>

    """,
    unsafe_allow_html=True
    )



def menu_card(icon,title,text,page):


    st.markdown(
    f"""

    <div class="card">


    <div class="icon">

    {icon}

    </div>


    <div class="card-title">

    {title}

    </div>


    <div class="card-text">

    {text}

    </div>


    </div>


    """,
    unsafe_allow_html=True
    )


    if st.button(title,key=page):

        go(page)



def back():

    if st.button("⬅ ANA MENÜ"):

        go("home")



# =====================================================
# ANA SAYFA
# =====================================================


def home():


    header(
        "🏆<br>DÜNYA KUPASI<br>TAHMİN LİGİ",
        "FIFA 2026 EXPERIENCE"
    )


    menu_card(
        "🥇",
        "GENEL PUAN",
        "Turnuva sıralaması ve liderlik",
        "genel"
    )


    menu_card(
        "⚡",
        "GÜNLÜK SONUÇLAR",
        "Günlük puan değişimleri",
        "gunluk"
    )


    menu_card(
        "📅",
        "MAÇ PROGRAMI",
        "Final yolundaki karşılaşmalar",
        "program"
    )


    menu_card(
        "⚽",
        "CANLI SKOR",
        "Maç takip merkezi",
        "canli"
    )



# =====================================================
# GENEL SIRALAMA
# =====================================================


def genel():


    header(
        "🏆 GENEL SIRALAMA",
        "LİDERLİK TABLOSU"
    )


    back()


    try:

        df=pd.read_csv(
            "genel_durum.csv"
        )


        if len(df)>=3:


            cols=st.columns(3)


            medals=["🥇","🥈","🥉"]


            for i,row in df.head(3).iterrows():

                with cols[i]:

                    st.markdown(
                    f"""

                    <div class="card">

                    <div class="icon">
                    {medals[i]}
                    </div>

                    <div class="card-title">

                    {row.iloc[1]}

                    </div>


                    <div class="card-text">

                    {row.iloc[-1]} PUAN

                    </div>

                    </div>

                    """,
                    unsafe_allow_html=True
                    )


        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


    except:

        st.warning(
            "genel_durum.csv bulunamadı."
        )
# =====================================================
# GÜNLÜK SONUÇLAR
# =====================================================


def gunluk():

    header(
        "⚡ GÜNLÜK SONUÇLAR",
        "PERFORMANS TAKİBİ"
    )

    back()


    try:

        df=pd.read_csv(
            "gunluk_sonuclar.csv"
        )


        gunler=df["Gün"].unique()


        secim=st.selectbox(
            "📅 Gün Seç",
            gunler
        )


        sonuc=df[
            df["Gün"]==secim
        ]


        st.markdown(

        f"""

        <div class="card">

        <div class="icon">
        ⚡
        </div>

        <div class="card-title">

        {secim}

        </div>


        <div class="card-text">

        Günlük sonuçlar

        </div>

        </div>

        """,

        unsafe_allow_html=True

        )


        st.dataframe(
            sonuc.drop(columns=["Gün"]),
            use_container_width=True,
            hide_index=True
        )


    except:

        st.warning(
            "gunluk_sonuclar.csv bulunamadı."
        )





# =====================================================
# MAÇ PROGRAMI
# =====================================================


def program():


    header(
        "📅 MAÇ PROGRAMI",
        "FİNAL YOLU"
    )


    back()


    maclar=[


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



    for gun,ev,deplasman,tur in maclar:


        st.markdown(

        f"""

        <div class="card">


        <div class="card-title">

        {gun}

        </div>


        <br>


        <div style="
        font-size:22px;
        font-weight:700;
        ">


        {ev}


        <br>

        ⚔️

        <br>


        {deplasman}


        </div>


        <br>


        <div class="card-text">

        {tur}

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )





# =====================================================
# CANLI SKOR
# =====================================================


def canli():


    header(
        "⚽ CANLI SKOR",
        "MAÇ TAKİP MERKEZİ"
    )


    back()



    maclar=[


        (
        "🇧🇷 Brezilya",
        "🇯🇵 Japonya",
        "2 - 1",
        "65'"
        ),


        (
        "🇵🇹 Portekiz",
        "🇭🇷 Hırvatistan",
        "0 - 0",
        "23'"
        ),


        (
        "🇩🇪 Almanya",
        "🇦🇷 Arjantin",
        "-",
        "Başlamadı"
        )


    ]



    for ev,dep,skor,zaman in maclar:


        st.markdown(

        f"""

        <div class="card">


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
        color:#D4AF37;
        font-size:30px;
        font-weight:800;
        ">

        {skor}

        </div>


        <div class="card-text">

        {zaman}

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )



    st.link_button(

        "🌐 DETAYLI SKORLAR",

        "https://www.flashscore.com.tr/",

        use_container_width=True

    )




# =====================================================
# FOOTER
# =====================================================


def footer():


    st.markdown(

    """

    <br><br>


    <div style="

    text-align:center;

    color:#777;

    font-size:13px;

    ">


    🏆 Dünya Kupası Tahmin Ligi

    <br>

    FIFA 2026 Experience

    <br><br>

    © 2026


    </div>


    """,

    unsafe_allow_html=True

    )





# =====================================================
# TEK SAYFA YÖNETİMİ
# =====================================================


if st.session_state.page=="home":

    home()


elif st.session_state.page=="genel":

    genel()


elif st.session_state.page=="gunluk":

    gunluk()


elif st.session_state.page=="program":

    program()


elif st.session_state.page=="canli":

    canli()



footer()
