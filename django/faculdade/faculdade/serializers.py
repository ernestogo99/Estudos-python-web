from rest_framework import serializers
from .models import Aluno,Curso,Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aluno
        fields='__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields='__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Matricula
        fields='__all__'


class ListaMatriculasAlunoSeriazer(serializers.ModelSerializer):
    curso=serializers.ReadOnlyField(source='curso.descricao')
    periodo=serializers.SerializerMethodField()
    class Meta:
        model=Matricula
        fields=['curso','periodo']

    def get_periodo(self,obj):
        return obj.get_periodo_display()
    

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    nome_aluno=serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model=Matricula
        fields=['nome_aluno']