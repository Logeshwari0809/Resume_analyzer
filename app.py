import streamlit as st
import PyPDF2
import spacy
from sentence_transformers import SentenceTransformer, util

# Load models with caching
@st.cache_resource
def load_models():
    nlp = spacy.load("en_core_web_sm")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return nlp, model

nlp, model = load_models()

# Extract text from uploaded PDF
def extract_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

# Analyze resume vs job description
def analyze_resume(resume_text, job_desc):
    doc = nlp(resume_text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    match_score = util.cos_sim(resume_embedding, job_embedding).item()

    return round(match_score * 100, 2), {"skills": skills}


# Streamlit UI
st.set_page_config(page_title="Resume Analyzer", layout="centered")
st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Enter Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        with st.spinner("Extracting text and analyzing..."):
            resume_text = extract_text(uploaded_file)
            match_score, insights = analyze_resume(resume_text, job_desc)

        st.success("✅ Analysis Complete!")
        st.metric("Match Score", f"{match_score}%")

        if match_score > 75:
            st.info("Strong match! ✅")
        elif match_score > 50:
            st.warning("Moderate match — could improve. ⚠️")
        else:
            st.error("Low match — consider updating your resume. ❌")

        st.write("🔍 **Extracted Skills:**")
        st.write(insights["skills"] or "No skills identified.")
    else:
        st.warning("Please upload a resume and enter a job description.")
