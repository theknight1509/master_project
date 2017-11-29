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
### Imports and global variables ###
import os, sys
### Get file from user ###
def get_files_cwd():
    #get all files in directory
    loa_files_cwd = os.listdir('.')
    #index files in a dictionary; print all options
    doa_files_cwd = dict(enumerate(loa_files_cwd)) #dictionary with index as key
    print "The files, and corresponding indeces, for this directory are:"
    print "\t %s"%doa_files_cwd
    return doa_files_cwd
def get_single_file_from_user():
    doa_files_cwd = get_files_cwd
    #if cmd-line argument is, and is integer, Use this as index
    if len(sys.argv) > 1: #there are cmd-line args
        try:
            file_index = int(sys.argv[1])
        except ValueError: #cmd-line arg could not be int
            None
    #otherwise ask for user to give index
    else:
        file_index = int(input("Give index of which data-file you want plotted!"))
    #print option selected
    filename = doa_files_cwd[file_index]
    print "The file selected is %s"%filename
    return filename
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
