from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Question(models.Model):
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1)  # '1', '2', '3', '4'
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.
