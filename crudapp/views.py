from django.shortcuts import render,redirect
from .models import studentdata

# Create your views here.
def home(request):
    if request.method=='GET':
       sd=studentdata.objects.all()
       return render(request,'home.html',{'sd':sd})

def studentreg(request):
    if request.method=='GET':
        return render(request,'studentregister.html')
    
         
    else:
        studentdata(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            mark1=request.POST.get('mark1'),
            mark2=request.POST.get('mark2'),
            mark3=request.POST.get('mark3'),
            mark4=request.POST.get('mark4'),
        ).save()
    sd=studentdata.objects.all()    
    return render(request,'home.html',{'sd':sd}) 

def update_data(request,id):
    sd=studentdata.objects.get(id=id)
    return render(request,'updateform.html',{'sd':sd})





def save_update_data(request,id):
    sd=studentdata.objects.get(id=id)
    sd.fname=request.POST.get('fname')
    sd.lname=request.POST.get('lname')
    sd.email=request.POST.get('email')
    sd.mobile=request.POST.get('mobile')
    sd.mark1=request.POST.get('mark1')
    sd.mark2=request.POST.get('mark2')
    sd.mark3=request.POST.get('mark3')
    sd.mark4=request.POST.get('mark4')
    sd.save()
    return redirect(home)
    
def delete_data(request,id):
    sd=studentdata.objects.get(id=id)
    sd.delete()
    return redirect(home)

        