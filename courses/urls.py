from django.urls import path
from courses.views import course_list

urlpatterns = [
    path("",course_list, name="course_list"),
]