# This is called vector quantization. This is done to calculate the shortest distance between 2 Values.

from numpy import argmin, sum, array, sqrt

observation = array([[112.0, 211.3]])
codes = array([[133.0, 211.1], [122.3, 144.5], [133.0, 211.1], [411.4, 122.3]])

diff = codes - observation
print(diff)

dist = sqrt(sum(diff**2))
print(f"This is the dist withwout axis=-1: {dist}")


dist = sqrt(sum(diff**2, axis=-1))
print(f"This is the dist with axis=-1: {dist}")

print(f"Lowest distance: {argmin(dist)} -> This is the class {codes[0]}")
