from ninja import Schema,ModelSchema
from .models import Livro
class LivroSchema(Schema):
    titulo:str
    descricao:str
    autor:str=None
    
    
class ModelLivroSchema(ModelSchema):
    class Config:
        model=Livro
        model_fields='__all__'