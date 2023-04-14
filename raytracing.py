from raytracing.ppmimage import PPMImage
from raytracing.color import Color
from raytracing.ray import Ray
from raytracing.vec3 import Vec3
from raytracing.point import Point

def ray_color(r: Ray):
    unit_direction = r.direction.unit_vector()
    t = (unit_direction.y() + 1) * 0.5
    return Color(1, 1, 1)*(1-t) + Color(0.5, 0.7, 1) * t

def main():
    # Image
    aspect_ratio = 16.0 / 9
    image = PPMImage(400, 225)

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Point(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - Vec3(0, 0, focal_length)

    # Render
    for j in range(image.height):
        for i in range(image.width):
            u = i * 1.0 / (image.width - 1)
            v = j * 1.0 / (image.height - 1)
            r = Ray(origin, - origin + lower_left_corner + horizontal*u + vertical*v)
            pixel_color = ray_color(r)
            pixel_color = Color(pixel_color.x(), pixel_color.y(), pixel_color.z())
            image.set_pixel(j, i, pixel_color)
    
    with open("blue_white_gradient.ppm", "w") as fout:
        image.write_file(fout)


if __name__ == "__main__":
    main()
    