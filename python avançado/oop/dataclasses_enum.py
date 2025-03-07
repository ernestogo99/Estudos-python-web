from dataclasses import dataclass
from pydantic import BaseModel

class Bow:
    def __init__(self,name,price,damage):
        self.name=name
        self.price=price
        self.damage=damage
        


bow_a=Bow('great bow',100,20)
print(bow_a.__dict__)


@dataclass
class NewBow:
    name:str
    price:float
    damage:float
    
bow1=NewBow('great boww',99.99,20)
bow2=NewBow('great boww',99.99,20)
print(bow1)


class PyBow(BaseModel):
    name:str
    price:float
    damage:int
    
bow3=PyBow(name='bow',price=99.99,damage=10)
print(bow3)
