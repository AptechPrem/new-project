from django.shortcuts import render
from newapp.forms import *

def demo(request):
    form=LoginModel(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'demo.html',{'form':form,'notification':"Data stored successfully"})
    else:
        return render(request,'demo.html',{'form':form,'notification':"Please fill all details"})


