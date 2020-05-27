class Animal:
    def __init__(self,breed,required_food_in_kgs,age_in_months = 1):
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        if self._required_food_in_kgs<=0:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
        self._age_in_months=age_in_months
        if self._age_in_months!=1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))

    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months

class Deer(Animal):
    @classmethod
    def make_sound(cls):
        print('Buck Buck')
    @classmethod 
    def breathe(cls):
        print('Breathe in air')

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=2

class Lion(Animal):
    @classmethod 
    def make_sound(cls):
        print('Roar Roar')
    @classmethod
    def breathe(cls):
        print('Breathe in air')

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=4
    def hunt(self,zoo):
        data = zoo.animals.count('Deer')
        if data>0:
            zoo.animals.remove('Deer')
        else:
            print('No deers to hunt')

class Shark(Animal):
    @classmethod 
    def make_sound(cls):
        print('Shark Sound')
    @classmethod
    def breathe(cls):
        print('Breathe oxygen from water')

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=8
    def hunt(self,zoo):
        data=zoo.animals.count('GoldFish')
        if data==0:
            print('No GoldFish to hunt')
        else:
            zoo.animals.remove('GoldFish')

class GoldFish(Animal):
    @classmethod
    def make_sound(cls):
        print('Hum Hum')
    @classmethod
    def breathe(cls):
        print('Breathe oxygen from water')

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=0.2



class Zoo:
    all_zoos=[]
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.animals=[]
        self.total_animals={}
        type(self).all_zoos.append(self)
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,amount):
        self._reserved_food_in_kgs +=amount
        
    def count_animals(self):
        return len(self.animals)
        
    def add_animal(self,animal):
        self.animals.append(type(animal).__name__)
        self.total_animals.setdefault(type(animal).__name__,0)
        self.total_animals[type(animal).__name__] +=1
        
    def feed(self,animal):
        animal_feed=animal._required_food_in_kgs
        if self._reserved_food_in_kgs>=animal_feed:
            animal.grow()
            self._reserved_food_in_kgs -=animal_feed
    
    
    @staticmethod
    def count_animals_in_all_zoos():
        total_no_animals=0
        for zoo in Zoo.all_zoos:
            total_no_animals +=zoo.count_animals()
        return total_no_animals

    @classmethod
    def count_animals_in_given_zoos(cls,zoos):
        no_animals=0
        for zoo in zoos:
            no_animals +=cls.count_animals(zoo)
        return no_animals


class Snake(Animal):
    @classmethod
    def make_sound(cls):
        print('Hiss Hiss')
    @classmethod
    def breathe(cls):
        print('Breathe in air')
        
    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs +=0.5
    def hunt(self,zoo):
        return zoo.animals.count('Deer')




        
'''        
class Deer:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._age_in_months = age_in_months
        
        if self._age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        
        
        self.breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        if self._required_food_in_kgs < 10:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    #Grow
    def grow(self):
        self._required_food_in_kgs += 2
        self._age_in_months += 1
    
    #sound
    def make_sound(self):
        print("Buck Buck")
    
    #breathe
    def breathe(self):
        print("Breathe in air")

class Lion:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        
        #super().__init__(age_in_months, breed, required_food_in_kgs)
        #if self._required_food_in_kgs < 10:
        #    raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
        self._age_in_months = age_in_months
        
        if self._age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        
        
        self.breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        if self._required_food_in_kgs < 10:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs += 4
        self._age_in_months += 1
        
    
    
    #sound
    def make_sound(self):
        print("Roar Roar")
        
    #breathe
    def breathe(self):
        print("Breathe in air")


class Shark:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        
        #super().__init__(age_in_months, breed, required_food_in_kgs)
        #if self._required_food_in_kgs < 10:
        #    raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
        self._age_in_months = age_in_months
        
        if self._age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        
        
        self.breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        if self._required_food_in_kgs < 10:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    
    def grow(self):
        self._required_food_in_kgs += 8
        self._age_in_months += 1
    
    
    
    #sound
    def make_sound(self):
        print('Shark Sound')
    
    #breathe
    def breathe(self):
        print("Breathe oxygen from water")
    

class GoldFish:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._age_in_months = age_in_months
        
        if self._age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        
        
        self.breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        if self._required_food_in_kgs < 0.2:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    def grow(self):
        self._required_food_in_kgs += 0.2
        self._age_in_months += 1
        
    
    
    #sound
    def make_sound(self):
        print('Hum Hum')
        
    #breathe
    def breathe(self):
        print("Breathe oxygen from water")
    


class Snake:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self._age_in_months = age_in_months
        
        if self._age_in_months != 1:
            raise ValueError('Invalid value for field age_in_months: {}'.format(self._age_in_months))
        
        
        self.breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        if self._required_food_in_kgs < 0.5:
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self._required_food_in_kgs))
    
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    def grow(self):
        self._required_food_in_kgs += 0.5
        self._age_in_months += 1
        
    
    
    #sound
    def make_sound(self):
        print('Hiss Hiss')
        
    #breathe
    def breathe(self):
        print("Breathe in air")



class Zoo:
    #GoldFish.__init__()
    def __init__(self):
        self.reserved_food_in_kgs = 0
        self.num_of_animals = []
        
    
        
    #add_food_in_kg
    def add_food_to_reserve(self, food_in_kgs):
        self.reserved_food_in_kgs += food_in_kgs
        
    #add_animals
    def count_animals(self):
        print(len(self.num_of_animals))
        
    #add_animals
    def add_animal(self, animal):
        self.num_of_animals.append(animal)
        
    def feed(self, animal):
        pass
'''