from raytracing.vec3 import Vec3
from raytracing.point import Point
from raytracing.ray import Ray
from raytracing.camera import Camera

def get_ray_lower_left():
    cam = Camera()
    u = v = 0
    r = cam.get_ray(u, v)
    assert r.origin == Point() and r.direction == Vec3(-19/9, -1, -1)
