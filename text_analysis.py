import spacy
from sentence_transformers import SentenceTransformer, util

# Lazy load models (avoids memory issues)
def load_models():
    """Loads NLP and Semantic models only when needed."""
    nlp = spacy.load("en_core_web_sm")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return nlp, model

def analyze_resume(resume_text, job_desc):
    """Analyzes resume text and compares it to job description."""
    nlp, model = load_models()  # Load models when function is called

    # Extract entities from resume (skills, education, experience)
    doc = nlp(resume_text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]

    # Compare job description with resume
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    match_score = util.cos_sim(resume_embedding, job_embedding).item()

    return round(match_score * 100, 2), {"skills": skills}
