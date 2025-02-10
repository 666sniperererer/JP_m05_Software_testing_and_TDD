from math import sqrt

class ComplexNumber:

    #konstruktor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    #rovnost
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    #menší než
    def __lt__(self, other):
        return abs(complex(self.real,self.imag)) < abs(complex(other.real,other.imag))

    #větší než
    def __gt__(self, other):
        return abs(complex(self.real,self.imag)) > abs(complex(other.real,other.imag))

    def __repr__(self):
        return 'Complex number - ' + str(self)

    def __str__(self):
        return (f"{self.real} + {self.imag}i")

    #gettery
    @property
    def real(self):
        return self.__real
    @property
    def imag(self):
        return self.__imag

    #settery
    @real.setter
    def real(self, real):
        self.__real = real
    @imag.setter
    def imag(self, imag):
        self.__imag = imag

    #add
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    #subtract
    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)

    #multiply
    def __mul__(self, other):
        return complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    #divide
    def div(self, other):
        r = float(other.real ** 2 + other.imag ** 2)
        return complex((self.real * other.real +self.imag * other.imag) /
                       r, (self.imag * other.real -self.real * other.imag) / r)

    #conjugate
    def con(self):
        __real = self.real
        __imag = self.imag * -1
        return complex(__real,__imag)

    #absolute_value
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

if __name__ == '__main__':
    complexnumber1 = ComplexNumber(5,3)
    complexnumber2 = ComplexNumber(7,4)

    print(complexnumber1, complexnumber2)
    print(complexnumber1 == complexnumber2)
    print(complexnumber1 < complexnumber2)
    print(complexnumber1 + complexnumber2)
    print(complexnumber1 - complexnumber2)
    print(complexnumber1.real, complexnumber1.imag)
    print(abs(complexnumber1), abs(complexnumber2))
    print(complexnumber1.con(), complexnumber2.con())
    print(ComplexNumber.div(complexnumber1, complexnumber2))