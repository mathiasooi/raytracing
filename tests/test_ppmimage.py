from raytracing.ppmimage import PPMImage
from raytracing.color import Color
from io import StringIO

def test_init():
    ppmimage = PPMImage(256, 256)
    assert ppmimage.width == 256 and ppmimage.height == 256

def test_set_pixel():
    ppmimage = PPMImage(256, 256)
    r, g, b = 0.25, 0.83, 0.99
    x, y = 2, 5
    color = Color(r, g, b)
    ppmimage.set_pixel(x, y, color)
    assert ppmimage._image[x][y] == color

def test_write_string():
    ppmimage = PPMImage(2, 3)
    s = ppmimage.write_string()
    expected_string = "P3\n{} {}\n255\n".format(ppmimage.width, ppmimage.height)
    for j in range(ppmimage.height):
        for i in range(ppmimage.width):
            expected_string += str(ppmimage._image[j][i]) + "\n"
    assert s == expected_string

def test_write_file():
    outfile = StringIO()
    ppmimage = PPMImage(256, 256)
    ppmimage.write_file(outfile)
    outfile.seek(0)
    content = outfile.read()
    expected_content = ppmimage.write_string()
    assert content == expected_content
