from .vec3 import Vec3
from .point import Point

class Ray:
    def __init__(self, origin: Point, direction: Vec3):
        self._origin = origin
        self._direction = direction
    def at(self, t: float):
        return self._origin + self._direction * t
    @property
    def origin(self):
        return self._origin
    @property
    def direction(self):
        return self._direction
    @origin.setter
    def origin(self, neworigin):
        self._origin = neworigin
    @direction.setter
    def direction(self, newdirection):
        self._direction = newdirection