class Pokemon:
    c=0
    sound=""
    swim_type = ""
    Pokemon_name=""
    def __init__(self,name,level):
        if name=="":
            raise ValueError("name cannot be empty")
        self._name=name
        if level<=0:
            raise ValueError("level should be > 0")
        self._level=level
        self._master=None
        
    
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
    @property
    def master(self):
        if self._master==None:
            print("No Master")
        else:
            return self._master
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod   
    def run(cls):
        print("{} running...".format(cls.Pokemon_name))   
        
    @classmethod
    def swim(cls):
        #if cls.swim_type == "":
        print("{} swimming...".format(cls.Pokemon_name))  
        """else:
            print("{} cannot swim".format(cls.Pokemon_name))"""
    @classmethod
    def fly(cls):
        print("{} flying...".format(cls.Pokemon_name))  
    
        
    def __str__(self):
        return("{} - Level {}".format(self._name,self._level))
        
class Water_pokemon(Pokemon):
    @classmethod
    def swim(cls):
        print("{} swimming...".format(cls.Pokemon_name))  
    
    
class Pikachu(Pokemon):
    swim_type = 'Pikachu cannot swim'
    sound="Pika Pika"
    Pokemon_name="Pikachu"
    
    def attack(self):
        print("Electric attack with {} damage".format(self._level*10))
    
    @classmethod       
    def swim(cls):
        if isinstance(cls,Water_pokemon):
            print("{} swimming...".format(cls.Pokemon_name))
        else:
            print("{} cannot swim".format(cls.Pokemon_name))    
        
    
        
a = Pikachu.swim()