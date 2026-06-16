import streamlit as st

def inject_custom_css():
    """Injects high-contrast light theme overrides to ensure readability and clear styling."""
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
        /* Force light background on all app viewports */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stCanvas"] {
            font-family: 'Inter', sans-serif !important;
            background-color: #f8fafc !important; /* Soft white/light slate */
            background-image: none !important;
            color: #0f172a !important;
        }

        /* Sidebar override to light theme */
        [data-testid="stSidebar"], [data-testid="stSidebar"] * {
            background-color: #ffffff !important;
            border-right: 1px solid #e2e8f0;
            color: #0f172a !important;
        }

        /* Hide default Streamlit headers & footers */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* FORCE HIGH CONTRAST ON ALL TEXT ELEMENTS (Avoid theme bleeding) */
        h1, h2, h3, h4, h5, h6, 
        p, span, label, li, a, div, 
        .stText, [data-testid="stMarkdownContainer"] p, [data-testid="stWidgetLabel"] p {
            color: #0f172a !important; 
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Specific header colors */
        .main-title {
            color: #1e1b4b !important; /* Deep navy */
            font-weight: 800 !important;
        }
        
        .subtitle {
            color: #3b82f6 !important; /* Professional blue */
            font-weight: 500 !important;
        }

        /* Solid White Cards (No opacity overlays to prevent background bleeding) */
        .glass-card, [data-testid="stForm"], [data-testid="stVerticalBlockBorder"] {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 16px !important;
            padding: 32px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
            margin-bottom: 24px !important;
        }

        /* Job Cards with defined background */
        .job-card {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 12px !important;
            padding: 20px !important;
            margin-bottom: 18px !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02) !important;
            transition: all 0.2s ease-in-out !important;
        }
        .job-card:hover {
            border-color: #3b82f6 !important;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.1) !important;
        }

        /* Form Controls Overrides (Inputs, Select boxes, Textareas) */
        input, select, textarea, [data-baseweb="input"], [data-baseweb="select"] {
            background-color: #ffffff !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 8px !important;
            color: #0f172a !important;
        }
        input::placeholder {
            color: #94a3b8 !important;
        }
        
        /* File Uploader override */
        [data-testid="stFileUploader"] {
            background-color: #ffffff !important;
            border: 2px dashed #3b82f6 !important;
            border-radius: 12px !important;
            padding: 24px !important;
        }
        [data-testid="stFileUploader"] * {
            color: #0f172a !important;
        }
        
        /* Primary Action Buttons styling */
        .stButton>button {
            background-color: #3525cd !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            padding: 10px 24px !important;
            font-size: 0.95rem !important;
            box-shadow: 0 4px 6px -1px rgba(53, 37, 205, 0.2) !important;
            transition: all 0.2s ease-in-out !important;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #4f46e5 !important;
            box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3) !important;
        }

        /* Badges styling */
        .badge {
            display: inline-block !important;
            padding: 4px 12px !important;
            border-radius: 9999px !important;
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            margin-right: 8px !important;
            margin-bottom: 8px !important;
        }
        .badge-purple {
            background-color: #e0e7ff !important;
            color: #4f46e5 !important;
            border: 1px solid #c7d2fe !important;
        }
        .badge-blue {
            background-color: #e0f2fe !important;
            color: #0369a1 !important;
            border: 1px solid #bae6fd !important;
        }
        .badge-green {
            background-color: #d1fae5 !important;
            color: #047857 !important;
            border: 1px solid #a7f3d0 !important;
        }

        /* Match Score display */
        .score-circle {
            font-size: 2.4rem !important;
            font-weight: 800 !important;
            color: #3525cd !important;
            text-align: right !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
