from .hittable import Hittable, hit_record
from .vec3 import Vec3
from .point import Point
from .ray import Ray
from math import sqrt

class Sphere(Hittable):
    def __init__(self, center: Point, radius: float):
        self._c = center
        self._r = radius
    
    def hit(self, r: Ray, t_min: float, t_max: float, rec: hit_record):
        oc = r.origin - self._c
        a = r.direction.length_squared()
        half_b = Vec3.dot(oc, r.direction)
        c = oc.length_squared() - self._r * self._r
        d = half_b * half_b - a*c
        if d < 0: return False
        sqrtd = sqrt(d)

        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self._c) / self._r
        rec.set_face_normal(r, outward_normal)
        return True