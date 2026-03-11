from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Lecture
from .forms import LectureForm
from django import forms


class LectureListView(ListView):
    model = Lecture
    template_name = "schedule/lecture_list.html"
    context_object_name = "lectures"


class LectureCreateView(CreateView):
    model = Lecture
    form_class = LectureForm
    template_name = "schedule/lecture_create.html"
    success_url = reverse_lazy("lecture_list")

    def get_initial(self):
        initial = super().get_initial()
        course_id = self.request.GET.get("course")

        if course_id:
            initial["course"] = course_id

        return initial

    def get_form(self, form_class=None):     # TODO
        form = super().get_form(form_class)

        course_id = self.request.GET.get("course")

        if course_id:
            form.fields["course"].widget = forms.HiddenInput()

        return form

    def form_valid(self, form):
        course_id = self.request.GET.get("course")

        if course_id:
            form.instance.course_id = course_id

        return super().form_valid(form)