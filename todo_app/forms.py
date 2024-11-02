from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "checkbox-list"
                }
            ),
        }
