import streamlit as st
import requests

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Enter Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/analyze/", files=files, data={"job_desc": job_desc})

        if response.status_code == 200:
            result = response.json()
            st.write(f"✅ Match Score: {result['match_score']}%")
            st.write("🔍 Extracted Skills:", result["insights"]["skills"])
        else:
            st.error("Error analyzing resume!")
    else:
        st.warning("Please upload a resume and enter a job description.")
