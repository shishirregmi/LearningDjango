from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/",views.agentDetail,name="agent-detail"),
    path("<int:id>/delete",views.agentDelete,name="agent-delete"),
    path("<int:id>/edit/",views.updateAgent,name="agent-update"),
    path("create/",views.addAgent,name="create-agent"),
    path("",views.index,name="home-agent"),
]
