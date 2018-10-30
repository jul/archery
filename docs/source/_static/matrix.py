#!/usr/bin/env python3
from archery import mdict, vdict
from math import pi, cos, sin, acos

class Matrix(mdict):
    def __call__(self, other):
        other = other.copy()
        res= vdict()
        for (src, dst), functor in self.items():
            res += mdict({ dst: functor(other[src])})
        return res


theta = pi/6

u = mdict(x=1, y=2)
v = mdict(x=1, y=0)
alien = vdict(x=u, y=v)

def rotation_maker(theta):
    """"Matrix takes as key (SRC, DST) (which is the opposite of "actual notation")
    """
    return Matrix({
        ("x", "x") : lambda v:1.0 *  v * cos(theta),
        ("y", "x") : lambda v:1.0 * -v * sin(theta),
        ("x", "y") : lambda v:1.0 *  v * sin(theta),
        ("y", "y") : lambda v:1.0 *  v * cos(theta)
    })

rotation = rotation_maker(pi/6)

print(u)
# OUT:{'x': 1, 'y': 2}
print(rotation(u))
# OUT:{'x': -0.13397459621556118, 'y': 2.232050807568877}
print("*" * 80)
# OUT:********************************************************************************
print(v)
# OUT:{'x': 1, 'y': 0}
print(rotation(v))
# OUT:{'x': 0.8660254037844387, 'y': 0.49999999999999994}
print(acos(vdict(v).cos(vdict(rotation(v))))/2 / pi * 360)
# OUT:29.999999999999993
print(acos(vdict(v).cos(vdict(rotation_maker(pi/3)(v))))/2 / pi * 360)
# OUT:60.0
print(acos(vdict(v).cos(vdict(rotation_maker(pi/5)(v))))/2 / pi * 360)
# OUT:36.0
print(alien)
print(acos(alien.cos(rotation_maker(pi/4)(alien)))/2 / pi * 360)
print(alien)
print(rotation_maker(pi/4)(alien))
print(alien)
print(u)
print(v)

