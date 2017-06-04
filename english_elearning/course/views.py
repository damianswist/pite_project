# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView

from utils import WordsManager


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
        number_of_words = len(words)


        wordsManager = WordsManager()
        polish_word = wordsManager.get_random_polish_word()
        english_word = wordsManager.translate_from_polish_to_english(polish_word)

        context = dict()
        context["polish_word"] = polish_word
        context["english_word"] = english_word

        if number_of_words == 3:
            context["words_number"] = 1 + words["words_number"]
        else:
            if words[-1]["words_number"] == 20:
                return render(request, 'words_course.html', {})
            context["words_number"] = 1 + words[-1]["words_number"]

        all_data = list()
        all_data.append(words)
        all_data.append(context)

        request.session['words_course_session'] = all_data
        return render(request, 'words_course.html', context)
