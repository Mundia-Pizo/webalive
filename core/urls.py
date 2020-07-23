from django.urls import  path
from .views import HomeView, AboutView, ProjectView,ContactCreateView


urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('projects', ProjectView.as_view(), name='projects'),
    path('contact', ContactCreateView.as_view(),name='contact')

]