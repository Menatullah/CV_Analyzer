# 📄 CV Analyzer

An AI-powered web app that compares a CV against a job description and
returns a match score, missing keywords, and tailored suggestions —
built while preparing my own CV for internship applications, when I
wanted a quick way to check how well it matched a specific role before
submitting.

## Features

- Upload a CV (PDF or DOCX)
- Paste in any job description
- Get back:
  - A match score (0–100)
  - Missing keywords worth adding
  - Existing strengths the CV already covers
  - Concrete, actionable suggestions to improve the fit

## Tech stack

Python · Streamlit · Google Gemini API · pdfplumber · python-docx · Prompt engineering

## Getting started

### Prerequisites
- Python 3.10+
- A free [Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
git clone https://github.com/Menatullah/CV-Analyzer.git
cd CV-Analyzer
pip install -r requirements.txt
```

### Configuration

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your-key-here"
```
On Windows: `set GEMINI_API_KEY=your-key-here`

### Run

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## Project structure

```
CV-Analyzer/
├── app.py          # Streamlit web interface
├── parser.py        # Extracts raw text from uploaded PDF/DOCX files
├── analyzer.py        # Sends the CV + job description to Gemini and parses the response
├── prompts.py         # Builds the prompt sent to the model
└── requirements.txt
```

## License

MIT