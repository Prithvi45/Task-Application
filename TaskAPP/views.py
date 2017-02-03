from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Task
from .Serializers import TaskSerializers


class TaskViewset(viewsets.ModelViewSet):

	queryset = Task.objects.all().order_by('date_created')
	serializer_class = TaskSerializers


class DueTaskViewset(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('date_created').filter(completed=False)
	serializer_class = TaskSerializers


class CompletedViewset(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('date_created').filter(completed=True)
	serializer_class = TaskSerializers