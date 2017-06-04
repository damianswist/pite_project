

class CourseTest(object):
    def parse_session_data_to_words_list(self, data):
        words_list = list()
        for element in data:
            words_list.append(element["polish_word"])
        return words_list