"""
Polar Coordinates

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number z is completely determined by its real part x and imaginary part y. Here, j is the imaginary unit.

A polar coordinate (r, φ) is completely determined by modulus r and phase angle φ.

If we convert complex number z to its polar coordinate, we find:
- r: Distance from z to origin, i.e., √(x² + y²)
- φ: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.

This tool returns the phase of complex number z (also known as the argument of z).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931

This tool returns the modulus (absolute value) of complex number z.

>>> abs(complex(-1.0, 0.0))
1.0

Task

You are given a complex z. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number z. Note: complex() function can be used in Python to convert the input as a complex number.

Constraints

Given number is a valid complex number.

Output Format

Output two lines:
- The first line should contain the value of r.
- The second line should contain the value of φ.

Sample Input

1+2j

Sample Output

2.23606797749979
1.1071487177940904
"""

import math

def polarcoords(z):
    x = z.real
    y = z.imag
    r = math.sqrt(x**2 + y**2)
    phi = math.atan(y/x)
    print(r)
    print(phi/math.pi)


z = complex(1,3)
polarcoords(z)