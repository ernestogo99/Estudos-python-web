from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


#class UserTasksSerializer(serializers.ModelSerializer):
    #class Meta:
        #model=UserTasks
        #fields=['user_nickname','user_task']