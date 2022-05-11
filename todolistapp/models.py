from django.db import models

# Create your models here.
class Todolist(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    task = models.CharField(max_length=200, blank=False)
    checked = models.BooleanField(default=True)
    order = models.IntegerField(null=True, unique=False, default=0)

    def __str__(self):
        return self.task

