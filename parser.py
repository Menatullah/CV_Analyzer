import pdfplumber
from docx import Document


def extract_text(file) -> str:
    """Extracts raw text from an uploaded PDF or DOCX file."""
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return _extract_from_pdf(file)
    elif filename.endswith(".docx"):
        return _extract_from_docx(file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")


def _extract_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def _extract_from_docx(file) -> str:
    document = Document(file)
    text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    return text.strip()
