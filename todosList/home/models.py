from django.db import models

# Create your models here.
class ToDos(models.Model):
    taskTitle = models.CharField(max_length=50) 
    taskDesc = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle