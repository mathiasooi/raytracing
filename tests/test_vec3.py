from raytracing.vec3 import Vec3
from math import sqrt
import pytest

def test_default_init():
    assert Vec3() == Vec3(0, 0, 0)

def test_scalar_mul_zero_prop():
    assert Vec3() == Vec3(1, 2, 2) * 0

def test_zero_length():
    assert Vec3().length() == 0

def test_zero_add():
    assert Vec3() + Vec3(1, 2, 2) == Vec3(1, 2, 2)

def test_scalar_mul_lhs():
    assert Vec3(1, 2, 2) * 2 == Vec3(2, 4, 4)

def test_scalar_mul_rhs():
    assert 2 * Vec3(1, 2, 2) == Vec3(2, 4, 4)

def test_scalar_div():
    assert Vec3(2, 4, 4) / 2 == Vec3(1, 2, 2)

def test_dot_ii():
    assert Vec3.dot(Vec3(1, 0, 0), Vec3(1, 0, 0)) == pytest.approx(1)

def test_dot_jj():
    assert Vec3.dot(Vec3(0, 1, 0), Vec3(0, 1, 0)) == pytest.approx(1)

def test_dot_kk():
    assert Vec3.dot(Vec3(0, 0, 1), Vec3(0, 0, 1)) == pytest.approx(1)

def test_dot_ij():
    assert Vec3.dot(Vec3(1, 0, 0), Vec3(0, 1, 0)) == pytest.approx(0)

def test_dot_ik():
    assert Vec3.dot(Vec3(1, 0, 0), Vec3(0, 0, 1)) == pytest.approx(0)

def test_dot_jk():
    assert Vec3.dot(Vec3(0, 1, 0), Vec3(0, 0, 1)) == pytest.approx(0)

def test_len():
    assert Vec3(1, 2, 2).length() == pytest.approx(3)

def test_cross():
    # axb == -bxa
    assert Vec3.cross(Vec3(1, 2, 2), Vec3(2, 7, 8)) == Vec3.cross(-Vec3(2, 7, 8), Vec3(1, 2, 2))