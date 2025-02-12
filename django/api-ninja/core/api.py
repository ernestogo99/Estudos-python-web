from ninja import NinjaAPI
from cadastro.api import cadastro_router
import orjson
from django.http import HttpRequest
from ninja.parser import Parser

class ORJSONParser(Parser):
    def parse_body(self, request:HttpRequest):
        return orjson.loads(request.body)


api=NinjaAPI(parser=ORJSONParser())

api.add_router('cadastro/',cadastro_router)

