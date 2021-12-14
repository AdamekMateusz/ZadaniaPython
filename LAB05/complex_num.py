import math
from math import sqrt
class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __truediv__(self, other):
        sr, si, oreal, oimg = self.real, self.imag, other.real, other.imag # short forms
        r = float(oreal**2 + oimg**2)
        return Complex((sr*oreal+si*oimg)/r, (si*oreal-sr*oimg)/r)


    def __str__(self):
        if self.imag > 0:
            return '({} + {}j)'.format(self.real,self.imag)
        elif self.imag == 0:
            return '({})'.format(self.real)
        elif self.imag < 0:
            return '({} {}j)'.format(self.real,self.imag)
        #return '(%g, %g)' % (self.real, self.imag)


