"""
Description: Test various ways of making an 'Experiment'-class that will fuck with the yields of a specific isotope.
TODO:
"""
################################################
### Import modules and set global parameters ###
################################################
#Get module for handling folders correctly
import sys
import directory_master as dir_m
folder = dir_m.Foldermap() #instance with all the correct folders
#Set environment option for the 'Omega' simulation
import os
os.environ['SYGMADIR'] = folder.nupycee[:-1]
#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs
import sys
import numpy as np

###############################################
### Get boolean test-switches from cmd-line ###
###############################################

print "Using boolean cmd-line args: *all* *test1* *test2* etc."
try:
    test_all = bool(int(sys.argv[1]))
except:
    test_all = True
try:
    test_array_bool = [bool(int(arg)) for arg in sys.argv[2:]]
except:
    test_array_bool = []
    
num_tests = 2
while len(test_array_bool) < num_tests:
    test_array_bool.append(False)
num_steps = 150

###########################################
### Tests various ways of inserting SFR ###
###########################################

#relative path to sfh-file from 'NuPyCEE'-directory
sfh_file_dir = "../reproduce_shen/"
sfh_file_relpath1 = sfh_file_dir+"time_sfr_Shen_2015.txt"
sfh_file_relpath2 = sfh_file_dir+"timegal5e8_sfr_Shen_2015.txt"

if test_all or test_array_bool[0]: #for simple testing of omega
    yield_omega = om.omega(special_timesteps=5)

if test_all or test_array_bool[1]:
    class experiment(omega):
        def __init__(self):
            None
        def __add_yields_mdot(self):
            #Modify this function
            None
