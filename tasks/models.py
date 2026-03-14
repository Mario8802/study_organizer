from django.db import models

from courses.models import Course


class Task(models.Model):
    title = models.CharField(
        max_length=100,
    )

    deadline = models.DateField()

    description = models.TextField()

    completed = models.BooleanField(
        default=False
    )

    courses = models.ManyToManyField(
        Course,
        related_name="tasks"
    )


    def __str__(self):
        return self.title
