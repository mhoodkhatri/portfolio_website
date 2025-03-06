import streamlit as st
from PIL import Image

def home():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("image.png", width=350)
    with col2:
        st.title("✨ Muhammad Hood")
        st.write("👋 Hello! I am a **biomedical engineer** passionate about merging AI with healthcare. Explore my portfolio to learn more about my work, skills, and innovations.")
    
    st.subheader("⚡ Quick Info")
    st.write("- 🎓 **Field:** Biomedical Engineering - NED University of Engineering & Technology")
    st.write("- 🛠 **Skills:** Python, Arduino, Raspberry pi, MATLAB, Biomedical Imaging")
    st.write("- 🔬 **Interests:** AI in Healthcare, Speech Therapy Systems, Medical Device Development")
    
    st.write("📌 Currently, I am learning about **Agentic AI**, a cutting-edge technology that enables AI systems to autonomously make decisions and adapt in real-time.")
    
    st.write("🗺 Use the navigation bar to explore different sections of my portfolio.")

def projects():
    st.title("🛠 My Projects")
    
    st.write("### 🗣️ Speech Therapy System - FYDP")
    st.write("Developed a **unified speech disorder therapy system** integrating sensors for real-time analysis.")
    
    st.write("### 🤖 Chatbot using Gemini API")
    st.write("Created a **chatbot** leveraging **Google's Gemini API** to provide intelligent responses and enhance user interaction.")

    st.write("### 🏥 Biomedical Imaging & Signal Processing")
    st.write("Worked on **noise removal techniques** in biomedical imaging and real-time bio-signal processing.")

    st.write("### ⚖️ BMI Calculator")
    st.write("Developed a **BMI Calculator** using Python and Streamlit to help users easily determine their Body Mass Index.")
    
    st.write("### 🌀 Arduino-based Cytocentrifuge")
    st.write("Designed and developed a **cytocentrifuge** for lab applications using Arduino and motor control.")
    
    

def contact():
    st.title("📬 Get in Touch")
    st.write("📩 **Feel free to reach out!**")
    st.write("📧 Email: m.hoodkhatri7@gmail.com")
    st.write("🔗 LinkedIn: [My LinkedIn](https://www.linkedin.com/in/m-hood-khatri-7242342b8/)")
    st.write("🌐 Facebook: [My Facebook](https://www.facebook.com/mhood.asattar/)")
    
    st.subheader("✍️ Leave a Message")
    name = st.text_input("📝 Your Name")
    message = st.text_area("💬 Your Message")
    if st.button("📨 Send Message"):
        st.success("✅ Thank you for your message! I will get back to you soon.")

# Navigation
st.sidebar.title("🧭 Navigation")
st.session_state["page"] = st.sidebar.radio("📌 Go to", ["Home", "Projects", "Contact"], index=["Home", "Projects", "Contact"].index(st.session_state.get("page", "Home")))

if st.session_state["page"] == "Home":
    home()
elif st.session_state["page"] == "Projects":
    projects()
elif st.session_state["page"] == "Contact":
    contact()
