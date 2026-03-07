from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Course Title"
    )

    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Course Code"
    )

    description = models.TextField(
        blank=True
    )

    start_date = models.DateField()

    professor = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f"{self.title} ({self.code})"

    class Meta:
        ordering = ["start_date"]