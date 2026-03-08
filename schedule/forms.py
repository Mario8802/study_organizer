from django import forms
from .models import Lecture


class LectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),

            "date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "room": forms.TextInput(attrs={"class": "form-control"}),

            "course": forms.Select(attrs={"class": "form-select"}),
        }