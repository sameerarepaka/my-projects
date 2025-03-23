from faker import Faker
from django.shortcuts import render, HttpResponse, redirect
from .models import Student
from django.contrib import messages


fake = Faker()

def add_student(request):
    student = Student(
        name=fake.name(),
        age=fake.random_int(min=18, max=30),
        email=fake.email()
    )
    student.save()
    return redirect('student_list')  # Corrected: Added return before redirect

def student_list(request):
    students = Student.objects.all()
    return render(request, 'm1.html', {'students': students})