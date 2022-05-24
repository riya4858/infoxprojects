from django.shortcuts import redirect, render

from studentregapp.models import register
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def reg(request):
    if request.method=='POST':
        studname=request.POST['name']
        studaddress=request.POST['address']
        studage=request.POST['age']
        studjoiningdate=request.POST['joiningdate']
        studcontact=request.POST['contact']
        studemail=request.POST['email']
        studgender=request.POST['gender']
        studqualification=request.POST['qualification']
        registration=register(name=studname,address=studaddress,age=studage,joiningdate=studjoiningdate,contact=studcontact,email=studemail,gender=studgender,qualification=studqualification)
        registration.save()
        messages.success(request,"Successfully registered")
        return render(request,'home.html') 
    
         
     
        
    
def studentlist(request):
     studreg=register.objects.all()
     return render(request,'studentlist.html',{'studreg':studreg})
     
def editpage(request,pk):
    regedit=register.objects.get(id=pk)
    return render(request,'edit.html',{'reg':regedit})

def edit_details(request,pk):
    if request.method=='POST':
        regedit=register.objects.get(id=pk)
        regedit.name=request.POST.get('name')
        regedit.address=request.POST.get('address')
        regedit.age=request.POST.get('age')
        regedit.joiningdate=request.POST.get('joiningdate')
        regedit.contact=request.POST.get('contact')
        regedit.email=request.POST.get('email')
        regedit.gender=request.POST.get('gender')
        regedit.qualification=request.POST.get('qualification')
        regedit.save()
        return redirect('studentlist')
    return render(request,'edit.html')

def deletepage(request,pk):
    regedit=register.objects.get(id=pk)
    regedit.delete()
    messages.success(request,"Deleted")

    return redirect('studentlist')

def viewstudents(request,pk):
    studreg=register.objects.get(id=pk)
    return render(request,'studentdetails.html',{'reg':studreg})

