from .vec3 import Vec3
from .utility import clamp

class Color(Vec3):
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0, samples = 1):
        super().__init__(e0, e1, e2)
        self._samples = samples

    def __str__(self):
        return "{} {} {}".format(*[int(255.999 * clamp(hue * 1.0 / self._samples, 0, 0.999)) for hue in self._e])