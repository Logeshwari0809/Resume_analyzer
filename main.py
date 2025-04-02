from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text
from text_analysis import analyze_resume
import uvicorn
import os  # ✅ Added this to read PORT from environment

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

# ✅ Run the app (For local testing & deployment)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Get PORT from Render
    uvicorn.run(app, host="0.0.0.0", port=port)
