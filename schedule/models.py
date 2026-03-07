from django.db import models
from courses.models import Course


class Lecture(models.Model):
    title = models.CharField(max_length=100)

    date = models.DateTimeField()

    room = models.CharField(max_length=50)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lectures"
    )

    def __str__(self):
        return f"{self.title} - {self.course.title}"