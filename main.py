import os
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware  # <--- Add this import
from resume_parser import extract_text
from text_analysis import analyze_resume

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_resume_api(file: UploadFile = File(...), job_desc: str = ""):
    text = extract_text(file)
    match_score, insights = analyze_resume(text, job_desc)
    return {"match_score": match_score, "insights": insights}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
