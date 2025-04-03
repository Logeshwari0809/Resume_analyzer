import PyPDF2

def extract_text(file):
    """Extracts text from uploaded PDF file."""
    pdf_reader = PyPDF2.PdfReader(file.file)
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

