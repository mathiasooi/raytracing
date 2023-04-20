import sys

INFINITY = sys.float_info.max

def clamp(x, min_value, max_value):
    return max(min(x, max_value), min_value)




