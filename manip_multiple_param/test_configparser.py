"""
Make a simple test for the configparser-module 
in order to include config-files for pasing experiment-arguments
"""
import configparser as cp
import sys

### Parser Object ###
parser_object = cp.ConfigParser()

### Write parameters of Monte Carlo simulation ###
parser_object["montecarlo parameters"] = {}
MC = parser_object["montecarlo parameters"]

MC["description"] = "Parameters that determine how the experiment is run. Keys cannot handle capitol letters."
MC["n_experiments"] = "50"
MC["n_processors"] = "4"
MC["directory_name"] = "test_dir"
MC["datafiles_name"] = "test_files"

### Write parameters for Omega model ###
parser_object["model parameters"] = {}
param = parser_object["model parameters"]

param["Description"] = "Contains values of the relative standard deviation to be applied to the parameters."
param["re-187"] = "0.15"
param["re-185"] = "0.15"
param["os-187"] = "0.10"
param["ej_mass"] = "0.1"
param["f_merger"] = "0.1"
param["nsm_dtd_slope"] = "1.0"

### Write results to file ###
output_filename = "test_config_file.ini"
with open(output_filename, 'w') as outfile:
    parser_object.write(outfile)

### Cleanup ###
del parser_object

### Open file and print some parameters ###
if (__name__ == '__main__') and ("filecheck" in sys.argv):
    parser_object = cp.ConfigParser()
    parser_object.read(output_filename)
    print "All keys of ConfigParser-object: ", parser_object.keys()
    for key in parser_object.keys():
        print "Keys of %s: "%(key), parser_object[key].keys()
    print "Finding the number of processors from config-file:"
    print "\t"+"ConfigParser-object [montecarlo parameters] [n_processors]"
    print type(parser_object["montecarlo parameters"]["n_processors"]), parser_object["montecarlo parameters"]["n_processors"]
