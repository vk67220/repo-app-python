import json
import random

def get_random_questions(tool):
    file_map = {
        "AWS": "database/questions/aws_questions.json",
        "DevOps": "database/questions/devops_questions.json"
    }
    with open(file_map[tool], "r") as f:
        data = json.load(f)
    return random.sample(data, 10)

def evaluate_answers(form_data):
    tool = form_data["tool"]
    answers = {k: v for k, v in form_data.items() if k.startswith("q")}
    file_map = {
        "AWS": "database/questions/aws_questions.json",
        "DevOps": "database/questions/devops_questions.json"
    }
    with open(file_map[tool], "r") as f:
        correct_answers = {str(q["id"]): q["answer"] for q in json.load(f)}
    score = sum(1 for qid, ans in answers.items() if ans == correct_answers[qid])
    return score
