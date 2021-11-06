from django.db import models



# Create teacher model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)

