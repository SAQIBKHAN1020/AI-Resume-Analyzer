import streamlit as st
from utils.pdf_reader import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.score_checker import calculate_score, missing_skills
from utils.job_matcher import match_resume_job

st.title("AI Resume Analyzer")


resume = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


if resume:

    text = extract_text(resume)

    clean = clean_text(text)

    skills = extract_skills(clean)

    st.write(clean)

    st.write(skills)

    score = calculate_score(skills)

    missing = missing_skills(skills)


    st.subheader("Resume Score")

    st.write(str(score) + "%")


    st.subheader("Missing Skills")

    st.write(missing)


    job_description = st.text_area(
        "Paste Job Description"
    )


    if job_description:

        job_clean = clean_text(job_description)

        job_skills = extract_skills(job_clean)


        match_score, missing_job = match_resume_job(
            skills,
            job_skills
        )


        st.subheader("Job Match Score")

        st.write(str(match_score) + "%")


        st.subheader("Missing Job Skills")

        st.write(missing_job)