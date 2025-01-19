from .models import Answer


class AnswerController:
    @staticmethod
    def create_answer(user_info, question, answer):
        answer = Answer(user_info=user_info, question=question, answer=answer)
        answer.save()
