from django.shortcuts import render, redirect
from django.views import View
from .models import Students
from .forms import AddStudentForm
class Home(View):
    def get(self,request):
        students = Students.objects.all()
        print(students)
        return render(request,'core/home.html',{'students': students})
# Create your views here.
class Add_Student(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request,'core/addstudent.html',{'form':fm})
    def post(self,request):
        fm = AddStudentForm(request.POST)
        print(fm)
        if fm.is_valid():
            fm.save()
            return redirect("/")

class Delete_Student(View):
    def post(self, request):
        data= request.POST
        id = data.get('id')
        student = Students.objects.get(id=id)
        student.delete()
        return redirect('/')
    

class Edit_Student(View):
    def get(self,request,id):
        student= Students.objects.get(id=id)
        fm= AddStudentForm(instance=student)
        return render(request,'core/editstudent.html',{'form':fm})
    def post(self,request,id):
        student= Students.objects.get(id=id)
        fm= AddStudentForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
        return redirect("/")
