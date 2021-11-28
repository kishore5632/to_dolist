from django.db import models
import datetime

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length = 50)
    Priority = models.CharField(max_length = 50)
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.task_name
    
    
