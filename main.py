import os
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text
from text_analysis import analyze_resume

app = FastAPI()

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API Endpoint
@app.post("/analyze/")
async def analyze_resume_api(file: UploadFile = File(...), job_desc: str = ""):
    text = extract_text(file)
    match_score, insights = analyze_resume(text, job_desc)
    return {"match_score": match_score, "insights": insights}

# ✅ Correct Port Binding for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Bind to Render's PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
