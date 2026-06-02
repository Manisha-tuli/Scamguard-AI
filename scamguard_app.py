import streamlit as st
from scoring.scoring import run_scoring
from main import chain

st.set_page_config(
    page_title="Email Scam Detector",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Email Scam Detector")

option = st.radio(
    "Choose Input Method",
    ["Paste Email Text", "Upload CSV"]
)

if option == "Paste Email Text":
    email_text = st.text_area(
        "Enter Email Content",
        height=250
    )

    if st.button("Analyze Email"):
        if email_text:
            with st.spinner("Analyzing..."):
                result = run_scoring(
                    chain,
                    email_text=email_text,
                    file_path=None
                )

            st.success("Analysis Complete")
            st.json(result)

elif option == "Upload CSV":

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file and st.button("Analyze CSV"):

        file_path = f"temp_{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Analyzing CSV..."):
            result = run_scoring(
                chain,
                email_text=None,
                file_path=file_path
            )

        st.success("Analysis Complete")
        st.json(result)