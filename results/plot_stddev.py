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
def get_files_wd(working_dir='.'):
    #get all files in directory
    loa_files_wd = os.listdir(working_dir)
    #index files in a dictionary; print all options
    doa_files_wd = dict(enumerate(loa_files_wd)) #dictionary with index as key
    print "The files, and corresponding indeces, for this directory are:"
    print "\t %s"%doa_files_wd
    return doa_files_wd

def get_single_filename_from_user(working_dir='.'):
    doa_files_cwd = get_files_cwd(working_dir=working_dir)
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
    return working_dir + "/" + filename

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
    matrix_format = ["time_array", "default_array", "data_mean", "data_median", "data_sigma", "data_2sigma"]
    print "using the following format for numpy-matrix"
    print "\t %s"%matrix_format
    #make arrays from matrix #Consider switching to dictionary
    time_array = numpy_matrix[0,:]
    default_array = numpy_matrix[1,:]
    data_mean = numpy_matrix[2,:]
    data_median = numpy_matrix[3,:]
    data_sigma = numpy_matrix[4,:]
    data_2sigma = numpy_matrix[5,:]
    return time_array, default_array, data_mean, data_sigma, data_sigma2, data_median

### Plotting syntax ###
def plot_deviation(axis, toa_arrays, default=True, c='g'):
    #toa_arrays format (time_array, default_array, data_mean, data_sigma, data_sigma2, data_median)
    x = toa_arrays[0]
    if default:
        axis.plot(x, toa_arrays[1], label="$f=1.0$") #plot default value
    
    #plot mean
    axis.plot(x, toa_arrays[2], color=c) 
    #plot one-sigma area
    lower_1sigma = toa_arrays[2] - toa_arrays[3]
    upper_1sigma = toa_arrays[2] + toa_arrays[3]
    axis.plot(x, upper_1sigma, color=c, alpha=0.7)
    axis.plot(x, lower_1sigma, color=c, alpha=0.7)
    axis.fill_between(x, lower_1sigma, upper_1sigma, color=c, alpha=0.5) 
    #plot two-sigma area
    lower_2sigma = toa_arrays[2] - toa_arrays[4]
    upper_2sigma = toa_arrays[2] + toa_arrays[4]
    axis.plot(x, upper_2sigma, color=c, alpha=0.5)
    axis.plot(x, upper_2sigma, color=c, alpha=0.5)
    axis.fill_between(x, lower_2sigma, upper_2sigma, color=c, alpha=0.3) 
    
if __name__ == '__main__':
    """ Sample for extracting folder from /stornext/
    from directory_master import Foldermap as FM
    #stornext_folder = FM().stornext_dir()
    loa_contents = os.listdir(location_dir)
    loa_folders = []
    for content in loa_contents: #loop over all strings in cwd
    ...:if not ('.' in content): #string is not a filename, but folder
    ...:...:loa_folders.append(content)
    """
    filename_data = get_single_filename_from_user()
    data = extract_arrays_from_filename(filename_data)
    data = make_plottable_arrays(data)
    
    fig, ax = pl.subplots(111); ax.hold(True); ax.grid(True)
    ax.set_title("")
    ax.set_xlabel("")
    ax.set_ylabel("")
    plot_deviation(ax, data)
    
    savename = "%s.png"%filename_data
    fig.savefig(savename)
    pl.show()
    
    
