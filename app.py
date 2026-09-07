import streamlit as st
from parser import extract_text
from analyzer import analyze_cv

st.set_page_config(page_title="CV Analyzer", page_icon="📄", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@600;700&display=swap');

.stApp { background-color: #FFFFFF; }

.hero-title {
    font-family: 'Source Serif 4', serif;
    font-weight: 700;
    font-size: 2.6rem;
    color: #1C2B39;
    margin-bottom: 0.2rem;
    letter-spacing: -0.01em;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: #5B6B7A;
    margin-bottom: 2rem;
    max-width: 640px;
    line-height: 1.6;
}
.section-label {
    font-family: 'Source Serif 4', serif;
    font-weight: 600;
    font-size: 1.05rem;
    color: #1C2B39;
    margin-bottom: 0.6rem;
}
.result-card {
    background-color: #F4F4F2;
    border: 1px solid #E2E1DC;
    border-radius: 10px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.score-number {
    font-family: 'Source Serif 4', serif;
    font-weight: 700;
    font-size: 1.9rem;
    color: #1C2B39;
}
.score-bar-track {
    background-color: #E2E1DC;
    border-radius: 999px;
    height: 14px;
    width: 100%;
    overflow: hidden;
    margin: 0.6rem 0 0.4rem 0;
}
.score-bar-fill {
    background-color: #F4B400;
    height: 100%;
    border-radius: 999px;
}
.keyword-pill {
    display: inline-block;
    background-color: #FBEAE8;
    color: #9C3A32;
    border: 1px solid #E9C4BF;
    border-radius: 999px;
    padding: 0.25rem 0.8rem;
    margin: 0.2rem 0.3rem 0.2rem 0;
    font-size: 0.9rem;
}
.strength-item, .suggestion-item {
    padding: 0.35rem 0;
    color: #33414D;
    line-height: 1.6;
}
div.stButton > button {
    background-color: #1C2B39;
    color: #FFFFFF;
    border-radius: 6px;
    padding: 0.6rem 2rem;
    border: none;
    font-weight: 500;
}
div.stButton > button:hover { background-color: #2E4258; color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">CV Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Upload your CV and paste a job description to see how well '
    'they match — with a score, missing keywords, and concrete suggestions to improve the fit.</div>',
    unsafe_allow_html=True,
)

left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown('<div class="section-label">Your CV</div>', unsafe_allow_html=True)
    cv_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"], label_visibility="collapsed")

with right_col:
    st.markdown('<div class="section-label">Job description</div>', unsafe_allow_html=True)
    job_description = st.text_area("Paste the job description", height=220, label_visibility="collapsed")

st.write("")
button_col = st.columns([1, 1, 1])[1]
with button_col:
    analyze_clicked = st.button("Analyze", use_container_width=True)

if analyze_clicked:
    if not cv_file or not job_description.strip():
        st.warning("Please upload a CV and paste a job description.")
    else:
        with st.spinner("Analyzing your CV..."):
            cv_text = extract_text(cv_file)
            st.session_state["result"] = analyze_cv(cv_text, job_description)

if "result" in st.session_state:
    result = st.session_state["result"]
    st.write("")
    result_left, result_right = st.columns(2, gap="large")

    with result_left:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">Match score</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-number">{result["match_score"]}/100</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="score-bar-track"><div class="score-bar-fill" '
            f'style="width:{result["match_score"]}%"></div></div>',
            unsafe_allow_html=True,
        )
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Strengths</div>', unsafe_allow_html=True)
        for item in result["strengths"]:
            st.markdown(f'<div class="strength-item">✓ {item}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with result_right:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">Missing keywords</div>', unsafe_allow_html=True)
        pills = "".join(f'<span class="keyword-pill">{kw}</span>' for kw in result["missing_keywords"])
        st.markdown(pills if pills else '<span style="color:#5B6B7A;">None — good coverage.</span>', unsafe_allow_html=True)
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Suggestions</div>', unsafe_allow_html=True)
        for item in result["suggestions"]:
            st.markdown(f'<div class="suggestion-item">• {item}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
