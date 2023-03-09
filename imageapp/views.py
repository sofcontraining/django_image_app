from django.shortcuts import render, HttpResponse, redirect
from .models import Employee

# Create your views here.
def home(request):
    return render(request, "home.html")
def addEmployee(request):
    if request.method =="POST":
        empid = request.POST['empid']
        name=request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        dept = request.POST['dept']
        doj = request.POST['doj']
        dob = request.POST['dob']
        empphoto = request.FILES['empphoto']
        
        empdetails = Employee(empid=empid, name=name, contact=contact, email=email, dept=dept, doj=doj, dob=dob, empphoto=empphoto)
        empdetails.save()
        return redirect('/addemployee')
    else:
        emp_details = Employee.objects.all()
        context = {'emp_details':emp_details}
        return render(request, 'addemployee.html', context)
    
def addExcel(request):
    return render(request, 'addexcel.html')

def addImage(request):
    return render(request, 'addimage.html')

