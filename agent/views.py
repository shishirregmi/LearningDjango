import logging
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

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

def updateAgent(UpdateView):
    form_class  = CreateNewAgent
    redirect_field_name = 'agent/create.html'
    model = Agent