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
    Lorenz Attractor Link: https://www.youtube.com/watch?v=VjP90rwpBwU

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    sigma = 10, beta = 8/3, rho = 28

    timeInterval = [0, 4]
    AttractorFunc = AttractorFunctions.Deriv_Lorenz
    saveName = "LorenzAttractor"
    GenerationLimits = [(-15, 15), (-15, 15), (-15, 15)]
    plotLims = [(-30, 30), (-30, 30), (0, 55)]
    speedUpFactor = 2

    frames = 250
    """
    x, y, z = pt

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return [dx, dy, dz]

def Deriv_Aizawa(pt, t0, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
    """Compute the time-derivative of a Aizawa system."""
    """
    Aizawa Attractor Link: https://www.youtube.com/watch?v=RBqbQUu-p00

    dx = (z-b) * x - d*y
    dy = d * x + (z-b) * y
    dz = c + a*z - z**3 /3 - x**2 + f * z * x**3

    a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1

    timeInterval = [0, 10]
    AttractorFunc = AttractorFunctions.Deriv_Aizawa
    saveName = "AizawaAttractor"
    GenerationLimits = [(-0.01, -0.01), (-0.01, 0.01), (-0.01, 0.01)]
    plotLims = [(-1.5, 1.5), (-1.5, 1.5), (-0.5, 1.5)]
    speedUpFactor = 2

    frames = 250
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

    timeInterval = [0, 60]
    AttractorFunc = AttractorFunctions.Deriv_NewtonLeipnik
    saveName = "NewtonLeipnikAttractor"
    GenerationLimits = [(-0.01, -0.01), (-0.01, 0.01), (-0.01, 0.01)]
    plotLims = [(-1, 1), (-1, 1), (-0.375, 0.65)]
    speedUpFactor = 2

    frames = 500
    """
    x, y, z = pt

    dx = -a*x + y + 10*y*z
    dy = -x - 0.4*y + 5*x*z
    dz = b*z - 5*x*y

    return [dx, dy, dz]

def Deriv_3CellCNN(pt, t0, p1=1.24, p2=1.1, r=4.4, s=3.21):
    """Compute the time-derivative of a 3-Cell CNN system."""
    """
    dx = -x + p1*h1 - s*h2 - s*h3
    dy = -y - s*h1 + p2*h2 - r*h3
    dz = -z - s*h1 + r*h2 + h3

    h1 = (1/2)*(|x+1| - |x-1|)
    h2 = (1/2)*(|y+1| - |y-1|)
    h3 = (1/2)*(|z+1| - |z-1|)
    p1 = 1.24, p2 = 1.1, r = 4.4, s = 3.21

    timeInterval = [0, 25]
    AttractorFunc = AttractorFunctions.Deriv_3CellCNN
    saveName = "3CellCNNAttractor"
    GenerationLimits = [(-0.01, -0.01), (-0.01, 0.01), (-0.01, 0.01)]
    plotLims = [(-1.5, 1.5), (-1.5, 1.5), (-1.0, 1.0)]
    speedUpFactor = 2

    frames = 250
    """
    x, y, z = pt

    h1 = (1/2)*(abs(x+1) - abs(x-1))
    h2 = (1/2)*(abs(y+1) - abs(y-1))
    h3 = (1/2)*(abs(z+1) - abs(z-1))

    dx = -x + p1*h1 - s*h2 - s*h3
    dy = -y - s*h1 + p2*h2 - r*h3
    dz = -z - s*h1 + r*h2 + h3

    return [dx, dy, dz]

def Deriv_Arneodo(pt, t0, a=-5.5, b=3.5, c=-1.0):
    """Compute the time-derivative of a Arneodo system."""
    """
    dx = y
    dy = z
    dz = -a*x -b*y - z + c*(x**3)

    a = -5.5, b = 3.5, c = -1.0

    timeInterval = [0, 50]
    AttractorFunc = AttractorFunctions.Deriv_Arneodo
    saveName = "ArneodoAttractor"
    GenerationLimits = [(-0.05, -0.05), (-0.05, 0.05), (-0.05, 0.05)]
    plotLims = [(-4, 4), (-4, 4), (-7.0, 7.0)]
    speedUpFactor = 1

    frames = 500
    """
    x, y, z = pt

    dx = y
    dy = z
    dz = -a*x -b*y - z + c*(x**3)

    return [dx, dy, dz]

def Deriv_Bouali(pt, t0, a=0.3, s=1.0):     # OVERSHOOTS
    """Compute the time-derivative of a Bouali system."""
    """
    dx = x*(4 - y) + a*z
    dy = -y*(1 - (x**2))
    dz = -x*(1.5 - s*z) - 0.05*z

    a = 0.3, s = 1.0

    timeInterval = [0, 50]
    AttractorFunc = AttractorFunctions.Deriv_Bouali
    saveName = "BoualiAttractor"
    GenerationLimits = [(-0.05, -0.05), (-0.05, 0.05), (-0.05, 0.05)]
    plotLims = [(-4, 4), (-4, 4), (-7.0, 7.0)]
    speedUpFactor = 1

    frames = 500
    """
    x, y, z = pt

    dx = x*(4 - y) + a*z
    dy = -y*(1 - (x**2))
    dz = -x*(1.5 - s*z) - 0.05*z

    return [dx, dy, dz]

def Deriv_BurkeShaw(pt, t0, s=10, v=4.272):
    """Compute the time-derivative of a Burke-Shaw system."""
    """
    dx = -s*(x + y)
    dy = -y - s*x*z
    dz = s*x*y + v

    s = 10, v = 4.272

    timeInterval = [0, 7.5]
    AttractorFunc = AttractorFunctions.Deriv_BurkeShaw
    saveName = "BurkeShawAttractor"
    GenerationLimits = [(-0.05, -0.05), (-0.05, 0.05), (-0.05, 0.05)]
    plotLims = [(-2.5, 2.5), (-2.5, 2.5), (-2.5, 2.5)]
    speedUpFactor = 2

    frames = 250
    """
    x, y, z = pt

    dx = -s*(x + y)
    dy = -y - s*x*z
    dz = s*x*y + v

    return [dx, dy, dz]

def Deriv_ChenCelikovsky(pt, t0, a=36, b=3, c=20):
    """Compute the time-derivative of a Chen-Celikovsky system."""
    """
    dx = a*(y - x)
    dy = -x*z + c*y
    dz = x*y - b*z

    a = 36, b = 3, c = 20

    timeInterval = [0, 5]
    AttractorFunc = AttractorFunctions.Deriv_ChenCelikovsky
    saveName = "ChenCelikovskyAttractor"
    GenerationLimits = [(-1, 1), (-1, 1), (-1, 1)]
    plotLims = [(-25, 25), (-25, 25), (10, 45)]
    speedUpFactor = 2

    frames = 250
    """
    x, y, z = pt

    dx = a*(y - x)
    dy = -x*z + c*y
    dz = x*y - b*z

    return [dx, dy, dz]