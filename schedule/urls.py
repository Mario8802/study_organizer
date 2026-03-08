from django.urls import path
from schedule.views import LectureListView, LectureCreateView


urlpatterns = [
   path("", LectureListView.as_view(), name="lecture_list"),
    path("create/", LectureCreateView.as_view(), name="lecture_create"),
]