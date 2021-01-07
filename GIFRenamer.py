"""
Script to Rename Compressed GIFs from online

Compress GIFS here: https://gifcompressor.com/
"""

# Imports
import os
from tqdm import tqdm

# Main Functions
def RenameFiles(dirPath, aP=None, aS=None, rP=None, rS=None):
    for f in tqdm(os.listdir(dirPath)):
        fname = os.path.splitext(f)[0]
        fext = os.path.splitext(f)[1]
        if rP is not None:
            if fname.startswith(rP):
                fname = fname[len(rP):]
        if rS is not None:
            if fname.endswith(rS):
                fname = fname[:-len(rP)]
        if aP is not None:
            fname = rP + fname
        if aS is not None:
            fname = fname + aS
        
        if not f == fname + fext:
            os.rename(dirPath + f, dirPath + fname + fext)
            print(f, "->", fname + fext)

# Driver Code
# Params
dirPath = "GeneratedVisualisations/"
addPrefix = None
removePrefix = "0_"
addSuffix = None
removeSuffix = "-m"
# Params

# RunCode
RenameFiles(dirPath, aP=addPrefix, aS=addSuffix, rP=removePrefix, rS=removeSuffix)