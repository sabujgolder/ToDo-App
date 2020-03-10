from django.shortcuts import render,redirect
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

def home(request):
    items = ToDo.objects.all().order_by("-added_date")
    return render(request,'ToDoApp/index.html',{'items':items})

def add_todo(request):
    if request.method =="POST":
        current_date = timezone.now()
        content = request.POST["data"]
        ToDo.objects.create(added_date=current_date,text=content)
        return HttpResponseRedirect('/')

def delete_todo(request,id):
        print(id)
        ToDo.objects.get(id=id).delete()
        return HttpResponseRedirect('/')
