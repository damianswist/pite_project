from random import randint

from models import Words, Translations


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
        if user_translation == "":
            return False
        user_translation = user_translation.lower()
        official_translation = official_translation.lower()

        translations = official_translation.split(",")
        for word in translations:
            if user_translation in word:
                return True
        return False

    def get_word_id(self, word):
        query_set = list(Words.objects.filter(word=word))
        word_id = query_set[0].id
        return word_id

    def get_words_ids_list(self, words):
        words_ids = list()
        for word in words:
            id = self.get_word_id(word)
            words_ids.append(id)
        return words_ids

    def get_word_from_id(self, word_id):
        query_set = list(Words.objects.filter(id=word_id))
        word = query_set[0].word
        return word

    def get_words_from_ids_list(self, ids):
        words = list()
        for id in ids:
            word = self.get_word_from_id(id)
            words.append(word)
        return words

    def translate_polish_words_list(self, words):
        translations = list()
        for word in words:
            translation = self.translate_from_polish_to_english(word)
            translations.append(translation)
        return translations