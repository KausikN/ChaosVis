"""
Stream lit GUI for hosting ChaosVis
"""

# Imports
import os
import functools
import streamlit as st
import json

import ChaosVis

# Main Vars
config = json.load(open('./StreamLitGUI/UIConfig.json', 'r'))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
        tuple(
            [config['PROJECT_NAME']] + 
            config['PROJECT_MODES']
        )
    )
    
    if selected_box == config['PROJECT_NAME']:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(' ', '_').lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config['PROJECT_NAME'])
    st.markdown('Github Repo: ' + "[" + config['PROJECT_LINK'] + "](" + config['PROJECT_LINK'] + ")")
    st.markdown(config['PROJECT_DESC'])

    # st.write(open(config['PROJECT_README'], 'r').read())

#############################################################################################################################
# Repo Based Vars
CACHE_PATH = "StreamLitGUI/CacheData/Cache.json"
SAVE_GIF_PATH = "StreamLitGUI/CacheData/CacheGIF.gif"

# Util Vars
CACHE = {}

# Util Functions
def LoadCache():
    global CACHE
    CACHE = json.load(open(CACHE_PATH, 'r'))

def SaveCache():
    global CACHE
    json.dump(CACHE, open(CACHE_PATH, 'w'), indent=4)

# Main Functions
def ChaosVis_Attractor(USERINPUT_AttractorFuncName, USERINPUT_N, USERINPUT_GenFuncName, timeInterval, frames):
    AttractorFunc = ChaosVis.ATTRACTOR_FUNCS[USERINPUT_AttractorFuncName]["func"]
    N_trajectories = USERINPUT_N
    GeneratorFunc = ChaosVis.GENERATOR_FUNCS[USERINPUT_GenFuncName]

    GenerationLimits = ChaosVis.ATTRACTOR_FUNCS[USERINPUT_AttractorFuncName]["GenerationLimits"]
    plotLims = ChaosVis.ATTRACTOR_FUNCS[USERINPUT_AttractorFuncName]["plotLims"]
    ChaosVis.speedUpFactor = ChaosVis.ATTRACTOR_FUNCS[USERINPUT_AttractorFuncName]["speedUpFactor"]

    frame_interval = 30
    ChaosVis.rotationSpeed = 3

    plotData = False
    saveData = {
        "save": True,
        "path": SAVE_GIF_PATH,
        "fps": 30,
        "figSize": [320, 240]
    }
    saveData["figSize"] = (saveData["figSize"][0]/100, saveData["figSize"][1]/100) # Change FigSize to inches (dpi = 100)

    ChaosVis.AnimateChaos(AttractorFunc, N_trajectories, 
        functools.partial(GeneratorFunc, Limits=GenerationLimits), 
        timeInterval=timeInterval, plotLims=plotLims, frames=frames, frame_interval=frame_interval, 
        plotData=plotData, saveData=saveData,
        progressObj=st.progress(0.0))

# UI Functions


# Repo Based Functions
def attractor_systems():
    # Title
    st.header("Chaotic Attractor Systems")

    # Prereq Loaders

    # Load Inputs
    USERINPUT_AttractorFuncName = st.selectbox("Attractor Function", list(ChaosVis.ATTRACTOR_FUNCS.keys()))
    col1, col2 = st.columns(2)
    USERINPUT_GenFuncName = col1.selectbox("Point Generator Function", list(ChaosVis.GENERATOR_FUNCS.keys()))
    USERINPUT_N = col2.number_input("Number of Trajectories", min_value=1, max_value=100, value=9, step=1)
    col1, col2, col3 = st.columns(3)
    USERINPUT_TimeIntervalStart = col1.number_input("Time Interval Start", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    USERINPUT_TimeIntervalEnd = col2.number_input("Time Interval End", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
    USERINPUT_frames = col3.number_input("Number of Frames", min_value=1, max_value=3000, value=90, step=1)

    # Process Inputs
    if st.button("Visualise"):
        timeInterval = [USERINPUT_TimeIntervalStart, USERINPUT_TimeIntervalEnd]
        ChaosVis_Attractor(USERINPUT_AttractorFuncName, USERINPUT_N, USERINPUT_GenFuncName, timeInterval, USERINPUT_frames)

        # Display Outputs
        st.markdown("## Visualisation")
        st.image(SAVE_GIF_PATH, caption="Chaos Visualisation", use_column_width=True)
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()