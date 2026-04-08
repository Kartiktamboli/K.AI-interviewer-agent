def score_answer(answer: str):
    if not answer or len(answer.strip()) < 20:
        return 0
    elif len(answer) < 60:
        return 1
    else:
        return 2


def detect_level(total_score: int):
    if total_score <= 4:
        return "Junior"
    elif total_score <= 7:
        return "Mid"
    else:
        return "Senior"
