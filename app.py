import streamlit as st

st.title("AI Talent Scouting & Engagement Agent")

# Input
jd_input = st.text_area("Paste Job Description here", key="jd_input")

# Candidate Database (Tech + Finance)
candidates = [
    {"name": "Amit", "skills": ["python", "apis", "data analysis"], "experience": 2},
    {"name": "Riya", "skills": ["javascript", "react", "frontend"], "experience": 3},
    {"name": "Karan", "skills": ["python", "machine learning"], "experience": 1},
    {"name": "Sneha", "skills": ["python", "apis"], "experience": 2},

    {"name": "Rahul", "skills": ["financial modeling", "valuation", "excel"], "experience": 2},
    {"name": "Neha", "skills": ["equity research", "dcf", "accounting"], "experience": 3},
    {"name": "Arjun", "skills": ["data analysis", "sql", "finance"], "experience": 3},
    {"name": "Priya", "skills": ["risk management", "portfolio management"], "experience": 2}
]

# 🔧 Simple JD parser (NO AI)
def extract_jd_info(jd):
    jd = jd.lower()

    skills = []
    skill_keywords = [
        "python", "apis", "data analysis", "machine learning",
        "javascript", "react",
        "financial modeling", "valuation", "excel",
        "equity research", "dcf", "accounting",
        "sql", "risk management", "portfolio management"
    ]

    for skill in skill_keywords:
        if skill in jd:
            skills.append(skill)

    return {
        "role": "Detected Role",
        "skills": skills,
        "experience": "Not specified"
    }

# Match Score
def calculate_match_score(jd_skills, candidate_skills):
    if not jd_skills:
        return 0
    match = len(set(jd_skills).intersection(set(candidate_skills)))
    return int((match / len(jd_skills)) * 100)

# 🤖 Simulated Interest Score (NO AI)
def calculate_interest_score(match_score):
    if match_score > 70:
        return 90
    elif match_score > 40:
        return 70
    elif match_score > 20:
        return 50
    else:
        return 30

# Explanation
def generate_explanation(jd_skills, candidate):
    matched = list(set(jd_skills).intersection(set(candidate["skills"])))
    if matched:
        return f"Matched skills: {', '.join(matched)}"
    else:
        return "Low overlap"

# MAIN
if st.button("Analyze", key="analyze_button"):

    if jd_input:
        parsed = extract_jd_info(jd_input)
        jd_skills = parsed["skills"]

        st.subheader("📌 Extracted JD Info")
        st.json(parsed)

        st.subheader("🎯 Candidate Results")

        results = []

        for c in candidates:
            match_score = calculate_match_score(jd_skills, c["skills"])
            interest_score = calculate_interest_score(match_score)
            final_score = (0.7 * match_score) + (0.3 * interest_score)

            results.append({
                "name": c["name"],
                "match_score": match_score,
                "interest_score": interest_score,
                "final_score": round(final_score, 2),
                "explanation": generate_explanation(jd_skills, c)
            })

        # Sort
        results = sorted(results, key=lambda x: x["final_score"], reverse=True)

        for r in results:
            st.write(r)