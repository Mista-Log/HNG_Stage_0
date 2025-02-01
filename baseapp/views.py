from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework. response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.http import HttpResponseRedirect







class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def back_link(request):
            return HttpResponseRedirect("https://hng.tech/hire/python-developers")