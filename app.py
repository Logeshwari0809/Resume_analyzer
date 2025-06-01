import streamlit as st
import requests

API_URL = "https://resume-analyzer-1tls.onrender.com/analyze/"


st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Enter Job Description")


if st.button("Analyze"):
    if uploaded_file and job_desc:
        files = {"file": uploaded_file.getvalue()}
        data = {"job_desc": job_desc}

        response = requests.post(API_URL, files={"file": uploaded_file.getvalue()}, data={"job_desc": job_desc})
        
        if response.status_code == 200:
            result = response.json()
            st.write(f"✅ Match Score: {result['match_score']}%")
            st.write("🔍 Extracted Skills:", result["insights"]["skills"]) 
        else:
            st.error("❌ Error analyzing resume! Check backend logs.")

    else:
        st.warning("⚠️ Please upload a resume and enter a job description.")

