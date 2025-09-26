import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Home • Javyn Angra", page_icon="🏠")

# --- HEADER ---
st.title("Javyn Angra")
st.header("CS 1301")
st.subheader("Web Development - Section 2")  # replace X with your real section if known

st.write("---")

# --- INTRODUCTION ---
st.markdown("""
Welcome to my Super Saucy Streamlit Web Development Lab01 app!  
Use the sidebar on the left to navigate between the different pages.  
Here’s what you’ll find:
""")

# --- PAGE DESCRIPTIONS ---
st.markdown("""
1. **Portfolio**: My personal profile with education, courses, experience, leadership, and activities.  
2. **Saucy Basketball Quiz**: A saucy basketball quiz to quiz your basketballness.
""")



