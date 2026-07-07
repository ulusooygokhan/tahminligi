import streamlit as st
import pandas as pd


# =====================================
# SAYFA AYARI
# =====================================

st.set_page_config(
    page_title="Dünya Kupası Tahmin Ligi",
    page_icon="⚽",
    layout="centered"
)


# =====================================
# FUTBOL TEMASI CSS
# =====================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap'
);


*{
font-family:Poppins,sans-serif;
}


.stApp{

background:
linear-gradient(
rgba(0,20,10,.85),
rgba(0,0,0,.92)
),
url(
"https://images.unsplash.com/photo-1553778263-73a83bab9b0c"
);

background-size:cover;
background-position:center;
background-attachment:fixed;

color:white;

}



.block-container{

max-width:850px;

padding-top:30px;

}



/* Başlık */

.title{

text-align:center;

font-size:40px;

font-weight:800;

letter-spacing:2px;

}


.subtitle{

text-align:center;

color:#FFD700;

font-size:16px;

letter-spacing:4px;

margin-bottom:40px;

}




/* Kart */

.card{

background:

linear-gradient(
135deg,
rgba(0,90,45,.35),
rgba(0,0,0,.7)
);


border:

1px solid rgba(255,255,255,.2);


border-radius:25px;


padding:25px;


margin:15px 0;


text-align:center;


box-shadow:

0 10px 30px rgba(0,0,0,.5);

}



.icon{

font-size:45px;

}



.card-title{

font-size:23px;

font-weight:800;

margin-top:10px;

}



.card-text{

color:#ddd;

font-size:14px;

margin-top:10px;

}



/* Buton */

.stButton button{


width:100%;

height:55px;


background:

linear-gradient(
90deg,
#D4AF37,
#FFD700
);


border:none;


border-radius:20px;


color:#111!important;


font-weight:800;


font-size:16px;


transition:.3s;


}



.stButton button:hover{

transform:scale(1.03);

}




/* Tablo */

[data-testid="stDataFrame"]{

border-radius:20px;

overflow:hidden;

}



</style>

""",
unsafe_allow_html=True)



# =====================================
# SAYFA SİSTEMİ
# =====================================

if "page" not in st.session_state:

    st.session_state.page="home"



def git(sayfa):

    st.session_state.page=sayfa

    st.rerun()



# =====================================
# ORTAK TASARIMLAR
# =====================================


def baslik(baslik,alt):

    st.markdown(
    f"""

    <div class="title">

    {baslik}

    </div>


    <div class="subtitle">

    {alt}

    </div>

    """,
    unsafe_allow_html=True
    )



def kart(icon,title,text,key):


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


    if st.button(
        title,
        key=key
    ):

        git(key)



def geri():

    if st.button("⬅ ANA MENÜ"):

        git("home")



# =====================================
# ANA SAYFA
# =====================================


def ana_sayfa():


    baslik(
        "🏆<br>DÜNYA KUPASI<br>TAHMİN LİGİ",
        "FIFA 2026 EXPERIENCE"
    )


    kart(
        "🥇",
        "GENEL PUAN",
        "Oyuncu sıralaması ve liderlik tablosu",
        "genel"
    )


    kart(
        "⚡",
        "GÜNLÜK SONUÇLAR",
        "Günlük alınan puanlar",
        "gunluk"
    )


    kart(
        "📅",
        "MAÇ PROGRAMI",
        "Turnuva fikstürü",
        "program"
    )


    kart(
        "⚽",
        "CANLI SKOR",
        "Karşılaşma takip merkezi",
        "canli"
    )



# =====================================
# GENEL PUAN
# =====================================


def genel():

    baslik(
        "🥇 GENEL PUAN",
        "LİDERLİK TABLOSU"
    )


    geri()


    try:

        df=pd.read_csv(
            "genel_durum.csv"
        )


        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


    except:

        st.error(
            "genel_durum.csv bulunamadı"
        )# =====================================
# GÜNLÜK SONUÇLAR
# =====================================


def gunluk():


    baslik(
        "⚡ GÜNLÜK SONUÇLAR",
        "PUAN DEĞİŞİMLERİ"
    )


    geri()


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

        Günlük performans

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


        st.error(
            "gunluk_sonuclar.csv bulunamadı"
        )





# =====================================
# MAÇ PROGRAMI
# =====================================


def program():


    baslik(
        "📅 MAÇ PROGRAMI",
        "ŞAMPİYONLUK YOLU"
    )


    geri()



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
        "🏆 FİNAL",
        "🌍 ŞAMPİYON",
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
        font-weight:800;
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






# =====================================
# CANLI SKOR
# =====================================


def canli():


    baslik(
        "⚽ CANLI SKOR",
        "MAÇ MERKEZİ"
    )


    geri()



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
        font-weight:800;
        ">

        {ev}

        <br>

        ⚔️

        <br>

        {dep}

        </div>


        <br>


        <div style="
        color:#FFD700;
        font-size:32px;
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

        "🌐 FLASH SCORE",

        "https://www.flashscore.com.tr/",

        use_container_width=True

    )





# =====================================
# FOOTER
# =====================================


def footer():

    st.markdown(

    """

    <br><br>

    <div style="
    text-align:center;
    color:#888;
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




# =====================================
# TEK YÖNLENDİRME NOKTASI
# =====================================


if st.session_state.page=="home":

    ana_sayfa()



elif st.session_state.page=="genel":

    genel()



elif st.session_state.page=="gunluk":

    gunluk()



elif st.session_state.page=="program":

    program()



elif st.session_state.page=="canli":

    canli()



footer()
