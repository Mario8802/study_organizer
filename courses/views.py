from django.shortcuts import render
from .models import Course


def course_list(request):
    courses = Course.objects.all()

    context = {
        "courses": courses
    }

    return render(request, "courses/course_list.html", context)
