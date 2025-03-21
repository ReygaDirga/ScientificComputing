import numpy as np

def f(x):
    return x*2

a = 2
b = 5
points = 4
width = (b - a) / (points - 1)
x = np.linspace(a, b, points)
print(x)

trapezoid = (width / 2) * (f(x[0]) + np.sum(f(2*x[1:-1])) + f(x[-1]))
print(trapezoid)