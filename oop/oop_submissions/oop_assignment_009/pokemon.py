class Pokemon:
    sound = ""
    fly_type = ""
    swim_type = ""
    run_type = ""
    def __init__(self,name="",level=1):
        if(level<=0):
            raise ValueError("level should be > 0")
        if(len(name)==0):
            raise ValueError("name cannot be empty")
        self._name=name
        self._level=level
        self._master=None
        
    @property
    def master(self):
        if(self._master==None):
            print("No Master")
        else:
            return self._master
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
        
    @classmethod   
    def make_sound(cls):
        print(cls.sound)

    def __str__(self):
        return (f"{self.name} - Level {self.level}")
    
    @classmethod
    def fly(cls):
        print(cls.fly_type)
    
    # @classmethod
    # def swim(cls,pokemon):
    #     if pokemon.isinstance(water_pokemon):
    #         print("{} swimming...".format(cls.pokemon_name))
    #     else:
    #         print("it cannot swim")
    # @classmethod
    # def swim(cls):
    #     print(cls.swim_type)
    
    @classmethod
    def run(cls):
        print(cls.run_type)

#-------------
# paste here
class water_pokemon(Pokemon):
    @classmethod
    def swim(cls,pokemon):
        if pokemon.isinstance(water_pokemon):
            print("{} swimming...".format(cls.pokemon_name))
        else:
            print("it cannot swim")

pasted at 555 line

#--------
class Flying:
    pass
    
        
class Swimming: 
    pass
    
        
class Running:
    pass
    
        


class Pikachu(Pokemon,Running,Swimming):
    sound="Pika Pika"
    run_type="Pikachu running..."
    swim_type = "Pikachu cannot swim"
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")

class Squirtle(Pokemon,Swimming,Running):
    sound="Squirtle...Squirtle"
    run_type="Squirtle running..."
    swim_type="Squirtle swimming..."
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")

 
class Pidgey(Pokemon,Flying):
    sound="Pidgey...Pidgey"
    fly_type="Pidgey flying..."
   
    def attack(self):
        print(f"Air attack with {self.level*5} damage")
  
class Swanna(Pokemon,Flying,Swimming):
    sound="Swanna...Swanna"
    fly_type="Swanna flying..."
    swim_type="Swanna swimming..."

    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        print(f"Air attack with {self.level*5} damage")
        
class Zapdos(Pokemon,Flying):
    sound="Zap...Zap"
    fly_type="Zapdos flying..."
   
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        print(f"Air attack with {self.level*5} damage")
  
  
  
class Island:
    island_list=[]
    def __init__(self,name, max_no_of_pokemon=0, total_food_available_in_kgs=0):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        Island.island_list.append(self)
        
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def add_pokemon(self,pokemon):
        
        if(self._pokemon_left_to_catch+1>self._max_no_of_pokemon):
            print ("Island at its max pokemon capacity")
        else:
            self._pokemon_left_to_catch+=1
            
            
    @classmethod
    def get_all_islands(cls):
        l=[]
        for i in Island.island_list:
            #print(str(i))
            l.append(i)
        return l
    def __str__(self):
        return (f"{self._name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food")
  
    
