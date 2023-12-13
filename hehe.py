import streamlit as st
import base64

# Function to encode video
def get_encoded_video(video_path):
    with open(video_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

# Set page configuration
st.set_page_config(page_title="Fraud Dashboard", page_icon=":bar_chart:", layout="wide")

# Initialize session state if not already done
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# Functions to display each video
def display_first_video():
    encoded_video = get_encoded_video("Advance_technology_to_detect_defective_transactions.mp4")
    video_html = f"""
    <style>
    .video-container {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
    }}
    .stApp {{
        background: transparent;
    }}
    </style>
    <div class="video-container">
        <video autoplay loop muted controls style="height:100%;width:100%">
            <source type="video/mp4" src="data:video/mp4;base64,{encoded_video}">
        </video>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)

def display_second_video():
    encoded_video = get_encoded_video("star.mp4")
    video_html = f"""
    <style>
    .video--container {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: 0;
    }}
    .stApp {{
        background: transparent;
    }}
    </style>
    <div class="video--container">
        <video autoplay loop muted controls style="height:100%;width:100%">
            <source type="video/mp4" src="data:video/mp4;base64,{encoded_video}">
        </video>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)

# Streamlit interface
if not st.session_state['submitted']:
    # Display first video
    display_first_video()

    # Rest of your code for the start page...
    submitted = st.button("Let's GO")

    if submitted:
        st.session_state['submitted'] = True

elif st.session_state['submitted']:
    # Display second video
    display_second_video()

    # Rest of your code for the tabs/next section...
    # Define your tabs
