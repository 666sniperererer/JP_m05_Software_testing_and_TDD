class ComplexNumber:

    #konstruktor
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    #rovnost
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    #menší než
    def __lt__(self, other):
        pass

    #větší než
    def __gt__(self, other):
        pass

    def __repr__(self):
        return 'Complex number - ' + str(self)

    def __str__(self):
        return (self.real, self.imag)

    #gettery
    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    #settery
    def set_real(self):
        self.real = real

    def set_imag(self):
        self.imag = imag

    #add
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    #subtract
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    #multiply
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    #divide
    def __div__(self, other):
        r = float(other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real +self.imag * other.imag) /
                       r, (self.imag * other.real -self.real * other.imag) / r)

    #conjugate
    def __con__(self, other):
        pass

    #absolute_value
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)