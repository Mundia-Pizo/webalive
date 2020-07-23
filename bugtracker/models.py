from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def bugs(self):
        return self.bug_set.all().order_by('-date_created')


class Bug(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    resolved     = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_resolved= models.DateTimeField(null=True, blank=True)
    project      = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
