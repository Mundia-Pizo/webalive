from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Project, Bug


class BugProjectView(ListView):
    model = Project
    template_name='bugtracker/bug_project.html'


class BugDetailView(DetailView):
    model =Project
    template_name='bugtracker/bug_list.html'


class BugCreateView(TemplateView):
    template_name  = 'bugtracker/addbug.html'

class ResolvedBugView(DetailView):
    model = Bug
    queryset = Bug.objects.filter(resolved=True)
    template_name='bugtracker/resolved_bugs.html'