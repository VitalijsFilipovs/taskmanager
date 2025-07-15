from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done')
    ])
    deadline = models.DateField()

    def __str__(self):
        return self.title

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done')
    ])
    deadline = models.DateField()

    def __str__(self):
        return self.title
