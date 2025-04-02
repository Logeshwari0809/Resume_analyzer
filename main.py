from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text
from text_analysis import analyze_resume
import uvicorn

app = FastAPI()

# ✅ CORS Middleware (Allow Frontend Requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API Endpoint
@app.post("/analyze/")
async def analyze_resume_api(file: UploadFile = File(...), job_desc: str = ""):
    text = extract_text(file)
    match_score, insights = analyze_resume(text, job_desc)

    return {
        "match_score": match_score,
        "insights": insights
    }

# ✅ Run the app (For local testing)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
