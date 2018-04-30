"""
This script is for picking an experiment on the stornext folder,
get all the adequate results and write them to the results-folder 
in \thesis\
"""
import os
from save_results import save_results
from directory_master import Foldermap
folder = Foldermap()
stornext_folder = folder.stornext_folder()
hume_folder = folder.hume_folder()
results_folder = "latex/thesis/results/" #direction to thesis-results-folder from /Master/

if __name__ == '__main__':
    #which experiment?
    inventory = dict(enumerate(os.listdir(stornext_folder)))
    question = "Choose the index of the appropriate experiment?\n%s"%(inventory)
    response = int(raw_input(question))
    
    experiment = inventory[response]
    get_directory = stornext_folder + experiment + "/"
    save_directory = hume_folder + results_folder + experiment + "/"
    
    #which arrays?
    loa_array_strings = []
    #nb_nsm, rate_nsm
    loa_array_strings.append("num_nsm")
    #elem & iso yield+ism
    iso_list = ["Re-185", "Re-187", "Os-187", "Os-188", "Os-186", "W-184"]
    elem_list = ["Re", "Os", "W"]
    for iso in iso_list:
        loa_array_strings.append("ism_iso_%s"%(iso))
        loa_array_strings.append("yield_%s"%(iso))
    for elem in elem_list:
        loa_array_strings.append("ism_elem_%s"%(elem))
    
    #which timepoints? (9.5Gyr, 14Gyr)
    loa_timepoints = [9.5e+9, 14e+9]
    
    save_results(get_directory=get_directory,
                 save_directory=save_directory,
                 experiment=experiment,
                 loa_array_strings=loa_array_strings,
                 loa_timepoints=loa_timepoints)
