import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Professional Data Scrubber", layout="wide")
st.title("🧼 Universal Data Cleaning Tool")
st.subheader("Upload any messy CSV and get a standardized version back.")

# 1. File Uploader
uploaded_file = st.file_uploader("Choose a messy CSV file", type="csv")

if uploaded_file is not None:
    # Read the data
    df = pd.read_csv(uploaded_file)
    
    st.write("### Raw Data Preview (First 5 Rows)")
    st.dataframe(df.head())

    # 2. Cleaning Operations
    st.sidebar.header("Cleaning Settings")
    remove_dupes = st.sidebar.checkbox("Remove Duplicate Rows", value=True)
    fix_case = st.sidebar.checkbox("Standardize Text (Proper Case)", value=True)
    fill_na = st.sidebar.selectbox("Handle Missing Values", ["Keep as is", "Fill with 0", "Drop Row"])

    if st.button("🚀 Clean My Data"):
        cleaned_df = df.copy()

        # Logic: Duplicates
        if remove_dupes:
            cleaned_df = cleaned_df.drop_duplicates()

        # Logic: Text Standardizing
        if fix_case:
            for col in cleaned_df.select_dtypes(include=['object']).columns:
                cleaned_df[col] = cleaned_df[col].astype(str).str.title()

        # Logic: Missing Values
        if fill_na == "Fill with 0":
            cleaned_df = cleaned_df.fillna(0)
        elif fill_na == "Drop Row":
            cleaned_df = cleaned_df.dropna()

        st.success("Cleaning Complete!")
        st.write("### Cleaned Data Preview")
        st.dataframe(cleaned_df.head())

        # 3. Download Feature (The "Unique" Part)
        # Convert dataframe to Excel in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            cleaned_df.to_excel(writer, index=False, sheet_name='Cleaned_Data')
        
        processed_data = output.getvalue()

        st.download_button(
            label="📥 Download Cleaned Excel File",
            data=processed_data,
            file_name="cleaned_operations_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )