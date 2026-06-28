from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "age",
            "email",
            "course",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Name"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Age"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email"
            }),

            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Course"
            }),
        }