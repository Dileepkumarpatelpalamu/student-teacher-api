from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    grade_level = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
