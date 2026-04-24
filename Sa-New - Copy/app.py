import streamlit as st
from core.engine import run_sa_report

st.set_page_config("SA Report Automation", layout="wide")
st.title("📊 SA Monthly Report")

uploaded_files = st.file_uploader(
    "Upload Media Plan, CRAFT & Publisher Reports",
    type=["xlsx", "xls", "csv"],
    accept_multiple_files=True
)

if uploaded_files:

    file_bytes, brand, qt = run_sa_report(uploaded_files)

    st.download_button(
        "⬇️ Download SA Report",
        data=file_bytes,
        file_name=f"SA_Report_{brand}_{qt}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )















