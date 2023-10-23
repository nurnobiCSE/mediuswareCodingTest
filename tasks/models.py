from django.db import models
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.get(username='default_user')

class TaskModel(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    task_img = models.ImageField(upload_to='task_img')

    def __str__(self):
        return self.title
