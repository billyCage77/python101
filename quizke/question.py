from dataclasses import dataclass

@dataclass
class Secret:
    answer: str
    all_questions: list


class Question:
    def __init__(self, question: str, correct_answer: str, secret_enabled: bool = False):
        self.secret_enabled = secret_enabled
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"Question({self.question},{self.correct_answer},{self.secret_enabled})"

    def answer(self, user_answer: str) -> bool:
        return self.correct_answer == user_answer

    def pose(self, question_index: int, name: str, secret: Secret) -> bool:
        question = f"Beste {name}, beantwoordt graag vraag {question_index}: {self.question}\n"
        user_answer = input(question).lower().strip()
        if self.secret_enabled:
            if secret.answer == user_answer:
                print("====================================================================================================")
                print("==========================CHEATING MODE ENABLED=====================================================")
                print("====================================================================================================")
                for question in secret.all_questions:
                    total_length = 100
                    space_left = total_length - len(question.__repr__())
                    append_final_character = 0
                    if (space_left % 2) != 0:
                        space_left -= 1
                        append_final_character = 1
                    space_left /= 2
                    space_left = int(space_left)
                    prefix = 10 * '='
                    prefix_2 = (space_left - len(prefix)) * ' '
                    suffix = (space_left + append_final_character - len(prefix)) * ' '
                    
                    print(f"{prefix}{prefix_2}{question}{suffix}{prefix}")
                print("====================================================================================================")
                print("==========================CHEATING MODE DISABLED====================================================")
                print("====================================================================================================")
        if user_answer == 'boelli':
            print(f"Doet zo onnozel ni he menneke!!!")
            exit()
        return self.answer(user_answer)
