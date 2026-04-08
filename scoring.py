
def score_answer(answer: str):
    if len(answer.strip()) < 30:
        return 0
    if len(answer) < 80:
        return 1
    return 2
