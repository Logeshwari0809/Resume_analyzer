 # ***Resume Analyzer*** 📄 


A Resume Analyzer that uses FastAPI for the backend and Streamlit for the frontend. Upload your resume, analyze its content, and compare it with job descriptions.

Features

FastAPI Backend: Handles resume processing and job description matching.

Streamlit Frontend: User-friendly interface to upload resumes.

Python Virtual Environment: Uses .venv to manage dependencies.

Dependency Management: Uses requirements.txt for easy installation

# Installation & Setup

1  *Clone the Repository*


git clone https://github.com/yourusername/resume_analyzer.git

cd resume_analyzer

2  *Create & Activate Virtual Environment*

python -m venv .venv

.venv\Scripts\activate

3 *Install Dependencies*


pip install -r requirements.txt


# Running the Application

1 *Start the FastAPI Backend*


uvicorn main:app --reload


Access API Docs: Open http://127.0.0.1:8000/docs


2 *Start the Streamlit Frontend*


streamlit run app.py


View in Browser: Open http://localhost:8501

![image alt](https://github.com/Logeshwari0809/Resume_analyzer/blob/41bd93822ab5bdda4153e697c1de7b99bda6fa16/Screenshot%202025-04-01%20162548.png)
