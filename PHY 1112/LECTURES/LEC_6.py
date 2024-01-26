class MyComplex:
    def __init__(self, real, imag):
        '''
        (num, num) -> (None)
        Initializes the real and imaginary parts of the complex number.
        '''
        self.real = real
        self.imag = imag        

    def conjugate(self):
        '''
        () -> (MyComplex)
        Returns the conjugate of the complex number.
        '''
        return MyComplex(self.real, -self.imag)
    
    def __str__(self):
        '''
        () -> (str)
        Returns the string representation of the complex number.
        '''
        if self.imag < 0:
            return str(self.real) + " - " + str(-self.imag) + "i"
        else:
            return str(self.real) + " + " + str(self.imag) + "i"
