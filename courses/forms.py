from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "professor": forms.TextInput(attrs={"class": "form-control"}),
        }