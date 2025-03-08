import streamlit as st
import pandas as pd
import time

# ✅ Set page config at the very top
st.set_page_config(page_title="Enhanced Streamlit App", layout="wide")

# ✅ Custom Styles
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; padding: 20px; }
    .stButton>button { background-color: #4CAF50; color: white; font-size: 16px; }
    .stSidebar { background-color: #dddddd; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

def main():
    # ✅ Sidebar Navigation
    with st.sidebar:
        st.header("Navigation")
        page = st.radio("Go to:", ["Home", "About"])

    if page == "Home":
        st.title("🚀 My Styled Streamlit Web App")

        # ✅ Text input
        name = st.text_input("Enter your name:")
        if name:
            st.success(f"Hello, {name}!")

        # ✅ Number input with a slider
        age = st.slider("Select your age:", 1, 100, 25)
        st.write(f"You are **{age} years old**!")

        # ✅ File Uploader
        uploaded_file = st.file_uploader("Upload a file")
        if uploaded_file:
            st.write("✅ File uploaded successfully!")

        # ✅ Progress Bar Simulation
        if st.button("Start Process"):
            with st.spinner("Processing..."):
                for i in range(100):
                    time.sleep(0.05)
                    st.progress(i + 1)
            st.success("✅ Process completed!")

    elif page == "About":
        st.title("ℹ️ About This App")
        st.write("This is a simple **Streamlit web app** with UI styling and interactive elements.")

if __name__ == "__main__":
    main()
