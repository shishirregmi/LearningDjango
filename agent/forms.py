from django import forms

from agent.models import Agent

class CreateNewAgent(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('name', 'gender','age','address','phone','email','profile_pic')