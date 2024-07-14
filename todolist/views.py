from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList
from rest_framework.decorators import api_view
# Create your views here.


def todo(request):
    Todo = ToDoList(title="Harry Potter",discription="Best Selling Book")
    #Todo.save()
    context=ToDoList.objects.all()
    return render(request,'HelloWorld.html',context={'data':context})


@api_view(['get','post'])
def get_todo(request):
    pass