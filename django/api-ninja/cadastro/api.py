from typing import List
from ninja import Router
from .models import Livro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .schemas import LivroSchema,ModelLivroSchema


cadastro_router=Router()


@cadastro_router.get('livro/',response=List[ModelLivroSchema])
def listar(request):
    livros=Livro.objects.all()
    return livros

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
    
    
@cadastro_router.delete('livro/{id}',response={204:None})
def delete_livro(request,id:int):
    livro=get_object_or_404(Livro,id=id)
    livro.delete()
    return 204,None


@cadastro_router.put('livro/{id}',response=LivroSchema)
def update_livro(request,id:int,livro_update:LivroSchema):
    Livro.objects.filter(id=id).update(**livro_update.dict())
    
    livro=get_object_or_404(Livro,id=id)
    
    livro.refresh_from_db()
    
    return livro
    
    