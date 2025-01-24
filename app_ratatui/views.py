from django.shortcuts import render
from django.views.generic import ListView
from app_ratatui.models import ProjectsModel


class LososbListView(ListView):
    """Класс рендерит страницу и преедаём в неё данные из БД"""
    model = ProjectsModel   # из какой модели берём данные
    template_name = "portfolio.html"    # в какой html код передаём данные
    context_object_name = "projects"    # название переменной в html
