"""
TODO LIST:
==========
[X] - write description
[x] - write commented skeleton
[] - write skeleton from comments
[] - fill in skeleton with code
[] - run/test/debug
[] - rewrite description and write usage

Description:
============
Choose a data-file in this folder, and plot the mean p/m two sigma areas for the data.
Assuming, ofcourse, that the data-files are in the stddev-format.

Detailed description:
---------------------

Usage:
======

"""

### Get file from user ###
#get all files in directory
#index files in a dictionary; print all options
#if cmd-line argumnet is, and is integer, Use this as index
#otherwise ask for user to give index or path(or full path)
#print option selected
""" example code from 'analyze_stddev.py'
loa_contents = os.listdir(location_dir)
loa_folders = []
for content in loa_contents: #loop over all strings in cwd
    if not ('.' in content): #string is not a filename, but folder
        loa_folders.append(content)
#find folder name
print "Current available folders: ", dict(enumerate(loa_folders))
response = raw_input("What folder would you like to choose? (full path or index)")
try:
    #is response the index of folder-list?
    response = int(response)
    input_index = response
    input_datafolder = loa_folders[response]
except ValueError: 
    #the response cannot be integer, full path is given
    input_datafolder = response
    input_index = loa_folders.index(input_datafolder)
    #check that folder exist in list
    if not (input_datafolder in loa_folders):
        print "Folder: %s not available"%(input_datafolder)
        sys.exit("Exiting!")
except IndexError:
    #index is out of range of folder-list
    print "Index: %d is not available"%response
    sys.exit("Exiting!")
#add backslash to input-foldername
input_datafolder += "/"
"""
### Read file into separate arrays ###
#check for numpy-extension
#read matrix from filename
#make arrays from matrix
#make plottable arrays 
### Plotting syntax ###
#figure/axis objects
#plot default
#plot mean
#plot one-sigma area
#plot two-sigma area
