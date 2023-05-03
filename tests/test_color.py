from raytracing.color import Color
import pytest

def test_default_init():
    assert Color() == Color(0, 0, 0)

def test_str():
    assert str(Color(1, 0.5, 0)) == "255 181 0"

def test_str_with_clamping():
    c = Color(2, 0.5, -1)
    with pytest.raises(ValueError):
        str(c)


def test_str_with_samples():
    c = Color(2, 1, 0, 2)
    assert str(c) == "255 181 0"
