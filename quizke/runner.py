import random
from question import Secret
from answers import answer_question_correct, answer_question_incorrect

class Runner:
    def __init__(self, list_of_questions: list, name: str, secret: Secret):
        self.questions = list_of_questions
        self.score = 0
        self.total = len(list_of_questions)
        self.name = name
        self.secret = secret
    
    def randomize(self):
        random.shuffle(self.questions)
        return self

    def pose_questions(self):
        for index, question in enumerate(self.questions):
            if question.pose(index + 1, self.name, self.secret):
                print(random.choice(answer_question_correct), self.name)
                self.score += 1
            else:
                print(random.choice(answer_question_incorrect), self.name)

    def calculate_score(self) -> int:
        return int((self.score / self.total) * 100.0)

    def run(self):
        self.pose_questions()
        print(f"You've scored {self.calculate_score()}% on this quiz.")
