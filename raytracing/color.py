from .vec3 import Vec3

class Color(Vec3):
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0):
        super().__init__(e0, e1, e2)
    def __str__(self):
        return "{} {} {}".format(*[int(255.999 * hue) for hue in self._e])