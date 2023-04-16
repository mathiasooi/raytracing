from .ray import Ray
from .point import Point
from .vec3 import Vec3
from abc import *

class hit_record:
    def __init__(self):
        self._p = None
        self._normal = None
        self._t = None
        self._frontface = False
    def set_face_normal(self, r: Ray, outward_normal: Vec3):
        self._frontface = Vec3.dot(r.direction, outward_normal) < 0
        self._normal = outward_normal if self._frontface else -outward_normal
    @property
    def p(self):
        return self._p
    @p.setter
    def p(self, newp):
        self._p = newp
    @property
    def normal(self):
        return self._normal
    @normal.setter
    def normal(self, newnormal):
        self._normal = newnormal
    @property
    def t(self):
        return self._t
    @t.setter
    def t(self, newt):
        self._t = newt
    @property
    def frontface(self):
        return self._frontface
    @frontface.setter
    def frontface(self, newfrontface):
        self._frontface = newfrontface
    
class Hittable(ABC):
    def hit(r: Ray, t_min: float, t_max: float, rec: hit_record):
        pass
