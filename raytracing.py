from raytracing.ppmimage import PPMImage
from raytracing.color import Color
from raytracing.ray import Ray
from raytracing.vec3 import Vec3
from raytracing.point import Point
from raytracing.hittable import Hittable, hit_record
from raytracing.hittable_list import HittableList
from raytracing.sphere import Sphere
from raytracing.camera import Camera
from raytracing.utility import clamp, INFINITY, load_world
from random import random, uniform
import sys


def ray_color(r: Ray, world: Hittable):
    rec = hit_record()
    if world.hit(r, 0, INFINITY, rec):
        return (rec.normal + Color(1, 1, 1)) * 0.5

    unit_direction = r.direction.unit_vector()
    t = (unit_direction.y() + 1) * 0.5
    return Color(1, 1, 1)*(1-t) + Color(0.5, 0.7, 1) * t

def main():
    # Image
    aspect_ratio = 16.0 / 9
    image = PPMImage(400, 225)
    # image = PPMImage(1600, 900)
    samples = 16

    # Camera
    cam = Camera()

    # World
    filename = "shapes.json"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as data:
        world = load_world(data)

    # Render
    for j in range(image.height): 
        print("Completed line: {}/{}".format(j+1, image.height))
        for i in range(image.width):
            pixel_color = Color(0, 0, 0, samples)
            for _ in range(samples):
                u = (i + random()) / (image.width - 1)
                v = (j + random()) / (image.height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world)
            pixel_color = Color(pixel_color.x(), pixel_color.y(), pixel_color.z(), samples)
            image.set_pixel(j, i, pixel_color)
    
    with open("test.ppm", "w") as fout:
        image.write_file(fout)


if __name__ == "__main__":
    main()
