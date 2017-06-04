# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView

from stats_manager import StatsManager


class StatisticsView(DetailView):
    def get(self, request):
        sm = StatsManager()
        user_id = request.user.id

        results = sm.get_data(user_id)
        return render(request, 'quiz_statistics.html', context=results)