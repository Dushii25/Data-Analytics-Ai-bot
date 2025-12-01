import streamlit as st
from data_processing import load_data, clean_data, transform_data, analyze_data
from visualization import create_bar_chart, create_pie_chart, create_line_chart, create_scatter_plot, create_heatmap
from database import log_user_data
import pandas as pd

st.set_page_config(page_title="Data Analytics Bot 🤖", layout="wide")

# User Flow: Enter name and upload dataset
st.title("Data Analytics Bot 🤖")
username = st.text_input("Enter your name:")
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel):", type=['csv', 'xlsx', 'xls'])

if username and uploaded_file:
    st.success(f"Welcome to Data Analytics Bot 🤖, {username}!")
    
    # Load and log data
    df = load_data(uploaded_file)
    log_user_data(username, uploaded_file.name)
    
    # Display raw data
    st.subheader("Raw Data Preview 👀")
    st.dataframe(df.head())
    
    # Data Cleaning
    if st.button("Clean Data 🧹"):
        df = clean_data(df)
        st.success("Data cleaned! (Handled missing values, removed duplicates, and outliers)")
        st.dataframe(df.head())
    
    # Data Transformation
    st.subheader("Data Transformation 🔄")
    rename_dict = st.text_area("Rename columns (e.g., {'old_name': 'new_name'}):", value="{}")
    type_changes = st.text_area("Change data types (e.g., {'col': 'int64'}):", value="{}")
    encode_categoricals = st.checkbox("Encode categorical values (one-hot)")
    if st.button("Transform Data  🚀"):
        try:
            rename_dict = eval(rename_dict) if rename_dict else None
            type_changes = eval(type_changes) if type_changes else None
            df = transform_data(df, rename_dict, type_changes, encode_categoricals)
            st.success("Data transformed!")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error: {e}")
    
    # Data Analysis
    if st.button("Analyze Data 📊"):
        summary, correlations, patterns = analyze_data(df)
        st.subheader("Summary Statistics 📈")
        st.dataframe(summary)
        if correlations is not None:
            st.subheader("Correlations 📉")
            st.pyplot(create_heatmap(correlations))
        st.subheader("Patterns 🔍(Categorical Value Counts)")
        for col, counts in patterns.items():
            st.write(f"**{col}:**")
            st.dataframe(counts)
    
    # Data Visualization
    st.subheader("Data Visualization  📊")
    chart_type = st.selectbox("Select Chart Type:", ["Bar", "Pie", "Line", "Scatter"])
    if chart_type in ["Bar", "Line", "Scatter"]:
        x_col = st.selectbox("X-axis Column:", df.columns)
        y_col = st.selectbox("Y-axis Column:", df.columns)
        if st.button("Generate Chart 📡"):
            if chart_type == "Bar":
                fig = create_bar_chart(df, x_col, y_col)
            elif chart_type == "Line":
                fig = create_line_chart(df, x_col, y_col)
            elif chart_type == "Scatter":
                fig = create_scatter_plot(df, x_col, y_col)
            st.plotly_chart(fig)
    elif chart_type == "Pie":
        col = st.selectbox("Column for Pie Chart:", df.columns)
        if st.button("Generate Chart 📡"):
            fig = create_pie_chart(df, col)
            st.plotly_chart(fig)
