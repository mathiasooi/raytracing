from raytracing.ppmimage import PPMImage
from raytracing.color import Color
from raytracing.ray import Ray
from raytracing.vec3 import Vec3
from raytracing.point import Point
from raytracing.hittable import Hittable, hit_record
from raytracing.hittable_list import HittableList
from raytracing.sphere import Sphere
from raytracing.camera import Camera
from raytracing.utility import INFINITY
from random import random
from typing import TextIO
import json
import sys

def load_scene(file: TextIO):
    data = json.loads(file.read())

    # Image
    image = PPMImage(data["image"]["width"], data["image"]["height"])

    # Camera
    cam = Camera()

    # World
    objects = HittableList()
    for obj in data["objects"]:
        if obj["type"] == "sphere":
            objects.add(Sphere(Point(*obj["position"]), obj["radius"]))

    return image, cam, objects, data["samples"]

def ray_color(r: Ray, objects: Hittable, depth):
    rec = hit_record()

    if depth < 0: return Color()

    if objects.hit(r, 0.001, INFINITY, rec):
        target = rec.p + rec.normal + Vec3.random_in_hemisphere(rec.normal)
        return ray_color(Ray(rec.p, target - rec.p), objects, depth - 1) * 0.5

    unit_direction = r.direction.unit_vector()
    t = (unit_direction.y() + 1) * 0.5
    return Color(1, 1, 1)*(1-t) + Color(0.5, 0.7, 1) * t

def main():
    # Load scene
    filename = "scene.json"
    if len(sys.argv) > 1: filename = sys.argv[1]
    with open(filename) as data:
        image, cam, objects, samples = load_scene(data)
    max_depth = 50

    # Render
    for j in range(image.height): 
        print("Completed line: {}/{}".format(j+1, image.height))
        for i in range(image.width):
            pixel_color = Color(0, 0, 0, samples)
            for _ in range(samples):
                u = (i + random()) / (image.width - 1)
                v = (j + random()) / (image.height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, objects, max_depth)
            pixel_color = Color(pixel_color.x(), pixel_color.y(), pixel_color.z(), samples)
            image.set_pixel(j, i, pixel_color)
    
    with open("test.ppm", "w") as fout:
        image.write_file(fout)


if __name__ == "__main__":
    main()
