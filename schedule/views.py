from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Lecture
from .forms import LectureForm


class LectureListView(ListView):
    model = Lecture
    template_name = "schedule/lecture_list.html"
    context_object_name = "lectures"


class LectureCreateView(CreateView):
    model = Lecture
    fields = "__all__"
    template_name = "schedule/lecture_create.html"
    success_url = reverse_lazy("lecture_list")

    def get_initial(self):
        initial = super().get_initial()
        course_id = self.request.GET.get("course")

        if course_id:
            initial["course"] = course_id

        return initial