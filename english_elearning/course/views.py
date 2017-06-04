# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView

from .words_course_test import CourseTest
from words_manager import WordsManager


class CourseView(DetailView):
    def get(self, request):
        return render(request, 'course_home_view.html', context={})


class WordsCourseView(DetailView):
    def get(self, request):
        wordsManager = WordsManager()
        polish_word = wordsManager.get_random_polish_word()
        english_word = wordsManager.translate_from_polish_to_english(polish_word)

        context = dict()
        context["polish_word"] = polish_word
        context["english_word"] = english_word
        context["words_number"] = 1

        request.session['words_course_session'] = context

        return render(request, 'words_course.html', context)

    def post(self, request):
        words = request.session.get('words_course_session')


        wordsManager = WordsManager()
        polish_word = wordsManager.get_random_polish_word()
        english_word = wordsManager.translate_from_polish_to_english(polish_word)

        context = dict()
        context["polish_word"] = polish_word
        context["english_word"] = english_word

        if type(words) == type(dict()):
            context["words_number"] = 1 + words["words_number"]
        else:
            if words[-1]["words_number"] == 20:
                courseTest = CourseTest()
                words_list = courseTest.parse_session_data_to_words_list(words)
                words_ids = wordsManager.get_words_ids_list(words_list)
                return render(request, 'words_course_test.html', {"words_list": words_list, "words_id_list": words_ids})
            context["words_number"] = 1 + words[-1]["words_number"]

        all_data = list()
        if type(words) == type(dict()):
            all_data.append(words)
        else:
            for word in words:
                all_data.append(word)
        all_data.append(context)

        request.session['words_course_session'] = all_data
        return render(request, 'words_course.html', context)


class CourseResultsView(DetailView):
    def post(self, request):
        original_words_id = list()
        user_translations = list()

        for i in range(1,21):
            original_words_id.append(request.POST.get("original_word_id{0}".format(i)))
            user_translations.append(request.POST.get("word{0}".format(i)))

        wordsManager = WordsManager()
        original_words = wordsManager.get_words_from_ids_list(original_words_id)

        translated_words = wordsManager.translate_polish_words_list(original_words)

        counter = 0.0
        for user, original in zip(user_translations, translated_words):
            if wordsManager.check_wheter_translation_is_correct(user, original):
                counter += 1.0

        result = float(counter/20.0) * 100.0
        return render(request, 'course_results.html', {"result": result})