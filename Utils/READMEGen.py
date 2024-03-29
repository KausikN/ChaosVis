"""
Script to Generate the README File for the repo
"""

# Imports
import os
from tqdm import tqdm

# Main Vars
ORDER_PATH = "ChaosLibrary/order.txt"

# Main Functions
def GetFiles(dirPath):
    fnames = []
    for f in tqdm(os.listdir(dirPath)):
        fnames.append(f)
    return fnames

def READMEGenerate(dirPath, start=None, end=None, reverse=False, orderPath=ORDER_PATH):
    gifs = GetFiles(dirPath)
    order = open(dirPath + orderPath, 'r').read().split('\n')
    if reverse:
        order = order[::-1]
    
    if end is not None:
        order = order[:end]
    if start is not None:
        order = order[start:]

    order_fileChecked = []
    for gif in tqdm(order):
        gifAltered = gif.replace('-', '').replace(' ', '').lower()
        for gifCheck in gifs:
            if gifCheck.lower().find(gifAltered) > -1:
                order_fileChecked.append(gif)
                break
    
    order = list(order_fileChecked)

    Header = """# ChaosVis
 ChaosVis is a Visualiser Tool for visualising attractor systems and other chaotic data
 
 Chaos theory is a branch of mathematics focusing on the study of chaos — dynamical systems whose apparently random states of disorder and irregularities are actually governed by underlying patterns and deterministic laws that are highly sensitive to initial conditions.

 Small differences in initial conditions lead to vastly different lifepaths in these systems

 Chaos theory led to other popular concepts like The Butterfly Effect

 Video on Chaos Theory
   
 [![Chaos Theory Video](https://img.youtube.com/vi/fDek6cYijxI/0.jpg)](https://www.youtube.com/watch?v=fDek6cYijxI)

# GUI
[![https://infinityjoker-apps.herokuapp.com/](https://pyheroku-badge.herokuapp.com/?app=infinityjoker-apps&style=plastic)](https://infinityjoker-apps.herokuapp.com/)

 - GUI built using streamlit
 - To use app locally,
    - Clone the repo and run [StartUI.sh](StartUI.sh) to view the app on your browser!
 - App is also hosted remotely on heroku using my common host app,
    - [https://infinityjoker-apps.herokuapp.com/](https://infinityjoker-apps.herokuapp.com/)

    - In the Common Host App, simply choose a project to load and click load and deploy.

    - Then go ahead and use the app! :)

    - If you want to change to another app, simply click on View Other Projects in top left and choose any other project and load and deploy.

# Attractor Systems
   - Visualise Chaos Theory using attractor systems
    """

    Format = """
      - {0} Attractor System

        ![{0} Attractor Random](GeneratedVisualisations/{1}Attractor_Random.gif)
        ![{0} Attractor Uniform](GeneratedVisualisations/{1}Attractor_Uniform.gif)

    """    

    READMEText = Header
    for gif in order:
        sysText = str(Format)
        READMEText = READMEText + sysText.format(gif, gif.replace('-', '').replace(' ', ''))
    
    return READMEText


# Driver Code
# Params
dirPath = "GeneratedVisualisations/"
reverse = True
start = None
end = 4
# Params

# RunCode - Main (Constrained) README
READMEText = READMEGenerate(dirPath, start=start, end=end, reverse=reverse, orderPath=ORDER_PATH)
open('README.md', 'w').write(READMEText)

# RunCode - Main (Constrained) README
READMEText = READMEGenerate(dirPath, start=None, end=None, reverse=False, orderPath=ORDER_PATH)
open('READMEFull.md', 'w').write(READMEText)