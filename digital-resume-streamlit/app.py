from pathlib import Path
import base64
import streamlit as st
from streamlit_timeline import timeline
import io
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "display.png"
timeline_file = current_dir / "assets" / "timeline.json"
icon = current_dir / "assets" / "icon.png"

image=Image.open(icon)

st.set_page_config(page_title="Arnab Chakraborty", page_icon=image, layout="wide")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local("./assets/bg3.jpg")

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/arnab-chakraborty13/",
    "Kaggle": "https://www.kaggle.com/chakrabortyarnab",
    "GitHub": "https://github.com/chakraborty-arnab"
}

# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg" style="background-color: #151515;">
  <a class="nav-link" href=" " target="_blank">Arnab Chakraborty</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#about-me">About Me</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#timeline">Career Snapshot</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Technical Skillset</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-ex">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact Me</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Custom function for printing text
def txt3(a, b):
  col0, col1, col2 = st.columns([0.5,1,3.5])
  with col0:
    st.empty()
  with col1:
    st.markdown('**<span style="color:#27278bff">' + a + '</span>**',unsafe_allow_html=True)
  with col2:
    st.markdown(b)
  
# --- HERO SECTION ---
col1, col2, col3, col4 = st.columns([1.5,1,1.5,1], gap="medium")
with col2:
    st.image(profile_pic, width=250)

with col3:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.title("Arnab Chakraborty",anchor="title")
    st.write("### &ensp;&ensp; Making <span style='color:red'> **IT** </span> Happen! 🤖", unsafe_allow_html=True)
    st.write("\n")

lcol,rcol = st.columns([1,1.4])
with rcol:
  st.write("📫", "chakraborty.arn@northeastern.edu")
  st.download_button(
    label=" 📄  Download Resume  📄",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
  )  

#   st.subheader("Connect👋🏻")
#   for platform, link in SOCIAL_MEDIA.items():
#     st.write(f"[{platform}]({link})")  

# --- Introduction  ---
st.write('\n')
st.subheader("A few things about me...📝",anchor="about-me")
st.write("---")
st.info(''' 

#### It's a ~~Bug~~ Feature

Not another Random Forest in this world of Over-fitting. 

My motivation stems from the necessity of using data to make better decisions and grow these offerings to a wider audience. I firmly believe in placing the customer at the heart of everything I do.

I'm presently pursuing a Master's degree in Computer Software engineering at Northeastern University. I have more than three years of experience leading a team of 20+ highly skilled engineers at Quantiphi, an award-winning AI-first digital engineering company. 
In my role, I enable modern enterprises to solve convoluted business problems by building highly-scalable data-intensive applications and services in diverse industries.

My hobbies include lifting weights and constantly investing all my hard-earned money into the stock market hoping to make a fortune!
''')

# --- Career Timeline  ---
st.write('\n')
st.subheader("Career Timeline 🗓️",anchor="timeline")
st.write("---")
with st.spinner(text="Building line"):
  with open(timeline_file,"r") as f:
    data = f.read()
    timeline(data, height=500)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skillset :hammer_and_wrench:",anchor="skills")
st.write("---")
txt3('Programming', '`Python` `Javascript` `SQL` `Spark` `Java` `C++`')
txt3('ML/DL Framework', '`Scikit-Learn` `Tensorflow` `Keras` `PyTorch` `PyCaret` `H20.ai` `MLlib`')
txt3('Data visualization', '`Matplotlib` `Seaborn` `Plotly` `Altair`, `Ggplot2`')
txt3('API/Web development', '`Node.js` `Express.js` `React` `Flask` `Django` `FastAPI` `Streamlit` ')
txt3('Cloud/Data Warehouse', '`AWS` `Azure` `GCP` `Databricks` `Snowflake`')
txt3('BI Tools', '`PowerBI` `Tableau` `Looker`')
txt3('Business', '`Client Engagement` `Retail` `CPG` `Market Research` `Project Scoping` `Proposal Constructions` `Storyboarding`')



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience 🧑🏻‍💼",anchor="work-ex")
st.write("---")

# --- JOB 1
with st.expander('''
👨🏻‍💼 **Senior Business Analyst** 

Quantiphi, Jun 2021 - May 2022
'''):
  st.write(
      """
  - ► Spearheaded development of an Enterprise-wide Product Availability report on PowerBI identifying monthly revenue leakages of **$15 MM** for over **25K supermarkets** using statistical models

  - ► Reduced annualized OPEX by **12 basis points** and time to generate sales order by **60%** by semi-automating process for over **200k stores** utilizing time series modeling techniques

  - ► Led a team of 10 in engineering a computer vision based palette picking assistance and inventory estimation system across **3 warehouses**
  
  - ► Introduced a Responsible and Ethical AI compliance framework; organized monthly business reviews and technical audits; devised growth strategies for retail sector by collaborating with sales and marketing team
  """
  )

# --- JOB 2
with st.expander('''
👨🏻‍💻 **Business Analyst** 

Quantiphi, Jun 2021 - May 2022
'''):
  st.write(
      """
  - ►  Increased annual revenue by **$4 MM** and optimized refill rate by **28%** for **300K** vending machines by providing real-time recommendations based on collaborative filtering and product popularity

  - ►  Built a customer churn model with a **75% recall** and prescriptive reports on Tableau to retain restaurant business

  - ►  Mentored **200+ campus recruits**; supervised training schedules, and designed evaluation framework
  """
  )

  # ---- CONTACT ----
st.header("Get In Touch With Me!👋🏻",anchor="contact")
st.write("---") 

contact_form = """
    <form action="https://formsubmit.co/arnabchakraborty663@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
left, mid, right = st.columns(3)
with left:
    st.markdown(contact_form, unsafe_allow_html=True)
with right:
    st.subheader("Social Media")
    for platform, link in SOCIAL_MEDIA.items():
          st.write(f"[{platform}]({link})")  

with open("./styles/main.css") as f:
  st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

a,b=st.columns([1,1.3])  
with b:
  st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/https://arnabxtech.streamlit.app/label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
