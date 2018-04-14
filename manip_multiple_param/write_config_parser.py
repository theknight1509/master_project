"""
Module/script for writing a config-file using the ConfigParser-module
"""
import configparser as cp
import sys

#list of acceptable parameter names (and default values)
loa_acc_param = ["re-187", "re-185", "os-187", "ej_mass", "f_merger", "nsm_dtd_slope"]
loa_def_values = ["0.15", "0.15", "0.1", "0.1", "0.1", "1.0"]

def write_config_file(num_exp, num_proc, dir_name, file_name,
                      dict_sigma_param):
    ### Parser Object ###
    parser_object = cp.ConfigParser()
    
    ### Write parameters of Monte Carlo simulation ###
    parser_object["montecarlo parameters"] = {}
    MC = parser_object["montecarlo parameters"]
    
    MC["description"] = "Parameters that determine how the experiment is run. Keys cannot handle capitol letters."
    MC["n_experiments"] = str(num_exp)
    MC["n_processors"] = str(num_proc)
    MC["directory_name"] = str(dir_name)
    MC["datafiles_name"] = str(file_name)
    
    ### Write parameters for Omega model ###
    parser_object["model parameters"] = {}
    param = parser_object["model parameters"]

    param["Description"] = "Contains values of the relative standard deviation to be applied to the parameters."
    for key, value in dict_sigma_param.iteritems():
        param[key] = value

    return parser_object

if __name__ == '__main__':
    print "Make a new config file!"

    #filename of config-file
    output_filename = raw_input("Name of new config-file? ")
    if output_filename: output_filename += ".ini"
    else: sys.exit()

    #get experiment-details
    num_exp = raw_input("Number of Omega-experiments? ")
    num_proc = raw_input("Number of processes available? (master-layer included) ")
    dir_name = raw_input("Full path of new directory? ")
    file_name = "datafile"

    #get standard deviation details of experiments
    dict_sigma_param = dict(zip(loa_acc_param, loa_def_values))
    response = raw_input("Use default sigma-values?(y/n) ")
    if response == "y": pass
    elif response == "n":
        for key in loa_acc_param:
            key_response = raw_input("New value for %s?(_/val) "%key)
            if not key_response: pass
            else: dict_sigma_param[key] = key_response
    else: sys.exit("Unintelligable! Exiting!")

    #make parser-object
    parser_object = write_config_file(num_exp=num_exp, num_proc=num_proc, dir_name=dir_name, file_name=file_name, dict_sigma_param=dict_sigma_param)
        
    with open(output_filename, 'w') as outfile:
        parser_object.write(outfile)
