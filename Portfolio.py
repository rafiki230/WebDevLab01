import streamlit as st
import pandas as pd
import importlib, pathlib
import info
importlib.reload(info)   # force reload
st.caption(f"Using info.py from: {pathlib.Path(info.__file__).resolve()}")

# ---------------------------
# Page setup
# ---------------------------
st.set_page_config(
    page_title="Javyn Angra • Portfolio",
    page_icon="📂",
    layout="wide",
)

# ---------------------------
# Section renderers
# ---------------------------
def about_me_section():
    st.header("👤 About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image(info.profile_picture, width=220)
        except Exception as e:
            st.info("Profile picture not found. Check info.profile_picture path.")
    with col2:
        st.write(getattr(info, "about_me", ""))
    st.write("---")

def education_section():
    st.header("🎓 Education")
    edu = getattr(info, "education_data", {})
    if edu:
        st.write(f"**{edu.get('Degree','')}**")
        st.write(f"{edu.get('Institution','')} — {edu.get('Location','')}")
        st.write(f"Graduation Date: {edu.get('Graduation Date','')}")
        st.write(f"GPA: {edu.get('GPA','')}")
    else:
        st.info("No education data found in info.education_data.")
    st.write("---")

def courses_section():
    st.header("📘 Courses")
    course_dict = getattr(info, "course_data", None)
    if isinstance(course_dict, dict) and len(course_dict) > 0:
        try:
            df_courses = pd.DataFrame(course_dict)
            st.dataframe(df_courses, use_container_width=True)
        except Exception:
            st.info("Your course_data shapes may not match. Ensure all lists are same length.")
    else:
        st.info("No course data found in info.course_data.")
    st.write("---")

def experience_section():
    st.header("💼 Experience")
    exp = getattr(info, "experience_data", {})
    if isinstance(exp, dict) and exp:
        for role, tasks in exp.items():
            st.subheader(role)
            for t in tasks:
                st.write(f"- {t}")
    else:
        st.info("No experience entries found in info.experience_data.")
    st.write("---")

def leadership_section():
    st.header("⭐ Leadership")
    lead = getattr(info, "leadership_data", {})
    if isinstance(lead, dict) and lead:
        for role, bullets in lead.items():
            st.subheader(role)
            for b in bullets:
                st.write(f"- {b}")
    else:
        st.info("No leadership entries found in info.leadership_data.")
    st.write("---")

def activities_section():
    st.header("🏅 Activities")
    if isinstance(info.activity_data, dict):
        for club, tasks in info.activity_data.items():
            st.subheader(club)
            for task in tasks:
                st.write(f"- {task}")
    elif isinstance(info.activity_data, str):
        st.markdown(info.activity_data)
    else:
        st.info("No activities found in info.activity_data.")
    st.write("---")

def contact_section():
    st.header("📫 Contact")
    if getattr(info, "my_linkedin_url", ""):
        st.write(f"[LinkedIn]({info.my_linkedin_url})")
    if getattr(info, "my_github_url", ""):
        st.write(f"[GitHub]({info.my_github_url})")
    if getattr(info, "my_email_address", ""):
        st.write(f"Email: {info.my_email_address}")
    st.write("---")

def overview():
    about_me_section()
    education_section()
    courses_section()
    experience_section()
    leadership_section()
    activities_section()
    contact_section()

# ---------------------------
# Sidebar navigation
# ---------------------------
with st.sidebar:
    st.markdown("### 📂 Javyn Angra")
    # Tiny avatar in sidebar if you like:
    try:
        st.image(info.profile_picture, width=120)
    except Exception:
        pass

    nav = st.radio(
        "Navigate",
        [
            "Overview",
            "About Me",
            "Education",
            "Courses",
            "Experience",
            "Leadership",
            "Activities",
            "Contact",
        ],
        index=0,
    )

    st.markdown("---")
    # Quick links in sidebar (optional)
    if getattr(info, "my_linkedin_url", ""):
        st.markdown(f"[LinkedIn]({info.my_linkedin_url})")
    if getattr(info, "my_github_url", ""):
        st.markdown(f"[GitHub]({info.my_github_url})")
    if getattr(info, "my_email_address", ""):
        st.markdown(f"[Email](mailto:{info.my_email_address})")

# ---------------------------
# Main router
# ---------------------------
st.title("📂 Portfolio")

if nav == "Overview":
    overview()
elif nav == "About Me":
    about_me_section()
elif nav == "Education":
    education_section()
elif nav == "Courses":
    courses_section()
elif nav == "Experience":
    experience_section()
elif nav == "Leadership":
    leadership_section()
elif nav == "Activities":
    activities_section()
elif nav == "Contact":
    contact_section()
