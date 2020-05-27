#Car_Class
class Car:
    #initialization
    def __init__(self, max_speed, acceleration, tyre_friction, color = None):
        self._max_speed = max_speed
        self._color =  color
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._current_speed = 0
        self._is_engine_started = False
        
        #raise_error_for_max_speed
        if self._max_speed < 0:
            raise ValueError('Invalid value for max_speed')
        
        #raise_error_for_acceleration
        if self._acceleration < 0:
            raise ValueError('Invalid value for acceleration')
        
        #raise_error_for_tyre_friction
        if self._tyre_friction < 0:
            raise ValueError('Invalid value for tyre_friction')
        
        
    
    @property
    def color(self):
        return self._color
        
    @property
    def current_speed(self):
        return self._current_speed
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def acceleration(self):
        return self._acceleration
    
    @property
    def tyre_friction(self):
        return self._tyre_friction
    
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    
    #Start_engine    
    def start_engine(self):
        self._is_engine_started = True
        
    #accelerate
    def accelerate(self):
        if self._is_engine_started == False:
            print('Start the engine to accelerate')
        if self._is_engine_started == True:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                Temp = self._max_speed - self._current_speed
                self._current_speed += Temp
    
    
    #applying_break
    def apply_brakes(self):
        if self._is_engine_started == True:
            if self._current_speed - self._tyre_friction >= 0:
                self._current_speed -= self._tyre_friction
            else:
                self._current_speed = 0
    
    #sound_horn
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Beep Beep')
        else:
            print('Start the engine to sound_horn')
    #stop_engine
    def stop_engine(self):
        self._is_engine_started = False









#Truck_Class
class Truck(Car):
    #initialization
    def __init__(self, max_speed = 1, acceleration = 1, tyre_friction = 1, max_cargo_weight = None, color = None):
        super().__init__(max_speed, acceleration, tyre_friction, color)
        self._max_cargo_weight = max_cargo_weight
        self._current_load_in_truck = 0
        
    
    
        #raise_error_for_max_cargo_weight
        if self._max_cargo_weight < 0:
            raise ValueError('Invalid value for max_cargo_weight')
        try:
            self._max_cargo_weight > 0
        except:
            raise ValueError('Invalid value for max_cargo_weight')
        
        
        
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    @property
    def current_load_in_truck(self):
        return self._current_load_in_truck
    
    
    
    #-----
    #loading_truck
    def load(self, weight_in):
        #raise_error_for_max_speed
        if weight_in < 0:
            raise ValueError('Invalid value for cargo_weight')
        '''try:
            weight_in > 0
        except:
            raise ValueError('Invalid value for cargo_weight')'''
        
        
        
        if (self._is_engine_started == False and self._current_speed == 0) or (self._is_engine_started == True and self._current_speed == 0):
            if self._current_load_in_truck + weight_in <= self._max_cargo_weight:
                self._current_load_in_truck += weight_in
            else:
                print('Cannot load cargo more than max limit: {}'.format(self._max_cargo_weight))
        else:
            print('Cannot load cargo during motion')
    
    
    #unloading_truck
    def unload(self, weight_de):
        #raise_error_for_max_speed
        if weight_de < 0:
            raise ValueError('Invalid value for cargo_weight')
        '''try:
            weight_de > 0
        except:
            raise ValueError('Invalid value for cargo_weight')'''
        
        
        if self._is_engine_started == False or (self._is_engine_started == True and self._current_speed == 0):
            if weight_de <= self._current_load_in_truck:
                if self._current_load_in_truck - weight_de >= 0:
                    self._current_load_in_truck -= weight_de
                else:
                    self._current_load_in_truck = 0
        else:
            print('Cannot unload cargo during motion')
    
    
        
    #sound_horn
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')