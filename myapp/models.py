from django.db import models
class details(models.Model):
    admissionno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    year=models.IntegerField()

