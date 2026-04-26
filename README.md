# AI Talent Scouting & Engagement Agent

## Problem
Recruiters spend significant time manually screening candidates and still struggle to identify the best fit efficiently.

---

## Solution
This project is an AI-powered talent scouting agent that automates candidate matching.

It takes a job description, extracts relevant skills, compares them with candidate profiles, calculates match and interest scores, and produces a ranked shortlist with explanations.

---

## Features
- Multi-domain support (Tech + Finance)
- Match Score calculation
- Interest Score simulation
- Explainable candidate ranking
- Ranked output

---

## Tech Stack
- Python
- Streamlit
- Rule-based logic (LLM-ready architecture)

---

## How to Run

```bash
pip install streamlit
python -m streamlit run app.py

A lightweight AI-powered recruitment assistant that automates candidate shortlisting using skill matching and scoring.

## Architecture

JD Input → Skill Extraction → Candidate Matching → Interest Scoring → Final Ranking → Output
