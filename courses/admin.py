from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ("title", "code", "professor", "start_date")

    search_fields = ("title", "code", "professor")

    list_filter = ("start_date",)

    ordering = ("start_date",)