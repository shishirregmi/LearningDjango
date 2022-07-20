import logging
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from agent.forms import CreateNewAgent
from agent.models import Agent
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)


# Create your views here.
def addAgent(request):
    if request.method == "POST":
        form = CreateNewAgent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-agent')
    else:
        form = CreateNewAgent()
    return render(request, "agent/create.html",{"form":form})

def index(request):
    data = Agent.objects.all
    return render(request,'agent/index.html',{'datas':data})

def agentDetail(request, id):
    data = Agent.objects.get(id=id)
    return render(request,'agent/details.html',{'data':data})

def agentDelete(request, id):
    obj = get_object_or_404(Agent, id = id)  
    if request.method =="POST":
        obj.delete()
        return redirect('home-agent') 
    return render(request, "delete_view.html")

def updateAgent(request,id):
    data = get_object_or_404(Agent,id=id)
    form = CreateNewAgent(request.POST or None, instance= data)
    context= {'form': form}
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        messages.success(request, "You successfully updated the post")
        context= {'form': form}
        return render(request, 'agent/update.html', context)
    else:
        context= {'form': form,'error': 'The form was not updated successfully. Please enter in a title and content'}
        return render(request,'agent/update.html' , context)