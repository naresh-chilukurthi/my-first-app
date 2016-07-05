from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from todolist.models import Todoitem,Todolist
from django.template import loader
from django.db.models import Count, Avg,Max,Min
# Create your views here.
from todolist.serializer import TodoListSerializer, TodoItemSerializer


def showlist(request):

    c=Todolist.objects.all();
    print c
    temp = loader.get_template("todolist_template.html");
    result=temp.render(context={"colleges":c})
    return HttpResponse(result)
def showitem(request,name):
    c=Todoitem.objects.all().filter(owner=Todolist.objects.get(name=name))

    temp = loader.get_template("todoitem_template.html");
    result = temp.render(context={"colleges": c})
    return HttpResponse(result)
@api_view(['GET', 'POST'])
def todo_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Todolist.objects.all()
        serializer = TodoListSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Todolist.objects.get(id=pk)
        print snippet
    except Todolist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoListSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoListSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def todo_item(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Todoitem.objects.all()
        serializer = TodoItemSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def todo_item_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    if request.method == 'GET':
        snippets = Todoitem.objects.all().filter(owner=Todolist.objects.get(name='works'))
        serializer = TodoItemSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

