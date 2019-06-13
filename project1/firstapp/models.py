from django.db import models

class jaipurjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
