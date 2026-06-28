from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def home(request):
    students = Student.objects.all().order_by("-id")

    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "students/home.html", {
        "students": students,
        "form": form
    })


def edit(request, id):
    student = get_object_or_404(Student, id=id)

    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "students/edit.html", {
        "form": form
    })


def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("home")