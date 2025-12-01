import streamlit as st
from database import get_all_user_logs
from config import ADMIN_USERNAME, ADMIN_PASSWORD
import pandas as pd

st.title("Admin Dashboard")

# Simple login
admin_user = st.text_input("Admin Username:")
admin_pass = st.text_input("Admin Password:", type="password")

if st.button("Login"):
    if admin_user == ADMIN_USERNAME and admin_pass == ADMIN_PASSWORD:
        st.success("Logged in as Admin!")
        
        # Display user logs
        logs = get_all_user_logs()
        if logs:
            st.subheader("User Logs")
            df_logs = pd.DataFrame(logs, columns=['ID', 'Username', 'File Name', 'Date', 'Time'])
            st.dataframe(df_logs)
        else:
            st.info("No user logs available.")
    else:
        st.error("Invalid credentials.")
