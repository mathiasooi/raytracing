from .vec3 import Vec3
from .utility import clamp
from math import sqrt

class Color(Vec3):
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0, samples = 1):
        super().__init__(e0, e1, e2)
        self._samples = samples

    def __str__(self):
        # Divide the color by the number of samples and gamma-correct for gamma=2.0.
        scale = 1.0 / self._samples
        hues = [sqrt(scale * e) for e in self._e]
        return "{} {} {}".format(*[int(256 * clamp(hue, 0, 0.999)) for hue in hues])