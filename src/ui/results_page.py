import streamlit as st
from src.ui.components import inject_custom_css

def results_page():
    # Inject Custom Light Styling and Tailwind
    inject_custom_css()
    
    # Render HTML Navbar
    st.markdown(
        """
        <header class="flex justify-between items-center w-full px-8 max-w-7xl mx-auto bg-white shadow-sm h-16 rounded-xl mt-2">
          <div class="flex items-center gap-4">
            <div class="text-xl font-extrabold text-primary flex items-center gap-2">
              <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">work</span>
              HireMe Agent
            </div>
            <nav class="hidden md:flex gap-6 items-center ml-8">
              <a class="text-sm text-primary font-semibold border-b-2 border-primary py-2" href="#">Features</a>
              <a class="text-sm text-slate-600 hover:text-primary py-2" href="#">How it Works</a>
              <a class="text-sm text-slate-600 hover:text-primary py-2" href="#">Pricing</a>
            </nav>
          </div>
          <div>
            <button class="text-sm font-semibold px-6 py-2 rounded-lg bg-primary text-white hover:bg-primary-container">
              Get Started
            </button>
          </div>
        </header>
        """,
        unsafe_allow_html=True
    )
    
    # Page layout container
    st.markdown('<div class="max-w-4xl mx-auto px-8 mt-8">', unsafe_allow_html=True)
    
    # Back to upload button
    if st.button("⬅️ Upload New CV"):
        st.session_state.stage = "upload"
        st.session_state.results = []
        st.session_state.cv_data = None
        st.rerun()
        
    st.markdown(
        """
        <div class="text-center mb-8">
          <h2 class="text-3xl font-extrabold text-slate-900">Recommendation Results</h2>
          <p class="text-sm text-slate-600">AI-matched opportunities curated specifically for your profile.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    cv_data = st.session_state.cv_data
    results = st.session_state.results
    
    # Display CV Details Card
    if cv_data:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader(f"👤 Profile: {cv_data.get('name', 'Candidate')}")
        if cv_data.get('email'):
            st.markdown(f"📧 **Email:** {cv_data.get('email')}")
            
        st.write("---")
        st.markdown(f"**Professional Summary:**  \n*{cv_data.get('summary', 'No summary available.')}*")
        
        st.write("---")
        st.markdown("**Skills:**")
        skills_html = ""
        for skill in cv_data.get('skills', []):
            skills_html += f'<span class="badge badge-purple">{skill}</span>'
        st.markdown(skills_html or "*No skills parsed*", unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("**Suggested Target Roles:**")
        roles_html = ""
        for role in cv_data.get('target_roles', []):
            roles_html += f'<span class="badge badge-blue">{role}</span>'
        st.markdown(roles_html or "*No target roles identified*", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Display Recommendations
    st.markdown("### 🔍 Evaluated Job Openings")
    if not results:
        st.info("No matching jobs found. Try adjusting target location or key criteria in your CV.")
    else:
        for job in results:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            col_details, col_score = st.columns([4, 1])
            
            with col_details:
                st.markdown(f"#### [{job['title']}]({job['url']})")
                st.write(f"🏢 **{job['company']}** — 📍 *{job['location']}*")
                
            with col_score:
                score = job.get('match_score', 50)
                st.markdown(f'<div class="score-circle">{score}%</div>', unsafe_allow_html=True)
                st.markdown('<div style="text-align: right; color:#3525cd; font-weight:600; font-size:0.9rem;">Match</div>', unsafe_allow_html=True)
                
            st.write("---")
            st.markdown(f"**🤖 AI Match Explanation:**  \n{job.get('reasoning', '')}")
            st.write("---")
            st.markdown(f"**Job Description Snippet:**  \n*{job['description']}*")
            
            # Application Link
            st.markdown(
                f'<a href="{job["url"]}" target="_blank" style="text-decoration:none;"><button style="background-color: #3525cd !important; color: white; border: none; border-radius: 12px; font-weight: 700; padding: 12px 24px; width: 100%; box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3); cursor: pointer; transition: all 0.2s ease; margin-top: 15px;">Apply to Job Post 🚀</button></a>',
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
    # Render HTML Footer
    st.markdown(
        """
        <footer class="w-full py-8 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-white border-t border-slate-200 mt-16">
          <div class="flex flex-col gap-1">
            <div class="text-md font-bold text-slate-800 flex items-center gap-2">
              <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">work</span>
              HireMe Agent
            </div>
            <p class="text-xs text-slate-500">© 2026 HireMe Agent. All rights reserved.</p>
          </div>
          <nav class="flex flex-wrap justify-center gap-6">
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Privacy Policy</a>
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Terms of Service</a>
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Cookie Policy</a>
            <a class="text-xs text-slate-500 hover:text-primary underline" href="#">Contact Us</a>
          </nav>
        </footer>
        """,
        unsafe_allow_html=True
    )
