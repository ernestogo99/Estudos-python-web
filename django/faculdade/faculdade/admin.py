from django.contrib import admin
from .models import Aluno,Curso,Matricula

class Alunos(admin.ModelAdmin):
    list_display=('id','nome','rg','cpf','data_nascimento')
    list_display_links=('id','nome')#quando eu quiser alterar algo, sera possivel clicar nesses 2 links
    search_fields=('nome',)
    list_per_page=20


admin.site.register(Aluno,Alunos)

class Cursos(admin.ModelAdmin):
    list_display=('id','codigo_curso','descricao')
    list_display_links=('id','codigo_curso')
    search_fields=('codigo_curso',)
    list_per_page=20

admin.site.register(Curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display=('id','aluno','curso','periodo')
    list_display_links=('id',)

admin.site.register(Matricula,Matriculas)