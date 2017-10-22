"""
Descriptoion/purpose:
This script will run all variable-scripts in this folder.
Method:
Find all 'vary_*.py' files in the current working directory,
run all script with a optioonal num-steps argument.
"""
import sys,os

#set number of timesteps
try:
    n = int(sys.argv[1])
except IndexError:
    n = 10

#find list of all files in folder
loa_files = os.listdir(os.getcwd()) #NB! requires script to be called in dir.
loa_scripts = [] #list of desired scripts
for filename in loa_files:
    extension = ".py"
    pretext = "vary_"
    length = len(filename)
    bool1 = filename[:len(pretext)]==pretext #starts with *pretext*
    bool2 = filename[length-len(extension):]==extension #ends with *extension*
    if bool1 and bool2:
        loa_scripts.append(filename)

for script in loa_scripts:
    call_string = "python %s %d &"%(script, n)
    #print call_string #test
    os.system(call_string)
