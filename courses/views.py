from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course


def course_list(request):
    courses = Course.objects.all()

    context = {
        "courses": courses
    }

    return render(request, "courses/course_list.html", context)


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm()

    context = {
        "form": form
    }

    return render(request, "courses/course_create.html", context)


def course_edit(request, pk):
    course = Course.objects.get(pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm(instance=course)

    return render(request, "courses/course_edit.html", {"form": form})


def course_delete(request, pk):
    course = Course.objects.get(pk=pk)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course_delete.html", {"course": course})


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)

    context = {
        "course": course
    }

    return render(request, "courses/course_detail.html", context)
