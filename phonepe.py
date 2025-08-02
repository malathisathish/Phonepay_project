import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 
from sqlalchemy import create_engine, text
import plotly.express as px
import json
import requests
import numpy as np
import pydeck as pdk
from insights_queries import QUERY_MAPPING

# Connecting to postgresql database
engine = create_engine("postgresql://postgres:MALATHI28@localhost:5432/phonepedb")

def execute_query(query):
    """Execute SQL query and return DataFrame"""
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        return df
    except Exception as e:
        st.error(f"Database query failed: {e}")
        return pd.DataFrame()

#page configuration
st.set_page_config(page_title="PhonePe Transaction insight Dashboard | The Beat of Progress",
                   page_icon="📱",
                   layout="wide",
                   initial_sidebar_state="expanded")

# PhonePe Pulse Exact CSS Styling with animations
st.markdown("""
<style>
    /* Import PhonePe fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main background - PhonePe Pulse dark theme */
    .main {
        background: linear-gradient(135deg, #2D1B69 0%, #5B2C87 50%, #8E44AD 100%);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    /* Remove default Streamlit styling */
    .css-1d391kg, .css-1y4p8pa {
        background: transparent;
    }
    
    /* Header styling */
    .phonepe-header {
        background: rgba(45, 27, 105, 0.9);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* PhonePe logo and title styling */
    .phonepe-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .phonepe-subtitle {
        font-size: 1.2rem;
        color: #E8E8E8;
        text-align: center;
        font-weight: 400;
        opacity: 0.9;
    }
    
    /* Navigation menu - PhonePe style */
    .nav-container {
        background: rgba(45, 27, 105, 0.8);
        border-radius: 50px;
        padding: 5px;
        margin: 20px 0;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Card styling - PhonePe design */
    .phonepe-card {
        background: rgba(45, 27, 105, 0.6);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .phonepe-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(45, 27, 105, 0.8), rgba(91, 44, 135, 0.8));
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 30px rgba(0, 212, 255, 0.4);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 5px;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #E8E8E8;
        opacity: 0.8;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(91, 44, 135, 0.2));
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #00D4FF;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(138, 43, 226, 0.4);
        border-left: 4px solid #FF6B6B;
    }
    
    /* Animation keyframes */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    .float-animation {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Button styling - PhonePe theme */
    .stButton > button {
        background: linear-gradient(135deg, #5B2C87, #8E44AD);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #8E44AD, #5B2C87);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(142, 68, 173, 0.4);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: rgba(45, 27, 105, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        color: white;
    }
    
    /* Text styling */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
    }
    
    /* Dataframe styling */
    .dataframe {
        background: rgba(45, 27, 105, 0.6);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Map container */
    .map-container {
        background: rgba(45, 27, 105, 0.4);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* PhonePe accent colors */
    .phonepe-accent {
        color: #00D4FF;
        font-weight: 600;
    }
    
    .phonepe-secondary {
        color: #FF6B6B;
        font-weight: 600;
    }
    
    /* Tech badge styling */
    .tech-badge {
        background: linear-gradient(135deg, #5B2C87, #8E44AD);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        display: inline-block;
        font-weight: 500;
        font-size: 14px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .tech-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(91, 44, 135, 0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(45, 27, 105, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #5B2C87, #8E44AD);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #8E44AD, #5B2C87);
    }
</style>
""", unsafe_allow_html=True)

#Header
st.markdown("""
<div class="phonepe-header">
    <div class="phonepe-title">📱 PhonePe Transaction Insight Dashboard</div>
    <div class="phonepe-subtitle">The Beat of Progress</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2], gap="medium")
with col1:
     st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h2 style="color: #FFD700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">📊 Data Visualization & Exploration</h2>
        <p style="color: #FFFFFF; font-size: 16px; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Explore India's digital payment ecosystem through interactive visualizations and comprehensive analytics.
        </p>
    </div>
""", unsafe_allow_html=True)

with col2:
     st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 20px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h3 style="color: #FFD700; margin-bottom: 15px; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">🚀 Powered By</h3>
        <p style="color: #FFFFFF; font-size: 14px; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        <strong>PostgreSQL</strong> • <strong>Streamlit</strong> • <strong>Plotly</strong> • <strong>PyDeck</strong>
        </p>
    </div>
