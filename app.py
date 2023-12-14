import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import requests 
import numpy as np
from streamlit_lottie import st_lottie 
import joblib
import base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
st.set_page_config(page_title="fraud Dashboard", page_icon=":bar_chart:", layout="wide")
count = 0 
sum = 0 
sum_frud = 0 
model = joblib.load('LR_model.pkl')
def plot_data(df):
    # Replace with your preprocessing logic
    # Assuming 'edadf' is a processed version of your dataframe 'df'
    edadf = df # Replace this with actual processing logic

    # Create individual plots
    fig1 = px.line(edadf.loc[edadf['Class']==0], x='Hour', y='sum', title='Class 0 - Sum by Hour')
    fig2 = px.line(edadf.loc[edadf['Class']==1], x='Hour', y='sum', title='Class 1 - Sum by Hour', color_discrete_sequence=["red"])

    fig3 = px.line(edadf.loc[edadf['Class']==0], x='Hour', y='count', title='Class 0 - Count by Hour')
    fig4 = px.line(edadf.loc[edadf['Class']==1], x='Hour', y='count', title='Class 1 - Count by Hour', color_discrete_sequence=["red"])

    fig5 = px.line(edadf.loc[edadf['Class']==0], x='Hour', y='mean', title='Class 0 - Mean by Hour')
    fig6 = px.line(edadf.loc[edadf['Class']==1], x='Hour', y='mean', title='Class 1 - Mean by Hour', color_discrete_sequence=["red"])
    for fig in [fig1, fig2, fig3, fig4, fig5, fig6]:
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig1, fig2, fig3, fig4, fig5, fig6

img = get_img_as_base64("7vMmx.jpg")
main_bg_image_url = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8PDw8PDw8PDw8PDw8PDw8PDw8PDw8PFRUWFhUVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDQ0NDg0NDysZFRkrKzcrKzcrKzcrLTc3Ky0tKzcrKysrKysrLSsrLSsrKysrKysrKysrKysrKysrKysrK//AABEIALcBEwMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAAAQcC/8QAFhABAQEAAAAAAAAAAAAAAAAAAAER/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAEEA//EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AMvAanEAAAAAAAQAAAFAAAAABAEUAEBQAAAAAAgCoqAogAAoBQABAAUIAgAAAAAAIoAUAQU0AAEUAAAAAAAAAWCaAiiKKIAoIgoCgiiAGgFQ0BQQFAAomAKIAqFAVABQQBRAUAAAFEAEAAVAFQBYkBRRBAUQAKAqWACiKAgAAAAAKIAogKigAAAAKIAgAAAAAAAAAAAAAAABoAAAAAqAAACoACgACAoAIKAhoAAAAgKAAAABoAAAAAAAAAAAAAAAqUBUAVFAAAAAQAAAAACAAAAAAAaAAABoAqABgAAAQAFQBUABQAAAABAABMUAKAAAEAAAAAAAFQAAAAAAAAAUQAUQFEUAMASgAAAAYAimgioAqFAUAATQFAgAAAEACgAAAAAAKgAoigAAAA5UQFCJAVFAEUBFgAAAAAAAAoIAAAAAAAAAAKgAqAoigYACBBUTQUAAUAQAAAAAAVAAVAAAAAAAAAACgAAAoIUAUQAEFQABQBUioIigKACAAoAAqAgoAqAKACAACyLgAgCiKCAIAugCv//Z"

# Apply the CSS styles using st.markdown
st.markdown("""
        <style>
            .main_container {
                background-color: #FFFFFF;
            }

            h1 {
                text-align: center;
                color: #269BBB;
            }
            h2{
                text-align: center;
               color: #126C85;
            }
         
                  }
            h3{
                text-align: center;
               color: #126C85;
            }




            .stTab{
               background-color:  #269BBB;
            }
            .stTabs [data-baseweb="tab-list"] {
		gap: 30px;
    }
    
          
            body {
            background-color: #F2F2F22;}
        </style>
    """, unsafe_allow_html=True)

########################################################################
# if you want to do something about the button
    #  .stButton>button {
    #             color: #ffffff;
    #             background-color: #126C85;
    #             border: none;
    #             border-radius: 4px;
    #             padding: 0.75rem 1.5rem;
    #             margin: 0.75rem 0;
    #             position: absolute;
    #             left:40%;

    #         }
    #         .stButton>button:hover {
    #             background-color:  #269BBB;
    #             text-align: center;
    #             color: #FFFFFF;
    #         }

########################################################################
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False
    
st.markdown("""
    <style>
    .floating-form {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 1000;
    }
    </style>
    <div class="floating-form">
        <!-- Your HTML form or content here -->
    </div>
    """, unsafe_allow_html=True)
