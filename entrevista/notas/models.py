from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Score(models.Model):
    name = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    def __str__(self):
        return self.name
