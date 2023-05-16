import datetime
from django.db import models

from django.contrib.auth.models import User
class Service(models.Model):
    type = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.type
        
class Detail(models.Model):
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.file.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_done = models.BooleanField(default=False)
    details = models.ManyToManyField(Detail)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.title



class Personnel(models.Model):
    name = models.CharField(max_length=255)
    cv_file = models.ImageField(upload_to='media/')
    photo_file = models.ImageField(upload_to='media/')
    linkedin = models.URLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    creation_date = models.DateField(default=datetime.date.today)
    members = models.ManyToManyField(Personnel)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name
