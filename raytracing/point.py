from .vec3 import Vec3

class Point(Vec3):
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0):
        super().__init__(e0, e1, e2)