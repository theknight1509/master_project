"""
"""
from handle_data_files import get_all_arrays

def save_results(directory, experiment, loa_array_strings):
    """ Some DocString """
    all_good = False
    #get all matrices
    doa_2Darrays = get_all_arrays(dir_name=directory, loa_array_strings=loa_array_strings)
    time_array = get_single_array(dir_name=directory, array_string="time")
    for array_string in loa_array_strings:
        #create outfilename dir+resultfile+exp+arrstr+type
        outfilename = lambda string: directory + "resultfile_" + \
                      experiment + "_" + \
                      array_string + "_" + string
        #get time evolution arrays
        
        ###get arrays
        ###get filename type=timeevol.npy
        ###get desc. string of all arrays
        #get histogram array
        ###get arrays
        ###get filename type=hist.npy
        ###get desc. string of all arrays
        #get description
        ###describe content
        ###get filename=desc.txt
    #Save all files
    if all_good:
        return True
    else:
        return False
