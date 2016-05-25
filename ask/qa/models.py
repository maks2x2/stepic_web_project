from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.CharField(max_length=256)
    likes = models.ForeignKey(User, db_index=True)

class Answer(models.Model):
    text = models.CharField(max_length=256)
    added_at = models.DateField()
    question = models.ForeignKey(Question, db_index=True)
    author = models.ForeignKey(User, db_index=True)