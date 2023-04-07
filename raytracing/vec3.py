from math import sqrt

class Vec3:
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0):
        self._e = [e0, e1, e2]
    def x(self): return self._e[0]
    def y(self): return self._e[1]
    def z(self): return self._e[2]
    def length(self): 
        return sqrt(self.length_squared())
    def length_squared(self):
        return sum(self._e[i] * self._e[i] for i in range(3))
    def unit_vector(self):
        return self / self.length()
    @staticmethod
    def dot(u1, u2):
        return sum(u1[i] + u2[i] for i in range(3))
    @staticmethod
    def cross(u1, u2):
        return Vec3(u1[1]*u2[2] - u1[2]*u2[1],
                    u1[2]*u2[0] - u1[0]*u2[2],
                    u1[0]*u2[1] - u1[1]*u2[0])
    def __str__(self): 
        return "<{} {} {}>".format(*self._e)
    def __repr__(self): 
        return "<{} {} {}>".format(*self._e)
    def __getitem__(self, key): 
        return self._e[key]
    def __setitem__(self, key, value):
        self._e[key] = value
    def __neg__(self):
        return Vec3(*[-self._e[i] for i in range(3)])
    def __add__(self, other): 
        return Vec3(*[self._e[i] + other[i] for i in range(3)])
    def __iadd__(self, other): 
        for i in range(3):
            self._e[i] += other[i]
        return self
    def __sub__(self, other): 
        return Vec3(*[self._e[i] - other[i] for i in range(3)])
    def __isub__(self, other): 
        for i in range(3):
            self._e[i] -= other[i]
        return self
    def __mul__(self, t):
        """Scalar multiplication"""
        return Vec3(*[self._e[i] * t for i in range(3)])
    def __imul__(self, t):
        for i in range(3):
            self._e[i] *= t
        return self
    def __truediv__(self, t):
        """Scalar division"""
        return Vec3(*[self._e[i] / t for i in range(3)])
    def __itruediv__(self, t):
        for i in range(3):
            self._e[i] /= t
        return self
    def __eq__(self, other):
        return all(self._e[i] == other[i] for i in range(3))