def extract_skills(text):

    skills_list = [
        "python",
        "sql",
        "pandas",
        "numpy",
        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "nlp",
        "nltk",
        "streamlit",
        "fastapi",
        "git",
        "github"
    ]

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills