from django.urls import path
from courses.views import course_list, course_create, course_detail, course_edit, course_delete

urlpatterns = [
    path("", course_list, name="course_list"),
    path("create/", course_create, name="course_create"),
    path("edit/<int:pk>", course_edit, name="course_edit"),
    path("delete/<int:pk>", course_delete, name="course_delete"),
    path("<int:pk>/", course_detail, name="course_detail"),
]
