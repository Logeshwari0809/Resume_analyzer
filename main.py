from fastapi import FastAPI, File, UploadFile
from resume_parser import extract_text
from text_analysis import analyze_resume

app = FastAPI()

@app.post("/analyze/")
async def analyze_resume_api(file: UploadFile = File(...), job_desc: str = ""):
    text = extract_text(file)
    match_score, insights = analyze_resume(text, job_desc)
    
    return {
        "match_score": match_score,
        "insights": insights
    }

