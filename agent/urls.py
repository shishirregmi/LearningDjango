from django.urls import path
from . import views

urlpatterns = [
    #path("<int:id>",views.index,name="index"),
    path("create/",views.addAgent,name="create-agent"),
    path("",views.index,name="home-agent"),
]
