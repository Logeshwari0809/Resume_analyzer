import spacy
from sentence_transformers import SentenceTransformer, util

nlp = None
model = None

def analyze_resume(resume_text, job_desc):
    global nlp, model

    if nlp is None:
        nlp = spacy.load("en_core_web_sm")
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')

    doc = nlp(resume_text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)
    match_score = util.cos_sim(resume_embedding, job_embedding).item()

    return round(match_score * 100, 2), {"skills": skills}
