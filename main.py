import os
import uvicorn
from fastapi import FastAPI, File, UploadFile
from resume_parser import extract_text
from text_analysis import analyze_resume

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "App is running!"}

@app.post("/parse_resume/")
async def parse_resume(file: UploadFile = File(...)):
    """Extracts text from uploaded PDF resume."""
    text = extract_text(file)
    return {"extracted_text": text}

@app.post("/analyze_resume/")
async def analyze(text: str, job_desc: str):
    """Compares resume text with job description."""
    match_score, skills = analyze_resume(text, job_desc)
    return {"match_score": match_score, "skills": skills}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Render's assigned port
    uvicorn.run(app, host="0.0.0.0", port=port, workers=1, timeout_keep_alive=5)
