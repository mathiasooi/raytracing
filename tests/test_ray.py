from raytracing.ray import Ray
from raytracing.point import Point
from raytracing.vec3 import Vec3

def test_init():
    p = Point()
    d = Vec3(1, 0, 0)
    r = Ray(p, d)
    assert r.origin == p and r.direction == d

def test_at():
    p = Point()
    d = Vec3(1, 0, 0)
    t = 0.5
    r = Ray(p, d)
    assert r.at(t) == p + d * t