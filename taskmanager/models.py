from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=128)
    date_of_creation = models.DateTimeField()
    def __str__(self):
        return self.tag_name


class Task(models.Model):
    task_name = models.CharField(max_length=128)
    description = models.TextField()
    date_of_creation = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name="task_list", blank = True)

    def __str__(self):
        return self.task_name