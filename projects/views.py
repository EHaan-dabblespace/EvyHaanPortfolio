from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Project
from django.shortcuts import render


class Home(TemplateView):
    """
    Displays the home page.

    Methods:
        GET : Renders all projects from the projects model.
    """
    template_name = 'projects/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['message'] = 'welcome to the home page'
        return context


class ProjectDetailView(DetailView):
    """
    Displays details of the selected project.

    Methods:
        GET : Renders details for the selected project.
    """

    model = Project
    template_name = 'projects/detail.html'

    def get_object_or_404(self):
        return get_object_or_404(Project, pk=request.session['project_id'])