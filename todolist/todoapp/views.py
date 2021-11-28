from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

def delete(request,id):
    delete = Task.objects.filter(id=id)
    context = {'delete':delete}
    return render(request,"delete.html",context)

def cdelete(request,id):
    d = Task.objects.filter(id=id)
    d.delete()
    return HttpResponseRedirect('/')

def detail(request):
    detail = Task.objects.all()
    context = {'detail':detail}
    return render(request,"detail.html",context)

def edit(request,id):
   t = Task.objects.get(id=id)
   form = TodoForm(request.POST,instance=t)
   if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
   context = {'task':t,'form':form}
   
   return render(request,"edit.html",context)

def task_view(request):
    if request.method == "POST":
        tname = request.POST["name"]
        priority = request.POST["priority"]
        date = request.POST["date"]
        s = Task(task_name= tname,Priority=priority,date=date,)
        s.save()
        return HttpResponseRedirect("redirect")
    else:
        task = Task.objects.all()

    return render(request,"task_view.html",{'task':task})

def redirect(request):
    return render(request,"redirect.html")