from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView, View
from .models import Contact
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ProjectView(TemplateView):
    template_name = 'core/projects.html'

class ContactCreateView(View):
    model = Contact
    template_name = 'core/footer.html'
    form_class = ContactForm
    success_url='/home/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, *args, **kwargs):
        form = self.form_class
        form.save(self)
        