from raytracing.hittable_list import HittableList
from raytracing.sphere import Sphere
from raytracing.point import Point
from raytracing.hittable import hit_record
from raytracing.ray import Ray
from raytracing.vec3 import Vec3
from raytracing.utility import INFINITY

def test_add():
    world = HittableList(Sphere(Point(), 1))
    assert len(world._objects) == 1

def test_clear():
    world = HittableList(Sphere(Point(), 1))
    world.clear()
    assert len(world._objects) == 0

def test_hit():
    world = HittableList(Sphere(Point(0, 0, -2), 1))
    rec = hit_record()
    r = Ray(Point(), Vec3(0, 0, -1))
    result = world.hit(r, 0, INFINITY, rec)
    assert result == True and rec.p == Point(0, 0, -1) and rec.normal == Vec3(0, 0, 1) and rec.t == 1 and rec.frontface == True
