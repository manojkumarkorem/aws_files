'''
class Animal:
    Sound = ""
    Breathe = ""
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        if age_in_months != 1:
            raise ValueError ("Invalid value for field age_in_months: {}".format(self._age_in_months))
        if self._required_food_in_kgs <= 0:
            raise ValueError ("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
            
    @classmethod
    def make_sound(cls):
        print(cls.Sound)
        
    @classmethod
    def breathe(cls):
        print(cls.Breathe)
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
   
    
        
class Deer(Animal):
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 2
    
class Hunting:
    Animal_Name = Deer
    Print = "No deers to hunt"
    def hunt(self,object3):
        for i in object3.List:
            if type(i) == self.Animal_Name:
                object3.List.remove(i)
        else:
            print(self.Print)
        
class Lion(Animal,Hunting):
    Sound = "Roar Roar"
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 4
        
class GoldFish(Animal):
    Sound = "Hum Hum"
    Breathe = "Breathe oxygen from water"
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2

        

class Shark(Animal,Hunting):
    Sound = "Shark Sound"
    Breathe = "Breathe oxygen from water"
    Animal_Name = GoldFish
    Print = "No GoldFish to hunt"
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 8
        
class Snake(Animal,Hunting):
    Sound = "Hiss Hiss"
    Animal_Name = Deer
    Print = "No deers to hunt"
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5
        
    
class Zoo:
    list1 = []
    X = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.List = []
        
    def add_food_to_reserve(self,reserve_amount_of_food):
        self._reserved_food_in_kgs += reserve_amount_of_food
        
    def add_animal(self,item):
        type(self).X += 1
        self.List.append(item)
        
    def count_animals(self):
        # self.X += len(self.List)
        return len(self.List)
        
    def feed(self,object1):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= object1.required_food_in_kgs
            object1.grow()
            
    @staticmethod
    def count_animals_in_given_zoos(object2):
        count = 0
        for i in object2:
            count += len(i.List)
        return count
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.X
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
'''


























class Animals:
    sound=""
    food = 0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._age_in_months = age_in_months
        
        #raise_error_for_age_in_months
        if self._age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
        #raise_error_for_required_food_in_kgs
        if self._required_food_in_kgs <= 0:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    #increasing_age_and_required_food
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.food
    
        
    #sound_of_animal
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        

class LandAnimals:
    breath = ""
    @classmethod
    def breathe(cls):
        print(cls.breath)


class WaterAnimals:
    breath = ""
    @classmethod
    def breathe(cls):
        print(cls.breath)


class Deer(Animals, LandAnimals):
    sound = 'Buck Buck'
    breath = 'Breathe in air'
    food = 2


class Hunting:
    Animal_Name = Deer
    Print = "No deers to hunt"
    def hunt(self,object3):
        for i in object3.List:
            if type(i) == self.Animal_Name:
                object3.List.remove(i)
        else:
            print(self.Print)
       



class Lion(Animals, LandAnimals):
    sound = 'Roar Roar'
    breath = 'Breathe in air'
    food = 4
    hunt_animal= ["Deer","deers"]
    
class GoldFish(Animals, WaterAnimals):
    sound = 'Hum Hum'
    breath = 'Breathe oxygen from water'
    food = 0.2

class Shark(Animals, WaterAnimals):
    sound = 'Shark Sound'
    breath = 'Breathe oxygen from water'
    food = 8
    '''hunt_animal = ["GoldFish","GoldFish"]'''
    hunt_animal = GoldFish
    Print = "No GoldFish to hunt"


class Snake(Animals, LandAnimals):
    sound = 'Hiss Hiss'
    breath = 'Breathe in air'
    food = 0.5
    '''hunt_animal = ["Deer","deers"]'''
    hunt_animal = Deer
    Print = "No deers to hunt"
    
    
class Zoo:
    list1 = []
    X = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.List = []
        
    def add_food_to_reserve(self,reserve_amount_of_food):
        self._reserved_food_in_kgs += reserve_amount_of_food
        
    def add_animal(self,item):
        type(self).X += 1
        self.List.append(item)
        
    def count_animals(self):
        # self.X += len(self.List)
        return len(self.List)
        
    def feed(self,object1):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= object1.required_food_in_kgs
            object1.grow()
            
    @staticmethod
    def count_animals_in_given_zoos(object2):
        count = 0
        for i in object2:
            count += len(i.List)
        return count
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.X
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs


    

'''
class Zoo:
    all_zoos=[]
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.count_of_animals_in_the_zoo = []
        self.total_animals = {}
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    #adding_food
    def add_food_to_reserve(self, reserved_food):
        self._reserved_food_in_kgs += reserved_food
    
    #count_animals_in_the_zoo
    def count_animals(self):
        return len(self.count_of_animals_in_the_zoo)
    
    #add_animals_to_the_zoo
    def add_animal(self, animal):
        #print(type(animal).__name__)
        self.count_of_animals_in_the_zoo.append(type(animal).__name__)
        self.total_animals.setdefault(type(animal).__name__,0)
        self.total_animals[type(animal).__name__] += 1
        #print(self.total_animals)
    
    #feeding_animals
    def feed(self,animal):
        animal_feed = animal._required_food_in_kgs
        if self._reserved_food_in_kgs>=animal_feed:
            animal.grow()
            self._reserved_food_in_kgs -= animal_feed
        
       
    @staticmethod
    def count_animals_in_all_zoos():
        total_no_animals=0
        for zoo in Zoo.all_zoos:
            total_no_animals += zoo.count_animals()
        return total_no_animals

    @classmethod
    def count_animals_in_given_zoos(cls,zoos):
        no_animals=0
        for zoo in zoos:
            no_animals += cls.count_animals(zoo)
        return no_animals
'''
'''
class Hunt:
    hunt_animal = ""
    c = 0
    def hunt(self,zoo_animals):
        for animal in zoo_animals.count_of_animals_in_the_zoo:
            if type(animal).__name__ == hunt_animal[0]:
                count_of_animals_in_the_zoo.remove(animal)
                c += 1
                break
        if c == 0:
            print(f"No {self.hunt_animal[1]} to hunt" )

'''