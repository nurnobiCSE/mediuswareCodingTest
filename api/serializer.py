from rest_framework import serializers
from tasks.models import TaskModel

class TaskApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields =  "__all__"