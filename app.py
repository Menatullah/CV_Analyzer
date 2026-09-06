import streamlit as st
from parser import extract_text
from analyzer import analyze_cv

st.set_page_config(page_title="CV Analyzer", page_icon="📄")

st.title("📄 CV Analyzer")
st.caption("Check how well your CV matches a job description before you apply.")

cv_file = st.file_uploader("Upload your CV (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the job description here", height=200)

if st.button("Analyze"):
    if not cv_file or not job_description.strip():
        st.warning("Please upload a CV and paste a job description.")
    else:
        with st.spinner("Analyzing your CV..."):
            cv_text = extract_text(cv_file)
            st.session_state["result"] = analyze_cv(cv_text, job_description)

if "result" in st.session_state:
    result = st.session_state["result"]

    st.subheader("Match Score")
    st.progress(result["match_score"] / 100)
    st.write(f"**{result['match_score']}/100**")

    st.subheader("✅ Strengths")
    for item in result["strengths"]:
        st.markdown(f"- {item}")

    st.subheader("🔍 Missing Keywords")
    for item in result["missing_keywords"]:
        st.markdown(f"- {item}")

    st.subheader("💡 Suggestions")
    for item in result["suggestions"]:
        st.markdown(f"- {item}")
