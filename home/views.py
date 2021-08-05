from django.shortcuts import render,HttpResponse
from home.models import Post,Teacher,Student
# Create your views here.
def index(request):
    return HttpResponse("main app for links")


def post(request):
    post = Post.objects.all()
    return render(request,'post.html',{'post':post})


def student(request):
    student = Student.objects.all()

    return render(request,'student.html',{'student':student})


def teacher(request):
    teacher = Teacher.objects.all()

    return render(request, 'teacher.html', {'teacher': teacher})