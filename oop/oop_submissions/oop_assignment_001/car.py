#'''
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
        else:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                '''Temp = self._max_speed - self._current_speed
                self._current_speed += Temp'''
                self._current_speed=self._max_speed
    
    
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
        #self._current_speed = 0
#'''        