def build_prompt(cv_text: str, job_description: str) -> str:
    """Builds the prompt asking the AI to compare a CV against a job description."""

    return f"""
You are a career advisor helping a student tailor their CV to a specific job description.

CV TEXT:
\"\"\"{cv_text}\"\"\"

JOB DESCRIPTION:
\"\"\"{job_description}\"\"\"

Analyze how well the CV matches the job description.

Respond ONLY with valid JSON in this EXACT format, with no extra text before or after:

{{
  "match_score": 0-100 integer,
  "missing_keywords": ["keyword1", "keyword2", "..."],
  "strengths": ["strength1", "strength2", "..."],
  "suggestions": ["suggestion1", "suggestion2", "suggestion3"]
}}
"""
