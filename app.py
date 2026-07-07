import streamlit as st
import pandas as pd


# ==========================================
# SAYFA AYARI
# ==========================================

st.set_page_config(
    page_title="Dünya Kupası Tahmin Ligi",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ==========================================
# MOBİL FUTBOL TASARIMI
# ==========================================

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
rgba(0,30,15,.88),
rgba(0,0,0,.95)
),

url(
"https://images.unsplash.com/photo-1522778119026-d647f0596c20"
);


background-size:cover;

background-position:center;

background-attachment:fixed;


}



.block-container{


padding-top:15px;

padding-left:12px;

padding-right:12px;

max-width:500px;


}



/* Başlık */

.title{


text-align:center;

font-size:28px;

line-height:1.2;

font-weight:800;

margin-top:15px;


}



.subtitle{


text-align:center;

font-size:12px;

letter-spacing:3px;

color:#FFD700;

margin-bottom:25px;


}




/* Menü kart */

.card{


background:

rgba(255,255,255,.08);


border-radius:18px;


border:

1px solid rgba(255,255,255,.15);


padding:18px 10px;


margin:10px 0;


text-align:center;


backdrop-filter:blur(10px);


}



.icon{


font-size:32px;

}



.card-title{


font-size:18px;

font-weight:700;

}



.card-text{


font-size:12px;

color:#ccc;


}



/* Küçük mobil buton */

.stButton button{


height:42px!important;


border-radius:14px!important;


font-size:13px!important;


font-weight:700!important;


background:

linear-gradient(
90deg,
#D4AF37,
#FFE477
)!important;


color:#111!important;


border:none!important;


}



.stButton{


margin-bottom:8px;

}




/* tablo */

[data-testid="stDataFrame"]{


border-radius:15px;

overflow:hidden;


}



</style>


""", unsafe_allow_html=True)



# ==========================================
# SAYFA SİSTEMİ
# ==========================================


if "page" not in st.session_state:

    st.session_state.page="home"



def git(page):

    st.session_state.page=page

    st.rerun()




# ==========================================
# ORTAK
# ==========================================


def baslik(main,sub):


    st.markdown(

    f"""

    <div class="title">

    {main}

    </div>


    <div class="subtitle">

    {sub}

    </div>

    """,

    unsafe_allow_html=True

    )




def geri():

    if st.button(
        "⬅ Geri",
        key="geri"
    ):

        git("home")





def kart(icon,title,text,page):


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
        key=page
    ):

        git(page)





# ==========================================
# ANA SAYFA
# ==========================================


def home():


    baslik(
        "🏆<br>DÜNYA KUPASI<br>TAHMİN LİGİ",
        "FIFA 2026"
    )


    kart(
        "🥇",
        "GENEL PUAN",
        "Liderlik tablosu",
        "genel"
    )


    kart(
        "⚡",
        "GÜNLÜK SONUÇ",
        "Günlük puan değişimleri",
        "gunluk"
    )


    kart(
        "📅",
        "MAÇ PROGRAMI",
        "Final yolunu takip et",
        "program"
    )


    kart(
        "⚽",
        "CANLI SKOR",
        "Maç merkezi",
        "canli"
    )# ==========================================
# GENEL PUAN
# ==========================================


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



        # İlk 3 oyuncu kartı

        if len(df)>=3:


            cols=st.columns(3)


            madalya=[

                "🥇",

                "🥈",

                "🥉"

            ]



            for i,row in df.head(3).iterrows():


                with cols[i]:


                    st.markdown(

                    f"""

                    <div class="card">


                    <div class="icon">

                    {madalya[i]}

                    </div>


                    <div class="card-title">

                    {row.iloc[1]}

                    </div>


                    <div class="card-text">

                    {row.iloc[-1]} Puan

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
            "Henüz puan verisi bulunmuyor."
        )





# ==========================================
# GÜNLÜK SONUÇLAR
# ==========================================


def gunluk():


    baslik(
        "⚡ GÜNLÜK SONUÇLAR",
        "GÜN GÜN PUANLAR"
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

        Günlük Performans

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





# ==========================================
# MAÇ PROGRAMI
# ==========================================


def program():


    baslik(

        "📅 MAÇ PROGRAMI",

        "DÜNYA KUPASI FİNAL YOLU"

    )


    geri()



    maclar=[


        "🏟️ 27. Gün | Son 32 Turu",

        "🏟️ 28. Gün | Son 16 Turu",

        "🔥 29. Gün | Son 16 Turu",

        "🔥 30. Gün | Çeyrek Final",

        "⚔️ 31. Gün | Çeyrek Final",

        "⚔️ 32. Gün | Yarı Final",

        "🥉 33. Gün | 3.'lük Maçı",

        "🏆 34. Gün | DÜNYA KUPASI FİNALİ"


    ]



    for mac in maclar:



        st.markdown(

        f"""

        <div class="card">


        <div class="icon">

        ⚽

        </div>


        <div class="card-title">

        {mac}

        </div>


        <div class="card-text">

        Tahminlerini yap ve puan kazan

        </div>


        </div>

        """,

        unsafe_allow_html=True

        )
# ==========================================
# CANLI SKOR
# ==========================================


def canli():


    baslik(

        "⚽ CANLI SKOR",

        "MAÇ TAKİP MERKEZİ"

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
            "🇦🇷 Arjantin",
            "🇩🇪 Almanya",
            "0 - 0",
            "23'"
        ),


        (
            "🇵🇹 Portekiz",
            "🇭🇷 Hırvatistan",
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


        <div style="font-size:18px;font-weight:700;">


        {ev}

        <br>

        ⚔️

        <br>

        {dep}


        </div>


        <br>


        <div style="
        color:#FFD700;
        font-size:28px;
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

        "🌐 CANLI SKORLAR",

        "https://www.flashscore.com.tr/",

        use_container_width=True

    )





# ==========================================
# FOOTER
# ==========================================


def footer():


    st.markdown(

    """

    <br>

    <div style="
    text-align:center;
    color:#888;
    font-size:11px;
    padding:15px;
    ">


    🏆 Dünya Kupası Tahmin Ligi

    <br>

    FIFA 2026 Experience


    </div>

    """,

    unsafe_allow_html=True

    )





# ==========================================
# TEK YÖNLENDİRME SİSTEMİ
# ==========================================


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
