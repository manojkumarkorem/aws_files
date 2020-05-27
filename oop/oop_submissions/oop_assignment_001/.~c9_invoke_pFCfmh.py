class Car:
    #initialization
    def __init__(self, max_speed, acceleration, tyre_friction, color = None):
        self.color =  color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self._current_speed = 0
        self.is_engine_stared = False
    
    
    @property
    def current_speed(self):
        return self._current_speed
    
    
    
    
    

    
    #Start_engine    
    def start_engine(self):
        self.is_engine_stared = True
        
    #accelerate
    def accelerate(self):
        if self.is_engine_stared == False:
            print('Start the engine to accelerate')
        if self.is_engine_stared == True:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                Temp = self.max_speed - self._current_speed
                self._current_speed += Temp
    
    
                
    #applying_break
    def apply_brakes(self):
        if self.is_engine_stared == True:
            self._current_speed -= self._tyre_friction
    
    #sound_horn
    def sound_horn(self):
        if self.is_engine_stared == False:
            print('Start the engine to sound_horn')
        if self.is_engine_stared == True:
            print('Beep Beep')
            
    #stop_engine
    def stop_engine(self):
        self.is_engine_stared = False
        self._current_speed = 0