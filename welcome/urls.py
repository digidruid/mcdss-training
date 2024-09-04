from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="welcome"),
    path("todos/", views.todos, name="Todos"),
    path("docs/<str:page>", views.docs ),

]



