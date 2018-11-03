from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    cmmnt=models.CharField(max_length=50)
