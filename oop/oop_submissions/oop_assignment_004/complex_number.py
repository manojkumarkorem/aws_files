class ComplexNumber:
    def __init__(self, real = 0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary
        
        #raising_error_for
        if type(self.real) == str and type(self.imaginary) == int:
            raise ValueError('Invalid value for real part')
        elif type(self.real) == int and type(self.imaginary) == str:
            raise ValueError('Invalid value for imaginary part')
        elif type(self.real) == str and type(self.imaginary) == str:
            raise ValueError('Invalid value for real and imaginary part')

        self.Temp = complex(self.real, self.imaginary)
        self.real_part = self.Temp.real
        self.imaginary_part = self.Temp.imag
    
    #string_format
    def __str__(self):
        if self.imaginary >= 0:
            return '{}+{}i'.format(self.real,self.imaginary)
        else:
            return '{}{}i'.format(self.real,self.imaginary)

    
    #cojugate
    def conjugate(self):
        '''
        if self.imaginary <= 0:
             return '{}+{}i'.format(self.real, -(self.imaginary))
        else:
            return '{}{}i'.format(self.real, -(self.imaginary))
        '''
        return ComplexNumber(self.real, -self.imaginary)


    #addition
    def __add__(self, other):
        self.real = self.real + other.real
        self.imaginary = self.imaginary + other.imaginary
        return ComplexNumber(self.real, self.imaginary)
    
    #subtraction
    def __sub__(self, other):
        self.real = self.real - other.real
        self.imaginary = self.imaginary - other.imaginary
        return ComplexNumber(self.real, self.imaginary)
        
    #multiplication
    def __mul__(self,other):
        self.real = int(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part)
        self.imaginary = int(self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
        return ComplexNumber(self.real, self.imaginary)
    
    #division
    def __truediv__(self, other):
        Conjugate = other.conjugate()
        self_ = self * Conjugate
        other_ = other * Conjugate
        den = other_.real
        return ComplexNumber(self_.real / den, self_.imaginary / den)

    
    #absolute
    def __abs__(self):
        from math import sqrt
        return round(sqrt(self.real ** 2 + self.imaginary ** 2), 3)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
'''
    #equal_or_not
    def __eq__(self,other):
        self.add = self.real + self.imaginary
        return complex_number1.add == complex_number2.add
'''