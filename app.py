# -*- coding: utf-8 -*-
"""
Dollar ↔ Syrian Lira Gain Calculator
-----------------------------------
• Arabic UI  → right-to-left (RTL)
• English UI → left-to-right (LTR)
"""
import streamlit as st

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Dollar / Syrian Lira Gain Calculator",
    page_icon="💱",          # simple icon; change or remove if you prefer
    layout="centered",
)

# ------------------------------------------------------------
# Language selector (Arabic default)
# ------------------------------------------------------------
lang = st.sidebar.radio(
    "Select Language / اختر اللغة:",
    ("English", "العربية"),
    index=1,           # default → Arabic
)

# ------------------------------------------------------------
# Direction helper (RTL for Arabic, LTR for English)
# ------------------------------------------------------------
def set_direction(is_rtl: bool):
    """Inject CSS so the whole app obeys RTL/LTR."""
    direction = "rtl" if is_rtl else "ltr"
    align     = "right" if is_rtl else "left"

    st.markdown(
        f"""
        <style>
            /* Main page */
            .stApp, .appview-container .main .block-container {{
                direction: {direction};
                text-align: {align};
            }}
            /* Sidebar */
            section[data-testid="stSidebar"] > div:first-child {{
                direction: {direction};
                text-align: {align};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_direction(lang == "العربية")

# ------------------------------------------------------------
# UI strings
# ------------------------------------------------------------
txt = {
    "English": {
        "title"        : "Dollar to Syrian Lira Gain Calculator",
        "sidebar_title": "How to Use",
        "sidebar_content": (
            "1. Enter the USD amount you want to convert.\n"
            "2. Set the current exchange rate (SYP per USD).\n"
            "3. Set your expected future rate.\n"
            "4. View results showing initial conversion, reconverted USD, "
            "and profit/loss."
        ),
        "amount"       : "Amount in USD:",
        "current_rate" : "Current rate (1 USD = X SYP):",
        "future_rate"  : "Expected future rate (1 USD = X SYP):",
        "results"      : "Results",
        "initial_conv" : "Initial conversion: {d:.2f} USD = {s:,.2f} SYP",
        "reconversion" : (
            "After rate changes to {r:.2f} SYP/USD, "
            "reconversion gives {u:.2f} USD"
        ),
        "profit_loss"  : "Profit/Loss: {p:.2f} USD ({pc:.2f}% )",
    },
    "العربية": {
        "title"        : "حاسبة الربح عند تحويل الدولار إلى الليرة السورية",
        "sidebar_title": "طريقة الاستخدام",
        "sidebar_content": (
            "1. أدخل المبلغ بالدولار الأمريكي الذي تريد تحويله.\n"
            "2. حدد السعر الحالي (ليرة سورية لكل دولار).\n"
            "3. حدد السعر المتوقع في المستقبل.\n"
            "4. اطلع على النتائج: التحويل الأولي، إعادة التحويل إلى دولار، "
            "والربح/الخسارة."
        ),
        "amount"       : "المبلغ بالدولار الأمريكي:",
        "current_rate" : "السعر الحالي (1 دولار = X ليرة سورية):",
        "future_rate"  : "السعر المتوقع مستقبلاً (1 دولار = X ليرة سورية):",
        "results"      : "النتائج",
        "initial_conv" : "المبلغ المحول أولاً: {d:.2f} دولار = {s:,.2f} ليرة سورية",
        "reconversion" : (
            "عند تغير السعر إلى {r:.2f} ليرة/دولار، "
            "تصبح قيمة إعادة التحويل: {u:.2f} دولار"
        ),
        "profit_loss"  : "الربح/الخسارة: {p:.2f} دولار ({pc:.2f}٪)",
    },
}

# ------------------------------------------------------------
# Sidebar instructions
# ------------------------------------------------------------
st.sidebar.header(txt[lang]["sidebar_title"])
st.sidebar.write(txt[lang]["sidebar_content"])

# Main title
st.title(txt[lang]["title"])

# ------------------------------------------------------------
# Inputs
# ------------------------------------------------------------
usd = st.number_input(
    txt[lang]["amount"],
    min_value=0.0,
    value=1.0,
    step=0.1,
    format="%.2f",
)
cur_rate = st.number_input(
    txt[lang]["current_rate"],
    min_value=0.0,
    value=10000.0,
    step=100.0,
    format="%.2f",
)
fut_rate = st.number_input(
    txt[lang]["future_rate"],
    min_value=0.0,
    value=5000.0,
    step=100.0,
    format="%.2f",
)

# ------------------------------------------------------------
# Calculations
# ------------------------------------------------------------
initial_syp = usd * cur_rate
reconv_usd  = initial_syp / fut_rate if fut_rate else 0.0
profit_usd  = reconv_usd - usd
profit_pct  = (profit_usd / usd * 100) if usd else 0.0

# ------------------------------------------------------------
# Results
# ------------------------------------------------------------
st.subheader(txt[lang]["results"])
st.write(txt[lang]["initial_conv"].format(d=usd, s=initial_syp))
st.write(txt[lang]["reconversion"].format(r=fut_rate, u=reconv_usd))
st.write(txt[lang]["profit_loss"].format(p=profit_usd, pc=profit_pct))
