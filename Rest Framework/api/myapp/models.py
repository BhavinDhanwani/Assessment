from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=60)
    city=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username