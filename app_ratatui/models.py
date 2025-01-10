"""Модели - это таблицы в базе данных"""

from django.db import models

class ProjectsModel(models.Model):
    NamesProjects = models.CharField(max_length=100) # название пректов мамы
    DescriptionProjects = models.TextField()
    SourceProjects = models.URLField()
    LinkProjects = models.URLField()


    ImageProjects = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)