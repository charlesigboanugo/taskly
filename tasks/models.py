from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    start_at = models.DateField()
    due_at = models.DateField()
    is_completed = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title