""", unsafe_allow_html=True)

# Navigation Menu - PhonePe Pulse Style
selected = option_menu(
    menu_title=None,
    options=["Home", "Explore Data", "Insights","Project Analytical Report","About_Developer"],
    icons=["house-fill", "bar-chart-line-fill", "graph-up-arrow","file-earmark-text", "info-circle-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important", 
            "background": "rgba(45, 27, 105, 0.8)",
            "border-radius": "50px",
            "backdrop-filter": "blur(15px)",
            "border": "1px solid rgba(255, 255, 255, 0.1)"
        },
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px", 
            "text-align": "center", 
            "margin": "5px", 
            "padding": "12px 20px",
            "border-radius": "25px", 
            "color": "white", 
            "background": "transparent",
            "transition": "all 0.3s ease"
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, #5B2C87, #8E44AD)", 
            "color": "white", 
            "font-weight": "600",
            "box-shadow": "0 4px 15px rgba(91, 44, 135, 0.4)"
        },
    }
)

# ----------------------------------------------------------------------------------- ENHANCED HOME
def home():
    if selected == "Home":
        # Hero Section with enhanced background
        st.markdown("""
        <div class="phonepe-card" style="text-align: center; padding: 40px; 
             background: linear-gradient(135deg, rgba(45, 27, 105, 0.9) 0%, rgba(91, 44, 135, 0.9) 50%, rgba(142, 68, 173, 0.9) 100%),
                         url('https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80');
             background-blend-mode: overlay; background-size: cover; background-position: center;">
            <h1 style="color: #00D4FF; font-size: 3rem; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);" class="float-animation">
                🇮🇳 India's Digital Payment Revolution
            </h1>
            <p style="color: #E8E8E8; font-size: 1.3rem; margin-bottom: 30px; text-shadow: 1px 1px 2px rgba(0,0,0,0.7);">
                Discover how money moves across a nation of 1.4 billion people
            </p>
        </div>
        """, unsafe_allow_html=True)

        # PhonePe Features Showcase
        st.markdown("""
    <div class="phonepe-card" style="margin: 30px 0; 
                                   background: radial-gradient(circle at center, #6A1B9A 0%, #4A148C 70%); 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.4);">
        <h2 style="color: #FFFFFF; text-align: center; margin-bottom: 30px; 
                   text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">🚀 PhonePe Digital Ecosystem</h2>
    </div>
""", unsafe_allow_html=True)


        # Feature Cards with enhanced styling
        col1, col2, col3 = st.columns(3)
        
        with col1:
           st.markdown("""
    <div class="feature-card" style="text-align: center; padding: 25px; 
                                   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                   border-radius: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
        <div style="font-size: 4rem; margin-bottom: 15px; color: #FFD700;" class="pulse-animation">💸</div>
        <h3 style="color: #FFFFFF; margin-bottom: 10px; font-weight: bold;">Money Transfer</h3>
        <p style="color: #F0F0F0; font-size: 14px; line-height: 1.5;">
        Send money instantly to friends, family, and merchants across India with just a few taps
        </p>
    </div>
""", unsafe_allow_html=True)

        with col2:
            st.markdown("""
    <div class="feature-card" style="text-align: center; padding: 25px; 
                                   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                   border-radius: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
        <div style="font-size: 4rem; margin-bottom: 15px; color: #FFD700;" class="pulse-animation">💡</div>
        <h3 style="color: #FFFFFF; margin-bottom: 10px; font-weight: bold;">Bill Payments</h3>
        <p style="color: #F0F0F0; font-size: 14px; line-height: 1.5;">
        Pay electricity, gas, water, mobile recharge, and DTH bills seamlessly
        </p>
    </div>
""", unsafe_allow_html=True)

        with col3:
            st.markdown("""
    <div class="feature-card" style="text-align: center; padding: 25px; 
                                   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                   border-radius: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
        <div style="font-size: 4rem; margin-bottom: 15px; color: #FFD700;" class="pulse-animation">🏪</div>
        <h3 style="color: #FFFFFF; margin-bottom: 10px; font-weight: bold;">Merchant Payments</h3>
        <p style="color: #F0F0F0; font-size: 14px; line-height: 1.5;">
        Shop online and offline with secure QR code payments at millions of stores
        </p>
    </div>
""", unsafe_allow_html=True)

        # Key Metrics Section with enhanced animations
        try:
            # Get key statistics from database
            total_amount_query = 'SELECT SUM("Transaction_amount") as total_amount FROM agg_trans_table'
            total_count_query = 'SELECT SUM("Transaction_count") as total_count FROM agg_trans_table'
            total_users_query = 'SELECT SUM("RegisteredUsers") as total_users FROM map_user_table'
            
            total_amount_df = execute_query(total_amount_query)
            total_count_df = execute_query(total_count_query)
            total_users_df = execute_query(total_users_query)
            
            if not total_amount_df.empty and not total_count_df.empty and not total_users_df.empty:
                st.markdown("""
    <div class="phonepe-card" style="margin: 30px 0; 
                                   background: radial-gradient(circle at center, #6A1B9A 0%, #4A148C 70%); 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.4);">
        <h2 style="color: #FFFFFF; text-align: center; margin-bottom: 30px; 
                   text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">📊 Live Dashboard Metrics</h2>
    </div>
""", unsafe_allow_html=True)
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.markdown(f"""
                    <div class="metric-card" style="background: linear-gradient(135deg, #FF6B6B, #FF1493);">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;" class="float-animation">💰</div>
                        <div class="metric-value">₹{total_amount_df.iloc[0]['total_amount']:,.0f}</div>
                        <div class="metric-label">Total Transaction Value</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="metric-card" style="background: linear-gradient(135deg, #00D4FF, #0099CC);">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;" class="float-animation">📱</div>
                        <div class="metric-value">{total_count_df.iloc[0]['total_count']:,.0f}</div>
                        <div class="metric-label">Total Transactions</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div class="metric-card" style="background: linear-gradient(135deg, #00FF7F, #32CD32);">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;" class="float-animation">👥</div>
                        <div class="metric-value">{total_users_df.iloc[0]['total_users']:,.0f}</div>
                        <div class="metric-label">Registered Users</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    avg_transaction = total_amount_df.iloc[0]['total_amount'] / total_count_df.iloc[0]['total_count']
                    st.markdown(f"""
                    <div class="metric-card" style="background: linear-gradient(135deg, #FFD700, #FFA500);">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;" class="float-animation">📊</div>
                        <div class="metric-value">₹{avg_transaction:,.0f}</div>
                        <div class="metric-label">Avg Transaction</div>
                    </div>
                    """, unsafe_allow_html=True)
        except:
            st.markdown("""
            <div class="phonepe-card" style="text-align: center;">
                <h3 style="color: #FF6B6B;">🔌 Database Connection Required</h3>
                <p style="color: #E8E8E8;">Please ensure your PostgreSQL database is running to view live metrics.</p>
            </div>
            """, unsafe_allow_html=True)

        # Enhanced Image Gallery with Unsplash
            st.markdown("""
    <div class="phonepe-card" style="margin: 30px 0; 
                                   background: radial-gradient(circle at center, #6A1B9A 0%, #4A148C 70%); 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.4);">
        <h2 style="color: #FFFFFF; text-align: center; margin-bottom: 30px; 
                   text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">📲 Digital Payment Features</h2>
    </div>
""", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
    <div style="text-align: center; padding: 15px;">
        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
              alt="QR Payments" style="width: 120px; height: 120px; border-radius: 15px;
              box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3); object-fit: cover; transition: all 0.3s ease;"
              onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <h4 style="background: linear-gradient(45deg, #0066CC, #00D4FF); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                   background-clip: text; margin-top: 10px; font-weight: bold;">📱 QR Payments</h4>
    </div>
""", unsafe_allow_html=True)
        with col2:
                 st.markdown("""
    <div style="text-align: center; padding: 15px;">
        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
              alt="QR Payments" style="width: 120px; height: 120px; border-radius: 15px;
              box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3); object-fit: cover; transition: all 0.3s ease;"
              onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <h4 style="background: linear-gradient(45deg, #0066CC, #00D4FF); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                   background-clip: text; margin-top: 10px; font-weight: bold;">🛡️ Insurance</h4>
    </div>
""", unsafe_allow_html=True)
        with col3:
             st.markdown("""
    <div style="text-align: center; padding: 15px;">
        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
              alt="QR Payments" style="width: 120px; height: 120px; border-radius: 15px;
              box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3); object-fit: cover; transition: all 0.3s ease;"
              onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <h4 style="background: linear-gradient(45deg, #0066CC, #00D4FF); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                   background-clip: text; margin-top: 10px; font-weight: bold;">📈Investment</h4>
    </div>
""", unsafe_allow_html=True)
        with col4:
              st.markdown("""
    <div style="text-align: center; padding: 15px;">
        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
              alt="QR Payments" style="width: 120px; height: 120px; border-radius: 15px;
              box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3); object-fit: cover; transition: all 0.3s ease;"
              onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <h4 style="background: linear-gradient(45deg, #0066CC, #00D4FF); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                   background-clip: text; margin-top: 10px; font-weight: bold;">🏆 Digital Gold</h4>
    </div>
""", unsafe_allow_html=True)

        # Enhanced footer section
        st.markdown("""
        <div class="phonepe-card" style="text-align: center; margin-top: 40px; 
             background: linear-gradient(135deg, #2D1B69, #8E44AD); border: 2px solid rgba(0, 212, 255, 0.3);">
            <h3 style="color: #00D4FF; margin-bottom: 15px;">🚀 Powered by Advanced Data Science</h3>
            <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-bottom: 20px;">
                <div class="tech-badge">🐍 Python</div>
                <div class="tech-badge">🐘 PostgreSQL</div>
                <div class="tech-badge">🚀 Streamlit</div>
                <div class="tech-badge">📊 Plotly</div>
                <div class="tech-badge">🗺️ PyDeck</div>
                <div class="tech-badge">🔍 Pandas</div>
            </div>
            <p style="color: #E8E8E8; margin-top: 15px; font-style: italic; font-size: 16px;">
                "Transforming raw transaction data into actionable insights for India's digital future"
            </p>
        </div>
        """, unsafe_allow_html=True)

home()

#-- -------------------------------------------------------------------------- ENHANCED EXPLORE DATA WITH 2D HEXAGON MAPS
def explore_data():
    if selected == "Explore Data":
        st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h2 style="color: #FFD700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">📊 Explore Data</h2>
        <p style="color: #FFFFFF; font-size: 16px; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Dive deep into transaction patterns and user behavior across India
        </p>
    </div>
""", unsafe_allow_html=True)
        
        tabm, tabc = st.tabs(["🗺️ **Analysis over Map**", "📈 **Analysis over Chart**"])

        with tabm:
            tab1, tab2 = st.tabs(["💳 **TRANSACTION**", "👥 **USER**"])
            
            # TRANSACTION TAB
            with tab1:
                st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h2 style="color: #FFD700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">💳 Transaction Analysis</h2>
        <p style="color: #FFFFFF; font-size: 16px; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Select parameters to analyze transaction patterns
        </p>
    </div>
""", unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    year = st.selectbox('**📅 Select Year**', ('2018', '2019', '2020', '2021', '2022', '2023'), key='year')
                with col2:
                    quarter = st.selectbox('**📊 Select Quarter**', ('1', '2', '3', '4'), key='quarter')
                with col3:
                    trans_type = st.selectbox('**💰 Select Transaction type**',
                                            ('Recharge & bill payments', 'Peer-to-peer payments',
                                             'Merchant payments', 'Financial Services', 'Others'), key='type')

                # Query with user's table structure
                query_trans_map = f"""
                SELECT "State", "Transaction_amount" 
                FROM agg_trans_table 
                WHERE "Year" = '{year}' AND "Quarter" = '{quarter}' AND "Transaction_type" = '{trans_type}'
                """
                df = execute_query(query_trans_map)
                
                query_trans_anly = f"""
                SELECT "State", "Transaction_count", "Transaction_amount" 
                FROM agg_trans_table 
                WHERE "Year" = '{year}' AND "Quarter" = '{quarter}' AND "Transaction_type" = '{trans_type}'
                """
                df_anly = execute_query(query_trans_anly)

                if not df.empty and not df_anly.empty:
                    # GEO VISUALISATION
                    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
                    response = requests.get(url)
                    data1 = json.loads(response.content)
                    state_name_geojson = [feature["properties"]["ST_NM"] for feature in data1["features"]]
                    state_name_geojson.sort()
                    
                    df_all_states = pd.DataFrame({"State": state_name_geojson})
                    df_tra = pd.merge(df_all_states, df, on="State", how="left").fillna(0)

                    # Geo plot with PhonePe colors
                    fig_tra = px.choropleth(
                        df_tra,
                        geojson=url,
                        featureidkey="properties.ST_NM",
                        locations="State",
                        color="Transaction_amount",
                        color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']],
                        range_color=(df_tra["Transaction_amount"].min(), df_tra["Transaction_amount"].max()),
                        title=f"Transaction Analysis: {trans_type} | {year} Q{quarter}",
                        hover_name="State",
                        labels={"Transaction_amount": "Transaction Amount (₹)"}
                    )
                    fig_tra.update_geos(fitbounds="locations", visible=False)
                    fig_tra.update_layout(
                        title_font=dict(size=24, color='#00D4FF'),
                        height=600,
                        font=dict(color='white'),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                    )
                    st.plotly_chart(fig_tra, use_container_width=True)

                    # Pie chart
                    fig_pie = px.pie(
                        df_anly,
                        values='Transaction_count',
                        names='State',
                        title=f'Transaction Distribution: {trans_type}',
                        color_discrete_sequence=px.colors.sequential.Plasma
                    )
                    fig_pie.update_layout(
                        title_font=dict(size=20, color='#00D4FF'),
                        font=dict(color='white'),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                    )
                    st.plotly_chart(fig_pie, use_container_width=True)
                    
                    st.markdown("""
                    <div class="phonepe-card">
                        <h3 style="color: #1f1f1f; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">
                            📊Transaction Analysis Summary
                        </h3>
                    </div>
                    """, unsafe_allow_html=True)
                    st.dataframe(df_anly, use_container_width=True)
                                    
                else:
                    st.warning("No data found for the selected criteria.")

            # USER TAB
            with tab2:
                st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h2 style="color: #FFD700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">👥 User Analysis</h2>
        <p style="color: #FFFFFF; font-size: 16px; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Analyze user patterns and device preferences
        </p>
    </div>
""", unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    yr = st.selectbox('**📅 Select Year**', ('2018', '2019', '2020', '2021', '2022', '2023'), key='yr')
                with col2:
                    qtr = st.selectbox('**📊 Select Quarter**', ('1', '2', '3', '4'), key='qtr')
                with col3:
                    brand = st.selectbox('**📱 Select Brand**',
                                       ('Samsung', 'Xiaomi', 'Vivo', 'Oppo', 'OnePlus', 'Realme',
                                        'Apple', 'Motorola', 'Lenovo', 'Huawei', 'Others', 'Tecno'), key='brand')

                query_user = f"""
                SELECT "State", SUM("Transaction_count") as user_count, "Device_Brand" 
                FROM agg_user_table 
                WHERE "Year" = '{yr}' AND "Quarter" = '{qtr}' AND "Device_Brand" = '{brand}' 
                GROUP BY "State", "Device_Brand"
                """
                df_user = execute_query(query_user)

                if not df_user.empty:
                    # User distribution visualization
                    fig_user = px.bar(
                        df_user,
                        x='State',
                        y='user_count',
                        color='user_count',
                        color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']],
                        title=f'User Analysis: {brand} | {yr} Q{qtr}',
                        height=600
                    )
                    fig_user.update_layout(
                        title_font=dict(size=20, color='#00D4FF'),
                        font=dict(color='white'),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        xaxis_tickangle=-45
                    )
                    st.plotly_chart(fig_user, use_container_width=True)

                    st.markdown("""
                    <div class="phonepe-card">
                        <h3 style="color: #1f1f1f; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">
                            📊User Analysis Summary
                        </h3>
                    </div>
                    """, unsafe_allow_html=True)
                    st.dataframe(df_anly, use_container_width=True)
                else:
                    st.warning("No data found for the selected criteria.")

        # ANALYSIS OVER CHART
        with tabc:
            st.markdown("**📈 Top Charts**")
            
            chart_type = st.selectbox('**Select Analysis Type**', ('Transactions', 'Users'))
            
            if chart_type == 'Transactions':
                Years = st.slider("**Year**", min_value=2018, max_value=2023)
                Quarter = st.slider("Quarter", min_value=1, max_value=4)
                
                tab1, tab2, tab3 = st.tabs(["State", "District", "Pincode"])
                
                with tab1:
                    st.markdown("**🏆 Top States**")
                    query = f"""
                    SELECT "State", SUM("Transaction_count") as Total_Transactions_Count, 
                           SUM("Transaction_amount") as Total_Transaction_Amount 
                    FROM agg_trans_table 
                    WHERE "Year" = '{Years}' AND "Quarter" = '{Quarter}' 
                    GROUP BY "State" 
                    ORDER BY Total_Transaction_Amount DESC 
                    LIMIT 10
                    """
                    df = execute_query(query)
                    
                    if not df.empty:
                        fig = px.pie(
                            df,
                            values='total_transaction_amount',
                            names='State',
                            title='Top 10 States by Transaction Amount',
                            color_discrete_sequence=px.colors.sequential.Plasma,
                            hover_data=['total_transactions_count']
                        )
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(
                            title_font=dict(size=20, color='#00D4FF'),
                            font=dict(color='white'),
                            paper_bgcolor='rgba(0,0,0,0)'
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df, use_container_width=True)

                with tab2:
                    st.markdown("**🏆 Top Districts**")
                    query = f"""
                    SELECT "District", SUM("Transaction_count") as Total_Count, 
                           SUM("Transaction_amount") as Total_Amount 
                    FROM map_trans_table 
                    WHERE "Year" = '{Years}' AND "Quarter" = '{Quarter}' 
                    GROUP BY "District" 
                    ORDER BY Total_Amount DESC 
                    LIMIT 10
                    """
                    df = execute_query(query)
                    
                    if not df.empty:
                        fig = px.bar(
                            df,
                            x='District',
                            y='total_amount',
                            color='total_amount',
                            title='Top 10 Districts by Transaction Amount',
                            color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']]
                        )
                        fig.update_layout(
                            title_font=dict(size=20, color='#00D4FF'),
                            font=dict(color='white'),
                            paper_bgcolor='rgba(0,0,0,0)',
                            xaxis_tickangle=-45
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df, use_container_width=True)
                        
                with tab3:
                    st.markdown("**🏆Top Pincodes**")
                    query = f"""
                    SELECT "Pincodes", SUM("Transaction_count") as Total_Count, 
                           SUM("Transaction_amount") as Total_Amount 
                    FROM top_trans_table 
                    WHERE "Year" = '{Years}' AND "Quarter" = '{Quarter}' 
                    GROUP BY "Pincodes" 
                    ORDER BY Total_Amount DESC 
                    LIMIT 10
                    """
                    df = execute_query(query)

                    if not df.empty:
                        fig=px.bar(
                            df,
                            x='Pincodes',
                            y='total_count',
                            color='total_amount',
                            title='Pincodes By Transaction Amount',
                            color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']]
                            )
                        
                        fig.update_layout(
                            title_font=dict(size=20, color='#00D4FF'),
                            font=dict(color='white'),
                            paper_bgcolor='rgba(0,0,0,0)',
                            xaxis_tickangle=-45
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df, use_container_width=True)
            
         
            elif chart_type == 'Users':
                Years = st.slider("**Year**", min_value=2018, max_value=2023, key='user_year')
                Quarter = st.slider("Quarter", min_value=1, max_value=4, key='user_quarter')
                
                tab1, tab2, tab3 = st.tabs(["State", "District", "Pincode"])
                
                with tab1:
                    st.markdown("**🏆 Top States by User Count**")
                    query = f"""
                    SELECT "State", SUM("RegisteredUsers") as Total_Users, 
                           SUM("AppOpens") as Total_App_Opens 
                    FROM map_user_table 
                    WHERE "Year" = '{Years}' AND "Quarter" = '{Quarter}' 
                    GROUP BY "State" 
                    ORDER BY Total_Users DESC 
                    LIMIT 10
                    """
                    df = execute_query(query)
                    
                    if not df.empty:
                        fig = px.pie(
                            df,
                            values='total_users',
                            names='State',
                            title='Top 10 States by User Count',
                            color_discrete_sequence=px.colors.sequential.Viridis,
                            hover_data=['total_app_opens']
                        )
                        fig.update_traces(textposition='inside', textinfo='percent+label')
                        fig.update_layout(
                            title_font=dict(size=20, color='#00D4FF'),
                            font=dict(color='white'),
                            paper_bgcolor='rgba(0,0,0,0)'
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df, use_container_width=True)

                with tab2:
                    st.markdown("**🏆 Top Districts by User Count**")
                    query = f"""
                    SELECT "District", SUM("RegisteredUsers") as Total_Users, 
                           SUM("AppOpens") as Total_App_Opens 
                    FROM map_user_table 
                    WHERE "Year" = '{Years}' AND "Quarter" = '{Quarter}' 
                    GROUP BY "District" 
                    ORDER BY Total_Users DESC 
                    LIMIT 10
                    """
                    df = execute_query(query)
                    
                    if not df.empty:
                        fig = px.bar(
                            df,
                            x='District',
                            y='total_users',
                            color='total_app_opens',
                            title='Top 10 Districts by User Count',
                            color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']],
                            labels={'total_users': 'Total Users', 'total_app_opens': 'App Opens'}
                        )
                        fig.update_layout(
                            title_font=dict(size=20, color='#00D4FF'),
                            font=dict(color='white'),
                            paper_bgcolor='rgba(0,0,0,0)',
                            xaxis_tickangle=-45
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df, use_container_width=True)
                        
                with tab3:
                    st.markdown("**🏆 Top Pincodes by User Count**")
                    query = f"""
                    SELECT "Pincodes", SUM("RegisteredUsers") as Total_Users 
                    FROM top_user_table 
                    WHERE "Year" = '{Years}' AND "Quarter" = '{Quarter}' 
                    GROUP BY "Pincodes" 
                    ORDER BY Total_Users DESC 
                    LIMIT 10
                    """
                    df = execute_query(query)

                    if not df.empty:
                        fig = px.bar(
                            df,
                            x='Pincodes',
                            y='total_users',
                            color='total_users',
                            title='Top 10 Pincodes by User Count',
                            color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']],
                            labels={'total_users': 'Total Users'}
                        )
                        
                        fig.update_layout(
                            title_font=dict(size=20, color='#00D4FF'),
                            font=dict(color='white'),
                            paper_bgcolor='rgba(0,0,0,0)',
                            xaxis_tickangle=-45
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df, use_container_width=True)
                    else:
                        st.warning("No user data found for the selected criteria.")

