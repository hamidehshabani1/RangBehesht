
import base64
from pathlib import Path

import streamlit as st

# ---------------- تنظیمات صفحه ----------------
st.set_page_config(
    page_title="رنگ بهشت | شبکه‌های اجتماعی",
    page_icon="🔗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# مسیر فایل‌ها
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

BACKGROUND = ASSETS_DIR / "background.jpg"
LOGO = ASSETS_DIR / "logo.jpg"

# ---------------- رنگ‌ها ----------------
CREAM = "#F5E9D0"
GOLD = "#C7A66A"
DARK = "#163D32"

# ---------------- بارگذاری تصویر ----------------
def image_to_base64(path):
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode()
    return None


background_base64 = image_to_base64(BACKGROUND)
logo_base64 = image_to_base64(LOGO)

# ---------------- طراحی ظاهری ----------------
background_style = ""

if background_base64:
    background_style = f"""
    background-image:
        linear-gradient(rgba(10, 25, 20, 0.48),
                        rgba(10, 25, 20, 0.65)),
        url("data:image/jpeg;base64,{background_base64}");
    background-size: cover;
    background-position: center;
    """

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap');

    .stApp {{
        {background_style}
        background-color: {DARK};
        background-attachment: fixed;
        font-family: 'Vazirmatn', sans-serif;
    }}

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    #MainMenu, footer {{
        visibility: hidden;
    }}

    .block-container {{
        max-width: 560px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    .brand-card {{
        background: rgba(15, 40, 32, 0.88);
        border: 1px solid rgba(245, 233, 208, 0.35);
        border-radius: 28px;
        padding: 30px 24px;
        text-align: center;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.22);
        backdrop-filter: blur(12px);
        direction: rtl;
    }}

    .brand-title {{
        color: {CREAM};
        font-size: 30px;
        font-weight: 800;
        margin: 10px 0;
    }}

    .brand-description {{
        color: #E9DFC9;
        font-size: 15px;
        line-height: 2;
        margin-bottom: 18px;
    }}

    .gold-line {{
        height: 2px;
        width: 75px;
        background: {GOLD};
        margin: 18px auto;
        border-radius: 10px;
    }}

    .section-title {{
        color: {CREAM};
        font-size: 17px;
        font-weight: 600;
        text-align: center;
        margin: 20px 0 12px 0;
        direction: rtl;
    }}

    div.stLinkButton > a {{
        background: rgba(245, 233, 208, 0.96);
        color: {DARK} !important;
        border: 1px solid {GOLD};
        border-radius: 14px;
        min-height: 52px;
        font-family: 'Vazirmatn', sans-serif;
        font-size: 15px;
        font-weight: 700;
        transition: all 0.2s ease;
        direction: rtl;
    }}

    div.stLinkButton > a:hover {{
        background: {GOLD};
        border-color: {CREAM};
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
    }}

    .footer-text {{
        color: #E9DFC9;
        text-align: center;
        font-size: 12px;
        margin-top: 24px;
        direction: rtl;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- لوگو ----------------
if logo_base64:
    st.markdown(
        f"""
        <div style="text-align:center; margin-bottom:18px;">
            <img
                src="data:image/png;base64,{logo_base64}"
                style="width:140px; max-width:45%; height:auto;"
            >
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div style="
            width:130px;
            height:130px;
            margin:0 auto 20px auto;
            border:2px dashed #C7A66A;
            border-radius:50%;
            display:flex;
            align-items:center;
            justify-content:center;
            color:#F5E9D0;
            text-align:center;
            font-size:14px;
            direction:rtl;
        ">
            محل قرارگیری<br>لوگوی رنگ بهشت
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- محتوای اصلی ----------------
st.markdown(
    """
    <div class="brand-card">
        <div class="brand-title">رنگ بهشت</div>
        <div class="gold-line"></div>
        <div class="brand-description">
            «رنگ بهشت، روایت قدم‌هایی است که برای زنده نگه‌داشتن یاد شهدا برداشته می‌شوند.
        ما در گروه جهادی رنگ بهشت، با تکیه بر روحیه خدمت و کار جمعی، برای رسیدگی، رنگ‌آمیزی و زیباسازی مزار شهدا تلاش می‌کنیم؛ به این امید که سهم کوچکی در پاسداشت یاد و آرمان‌های آن‌ها داشته باشیم.
        اینجا خدمت، تنها یک کار نیست؛ روایتی است از عشق، مسئولیت و عهدی که فراموش نمی‌شود.»
                </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title"> از طریق شبکه‌های اجتماعی با ما همراه باشید</div>',
    unsafe_allow_html=True
)



# ---------------- لینک‌های شبکه‌های اجتماعی ----------------


social_links = [
    {
        "name": "اینستاگرام",
        "url": "https://www.instagram.com/rangebehesht_ir",
        "icon": ASSETS_DIR / "instagram.jpg"
    },
    {
        "name": "آپارات",
        "url": "https://www.aparat.com/rangebehesht_ir",
        "icon": ASSETS_DIR / "aparat.png"
    },
    {
        "name": "بله",
        "url": "https://ble.ir/rangebehesht_ir",
        "icon": ASSETS_DIR / "bale.jpg"
    }
]


for social in social_links:
    col1, col2 = st.columns([1, 5], vertical_alignment="center")

    with col1:
        if social["icon"].exists():
            st.image(str(social["icon"]), width=42)

    with col2:
        st.link_button(
            social["name"],
            social["url"],
            use_container_width=True
        )
