class QuizEval:

    def __int__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        input("Q.{} {}. (True/False)".format(self.question_number, current_question))
