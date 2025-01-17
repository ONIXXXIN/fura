from django.shortcuts import render
from django.views.generic import ListView
from app_ratatui.models import ProjectsModel
# Create your views here.
class LososbListView(ListView):
    model = ProjectsModel
    template_name = "portfolio.html"
    context_object_name = "projects"