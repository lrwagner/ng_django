"""module required by django-rest-framework to serialize models to .json

- Serializers are used in views.py to serialize a model
- naming convention -> class {ModelName}Serializer

"""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
