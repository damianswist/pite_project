# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Words(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    word = models.TextField()
    language = models.TextField()

    class Meta:
        managed = False
        db_table = 'words'


class Translations(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    id_polish = models.IntegerField()
    id_eng = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'translations'
