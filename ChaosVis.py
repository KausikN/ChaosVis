'''
Algorithm Visualisation for Chaos Theory and Lorenz Attractor System
Chaos Theory Link: https://www.youtube.com/watch?v=fDek6cYijxI

Other Attractors Link: https://www.youtube.com/watch?v=idpOunnpKTo
'''

# Imports
import os
import functools
import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
from tqdm import tqdm

from ChaosLibrary.AttractorFunctions import *
from Utils.GeneratorFunctions import *

# Main Variables
Lines = []
Pts = []
fig = None
ax = None
x_t = []

# Main Functions
# Visualisation Functions
# initialization function: plot the background of each frame
def InitChaosAnimation():
    global Lines, Pts, x_t, fig, ax
    for line, pt in zip(Lines, Pts):
        line.set_data([], [])
        # line.set_3d_properties([])

        pt.set_data([], [])
        # pt.set_3d_properties([])
    return Lines + Pts

# animation function.  This will be called sequentially with the frame number
def UpdateChaosAnimation(i, progressObj=None, frames=1):
    global Lines, Pts, x_t, fig, ax, speedUpFactor, rotationSpeed

    # we'll step two time-steps per frame.  This leads to nice results.
    i_old = i
    i = (speedUpFactor * i) % x_t.shape[1]

    for line, pt, xi in zip(Lines, Pts, x_t):
        x, y, z = xi[:i].T
        line.set_data(x, y)
        line.set_3d_properties(z)

        pt.set_data(x[-1:], y[-1:])
        pt.set_3d_properties(z[-1:])

    ax.view_init(30, 0.3*i*rotationSpeed)
    fig.canvas.draw()

    print(i_old, "done", end='\r')
    if progressObj is not None: progressObj.progress((i_old+1)/frames)

    return Lines + Pts

def AnimateChaos(AttractorFunc, N_trajectories, GeneratorFunc, timeInterval=[0, 4], plotLims=[(-25, 25), (-35, 35), (5, 55)], frames=500, frame_interval=30, plotData=True, saveData={"save": False}, progressObj=None):
    global Lines, Pts, x_t, fig, ax, speedUpFactor
    # Choose random starting points, uniformly distributed from -15 to 15
    startPoints = GeneratorFunc(N_trajectories)
    N_trajectories = startPoints.shape[0]

    # Solve for the trajectories
    time = np.linspace(timeInterval[0], timeInterval[1], frames*speedUpFactor)
    x_t = np.asarray([integrate.odeint(AttractorFunc, sP, time) for sP in tqdm(startPoints)])

    # Set up figure & 3D axis for animation
    fig = plt.figure(figsize=saveData["figSize"])
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    ax.axis('off')

    # choose a different color for each trajectory
    colors = plt.cm.jet(np.linspace(0, 1, N_trajectories))

    # Set up lines and points
    Lines = sum([ax.plot([], [], [], '-', c=c) for c in colors], [])
    Pts = sum([ax.plot([], [], [], 'o', c=c) for c in colors], [])

    # Prepare the axes limits
    ax.set_xlim(plotLims[0])
    ax.set_ylim(plotLims[1])
    ax.set_zlim(plotLims[2])

    # Set point-of-view: specified by (altitude degrees, azimuth degrees)
    ax.view_init(30, 0)

    # Animate
    # InitAnim = functools.partial(InitChaosAnimation, Lines, Pts)
    # UpdateAnim = functools.partial(UpdateChaosAnimation, Lines=Lines, Pts=Pts, x_t=x_t, ax=ax, fig=fig)
    InitAnim = InitChaosAnimation
    UpdateAnim = functools.partial(UpdateChaosAnimation, progressObj=progressObj, frames=frames)
    anim = animation.FuncAnimation(fig, UpdateAnim, init_func=InitAnim, frames=frames, interval=frame_interval, blit=True)

    # Save as mp4. This requires mplayer or ffmpeg to be installed
    if saveData["save"]:
        if os.path.splitext(saveData["path"])[-1] == '.gif':
            writer = animation.PillowWriter(fps=saveData["fps"])
            anim.save(saveData["path"], writer=writer, )
        else:
            anim.save(saveData["path"], fps=saveData["fps"], extra_args=['-vcodec', 'libx264'])

    if plotData:
        plt.show()

# Driver Code
# # Params
# N_trajectories = 27
# GeneratorFunc = GeneratePoints_UniformRandom

# timeInterval = [0, 15]
# AttractorFunc = AttractorFunctions.Deriv_SprottLinzS
# saveName = "SprottLinzSAttractor"
# GenerationLimits = [(-0.1, 0.1), (-0.1, 0.1), (-0.1, 0.1)]
# plotLims = [(-5, 5), (-5, 5), (-3, 3)]
# speedUpFactor = 2

# frames = 250
# frame_interval = 30
# rotationSpeed = 3

# plotData = False
# saveData = {
#     "save": True,
#     "path":"GeneratedVisualisations/" + "0UC_" + saveName + "_" +
#         ("Uniform" if GeneratorFunc == GeneratePoints_Uniform else "Random") + ".gif",
#     "fps": 30,
#     "figSize": [320, 240]
#     }
# # Params

# # RunCode
# saveData["figSize"] = (saveData["figSize"][0]/100, saveData["figSize"][1]/100) # Change FigSize to inches (dpi = 100)
# AnimateChaos(AttractorFunc, N_trajectories, functools.partial(GeneratorFunc, Limits=GenerationLimits), timeInterval=timeInterval, plotLims=plotLims, frames=frames, frame_interval=frame_interval, plotData=plotData, saveData=saveData)