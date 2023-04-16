import sys
import json
from .hittable_list import HittableList
from .hittable import Hittable
from .sphere import Sphere
from .point import Point
from typing import TextIO

INFINITY = sys.float_info.max

def clamp(x, min_value, max_value):
    return max(min(x, max_value), min_value)

def load_world(file: TextIO):
    data = json.loads(file.read())
    world = HittableList()
    for obj in data:
        if obj["type"] == "sphere":
            world.add(Sphere(Point(obj["x"], obj["y"], obj["z"]), obj["r"]))
    return world


