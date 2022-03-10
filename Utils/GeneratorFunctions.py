'''
Generator Functions
'''

# Imports
import numpy as np

# Main Functions
def GeneratePoints_UniformRandom(N, Limits=[(-15, 15), (-15, 15), (-15, 15)], seed=5):
    np.random.seed(seed)
    x = Limits[0][0] + (Limits[0][1] - Limits[0][0]) * np.random.random(N)
    y = Limits[1][0] + (Limits[1][1] - Limits[1][0]) * np.random.random(N)
    z = Limits[2][0] + (Limits[2][1] - Limits[2][0]) * np.random.random(N)
    pts = np.reshape(np.dstack((x, y, z)), (-1, 3))
    print(pts.shape)
    return pts

def GeneratePoints_Uniform(N, Limits=[(-15, 15), (-15, 15), (-15, 15)]):
    x = np.linspace(Limits[0][0], Limits[0][1], N)
    y = np.linspace(Limits[1][0], Limits[1][1], N)
    z = np.linspace(Limits[2][0], Limits[2][1], N)

    pts = []
    for x0 in x:
        for y0 in y:
            for z0 in z:
                pts.append([x0, y0, z0])
    pts = np.array(pts)

    print(pts.shape)
    return pts

# Main Vars
GENERATOR_FUNCS = {
    "UniformRandom": GeneratePoints_UniformRandom,
    "Uniform": GeneratePoints_Uniform
}