from rest_framework import serializers
from .models import Task




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['email', 'created_at', 'github_link']


