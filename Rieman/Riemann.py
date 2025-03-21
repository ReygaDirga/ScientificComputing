import numpy as np

def f(x):
    return x*2

a = 2
b = 5
points = 4
width = (b - a) / (points - 1)
x = np.linspace(a, b, points)
print(x)

# Left Riemann
leftRiemann = width * np.sum(f(x[:-1]))
print(leftRiemann)

# Right Riemann
rightRiemann = width * np.sum(f(x[1:]))
print(rightRiemann)

#midpoint Riemann
mid = (x[:-1] + x[1:]) / 2
midpointRiemann = width * np.sum(f(mid))
print(midpointRiemann)