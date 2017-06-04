from models import Quiz


class StatsManager(object):
    def calculate_stats_for_selected_user_and_quiz(self, user_id, quiz_type):
        query_set = list(Quiz.objects.filter(id_user=user_id).filter(quiz_type_id=quiz_type))

        quizes_number = len(query_set)
        if quizes_number == 0:
            return 0
        result = 0.0
        for query in query_set:
            result += float(query.result)
        return float(result / quizes_number)

    def get_data(self, user_id):
        results = {"quiz{0}".format(i): self.calculate_stats_for_selected_user_and_quiz(user_id, i) for i in range(1,4)}
        return results