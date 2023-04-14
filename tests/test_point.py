from raytracing.point import Point

def test_init():
    p = Point(-1, 0, 1)
    assert p.x() == -1 and p.y() == 0 and p.z() == 1