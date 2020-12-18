from django.shortcuts import render, redirect
from .models import courses, student
from .forms import studentform
# Create your views here.
def get(request):
    course = courses.objects.all()
    students = student.objects.all()
    context = {
        'course': course,
        'students': students
    }
    return render(request, 'home.html' , context)

def index(request):
    course = courses.objects.all()
    request.POST.getlist('course')
    return render(request, 'index.html', {'course': course})

def studentView(request):
    form = studentform()
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
    return render(request, "form.html", {'form': form})

def view(request):
    form = Student()
    
    if request.method == "POST":
        form = Student(request.POST or None)
        if form.is_valid():
            form.save()
    
    return render(request, 'home.html', {'form', form})

def submit(request):
    a = request.POST(['initial'])
    return render(request, 'home.html', {
        'error_message': "returned"
    })