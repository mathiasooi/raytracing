from raytracing.vec3 import Vec3
from math import sqrt
import random

# random.seed(0)

def get_random_double():
    return random.random() * 10 ** random.randint(0, 9)

def gen_triplets():
    # Generates 100 random triplets of doubles (x, y, z) ranging from [0, 10^9]
    # Include edge cases like (0, 0, 0)
    for _ in range(100):
        yield tuple([get_random_double() for _ in range(3)])
    yield (0, 0, 0)

def test_deafult_init():
    assert Vec3() == Vec3(0, 0, 0)

def test_length():
    actual = []
    expected = []
    for x, y, z in gen_triplets():
        actual.append(Vec3(x, y, z).length())
        expected.append(sqrt(x*x + y*y + z*z))
    assert actual == expected

def test_length_sqaured():
    actual = []
    expected = []
    for x, y, z in gen_triplets():
        actual.append(Vec3(x, y, z).length_squared())
        expected.append(x*x + y*y + z*z)
    assert actual == expected

def test_unit_vector():
    actual = []
    expected = []
    for x, y, z in gen_triplets():
        length = sqrt(x*x + y*y + z*z)
        if length == 0:
            # No unit vector exists for a zero vector
            continue
        actual.append(Vec3(x, y, z).unit_vector())
        expected.append(Vec3(x/length, y/length, z/length))
    assert actual == expected

def test_dot():
    actual = []
    expected = []
    for u, v in zip(gen_triplets(), gen_triplets()):
        actual.append(Vec3.dot(Vec3(*u), Vec3(*v)))
        expected.append(sum(u[i] + v[i] for i in range(3)))
    assert actual == expected

def test_cross():
    actual = []
    expected = []
    for u, v in zip(gen_triplets(), gen_triplets()):
        actual.append(Vec3.cross(Vec3(*u), Vec3(*v)))
        x = u[1]*v[2] - u[2]*v[1]
        y = u[2]*v[0] - u[0]*v[2]
        z = u[0]*v[1] - u[1]*v[0]
        expected.append(Vec3(x, y, z))
    assert actual == expected

def test_str():
    actual = []
    expected = []
    for u in gen_triplets():
        actual.append(str(Vec3(*u)))
        expected.append("<{} {} {}>".format(*u))
    assert actual == expected

def test_getitem():
    actual = []
    expected = []
    for u in gen_triplets():
        v = Vec3(*u)
        for i in range(3):
            actual.append(v[i])
            expected.append(u[i])
    assert actual == expected

def test_setitem():
    actual = []
    expected = []
    for u in gen_triplets():
        v = Vec3(*u)
        t = [*u]
        for i in range(3):
            r = get_random_double()
            v[i] = r
            t[i] = r
        actual.append(v)
        expected.append(Vec3(*t))
    assert actual == expected

def test_negation():
    actual = []
    expected = []
    for x, y, z in gen_triplets():
        v = Vec3(x, y, z)
        actual.append(-v)
        x = -x
        y = -y
        z = -z
        expected.append(Vec3(x, y, z))
    assert actual == expected

def test_addition():
    actual = []
    expected = []
    for u, v in zip(gen_triplets(), gen_triplets()):
        actual.append(Vec3(*u) + Vec3(*v))
        expected.append(Vec3(*[u[i] + v[i] for i in range(3)]))
    assert actual == expected

def test_addition_assignment():
    actual = []
    expected = []
    for u, v in zip(gen_triplets(), gen_triplets()):
        t = Vec3(*u)
        t += Vec3(*v)
        actual.append(t)
        expected.append(Vec3(*[u[i] + v[i] for i in range(3)]))
    assert actual == expected

def test_subtraction():
    actual = []
    expected = []
    for u, v in zip(gen_triplets(), gen_triplets()):
        actual.append(Vec3(*u) - Vec3(*v))
        expected.append(Vec3(*[u[i] - v[i] for i in range(3)]))
    assert actual == expected

def test_subtraction_assignment():
    actual = []
    expected = []
    for u, v in zip(gen_triplets(), gen_triplets()):
        t = Vec3(*u)
        t -= Vec3(*v)
        actual.append(t)
        expected.append(Vec3(*[u[i] - v[i] for i in range(3)]))
    assert actual == expected

def test_scalar_multiplicaiton():
    actual = []
    expected = []
    for u in gen_triplets():
        r = get_random_double()
        actual.append(Vec3(*u) * r)
        expected.append(Vec3(*[u[i] * r for i in range(3)]))
    assert actual == expected

def test_scalar_multiplicaiton_assignment():
    actual = []
    expected = []
    for u in gen_triplets():
        r = get_random_double()
        t = Vec3(*u)
        t *= r
        actual.append(t)
        expected.append(Vec3(*[u[i] * r for i in range(3)]))
    assert actual == expected

def test_scalar_division():
    actual = []
    expected = []
    for u in gen_triplets():
        r = get_random_double()
        if r == 0:
            # should not divide by 0
            continue
        actual.append(Vec3(*u) / r)
        expected.append(Vec3(*[u[i] / r for i in range(3)]))
    assert actual == expected

def test_scalar_division_assignment():
    actual = []
    expected = []
    for u in gen_triplets():
        r = get_random_double()
        if r == 0:
            # should not divide by 0
            continue
        t = Vec3(*u)
        t /= r
        actual.append(t)
        expected.append(Vec3(*[u[i] / r for i in range(3)]))
    assert actual == expected

def test_equality_operator():
    assert Vec3(1, 2, 3) == Vec3(1, 2, 3)