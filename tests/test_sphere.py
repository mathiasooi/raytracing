from raytracing.sphere import Sphere
from raytracing.hittable import hit_record
from raytracing.ray import Ray
from raytracing.point import Point
from raytracing.vec3 import Vec3
from raytracing.utility import INFINITY

def test_init():
    s = Sphere(Point(), 5)
    assert s._c == Point() and s._r == 5

def test_hit_false():
    s = Sphere(Point(0, 0, -2), 1)
    rec = hit_record()
    r = Ray(Point(), Vec3(0, 0, 1))
    result = s.hit(r, 0, INFINITY, rec)
    assert result == False

def test_hit_true():
    s = Sphere(Point(0, 0, -2), 1)
    rec = hit_record()
    r = Ray(Point(), Vec3(0, 0, -1))
    result = s.hit(r, 0, INFINITY, rec)
    assert result == True and rec.p == Point(0, 0, -1) and rec.normal == Vec3(0, 0, 1) and rec.t == 1 and rec.frontface == True


