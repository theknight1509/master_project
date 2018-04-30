#!/usr/bin/python2
"""
This script is only to make functions for handling 
all data-files in a experiment-folder.
"""
import sys
import os
import numpy as np

def get_indeces_from_file(filename, loa_arraynames):
    #turn arrayname into list of strings
    loa_indeces = []
    #get all contents from 'filename'
    with open(filename, 'r') as infile:
        loa_content_rows = infile.readlines()

    #loop over array names
    for arrayname in loa_arraynames:
        array_found = False
        #loop over all rows in file
        for row in loa_content_rows:
            row_index = int(row.split()[0])
            name = row.split()[1]
            if (name == arrayname):
                loa_indeces.append(row_index)
                array_found = True
                break #go to next arrayname
        if not array_found:
            print "Error in index-file, %s does not exist"%(arrayname)

    return loa_indeces

def get_all_numpy_filenames(dir_name):
    loa_filenames = os.listdir(dir_name)
    loa_numpy_filenames = [dir_name + filename for filename
                           in loa_filenames if ('.npy' in filename)]
    return loa_numpy_filenames

def get_single_array(dir_name, numpy_filename=False, array_string="time"):
    index_filename = dir_name + "data_indeces.txt"
    if not numpy_filename: #not given, use any
        numpy_filename = get_all_numpy_filenames(dir_name)[0]
        if not "_pid" in numpy_filename:
            print "No pid-marker in time-filename"
    single_matrix = np.load(numpy_filename)
    array_index = get_indeces_from_file(index_filename, [array_string])[0]
    single_array = single_matrix[array_index,:]
    return single_array

def get_all_arrays(dir_name, loa_array_strings, index_filename="data_indeces.txt"):
    """ From a given directory, find all numpy-files and index-file.
    Take arrays from al numpy-files and stack them into 2D-arrays 
    for each indeces/array-strings."""
    
    # Get list of all indeces
    index_filename = dir_name + index_filename
    loa_array_indeces = get_indeces_from_file(filename=index_filename,loa_arraynames=loa_array_strings)
    
    # find all numpy filenames
    loa_numpy_filenames = get_all_numpy_filenames(dir_name=dir_name)
    
    # dictionary with array-string as keys and empty lists
    doa_2Darrays = {key:[] for key in loa_array_strings}
    # loop over all numpy-data-filenames
    for data_filename in loa_numpy_filenames:
        single_numpy_matrix = np.load(data_filename)
        # loop over all array-string
        for array_string, array_index in zip(loa_array_strings, loa_array_indeces):
            try:
                current_array = single_numpy_matrix[array_index,:]
                doa_2Darrays[array_string].append(current_array)
            except:
                print "matrix not large enough for file: %s"%(data_filename)
            
    # stack list of arrays to 2D matrix
    for array_string in loa_array_strings:
        doa_2Darrays[array_string] = np.stack(doa_2Darrays[array_string])

    return doa_2Darrays

### On direct call! ###
if __name__ == '__main__':
    ### Perform test of 'get_single_array' and 'get_all_arrays' for test-directory
    test_dir = "../test_dir/"
    time = get_single_array(test_dir, array_string="time") 
    doa_data = get_all_arrays(dir_name=test_dir, loa_array_strings=["gas_mass", "sfr"])
    print [arr.shape for key,arr in doa_data.items()]
