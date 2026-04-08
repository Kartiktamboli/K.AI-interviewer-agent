
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fetch_questions(domain: str, level: str, count: int = 5):
    prompt = f"""
    You are a senior IT interviewer.
    Generate {count} unique, non-repetitive interview questions for domain: {domain}
    Difficulty level: {level}
    Return ONLY a numbered list.
    """
    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    text = resp.output_text
    return [q.strip("- ") for q in text.split("\n") if q.strip()]


def copilot_evaluate(transcript: str, score: int):
    prompt = f"""
    You are Microsoft Copilot acting as an interview evaluator.

    Transcript:
    {transcript}

    Score: {score}

    Provide:
    1. Strengths
    2. Weaknesses
    3. Communication quality
    4. Seniority (Junior/Mid/Senior)
    5. Hire/No-Hire recommendation
    """
    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return resp.output_text
