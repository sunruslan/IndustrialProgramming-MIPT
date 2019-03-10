from django.db import models
import datetime


class Questions(models.Model):
    question = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
