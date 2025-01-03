from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Aluno,Curso,Matricula
from .serializers import AlunoSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasAlunoSeriazer,ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunoViewset(viewsets.ModelViewSet):
    queryset=Aluno.objects.all()
    serializer_class=AlunoSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


class CursoViewset(viewsets.ModelViewSet):
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer


class MatriculaViewset(viewsets.ModelViewSet):
    queryset=Matricula.objects.all()
    serializer_class=MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset=Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListaMatriculasAlunoSeriazer


class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset=Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    
    serializer_class=ListaAlunosMatriculadosSerializer