explore_data()
# ----------------------------------------------------------------------------------- INSIGHTS
def insights():
    if selected == "Insights":
        st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h2 style="color: #FFD700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">🔍 Advanced Insights</h2>
        <p style="color: #FFFFFF; font-size: 16px; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Deep dive analytics with your predefined queries
        </p>
    </div>
""", unsafe_allow_html=True)
        
        # User's predefined queries organized by category
        insight_category = st.selectbox(
            "**Select Insight Category**",
            list(QUERY_MAPPING.keys())
        )
        
        if insight_category in QUERY_MAPPING:
            st.markdown(f"### {insight_category}")
            
            # Get queries for selected category
            category_queries = QUERY_MAPPING[insight_category]
            
            # Create tabs for each query in the category
            query_names = list(category_queries.keys())
            if len(query_names) > 1:
                tabs = st.tabs(query_names)
                
                for i, (query_name, query_func) in enumerate(category_queries.items()):
                    with tabs[i]:
                        st.markdown(f"#### {query_name}")
                        
                        try:
                            df = query_func()
                            
                            if not df.empty:
                                # Create appropriate visualization based on data
                                if len(df.columns) >= 2:
                                    numeric_cols = df.select_dtypes(include=[np.number]).columns
                                    
                                    if len(numeric_cols) >= 1:
                                        # Create visualization
                                        if 'State' in df.columns and len(numeric_cols) >= 1:
                                            # Bar chart for state-wise data
                                            fig = px.bar(
                                                df.head(15),  # Limit to top 15 for readability
                                                x='State',
                                                y=numeric_cols[0],
                                                title=f'{query_name}',
                                                color=numeric_cols[0],
                                                color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']]
                                            )
                                        elif len(numeric_cols) >= 2:
                                            # Scatter plot for two numeric columns
                                            fig = px.scatter(
                                                df.head(20),
                                                x=numeric_cols[0],
                                                y=numeric_cols[1],
                                                title=f'{query_name}',
                                                color=numeric_cols[0] if len(numeric_cols) > 0 else None,
                                                color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']]
                                            )
                                        else:
                                            # Line chart for time series data
                                            fig = px.line(
                                                df.head(20),
                                                y=numeric_cols[0],
                                                title=f'{query_name}',
                                                markers=True
                                            )
                                        
                                        # Update layout with PhonePe theme
                                        fig.update_layout(
                                            title_font=dict(size=20, color='#00D4FF'),
                                            font=dict(color='white'),
                                            paper_bgcolor='rgba(0,0,0,0)',
                                            plot_bgcolor='rgba(0,0,0,0)',
                                            xaxis_tickangle=-45,
                                            height=500
                                        )
                                        st.plotly_chart(fig, use_container_width=True)
                                
                                # Display data table
                                st.markdown(f"""
                                <div class="phonepe-card">
                                    <h3 style="color: #00D4FF; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">
                                        📊 {query_name} - Data Summary
                                    </h3>
                                </div>
                                """, unsafe_allow_html=True)
                                st.dataframe(df, use_container_width=True) 
                                                                
                            else:
                                st.warning(f"No data available for {query_name}")
                                
                        except Exception as e:
                            st.error(f"Error executing query for {query_name}: {str(e)}")
            else:
                # Single query in category
                query_name, query_func = list(category_queries.items())[0]
                st.markdown(f"#### {query_name}")
                
                try:
                    df = query_func()
                    
                    if not df.empty:
                        # Create visualization and display data
                        numeric_cols = df.select_dtypes(include=[np.number]).columns
                        
                        if len(numeric_cols) >= 1:
                            fig = px.bar(
                                df.head(15),
                                x=df.columns[0],
                                y=numeric_cols[0],
                                title=f'{query_name}',
                                color=numeric_cols[0],
                                color_continuous_scale=[[0, '#2D1B69'], [0.5, '#5B2C87'], [1, '#00D4FF']]
                            )
                            fig.update_layout(
                                title_font=dict(size=20, color='#00D4FF'),
                                font=dict(color='white'),
                                paper_bgcolor='rgba(0,0,0,0)',
                                xaxis_tickangle=-45,
                                height=500
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        
                        st.markdown('<div class="phonepe-card">', unsafe_allow_html=True)
                        st.subheader(f'📊 {query_name} - Data Summary')
                        st.dataframe(df, use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    else:
                        st.warning(f"No data available for {query_name}")
                        
                except Exception as e:
                    st.error(f"Error executing query for {query_name}: {str(e)}")

insights()

# ----------------------------------------------------------------------------------- PROJECT ANALYTICAL REPORT
def Project_Analytical_Report():
    if selected == "Project Analytical Report":
        st.markdown("""
    <div class="phonepe-card" style="background-color: #4A148C; 
                                   padding: 25px; 
                                   border-radius: 15px;
                                   box-shadow: 0 8px 25px rgba(74, 20, 140, 0.3);">
        <h2 style="color: #FFD700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">📋 Project Analytical Report</h2>
        <p style="color: #FFFFFF; font-size: 16px; line-height: 1.6; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        Comprehensive analysis and insights from PhonePe transaction dat
        </p>
    </div>
