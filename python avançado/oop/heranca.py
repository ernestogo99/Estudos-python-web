class Baseplayer:
    def __init__(self,hp):
        self.hp=hp
    
    def walk(self):
        print('I am walking')
        
        
class Wizard(Baseplayer):
    def walk(self):
        print('i am floating')

class Archer(Baseplayer):
    
    def __init__(self, hp,arrows):
        super().__init__(hp=hp)
        self.arrows=arrows
    
    def shoot(self):
        self.arrows-=1
        print(f'Archer shoots... {self.arrows} arrows left')

wizard1=Wizard(50)
wizard1.walk()
archer1=Archer(50,3)
archer1.shoot()
archer1.shoot()


class NoupdateDictionary(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('Key already present')
        super().__setitem__(key,value)
        
y=NoupdateDictionary()
y['key']=123
y['key']=190
print(y)
