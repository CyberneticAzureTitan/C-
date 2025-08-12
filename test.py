
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(page_title="Test", page_icon=":tada:", layout="wide")

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie asset
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# ---------- HEADER SECTION ----------
with st.container():
    st.title("Hi, I am Utochukwu :wave:")
    st.write("I am a 15-year-old in Estonia and I am into programming with languages such as Python.")
    st.write("I use Python to write basic programs and I am still learning how to use it effectively in all settings.")
    st.write('[Learn More >](https://pythonandvba.com)')

# ---------- "WHAT I DO" SECTION ----------
with st.container():
    st.subheader("PLEASE NOTE THAT THIS IS A TEST VERSION. DO NOT SHARE THE LINK WITHOUT AUTHORIZATION!")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("All about me")
        st.markdown(""" 
        - I am a 15-year-old student from Estonia with a strong sense of justice and a clear stance against racism.  
        - Curious and digitally capable, I am exploring tools like Streamlit and engaging with AI to learn and build.  
        - Passionate about fairness and technology.  
        - Still early in my journey but already showing the mindset of someone with potential to lead and make a positive impact.
        """)

        st.subheader("A short biography about me")
        st.markdown("""
        These are facts about me that I consider interesting:
        - I was born on the 8th of November 2009.
        - I used to play Roblox, but I find it boring and a waste of time and brain cells.
        - Everything you do in life should be something that helps you in a good way. 
        """)

        st.subheader("Where to learn Python")
        st.write('If you are interested in learning Python, I recommend [Programming with Mosh](https://www.youtube.com/@programmingwithmosh) on YouTube.')
        st.write('You can also visit his [official site](https://codewithmosh.com) for professional courses on Angular, React, C#, Node.js, TypeScript, Django, JavaScript, SQL, Python, and HTML.')

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---------- CONTACT FORM ----------
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("Use the form below to get in touch:")

    contact_form = """
    <form action="https://formsubmit.co/Utochukwunnadi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Optional CSS to style form (basic)
    st.markdown("""
        <style>
        form {
            display: flex;
            flex-direction: column;
        }
        input, textarea {
            margin-bottom: 10px;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 25%;
        }
        button {
            padding: 10px;
            background-color: #00aaff;
            color: white;
            border: none;
            border-radius: 5px;
            width: 7%
        }
        </style>
    """, unsafe_allow_html=True)
