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
import numpy as np
import matplotlib as pl

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
def extract_arrays_from_filename(filename):
    #check for numpy-extension
    numpy_extension = ".npy"
    if numpy_extension in filename:
        #read matrix from filename
        numpy_mat = np.load(filename)
        print "numpy-matrix extracted from '%s', shape=%s"%(filename, numpy_mat.shape)
        return numpy_mat
    else:
        print "Bad usage, filename '%s' is not numpy-extension"%filename
        return False
def make_plottable_arrays(numpy_matrix):
    matrix_format = ["default_array", "data_mean", "data_median", "data_sigma", "data_2sigma"]
    print "using the following format for numpy-matrix"
    print "\t %s"%matrix_format
    #make arrays from matrix #Consider switching to dictionary
    default_array = numpy_matrix[0,:]
    data_mean = numpy_matrix[1,:]
    data_median = numpy_matrix[2,:]
    data_sigma = numpy_matrix[3,:]
    data_2sigma = numpy_matrix[4,:]
    return default_array, data_mean, data_sigma, data_sigma2, data_median

### Plotting syntax ###
#figure/axis objects
#plot default
#plot mean
#plot one-sigma area
#plot two-sigma area
#save figure
