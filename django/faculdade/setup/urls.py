from django.contrib import admin
from django.urls import path,include
from faculdade.views import AlunoViewset,CursoViewset,MatriculaViewset,ListaMatriculasAluno,ListaAlunosMatriculados
from rest_framework import routers

router=routers.DefaultRouter()
router.register('alunos',AlunoViewset,basename='Alunos')
router.register('cursos',CursoViewset,basename='Cursos')
router.register('matriculas',MatriculaViewset,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('aluno/<int:pk>/matriculas',ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas',ListaAlunosMatriculados.as_view())
]
