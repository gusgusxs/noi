from django.db import models

class subject(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    subject_name = models.CharField(max_length=100)
    std = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id},{self.subject_name},{self.std}"
    