import logging
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from agent.forms import CreateNewAgent
from agent.models import Agent

# Create your views here.
def addAgent(request):
    if request.method == "POST":
        form = CreateNewAgent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = CreateNewAgent()
    return render(request, "agent/create.html",{"form":form})