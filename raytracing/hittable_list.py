from .hittable import Hittable, hit_record
from .ray import Ray

class HittableList(Hittable):
    def __init__(self, obj: Hittable = None):
        self._objects = []
        if obj is not None: self.add(obj)
    def clear(self):
        self._objects.clear()
    def add(self, obj):
        self._objects.append(obj)
    def hit(self, r: Ray, t_min: float, t_max: float, rec: hit_record):
        hit_anything = False
        closest = t_max
        
        for obj in self._objects:
            if obj.hit(r, t_min, closest, rec):
                hit_anything = True
                closest = rec.t
        
        return hit_anything