""", unsafe_allow_html=True)
        st.markdown(" 🧠 **Project Name:** PhonePe Transaction Insight Dashboard**")
        st.markdown("""
        **Author:** Malathi.y 
        
        **Technologies Used:** Python, PostgreSQL, Streamlit, Plotly, pandas, PyDeck  
        
        **Data Source:** [PhonePe Pulse GitHub](https://github.com/PhonePe/pulse)
        """)
        st.markdown("---")
        st.markdown("🔍 **Problem Statement**")
        st.write("""
        With the increasing reliance on digital payment systems like PhonePe, 
        understanding the dynamics of transactions, user engagement, 
        and insurance-related data is crucial for improving services and targeting users effectively. 
        This project aims to analyze and visualize aggregated values of payment categories,
        create maps for total values at state and district levels, and identify top-performing states, districts, and pin codes.

        This project aims to visualize, analyze, and identify the underlying gaps and provide actionable insights to help PhonePe optimize outreach and resource allocation.
        """)

        st.markdown("---")
        st.markdown("🗃️ **Data Overview – 10 Structured Tables Used**")
        st.write("""
        1. **agg_trans_table** – Aggregated transaction metrics by state, year, and quarter  
        2. **agg_user_table** – Aggregated user device brand data with count and market share  
        3. **agg_ins_table** – Insurance subscription volume and value at state level  
        4. **map_trans_table** – District-wise mapped transaction values  
        5. **map_user_table** – District-wise registered users and app opens  
        6. **map_ins_table** – Interactive insurance data at state level  
        7. **map_ins1_table** – Granular hover-mapped insurance data by state  
        8. **top_trans_table** – Top performing districts in transaction amount/count  
        9. **top_user_table** – Top pincodes by user registrations  
        10. **top_ins_table** – Top pincodes by insurance transaction values
        """)

        st.markdown("---")
        st.markdown("🔎 **Exploratory Data Analysis (EDA)**")
        st.write("""
        - ✅ Maharashtra, Karnataka, and Tamil Nadu consistently lead in transaction volume
        - ✅ Xiaomi and Samsung dominate as preferred brands across India
        - ✅ Urban areas have the highest insurance and transaction activity
        - ✅ Northeast states and rural districts show underperformance in user adoption
        - ✅ More app opens correlate with higher registered users and transactions
        - ✅ Insurance transactions are concentrated in metros like Delhi, Mumbai, and Bangalore
        """)

        st.markdown("---")
        st.markdown("⚠️ **Identified Issues / Gaps**")
        st.write("""
        1. **Underutilized Regions:** Northeast and rural states have low transaction activity  
        2. **Brand Dependency:** Heavily reliant on Xiaomi/Samsung – less data from iPhone, Vivo, etc.  
        3. **Insurance Awareness:** Many districts show zero or very low insurance-related activity  
        4. **Pincode Skewness:** A small number of pincodes dominate user base and insurance use  
        5. **Engagement Drop:** Certain districts show high registration but poor app engagement
        """)

        st.markdown("---")
        st.markdown("💡 **Strategic Recommendations**")
        st.write("""
        - 🚀 **Launch awareness campaigns** in underperforming states for both PhonePe usage and insurance services
        - 📍 **Incentivize app engagement** in districts with high registered users but low app opens
        - 📈 **Push campaigns on less dominant brands** to increase data variety and user diversity
        - 🧠 **Use predictive analytics** to identify regions with high growth potential using current data
        - 🔁 **Enhance UI/UX** based on engagement metrics from high-performing districts
        """)

        st.markdown("---")
        st.markdown("🎯 **Project Outcome**")
        st.write("""
        The dashboard provides actionable insights through interactive maps and plots on:
        - Enhanced 2D hexagon transaction visualizations by region and year
        - User behavior and device usage with interactive scatter overlays
        - Insurance trend analysis with real-time tooltips
        - Pincode and district-wise heatmaps with PyDeck integration

        It helps stakeholders make data-backed decisions to improve outreach, customer experience, and market penetration.
        """)

        st.markdown("---")
        st.markdown("🙏 **Thank You!**")
        st.markdown("This project was developed as part of a data science journey to master end-to-end dashboard development using real-world digital payments data.")
        st.markdown("Made with 💜 by Malathi.y")

Project_Analytical_Report()

#--------------------------------------------------------------About_Developer
def About_Developer():
    if selected == "About_Developer":  # Fixed: Added quotes around the string
        st.markdown("🧑‍💻 About the Developer")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image("malathi.png", width=180, caption="Malathi Y")

        with col2:
            st.markdown("""
    👋 Hello! I'm **Malathi Y**

    I'm a former **Staff Nurse** from India (TamilNadu), now actively transitioning into the world of **Data Science**. My journey from healthcare to analytics is driven by my curiosity, love for problem-solving, and a deep interest in how data can transform decision-making.

    ---

    👩‍⚕️ My Past Profession:
    - 🏥 Former **Registered Staff Nurse**
    - 👩‍💼 Experienced in clinical decision-making and frontline hospital work
    - 💡 Fascinated by the way data is used to drive policies and performance in healthcare & fintech

    ---

    📚 My Present Mission:
    - 🔄 Career Shift to **Data Science / Analytics**
    - 🎯 Currently enrolled at **GUVI** to study Datascience course 
    - 🧠 Learning tools like Pandas, PostgreSQL, Streamlit, Seaborn, and Plotly

    ---

    📊 About the Project: PhonePe Transaction Insight Dashboard

    This dashboard is a real-world analytics project analyzing India's digital payment behavior using **PhonePe Pulse** data.

    🧰 Project Tools:
    - 💻 Python (Pandas, Numpy, Plotly, Seaborn, Pydeck)
    - 📊 PostgreSQL + SQLAlchemy for data querying
    - 🌐 Streamlit for UI
    - 🗺️ 2D Map Visualizations using GeoJSON + Pydeck

    📦 Data Sources:
    - 10 tables from **PhonePe Pulse GitHub dataset**
      - User data
      - Transactions
      - Insurance
      - Device brand info
      - Location-based analysis

    ---

    🌟 What I Built:
    - ✅ Complete India-level dashboard interface
    - 📍 Interactive state-wise 2D map visualizations
    - 🔎 Deep analytical insights using optimized SQL queries
    - 📈 Project Analytical Reports (EDA + Business Problems + Solutions)
    - 🎨 A violet-themed responsive dashboard inspired by PhonePe

    ---

    🛠️ My Skills So Far:
    - 🐍 Python, SQL, Pandas, NumPy, Streamlit
    - 🧠 EDA & Data Cleaning
    - 📊 Data Visualization (Plotly, Pydeck)
    - 🧱 Database Management using PostgreSQL
    - 💼 Business Insight Reporting

    ---
    
    🎯 My Future Goals:
    - 💼 Become a full-time **Data Analyst / Data Scientist**
    - 💡 Apply data insights in healthcare, finance & real-time dashboards
    - 📚 Keep learning tools like Power BI, Scikit-learn, and Cloud Analytics

    ---

    > _"From saving lives in the ICU to analyzing lives through data, I'm on a mission to make insights count."_ 🙏

    """)


About_Developer()
#------------------------------------------------------------------------footer
#Footer
st.markdown("""
    <hr style="border: 1px solid #ccc;" />
    <div style="text-align: center; color: grey;">
        📱 Phonepe Transaction Insight Dashboard Created With ❤️ By Using Python,Postgresql,Streamlit 
    </div

    """, unsafe_allow_html=True)
