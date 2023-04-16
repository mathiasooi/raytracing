from raytracing.utility import clamp

def test_clamp_over():
    x = 10
    a, b = 3, 7
    assert clamp(x, a, b) == 7

def test_clamp_under():
    x = -1
    a, b = 18, 19
    assert clamp(x, a, b) == 18

def test_clamp_inside():
    x = 15
    a, b = 0, 20
    assert clamp(x, a, b) == 15
