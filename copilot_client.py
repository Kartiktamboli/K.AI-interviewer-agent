import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fetch_questions(domain, resume_text):
    prompt = f"""
    You are a senior IT interviewer.

    Candidate Resume:
    {resume_text}

    Generate 5 unique interview questions for domain: {domain}.
    Questions must adapt to the resume and increase in difficulty.
    Return only numbered questions.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return [
        q.strip("0123456789. ")
        for q in response.output_text.split("\n")
        if q.strip()
    ]


def copilot_evaluate(transcript, score):
    prompt = f"""
    You are Microsoft Copilot evaluating an interview.

    Transcript:
    {transcript}

    Score: {score}

    Provide:
    - Strengths
    - Weaknesses
    - Communication
    - Seniority (Junior/Mid/Senior)
    - Hire or No-Hire decision
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
