from django.shortcuts import render, HttpResponse
from .models import TodoItem
import requests

# Create your views here.
def home(req):
    
    apidata = requests.get("http://127.0.0.1:8890/api/agendas/").json()

    apidata1 = []
    for agenda in apidata:
        if agenda['completed'] != True:
            apidata1.append(agenda)

    #filter(lambda x: x['Completed']!=True, apidata)

#    return HttpResponse(apidata)

    return render(req, "home0.html", {'agendas': apidata1 } )















def todos(req):

    items = TodoItem.objects.all()
    return HttpResponse(items)
    #return render(req, "todos.html", {'todos': items } )

def docs(req):
    return render(req, "docs.html", req)


