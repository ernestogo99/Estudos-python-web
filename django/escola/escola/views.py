from .models import Estudante,Curso,Matricula
from .serializers import EstudanteSerializer,EstudanteSerializerV2,CursoSerializer,MatriculaSeralizer,ListaMatriculasEstudanteSerializer,ListaMatriculasCursoSerializer
from rest_framework import viewsets,generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from .throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    
    queryset=Estudante.objects.all().order_by('id')
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields=['nome']
    search_fields=['nome','cpf']
    def get_serializer_class(self):
        if self.request.version =='v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    
    queryset=Curso.objects.all().order_by('id')
    serializer_class=CursoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]


class MatriculaViewset(viewsets.ModelViewSet):
    http_method_names=['get','post']
    throttle_classes=[UserRateThrottle,MatriculaAnonRateThrottle]
    queryset=Matricula.objects.all().order_by('id')
    serializer_class=MatriculaSeralizer

class ListaMatriculaEstudante(generics.ListAPIView):
    """ 
    Descrição da View:
    -Lista Matriculas por id de Estudante
    Parâmetros:
    -pk(int):o identificador primário do objeto. Deve ser um número inteiro
    """
    
    def get_queryset(self):
        queryset=Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class=ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """ 
    Descrição da View:
    -Lista Matriculas por id de Estudante
    Parâmetros:
    -pk(int):o identificador primário do objeto. Deve ser um número inteiro
    """

    def get_queryset(self):
        queryset=Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class=ListaMatriculasCursoSerializer
   