# Streamlit interface
if not st.session_state['submitted']:
        
    
        # st.write("Welcome to Eng.Majed AutoMobile Shop! Please submit to continue.")
        def get_encoded_video(video_path):
            with open(video_path, "rb") as file:
                return base64.b64encode(file.read()).decode()

    # Encode your video and create the data URI
        encoded_video = get_encoded_video("Advance_technology_to_detect_defective_transactions.mp4")

    # HTML string with the video element
        video_html = f"""
    <style>
    
            .stButton > button {{
            color: #ffffff;
            background-color: #126C85;
            border: 2px solid transparent; /* Adjusted for a clear border */
            border-radius: 4px;
            padding: 0.75rem 1.5rem;
            margin: 0.75rem 0;
             position: fixed;
                right: 30;
                left:47%;
                top: 80%;
                bottom: 70%;
           
            transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
            font-size: 16px; /* Adjusted font size for clarity */
            line-height: 1.5; /* Line height for better text alignment */
        }}

        .stButton > button:hover {{
            background-color: #269BBB;
            border-color: #269BBB; /* Border color change on hover for consistency */
            box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2); /* Optional: Adds a slight shadow for depth */
        }}
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

    # Injecting the HTML for the video background
        st.markdown(video_html, unsafe_allow_html=True)
        # st.markdown("----", unsafe_allow_html=True)
        # st.subheader("Welcome to..")
  
       
        # st.title('Credit Card Fraud Detection')
        # st.subheader("The PERFECT place to manage your Fraud with the touch of machine learning")
        # st.markdown("----", unsafe_allow_html=True)
        submitted = st.button("Let's GO")
        url = requests.get( "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json") 
        url1 = requests.get("https://assets5.lottiefiles.com/packages/lf20_awP420Zf8l.json")
# Creating a blank dictionary to store JSON file, 
# as their structure is similar to Python Dictionary 
        url_json = dict() 
        
        if url.status_code == 200: 
            url_json = url.json() 
            url_json1 = url1.json() 
        else: 
            print("Error in the URL") 
        
        st.write('')      
        st.write('') 
        st.write('')      
     
        cp , cpp =st.columns([0.3,0.1])
        # with cp:
        #     st_lottie(url_json, height=300, width=300)
        # with cpp:
        #     st_lottie(url_json1, height=250, width=250)
        if submitted:
            st.session_state['submitted'] = True
            st.experimental_rerun()  # Rerun the app to update the state
# Define your tabs
if st.session_state['submitted']:
    # encoded_video = get_encoded_video("star.mp4")

    # # HTML string with the video element
    # video_html = f"""
    # <style>
    # .video-container {{
    #     position: fixed;
    #     right: 0;
    #     bottom: 0;
    #     min-width: 100%;
    #     min-height: 100%;
    #     z-index: -1;
    # }}
    # .stApp {{
    #     background: transparent;
    # }}
    # </style>
    # <div class="video-container">
    #     <video autoplay loop muted controls style="height:100%;width:100%">
    #         <source type="video/mp4" src="data:video/mp4;base64,{encoded_video}">
    #     </video>
    # </div>
    # """

    # # Injecting the HTML for the video background
    # st.markdown(video_html, unsafe_allow_html=True)

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("{main_bg_image_url}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img}");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0, 0, 0, 0);
    }}

    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    tab1, tab2,tab3,tab4 = st.tabs(["Cluster Analysis", "Visualzation","Upload CSV ",'Details :sunglasses:'])
    with tab4:
        st.markdown('''# Fraud Detection Project

## Welcome to the :red[**Fraud Detection Project**] the culminating endeavor of the Capstone Series.
---
## Project Overview

In this project, we address significant challenges such as limited domain knowledge and the handling of imbalanced datasets in the realm of fraud detection. The primary focus lies in the analysis of transactional values rather than column names, coupled with the implementation of various sophisticated machine learning algorithms and techniques to manage unbalanced data.

### Key Algorithms and Techniques:

- Logistic Regression
- Random Forest
- XGBoost
- Neural Networks
- Unbalanced Data Techniques

### Visualization Tools:

- Seaborn
- Matplotlib
- Other relevant libraries

### Special Focus:

- Data Drift and Model Drift in ML and MLOps
- Monitoring and validation tools for ML models and data
- Deepchecks for Data Integrity, Train-Test Validation, and Model Evaluation

Deepchecks Introduction: [Watch Video](https://youtu.be/7ELdizoi6BU)

Finally, the project culminates in the deployment of the model using the **Streamlit API**.

## Determines

The dataset features credit card transactions from September 2013 by European cardholders, spanning two days with **492 frauds** out of **284,807 transactions**. This highly unbalanced dataset poses a unique challenge.

### Feature Information:

- **Time**: Seconds elapsed between each transaction and the first transaction in the dataset.
- **Amount**: Transaction amount; relevant for cost-sensitive learning.
- **Class**: Target variable indicating fraud (1) or non-fraud (0).

## Project Aim

The goal is to accurately predict fraudulent credit card transactions, a task that requires a thorough analysis and understanding of the data.

### Preliminary Steps:

- Analyze frequency distributions of variables
- Investigate variable correlations and multicollinearity
- Examine the distribution of target variable classes
- Address missing values and outliers

### Model Building:

Commence with Logistic Regression, applying Unbalanced Data Techniques to enhance performance. Progress through four different algorithms, evaluating each for effectiveness.

## Tasks

### 1. Exploratory Data Analysis & Data Cleaning

- Import Modules, Load Data & Data Review
- Data Integrity Checks
- Exploratory Data Analysis
- Data Cleaning

### 2. Data Preprocessing

- Train - Test Split
- Train - Test Split Validation Checks
- Scaling

### 3. Model Building

- Implement Logistic Regression, Random Forest Classifier, XGBoost Classifier, and Neural Network
- Evaluate and compare model performances

### 4. Model Deployment

- Save and Export the Best Model
- Save and Export Variables for future use

## Conclusion

Through comprehensive EDA, data visualization, and the training of five models (LR, SVC, RF, XGBoost, and ANN), we have developed a robust solution to identify fraudulent transactions. The project is brought to fruition with the deployment of our model on Streamlit.

---

''')
                    
    with tab3:
        st.title('Credit Card Fraud Detection')
        st.write("")
        st.write("")
        st.subheader('Please upload your CSV file for prediction:')
        st.write("")

        # File uploader
        uploaded_file = st.sidebar.file_uploader("Choose a file")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            data1 = data.copy()
            predictions = model.predict(data)
            data1['Class'] = predictions
            

            data1['Hour'] = data1['Time'].apply(lambda x : np.floor(x/3600))
            edadf = pd.DataFrame(data1.groupby(['Hour','Class'])['Amount'].aggregate(['min','max','count','sum','mean','median','var']).reset_index())
            
            
        ############################################################################
        # To calculate the values for the indicator
            
            for i in predictions[:]:
                if i == 1: 
                    count = count + 1 
            for ii in data['Amount'].values[:]: 
                sum = ii + sum
            for ii in data1[data1['Class']==1]['Amount']:
                sum_frud = ii + sum_frud
                
            
            with st.expander("Data"):
                st.dataframe(data)
            m , mm = st.columns([0.3,0.3])
            

        ########################################################################
        # plot the frud and not frud indcators
        try:
            
            fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=count,
                    title={'text': "Fraud"},
                    domain={'x': [0, 1], 'y': [0, 1]},
                    gauge={'axis': {'range': [0, len(predictions)]}}  # Set the range here
                    ))
            
            fig.update_layout(
                height=200,
                margin=dict(l=10, r=10, t=50, b=10, pad=8),
            )
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            m.plotly_chart(fig)
            fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=len(predictions)-count,
                    title={'text': "Not Fraud"},
                    domain={'x': [0, 1], 'y': [0, 1]},
                    gauge={'axis': {'range': [0, len(predictions)]}}  # Set the range here
                    ))
            fig.update_layout(
                height=200,
                margin=dict(l=10, r=10, t=50, b=10, pad=8),
            )
            st.write("")
            
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            mm.plotly_chart(fig)

        ################################################################
        # calculate the amount
            st.write("")
            st.write("")
            st.write("")    
            st.title('The Amount')
            n , nn = st.columns([0.3,0.3])

            fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=sum_frud,
                    title={'text': "Fraud"},
                    domain={'x': [0, 1], 'y': [0, 1]},
                    gauge={'axis': {'range': [0, sum]}}  # Set the range here
                    ))
            fig.update_layout(
                height=200,
                margin=dict(l=10, r=10, t=50, b=10, pad=8),
            )
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

            nn.plotly_chart(fig)

            fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=sum-sum_frud,
                    title={'text': "Fraud"},
                    domain={'x': [0, 1], 'y': [0, 1]},
                    gauge={'axis': {'range': [0, sum]}}  # Set the range here
                    ))
            fig.update_layout(
                height=200,
                margin=dict(l=10, r=10, t=50, b=10, pad=8),
            )
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            n.plotly_chart(fig)
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            with st.expander("Data Fraud"):
                st.dataframe(data1[data1['Class']==1])
            fig1, fig2, fig3, fig4, fig5, fig6 = plot_data(edadf)
        except NameError:
            pass
    with tab2: 
        st.write("")
        st.write("")
        st.write("")

        try:
            with st.expander("Data"):
                st.dataframe(edadf)
            h,hh = st.columns([0.5,0.5])
            h.plotly_chart(fig1)
            hh.plotly_chart(fig2)
            h.plotly_chart(fig3)
            hh.plotly_chart(fig4)
            h.plotly_chart(fig5)
            hh.plotly_chart(fig6)
        except:pass
    with tab1: 
        k = st.slider('Select the number of clusters (k)', min_value=2, max_value=6)
       
        col1,col2,col3= st.columns([0.5,0.8,0.5])
        with col2:
            col2.submitted11 = st.button("Let's GO")
            if col2.submitted11:
                
                    st.write("")
                    st.write("")
                    st.subheader("Yeah we know what you expected :sunglasses:")
                    st.write("---")                  
                    st.image('vecteezy_lasagna-png-with-ai-generated_26757687.png')

