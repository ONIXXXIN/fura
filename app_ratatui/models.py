"""Модели - это таблицы в базе данных"""

from django.db import models


class ProjectsModel(models.Model):
    NamesProjects = models.CharField(max_length=100)    # название пректов мамы
    DescriptionProjects = models.TextField()    # описание проекта
    SourceProjects = models.URLField()  # ссылка на нашем сайте
    LinkProjects = models.URLField()    # ссылка на источник (кому выполнялся проект)
    ImageProjects = models.ImageField()     # картинка для проекта

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.NamesProjects}//////{self.created_at}"

ЗАПУУУУУУУУУУУУУУУШЬ КОД ВАДЯ 😁😁 ffffffff