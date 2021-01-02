'''
Attractor Functions for Chaos Theory
'''

# Imports
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

# Attractor Functions
def Deriv_Lorenz(pt, t0, sigma=10, beta=8/3, rho=28):
    """Compute the time-derivative of a Lorentz system."""
    """
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    sigma = 10, beta = 8/3, rho = 28

    timeInterval = [0, 4]
    GenerationLimits = [(-15, 15), (-15, 15), (-15, 15)]
    plotLims = [(-30, 30), (-30, 30), (0, 50)]
    speedUpFactor = 2
    """
    x, y, z = pt

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return [dx, dy, dz]

def Deriv_Aizawa(pt, t0, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
    """Compute the time-derivative of a Aizawa system."""
    """
    dx = (z-b) * x - d*y
    dy = d * x + (z-b) * y
    dz = c + a*z - z**3 /3 - x**2 + f * z * x**3

    a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1

    timeInterval = [0, 10]
    GenerationLimits = [(-0.01, -0.01), (-0.01, 0.01), (-0.01, 0.01)]
    plotLims = [(-1.5, 1.5), (-1.5, 1.5), (-0.5, 1.5)]
    speedUpFactor = 2
    """
    x, y, z = pt

    dx = ((z-b)*x) - d*y
    dy = d*x + ((z-b)*y)
    dz = c + a*z - ((z**3)/3) - (x**2) + f*z*(x**3)

    return [dx, dy, dz]

def Deriv_NewtonLeipnik(pt, t0, a=0.4, b=0.175):
    """Compute the time-derivative of a Newton-Leipnik system."""
    """
    dx = -a*x + y + 10*y*z
    dy = -x - 0.4*y + 5*x*z
    dz = b*z - 5*x*y

    a = 0.4, b = 0.175
    """
    x, y, z = pt

    dx = -a*x + y + 10*y*z
    dy = -x - 0.4*y + 5*x*z
    dz = b*z - 5*x*y

    return [dx, dy, dz]

def Deriv_NewtonLeipnik(pt, t0, p1=1.24, p2=1.1, r=4.4, s=3.21):
    """Compute the time-derivative of a 3-Cell CNN system."""
    """
    dx = -x + p1*h1 - s*h2 - s*h3
    dy = -y - s*h1 + p2*h2 - r*h3
    dz = -z - s*h1 + r*h2 + h3

    h1 = (1/2)*(|x+1| - |x-1|)
    h2 = (1/2)*(|y+1| - |y-1|)
    h3 = (1/2)*(|z+1| - |z-1|)
    p1 = 1.24, p2 = 1.1, r = 4.4, s = 3.21
    """
    x, y, z = pt

    h1 = (1/2)*(abs(x+1) - abs(x-1))
    h2 = (1/2)*(abs(y+1) - abs(y-1))
    h3 = (1/2)*(abs(z+1) - abs(z-1))

    dx = -x + p1*h1 - s*h2 - s*h3
    dy = -y - s*h1 + p2*h2 - r*h3
    dz = -z - s*h1 + r*h2 + h3

    return [dx, dy, dz]