class Trainer:
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=1000
        self._food_in_bag=0
        self._current_island=None
        self.catch_list=[]
    @property
    def name(self):
        return self._name
  
  
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    @property
    def current_island(self):
        if(self._current_island==None):
            print("You are not on any island")
        else:
            return (self._current_island)
            
    def __str__(self):
        return self._name
            
            
    def move_to_island(self,island):
        self._current_island=island
        
        
    def catch(self,pokemon):
        if(self._experience>=100 * pokemon.level):
            print(f"You caught {pokemon._name}")
            self._experience+=pokemon.level*20
            #l=f"{pokemon.name} - Level {pokemon.level}"
            self.catch_list.append(pokemon)
            #self._current_island._pokemon_left_to_catch-=1
        else:
            print(f"You need more experience to catch {pokemon.name}")
            
        pokemon._master=self

    def get_my_pokemon(self):
        l=[]
        for i in self.catch_list:
            l.append(i)
        return l
            
            
    def collect_food(self):
        if(self._current_island==None):
            print("Move to an island to collect food")
        else:
            if(self._food_in_bag==self._max_food_in_bag):
                pass
            elif(self._current_island._total_food_available_in_kgs>self._max_food_in_bag):
                self._food_in_bag+=self._max_food_in_bag
                self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
            elif(self._current_island._total_food_available_in_kgs<self._max_food_in_bag):
                self._food_in_bag+=self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs=0
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 
'''
class Pokimon:
    sound = ''
    Name = ''
    def __init__(self, name = '', level = 1):
        self._name = name
        
        if len(self._name) == 0:
            raise ValueError('name cannot be empty')
        
        
        self._level = level
        if self._level <= 0:
            raise ValueError('level should be > 0')
    
    def __str__(self):
        return '{} - Level {}'.format(self._name, self._level)
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod    
    def run(cls):
        print('{} running...'.format(cls.Name))
    
    
    @classmethod
    def swim(cls):
        print('{} swimming...'.format(cls.Name))
    
    @classmethod
    def fly(cls):
        print('{} flying...'.format(cls.Name))
    
    
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
       
class Pikachu(Pokimon):
    sound = 'Pika Pika'
    Name = 'Pikachu'
    def attack(self):
        print('Electric attack with {} damage'.format( self._level * 10))


class Squirtle(Pokimon):
    sound = 'Squirtle...Squirtle'
    Name = 'Squirtle'
    def attack(self):
        print('Water attack with {} damage'.format(self._level * 9))

class Pidgey(Pokimon):
    sound = 'Pidgey...Pidgey'
    Name = 'Pidgey'
    def attack(self):
        print('Air attack with {} damage'.format(self._level * 5))


class Swanna(Pokimon):
    sound = 'Swanna...Swanna'
    Name = 'Swanna'
    def attack(self):
        print('Water attack with {} damage'.format(self._level * 9))
        print('Air attack with {} damage'.format(self._level * 5))


class Zapdos(Pokimon):
    sound = 'Zap...Zap'
    Name = 'Zapdos'
    def attack(self):
        print('Electric attack with {} damage'.format(self._level * 10))
        print('Air attack with {} damage'.format(self._level * 5))

class Island:
    all_islands=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self.count=0
        self.islands=[]
        self.total_islands={}
        type(self).all_islands.append(self)
    
    def add_pokemon(self,pokemon):
        if (self.count)<self.max_no_of_pokemon:
            self.count+=1
            self.islands.append(type(pokemon).__name__)
            self.total_islands.setdefault(type(pokemon).__name__,0)
            self.total_islands[type(pokemon).__name__]+=1
        else:
            print('Island at its max pokemon capacity')
    
    @property
    def pokemon_left_to_catch(self):
        return self.count
    
    def __str__(self):
            return '{} - {} pokemon - {} food'.format(self.name,self.count,self.total_food_available_in_kgs)
    @property     
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property 
    def  total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs


class Trainer(Island):
    def __init__(self,name,experience=100,max_food_in_bag=100*10):
        self._name=name
        self._experience=experience
        self._max_food_in_bag=max_food_in_bag
        self.food_in_bag=0
        self.c_i=""
        self.count=0
        self.m=0
        self.get_poke_list=[]
    
    @classmethod
    def  get_all_islands(cls):
        for i in Island.all_islands:
            print(i)
    def move_to_island(self,given_island):
        self.c_i=given_island
        self.count+=1
    @property
    def current_island(self):
        if self.count==0:
            print('You are not on any island')
        else:
            return self.c_i
            
    def collect_food(self):
        if self.count!=0:
            if super().total_food_available_in_kgs<=self.max_food_in_bag:
                self.food_in_bag=super().total_food_available_in_kgs
                super().total_food_available_in_kgs=0
            else:
                self.food_in_bag=self.max_food_in_bag
                self.total_food_available_in_kgs-=self.max_food_in_bag
        else:
            print('Move to an island to collect food')
    
    def catch(self,poke):
        if self.experience>=100*poke.level:
            print('You caught {}'.format(poke.name))
            self._experience+=poke._level*20
            self.get_poke_list.append(poke.name,poke.level)
            self.m+=1
        else:
            print('You need more experience to catch {}'.format(poke.name))
            
    #def get_my_pokemon(self):
      #  if len(self.get_poke_list)>0:
       #     def __str__(self):
        #        return 
        #else:
         #   return (self.get_poke_list)
    @property
    def master(self):
        if self.m==0:
            print("No Master")
        else:
            pass
            #return poke
            
    def __str__(self):
        return(self.name)
    @property 
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience  
    @property 
    def max_food_in_bag(self):
        return self._max_food_in_bag



'''

'''
class Island:
    list1 = []
    X = 0
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.List = []
        self.count = 0
        
    @property
    def name(self):
        return self._name
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
     
    
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    def __str__(self):
        return '{} - {} pokemon - {} food'.format(self._name, self._pokemon_left_to_catch, self._total_food_available_in_kgs)
    
    
    
    def add_pokemon(self, pokimon):
        #type(self).X += 1
        if self.count < self._max_no_of_pokemon:
            #self.List.append(pokimon)
            self._pokemon_left_to_catch += 1
        else:
            print('Island at its max pokemon capacity')
        self.count += 1
'''

'''

class Trainer(Island):
    def __init__(self, name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        self.List = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    def __str__(self):
        if self.List == []:
            return 'No items'
        return ''.join(map(str,self.List))
 '''  
 
 

 
 #------

 
 
 
    
        
i = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)        
t=Trainer("ram")
i1= Island(name="Island2", max_no_of_pokemon=5, total_food_available_in_kgs=10000)        
i2= Island(name="Island3", max_no_of_pokemon=5, total_food_available_in_kgs=10000)        
'''print(t)
t.collect_food()
t.move_to_island(i1)
print(t.food_in_bag)
#print(t.current_island==i1)
print(t.current_island)
print(i.total_food_available_in_kgs)
#print(Island.islands_list)
print(t.get_my_pokemon())'''
Pokemon.swim_or_not(Pikachu)

q="select date,(select sum(positive) from covid),(select sum(deaths) from covid) where date=18 group by date;"



#------