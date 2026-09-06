# 📄 CV Analyzer

Built while preparing my own CV for Internships —
I wanted a quick way to check how well a CV matches a specific job
description before submitting, so I built this tool using the Claude API.

## What it does
- Upload a CV (PDF or DOCX)
- Paste a job description
- Get back: a match score, missing keywords, existing strengths, and
  concrete suggestions to improve the fit

## How to run it locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set your Anthropic API key as an environment variable:
   ```
   export ANTHROPIC_API_KEY="your-key-here"
   ```
   (On Windows: `set ANTHROPIC_API_KEY=your-key-here`)

3. Run the app:
   ```
   streamlit run app.py
   ```

4. Open the local URL Streamlit gives you (usually http://localhost:8501)

## Tech stack
Python · Streamlit · Anthropic Claude API · pdfplumber · python-docx 

## Project structure
- `app.py` — Streamlit web interface
- `parser.py` — extracts raw text from uploaded PDF/DOCX files
- `analyzer.py` — sends the CV + job description to Claude and parses the response
- `prompts.py` — builds the prompt sent to the model
