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
    form_class = LectureForm
    template_name = "schedule/lecture_create.html"
    success_url = reverse_lazy("lecture_list")