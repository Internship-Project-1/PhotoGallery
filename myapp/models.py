# from django.core.exceptions import ValidationError
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User



class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'), ('CG', 'Calgary'), ('MR', 'Montreal'), ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    label = models.CharField(blank=True, max_length=100)
    student = models.ForeignKey(Student, related_name='gallery', on_delete=models.CASCADE)
    favourite = models.BooleanField(default=False)

