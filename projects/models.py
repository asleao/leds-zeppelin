from django.contrib.auth.models import User
from django.db import models

from languages.models import Language
from tools.models import Tool


class Project(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    tools = models.ManyToManyField(Tool, related_name='tools')
    team = models.ManyToManyField(User, related_name='team')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')

    def __str__(self):
        return self.name