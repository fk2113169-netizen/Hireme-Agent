import streamlit as st

def inject_custom_css():
    """Injects fonts, Tailwind CDN, and custom overrides for Streamlit elements to match the light theme design."""
    # Inject CDN scripts and style overrides
    st.markdown(
        """
        <!-- Load Tailwind CSS and Web Fonts -->
        <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
        
        <script>
            tailwind.config = {
              theme: {
                extend: {
                  colors: {
                    primary: "#3525cd",
                    "primary-container": "#4f46e5",
                    "surface-white": "#FFFFFF",
                    "surface-soft": "#F1F5F9",
                    "background": "#f7f9fb",
                    "slate-900": "#0F172A",
                    "slate-600": "#475569",
                  }
                }
              }
            }
        </script>
        
        <style>
        /* Main Streamlit Overrides */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            font-family: 'Inter', sans-serif !important;
            background-color: #f7f9fb !important;
            color: #191c1e !important;
        }

        /* Sidebar override */
        [data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1px solid #e2e8f0;
        }

        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Card Container */
        .glass-card, [data-testid="stForm"] {
            background: #ffffff !important;
            border: 1px solid rgba(226, 232, 240, 0.8) !important;
            border-radius: 24px !important;
            padding: 32px !important;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
            margin-bottom: 24px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #3525cd !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            padding: 12px 28px !important;
            font-size: 1rem !important;
            box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3) !important;
            transition: all 0.2s ease-in-out !important;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #4f46e5 !important;
            transform: scale(1.01) !important;
            box-shadow: 0 20px 25px -5px rgba(79, 70, 229, 0.4) !important;
        }
        
        /* Secondary Action Buttons */
        .secondary-btn>button {
            background-color: transparent !important;
            color: #0F172A !important;
            border: 1px solid #0F172A !important;
            box-shadow: none !important;
        }
        .secondary-btn>button:hover {
            background-color: #f8fafc !important;
            color: #0F172A !important;
        }

        /* Slider and Inputs styling */
        input, select, textarea, [data-baseweb="input"] {
            background-color: #F1F5F9 !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 12px !important;
            color: #0F172A !important;
        }
        
        /* Custom file uploader styling */
        [data-testid="stFileUploader"] {
            background-color: #f8fafc;
            border: 2px dashed #cbd5e1;
            border-radius: 16px;
            padding: 16px;
            text-align: center;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: #4f46e5;
        }
        
        /* Badge classes */
        .badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        .badge-purple {
            background-color: #e0e7ff;
            color: #4f46e5;
        }
        .badge-blue {
            background-color: #e0f2fe;
            color: #0284c7;
        }
        .badge-green {
            background-color: #d1fae5;
            color: #059669;
        }
        
        /* Score circle */
        .score-circle {
            font-size: 2.4rem;
            font-weight: 800;
            color: #3525cd;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
