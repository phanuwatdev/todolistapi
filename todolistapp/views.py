from tabnanny import check
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todolistapp.models import Todolist
from todolistapp.serializer import TodoSerializer, TodoCheckedSerializer, TodoUpdateALlSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# API List
URL = "http://localhost:8000/api"

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_list(request):
    api_urls = {
        'List': URL +'/todo-list/',
        'Create': URL + '/todo-create-task/',
        'Update Checked': URL + '/todo-task-checked/<str:getid>',
        'Update Task': URL + '/todo-update-task/<str:getid>',
        'Update All': URL + '/todo-update-all/<str:getid>',
        'Delete Task': URL + '/todo-delete-task/<str:getid>',
        'Delete All': URL + '/todo-delete-all/',
    }
    return Response(api_urls)


# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def todo_list(request):
    """
    Retrieve, update or delete a code Todolist.
    """
    try:
        # task = Todolist.objects.all()
        todo = Todolist.objects.filter(published=True)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def todo_create_task(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def todo_task_checked(request, getid):
    if request.method == 'PUT':
        todo = Todolist.objects.get(id=getid)
        serializer = TodoCheckedSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def todo_update_task(request, getid):
    if request.method == 'PUT':
        todo = Todolist.objects.get(id=getid)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def todo_update_all(request):
    if request.method == 'PUT':
        todo = Todolist.objects.get(id=request.data['id'])
        serializer = TodoUpdateALlSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def todo_delete_task(request, getid):
    if request.method == 'DELETE':
        todo = Todolist.objects.filter(id=getid).delete()
        return Response("Successfully delete task: " + getid)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def todo_delete_all(request):
    if request.method == 'DELETE':
        todo = Todolist.objects.filter(published=True)
        todo.delete()
        return Response("Successfully delete!")

