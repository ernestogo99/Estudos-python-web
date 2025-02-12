from ninja import Router,UploadedFile
from .models import Livro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .schemas import LivroSchema


cadastro_router=Router()


@cadastro_router.get('livro/')
def listar(request):
    livro=Livro.objects.all()
    response=[
        {
            'id':i.id,
            'titulo':i.titulo,
            'descricao':i.descricao,
            'autor':i.autor
        }
        for i in livro
    ]
    return response

@cadastro_router.get('livro/{id}')
def listar_livro(request,id:int):
    livro=get_object_or_404(Livro,id=id)
    return model_to_dict(livro)
    
    
@cadastro_router.get('livro_consulta/')
def listar_consulta(request,id:int=1):
        livro=get_object_or_404(Livro,id=id)
        return model_to_dict(livro)
    
    
@cadastro_router.post('livro/',response=LivroSchema)
def livro_criar(request,livro:LivroSchema):
        livro1=livro.dict()
        livro=Livro(**livro1)
        livro.save()
        return livro
    
    
@cadastro_router.post('/file')
def file_upload(request,file:UploadedFile):
    