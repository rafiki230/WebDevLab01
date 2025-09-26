import streamlit as st

st.set_page_config(page_title="Basketball Quiz", page_icon="🏀")

st.header("🏀 BuzzFeed-Style Quiz: What Kind of Basketball Player Are You?")
st.write("Answer the questions below to find out which iconic player matches your style!")

# --- Question 1 (Radio: single choice) ---
q1 = st.radio("1. What best describes your **physical size and build**? #NEW",
              ["Tall and lean (like a wing)", 
               "Strong and muscular (like a big man)", 
               "Quick and shifty (like a guard)"])

# --- Question 2 (Multiselect: multiple choice) ---
q2 = st.multiselect("2. Which words describe your **personality on the court**? (Pick all that apply) #NEW",
                    ["Leader 👑", "Flashy ✨", "Unselfish 🤝", "Tough 💪", "Calm 😎"])

# --- Question 3 (Slider: charisma) ---
q3 = st.slider("3. Rate your **charisma and swagger** on a scale of 1–10: #NEW", 
               min_value=1, max_value=10, value=5)

# --- Question 4 (Number Input: defense) ---
q4 = st.number_input("4. How many hours a week do you spend working on your **defense**?", 0, 40, 5)

# --- Question 5 (Selectbox: clutch factor) ---
q5 = st.selectbox("5. In crunch time, what’s your go-to move?", 
                  ["Drive to the hoop 🚀", 
                   "Pull-up jumper 🎯", 
                   "Lock-down defense 🔒", 
                   "Make the smart pass 📨"])

# --- Images (at least 3) ---
st.subheader("Some iconic players:")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("Images/mj.jpg", caption="Michael Jordan — The GOAT")
with col2:
    st.image("Images/rodman.jpg", caption="Dennis Rodman — The Hustler")
with col3:
    st.image("Images/lin.jpg", caption="Jeremy Lin — The Underdog Hero")

# --- Results Logic ---
if st.button("Get My Result!"):
    # Simplified scoring logic
    if "Tough 💪" in q2 or q4 > 15:
        st.success("You are **Dennis Rodman**! Rebounding beast, defensive stopper, and ultimate hustler 💪")
    elif q3 >= 8 and "Leader 👑" in q2:
        st.success("You are **Michael Jordan**! Charismatic, clutch, and the ultimate competitor 👑")
    elif "Quick and shifty (like a guard)" in q1 or "Unselfish 🤝" in q2:
        st.success("You are **Jeremy Lin**! Smart, skilled, and inspirational underdog ⭐")
    else:
        st.success("You’re a **Hybrid Player** — a mix of grit, charisma, and brains 🏀")
