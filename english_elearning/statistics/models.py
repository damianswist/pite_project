# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Quiz(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    id_user = models.IntegerField()
    result = models.TextField()
    quiz_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quiz'