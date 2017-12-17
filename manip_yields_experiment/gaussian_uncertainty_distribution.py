"""
The purpose of this script is to run MonteCarlo simulations on 'experiment.py'
"""
#import vital libraries
import sys, os
import time as tm
import numpy as np
import random as rn
import bestfit_param_omega.current_bestfit as current_bestfit
bestfit_imported = True
from experiment import experiment

#set global parameters

def start_experiment(folder_name, readme_text=""):
    """
    Function return True if succesful and False when something fails.
    """
    #Make sure script is called directly, from same folder
    if '/' in sys.argv[0]:
        print "The experiment has to be called directly"
        print "from the same directory"
        return False
    #Make folder for experiment if it does not exist
    if os.path.exists(folder_name): #folder already exist
        print "The suggested foldername already exist."
        return False
    os.mkdir(folder_name)
    #Initilize with a readme-file
    readme_path = folder_name + "/README.md"
    with open(readme_path, 'w') as readme:
        readme.write(folder_name + '\n')
        readme.write('='*len(folder_name) + '\n')
        readme.write('\n')
        if readme_text:
            readme.write(readme_text + '\n')
            readme.write('\n')
    if not os.path.exists(readme_path): #no readme-file
        print "README.md was not created"
        return False
    #Everything went alright so far
    return True

def gaussian_variate_experiment(folder_name, experiment_name,
                                isotope="Re-187", stddev=0.1,
                                num_experiments=10, num_timesteps=50):
    """
    Use the experiment class to vary *isotope* with 
    a "fudge factor" drawn from a gaussian distribution around 1.0
    with a standard deviation *stddev*.
    """
    #get array of cpu-clock values
    clock_array = np.zeros(num_experiments+1, dtype=float)
    clock_array[0] = tm.clock()
    factor_array = np.zeros(num_experiments, dtype=float)
    
    #loop over all experiments
    for i in range(num_experiments):
        status = "RUNNING EXPERIMENT: %d/%d"%(i,num_experiments)
        print '\n'
        print status
        print "="*len(status)
        
        #draw random gaussian fudge factor
        fudge_factor = rn.gauss(1.0, stddev)
        factor_array[i] = fudge_factor
        #get instance of experiment
        exp_instance = experiment(isotope, fudge_factor, num_timesteps,
                                  bestfit_namespace=current_bestfit)
        #save data to appropriately named file
        save_filename = folder_name + "/" + experiment_name + str(i) + ".csv"
        exp_instance.save2file(save_filename)
        #delete instance
        del exp_instance
        #get time of cpu-clock
        clock_array[i+1] = tm.clock()
        
    #calculate experiment times in seconds
    total_time = clock_array[-1] - clock_array[0]
    delta_time = clock_array[1:] - clock_array[:-1] #time for each iteration
    #save some data to readme-file
    readme_filename = folder_name + "/README.md"
    with open(readme_filename, 'a') as readme:
        #save isotope, stddev, total time, # of experiments to readme-file
        readme.write("Some parameters for this MC-simulation\n")
        readme.write("Isotope: %s \n"%isotope)
        readme.write("Gaussian-sigma: %1.4e \n"%stddev)
        readme.write("Total time lapsed: %1.4e s \n"%total_time)
        readme.write("Number of experiments: %d \n"%num_experiments)
        readme.write("\n")
        #save fudge-factor and time for each experiment to readme-file
        readme.write("Integer-id, time lapsed, and fudge_factor for each calculation (i,t,f) \n")
        total_data_string = ""
        for i in range(num_experiments):
            single_data_string = "(%d, %4.2f, %1.4f)"%(i,delta_time[i],factor_array[i])
            total_data_string += single_data_string + " "
        readme.write(total_data_string + "\n")

#############
### Cases ###
#############
def case_test():
    print "TEST!"
    folder_name = "test"
    experiment_name = folder_name
    start_experiment(folder_name)
    gaussian_variate_experiment(folder_name, experiment_name, num_experiments=10)

def case1():
    print "Case 1"
    folder_name = "FirstAttempt"
    experiment_name = "first_attempt"
    n = 250
    res = 1000
    if start_experiment(folder_name): #if new folder is made...
        gaussian_variate_experiment(folder_name, experiment_name,
                                    num_experiments=n, num_timesteps=res)
    else: #new folder is not made...
        print "Experiment failed already -_-"
        sys.exit("Exiting!")

if __name__ == '__main__':
    if len(sys.argv) == 1: #no cmd-line args -> test-case
        case_test()
    if len(sys.argv) == 2: #test_case or case_*number*
        if sys.argv[1].lower() == "test":
            case_test()
        elif sys.argv[1].lower() == "case1":
            case1()
    
    
