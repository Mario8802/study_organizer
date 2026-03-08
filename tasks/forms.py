from datetime import date

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "deadline", "description", "courses"]

        labels = {
            "title": "Task Title",
            "deadline": "Deadline",
            "description": "Description",
            "completed": "Completed",
            "courses": "Courses",
        }

        help_texts = {
            "deadline": "Choose a deadline for this task!!!",
        }

        error_messages = {
            "title": {
                "required": "Please enter a task title!!!"
            },
            "deadline": {
                "required": "Please select a deadline!!!"
            }
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Task title",
                }
            ),

            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Task description",
                }
            ),

            "completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "courses": forms.CheckboxSelectMultiple(),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")

        if deadline and deadline < date.today():
            raise forms.ValidationError("Deadline cannot be in the past.")

        return deadline


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "deadline", "description"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),
        }
