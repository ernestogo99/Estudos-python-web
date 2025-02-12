from rest_framework import serializers
from .models import Interprete

class InterpreteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interprete
        fields='__all__'