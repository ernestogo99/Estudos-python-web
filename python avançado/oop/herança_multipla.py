import json
class A:
    def say_hi(self):
        print('hello from A')
        
        
class B(A):
    def say_hi(self):
        print("Hello from B")
        
class C(A):
    def say_hi(self):
        print("Hello from C")
        
class D(B,C):
    pass


d=D()
d.say_hi()


class Archer:
    def __init__(self,hp):
        self.hp=hp
        
    def walk(self):
        return 'i am walking'

class JsonMixin:
    def to_json(self):
        json.dumps(self,default=lambda o:o.__dict__)
        
class SuperWalkMixin:
    def walk(self):
        return f'{super().walk()} extremely fast'
    
    
class SuperArcher(JsonMixin,SuperWalkMixin,Archer):
    pass

superr=SuperArcher(100)
print(superr.walk())
print(superr.to_json())
        