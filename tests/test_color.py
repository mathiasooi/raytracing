from raytracing.color import Color

def test_default_init():
    assert Color() == Color(0, 0, 0)

def test_str():
    assert str(Color(1, 0.5, 0)) == "255 127 0"