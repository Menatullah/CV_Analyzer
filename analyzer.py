import os
import json
from google import genai
from prompts import build_prompt

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def analyze_cv(cv_text: str, job_description: str) -> dict:
    """Sends the CV + job description to Gemini and returns a structured analysis."""

    prompt = build_prompt(cv_text, job_description)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    raw_text = response.text.strip()
    raw_text = raw_text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {
            "match_score": 0,
            "missing_keywords": [],
            "strengths": [],
            "suggestions": ["Could not parse the AI response. Please try again."],
        }