"""
"""
from handle_data_files import get_all_arrays, get_single_array
from plot_data_files import get_mean_sigma_extrema, get_timepoint_array
import numpy as np

def save_results(get_directory, save_directory, experiment, loa_array_strings, loa_timepoints):
    """ Some DocString """
    all_good = True
    #get all matrices
    doa_2Darrays = get_all_arrays(dir_name=get_directory,
                                  loa_array_strings=loa_array_strings)
    if "test_dir" in get_directory: #test script
        time_array = get_single_array(dir_name=get_directory,numpy_filename="../test_dir/test_files_pid0.npy", array_string="time")
    else:
        time_array = get_single_array(dir_name=get_directory,
                                      array_string="time")
    for array_string in loa_array_strings:
        #create outfilename dir+resultfile+exp+arrstr+type
        outfilename = lambda string: save_directory + \
                      "resultfile"+ "_" + \
                      experiment + "_" + \
                      array_string + "_" + string
        #get time evolution arrays
        ###get arrays
        mean, pos_sigma, neg_sigma, maximum, minimum = get_mean_sigma_extrema(numpy_matrix=doa_2Darrays[array_string])
        loa_save_arrays_timeevol = [mean, pos_sigma, neg_sigma, maximum, minimum]
        ###get filename type=timeevol.npy
        filename_timeevol = outfilename("timeevol.npy")
        ###get desc. string of all arrays
        loa_save_desc_timeevol = ["mean", "mean + 1 sigma",
                                  "mean + 1 sigma", "maximum",
                                  "minimum"]

        #get histogram array
        ###get arrays
        loa_save_arrays_hist = []
        loa_save_desc_hist = []
        for timepoint in loa_timepoints:
            array = get_timepoint_array(time_array=time_array,
                                        numpy_matrix=doa_2Darrays[array_string],
                                        timepoint=timepoint)
            #save array and description to lists
            loa_save_arrays_hist.append(array)
            loa_save_desc_hist.append("t=%2.4f Gyr"%(timepoint/1.0e+9))
        ###get filename type=hist.npy
        filename_hist = outfilename("hist.npy")
        
        #get description
        ###describe content
        desc_string = "This is the results from  \n"
        desc_string += "experiment: %s \n"%(experiment)
        desc_string += "array-type: %s \n \n"%(array_string)
        desc_string += "The time evolution data in file: %s \n"%(filename_timeevol)
        for i, desc in enumerate(loa_save_desc_timeevol):
            desc_string += "%d %s \n"%(i, desc)
        desc_string += "The timepoint data in file: %s \n"%(filename_hist)
        for i, desc in enumerate(loa_save_desc_hist):
            desc_string += "%d %s \n"%(i, desc)
        ###get filename=desc.txt
        filename_desc = outfilename("desc.txt")

        #Save all files
        try:
            #timeevol
            np.save(filename_timeevol, np.stack(loa_save_arrays_timeevol))
            #hist
            np.save(filename_hist, np.stack(loa_save_arrays_hist))
            
            #desc.
            with open(filename_desc, 'w') as desc_file:
                desc_file.write(desc_string)
            
            print "Writing results to ", outfilename("_etc")
        except: #something wrong happened
            all_good = False
    if all_good:
        return True
    else:
        return False

if __name__ == '__main__':
    #Test by writing results from 'test_dir' to 'test_dir'
    test_dir = "../test_dir/"
    return_bool = save_results(get_directory=test_dir,
                               save_directory=test_dir,
                               experiment="TestSaveResults",
                               loa_array_strings=["ism_iso_Re-187"],
                               loa_timepoints=[9.5e+9, 14e+9])
    print return_bool
