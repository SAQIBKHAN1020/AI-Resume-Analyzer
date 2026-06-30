def calculate_score(found_skills):

    total_skills = 10

    score = (len(found_skills) / total_skills) * 100

    return round(score)


def missing_skills(found_skills):

    required_skills = [
        "python",
        "sql",
        "pandas",
        "numpy",
        "machine learning",
        "deep learning",
        "tensorflow",
        "streamlit",
        "fastapi",
        "git"
    ]


    missing = []


    for skill in required_skills:

        if skill not in found_skills:
            missing.append(skill)


    return missing