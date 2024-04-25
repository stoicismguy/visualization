from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    docfile = models.FileField()