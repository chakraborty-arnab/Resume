from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Arnab Chakraborty"
PAGE_ICON = ":wave:"
NAME = "Arnab Chakraborty"
DESCRIPTION = """
**Senior Business Analyst**
"""
EMAIL = "chakraborty.arn@northeastern.edu"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/arnab-chakraborty13/",
    "Kaggle": "https://www.kaggle.com/chakrabortyarnab",
    "GitHub": "https://github.com",
}
PROJECTS = {}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Let me tell you a few things about me")
st.write("---")
st.write(
    """
My motivation stems from the necessity of using data to make better decisions and grow these offerings to a wider audience. I firmly believe in placing the customer at the heart of everything I do.

I'm presently pursuing a Master's degree in Computer Software engineering at Northeastern University. I have more than three years of experience leading a team of 20+ highly skilled engineers at Quantiphi, an award-winning AI-first digital engineering company. 
In my role, I enable modern enterprises to solve convoluted business problems by building highly-scalable data-intensive applications and services in diverse industries.

My hobbies include lifting weights and constantly investing all my hard-earned money into the stock market hoping to make a fortune!
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skillset")
st.write("---")
st.write(
    """
- **Programming:** Python, Javascript, Spark, SQL, Java, C++
- **ML/DL Frameworks:** SKLearn, Tensorflow, Keras, PyTorch, PyCaret, H20.ai, MLlib
- **API/Web Development Frameworks:** Node.js, Express.js, React, Flask, Django, FastAPI, Streamlit
- **Cloud/Data Warehouse:** AWS, Azure, GCP, Databricks, Snowflake
- **BI Tools:** PowerBI, Tableau, Looker
- **Business:** Client communication, Retail & CPG experience, Market research, Requirements gathering, Project scoping & proposal, Storyboarding, Growth Strategy, Documentation
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Business Analyst**")
st.write("🚧", "**Quantiphi**")
st.write("Jun 2021 - Sep 2022")
st.write(
    """
- ► Spearheaded development of an Enterprise-wide Product Availability report on PowerBI identifying monthly revenue leakages of $15 MM for over 25K supermarkets using statistical models
- ► Reduced annualized OPEX by 12 basis points and time to generate sales order by 60% by semi-automating process for over 200k stores utilizing time series modeling techniques
- ► Led a team of 10 in engineering a computer vision based palette picking assistance and inventory estimation system across 3 warehouses
- ► Introduced a Responsible and Ethical AI compliance framework; organized monthly business reviews and technical audits; devised growth strategies for retail sector by collaborating with sales and marketing team
"""
)

# --- JOB 2
st.write("🚧", "**Business Analyst**")
st.write("🚧", "**Quantiphi**")
st.write("Jun 2019 - May 2021")
st.write(
    """
- ►  Increased annual revenue by $4 MM and optimized refill rate by 28% for 300K vending machines by providing real-time recommendations based on collaborative filtering and product popularity
- ►  Built a customer churn model with a 75% recall and prescriptive reports on Tableau to retain restaurant business
- ►  Mentored 200+ campus recruits; supervised training schedules, and designed evaluation framework
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
