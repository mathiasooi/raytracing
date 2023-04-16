from .point import Point
from .vec3 import Vec3
from .ray import Ray

class Camera:
    def __init__(self):
        self._aspect_ratio = 16 / 9
        self._viewport_height = 2.0
        self._viewport_width = self._aspect_ratio * self._viewport_height
        self._focal_length = 1.0

        self._origin = Point()
        self._horizontal = Vec3(self._viewport_width, 0, 0)
        self._vertical = Vec3(0, self._viewport_height, 0)
        self._lower_left_corner = self._origin - self._horizontal / 2 - self._vertical / 2 - Vec3(0, 0, self._focal_length)
    def get_ray(self, u, v):
        return Ray(self._origin, self._lower_left_corner + self._horizontal * u + self._vertical * v - self._origin)