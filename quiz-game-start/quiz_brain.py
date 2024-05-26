class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.questions_list = ques_list
        self.score = 0

    def still_have_question(self):
        if self.question_number >= len(self.questions_list):
            return False
        else:
            return True

    def next_question(self):
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: "
                            f"{self.questions_list[self.question_number-1].text} (True/False): ")
        self.check_answer(user_answer)
        print("")

    def check_answer(self, user_answer):
        if user_answer.lower() == self.questions_list[self.question_number-1].answer.lower():
            self.score += 1
            print(f"You got it right!")
            print(f"The correct answer was: {self.questions_list[self.question_number-1].answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print(f"That's wrong!")
            print(f"The correct answer was: {self.questions_list[self.question_number-1].answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}")
