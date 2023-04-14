from .color import Color

class PPMImage:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._image = [[Color() for _ in range(width)] for _ in range(height)]
    def set_pixel(self, x, y, color):
        self._image[x][y] = color
    def write_string(self):
        s = "P3\n{} {}\n255\n".format(self.width, self.height)
        for j in range(self.height):
            for i in range(self.width):
                s += str(self._image[j][i]) + "\n"
        return s
    def write_file(self, filename: str):
        with open(filename, "w") as fout:
            fout.write(self.write_string())
    
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self, newwidth):
        self._width = newwidth
    @height.setter
    def height(self, newheight):
        self._height = newheight