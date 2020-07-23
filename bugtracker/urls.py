from django.urls import path
from .views import BugProjectView,BugDetailView, BugCreateView, ResolvedBugView


urlpatterns=[
    path('bug_project', BugProjectView.as_view()  ,name='bug-project'),
    path('<int:pk>/bugs', BugDetailView.as_view(), name='bugs'),
    path('addbug', BugCreateView.as_view(), name='addbug'),
    path('<int:pk>/bugs/resolved', ResolvedBugView.as_view(), name='resolved'),
]