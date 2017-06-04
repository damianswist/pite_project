from random import randint

from english_elearning.course.models import Words, Translations


class WordsManager(object):
    def get_random_polish_word(self):
        word_id = randint(1, 4567)
        polish_word = list(Words.objects.filter(id=word_id))
        return polish_word[0].word

    def translate_from_polish_to_english(self, polish_word):
        query_set = list(Words.objects.filter(word=polish_word))
        polish_word_id = int(query_set[0].id)
        english_word_id = list(Translations.objects.filter(id_polish=polish_word_id))[0].id_eng
        english_word = list(Words.objects.filter(id=english_word_id))[0].word
        return english_word

    def translate_from_english_to_polish(self, english_word):
        query_set = list(Words.objects.filter(word=english_word))
        english_word_id = int(query_set[0].id)
        polish_word_id = list(Translations.objects.filter(id_eng=english_word_id))[0].id_polish
        polish_word = list(Words.objects.filter(id=polish_word_id))[0].word
        return polish_word

    def check_wheter_translation_is_correct(self, user_translation, official_translation):
        user_translation = user_translation.lower()
        official_translation = official_translation.lower()

        translations = official_translation.split(",")
        for word in translations:
            if user_translation in word:
                return True
        return False
