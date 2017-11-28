"""
The purpose of this script is to run MonteCarlo simulations on 'experiment.py'.
The program uses 'gaussian_uncertainty_distribution.py' as a skeleton,
but takes fudge_factor_values from a table.
Paralellization is done with multiprocessing.
Input arguments are dealt with through 'argparse', use '-h' for help.
"""
#import vital libraries
import sys, os
import time as tm
import numpy as np
import random as rn
import multiprocessing as mp
from bestfit_param_omega.current_bestfit import *
from experiment import experiment
from make_fudge_factor_table import write_new_table, read_fudge_factor

def start_experiment(folder_name, fudge_factor_tuple=(), timestep_size=0):
    """
    Function return True if succesful and False when something fails.
    readme_text is string that describes the experiment in the folder.
    fudge_factor_tuple contains number of gaussian random numbers and
    their standard deviation.
    If *timeste_size is given(greater then zero), run a single experiment without fudgefactor
    """
    print "Attempting to create a new simulation."
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
    readme_text = raw_input("Please enter the Readme-text for this simulation!\n")
    with open(readme_path, 'w') as readme:
        readme.write(folder_name + '\n')
        readme.write('='*len(folder_name) + '\n')
        readme.write('\n')
        #write readme-text if it is necessary
        if readme_text:
            readme.write(readme_text + '\n')
            readme.write('\n')
        #write standard deviation from fudge-factor-table to readme
        if fudge_factor_tuple:
            readme.write("Data from fudge-factors: \n")
            readme.write("Gaussian-sigma: %1.4e \n"%fudge_factor_tuple[1])
    if not os.path.exists(readme_path): #no readme-file
        print "README.md was not created"
        return False
    #Make a data-file of fudge_factors in the folder
    if fudge_factor_tuple:
        n = fudge_factor_tuple[0]
        sigma = fudge_factor_tuple[1]
        write_new_table(filename=folder_name+r"/fudge_factors.dat",
                        num_factors=n, sigma=sigma)
    else:
        print "No fudge-factor table created!"
    #Everything went alright so far
    return True

def single_experiment(experiment_index, toa_strings=(),
                      isotope="Re-187", timestep_size=1e+6):
    """
    Run a single experiment with bestfit values, and a fudge-factor stapled 
    to the isotope. 
    *experiment_index* - int - index of experiment in queue
    *toa_strings* - tuple of all relevant strings (folder, name)
    *isotope* - str - name of isotope to be manipulated
    *timestep_size* - float - size of timestep in experiment
    """
    exp_folder = toa_strings[0] #name of experiment folder
    exp_name = toa_strings[1] #name of experiments
    exp_fudge = "fudge_factors.dat"
    #exp_fudge = toa_strings[2] #name of datafile in folder
    
    #bestfit_special_timesteps = 0 #disable log-timesteps
    #bestfit_dt = timestep_size

    fudge_factor = read_fudge_factor(filename=exp_folder+'/'+exp_fudge,
                                     req_index=experiment_index)
    data_filename = exp_folder + "/" + exp_name + str(experiment_index) + ".npy"

    #instance of experiment-object
    exp_instance = experiment(isotope, fudge_factor, dt=timestep_size)
    #save data to appropriately named file
    exp_instance.save2file(data_filename)
    del exp_instance #delete instance

def default_experiment(toa_strings=(), isotope="Re-187", timestep_size=1e+6):
    """
    Run a single experiment with no fudge_factor
    *toa_strings* - tuple of all relevant strings (folder, name)
    *isotope* - str - name of isotope to be manipulated
    *timestep_size* - float - size of timestep in experiment
    """
    exp_folder = toa_strings[0] #name of experiment folder
    exp_name = toa_strings[1]
    
    fudge_factor = 1.0
    data_filename = exp_folder + "/" + exp_name + "default.npy"

    #instance of experiment-object
    exp_instance = experiment(isotope, fudge_factor, dt=timestep_size)
    #save data to appropriately named file
    exp_instance.save2file(data_filename, write_index_file=True)
    #write number of timepoints to README
    readmestring = "Data from 'default-experiment' \n"
    readmestring += "timestep-number: %d \n"%len(exp_instance.age)
    readmefilename = exp_folder + "/README.md"
    with open(readmefilename, 'a') as readmefile:
        readmefile.write('\n')
        readmefile.write(readmestring)
    #delete object
    del exp_instance #delete instance

def parallel_queueing(toa_strings, num_experiments=10, timestep_size=1e+8):
    """ Description: """
    folder_name, experiment_name = toa_strings
    #timing
    t0 = tm.time()

    ### start queueing processes ###
    #get necessary parameters
    n_cpu = mp.cpu_count() #number of available cpus
    print "number of CPU's available: %d"%n_cpu
    n_cpu -= 1 #take into account the CPU for current this process
    loa_act_proc = [] #active processes
    num_act_proc = 0 #number of active processes
    isotope = "Re-187"

    #spawn one process per experiment
    for index_experiment in range(num_experiments):
        #as long as the cpus are filled, recheck until one is available
        while num_act_proc == n_cpu:
            #check list of processes
            for i in range(num_act_proc):
                proc = loa_act_proc[i]
                act_proc_status = proc.is_alive()
                #print proc.name, act_proc_status
                if not act_proc_status: #process is done
                    #terminate, join, remove
                    proc.terminate()
                    proc.join()
                    loa_act_proc.pop(i) #remove from list
                    num_act_proc -= 1 #update counter
                    break #go out of for loop
                else:
                    continue #go to next process

        #spawn new process and add to list
        arg_experiment_index = index_experiment
        arg_toa_strings = (folder_name, experiment_name)
        arg_isotope = isotope
        arg_timestep_size = timestep_size
        arg_tuple = (arg_experiment_index, arg_toa_strings, arg_isotope, arg_timestep_size)
        new_proc = mp.Process(target=single_experiment, name=index_experiment,
                              args=arg_tuple)
        new_proc.start() #start process
        loa_act_proc.append(new_proc)
        num_act_proc += 1
        
        status = "\nStarting experiment: %d/%d"%(index_experiment,num_experiments)
        print status
        print "="*len(status)

    #wait for all processes to stop
    while num_act_proc > 0:
        #check list of processes
        for i in range(num_act_proc):
            proc = loa_act_proc[i]
            act_proc_status = proc.is_alive()
            #print proc.name, act_proc_status
            if not act_proc_status: #process is done
                #terminate, join, remove
                proc.terminate()
                proc.join()
                loa_act_proc.pop(i) #remove from list
                num_act_proc -= 1 #update counter
                break #go out of for loop
            else:
                continue #go to next process
        

    #timing
    t1 = tm.time()
    total_time = t1 - t0
    
    #save some data to readme-file
    readme_filename = folder_name + "/README.md"
    with open(readme_filename, 'a') as readme:
        #save isotope, stddev, total time, # of experiments to readme-file
        readme.write("GCE timestep: %e yr\n"%timestep_size)
        readme.write("Some parameters for the MC-simulation\n")
        readme.write("Isotope: %s \n"%isotope)
        readme.write("Total time lapsed: %1.4e s \n"%total_time)
        readme.write("Number of experiments: %d \n"%num_experiments)
        readme.write("Number of processors used: %d \n"%n_cpu)

#############
### Cases ###
#############
def case_test():
    print "TEST!"
    folder_name = "test"
    experiment_name = folder_name
    n = 10
    sigma = 0.5
    dt = 3e+8

    start_experiment(folder_name, fudge_factor_tuple=(n, sigma),
                     timestep_size=dt)
    default_experiment(toa_strings=(folder_name, experiment_name), timestep_size=dt)
    parallel_queueing(toa_strings=(folder_name, experiment_name), 
                      num_experiments=n, timestep_size=dt)

def case_1(n):
    print "Starting Run #1"
    print "50% standard deviation"
    sigma = 0.5
    dt = 1e+7
    folder_name = "Case_1"
    experiment_name = "Omega_MCsimulation_Re187_"

    start_experiment(folder_name, fudge_factor_tuple=(n, sigma),
                     timestep_size=dt)
    default_experiment(toa_strings=(folder_name, experiment_name), timestep_size=dt)
    parallel_queueing(toa_strings=(folder_name, experiment_name), 
                      num_experiments=n, timestep_size=dt)

def case_general(exp_number, sigma, timestep_length, names):
    start_experiment(names[0], fudge_factor_tuple=(exp_number, sigma),
                     timestep_size=timestep_length)
    default_experiment(toa_strings=names, timestep_size=timestep_length)
    parallel_queueing(toa_strings=names, 
                      num_experiments=exp_number, timestep_size=timestep_length)

loa_cases = [case_1, case_general] #list of all case-functions

if __name__ == '__main__':
    #make default arguments
    default_sigma = 0.5
    default_dt = 4e+7
    default_iso = "Re-187"
    default_folder_name = "default_folder_name"
    default_experiment_name = "default_experiment_name"
    
    #Use argparse-module to sort program by cmd-line-input
    import argparse as ap
    prog_desc = "This is the parallelized MANIP experiment."
    
    parser = ap.ArgumentParser(description=prog_desc)
    #add argument for number of experiments
    help_string = "Number of experiments done."
    parser.add_argument('N', #'--num_experiments',
                        metavar="n",
                        type=int, help=help_string)
    #add argument for standard deviation
    help_string = "Relative standard deviation fraction of gaussian distribution(applied to *isotope*)."
    parser.add_argument('-s', '--standard_deviation', '--sigma',
                        metavar="SIGMA",dest="sigma",
                        type=float, help=help_string,
                        default=default_sigma)
    #add argument for lenght of timesteps
    help_string = "Length of constant timesteps [yr]."
    parser.add_argument('-dt', '--timestep',
                        metavar="DT",dest="dt",
                        type=float, help=help_string,
                        default=default_dt)
    #add argument for isotope
    help_string = "Isotope to be varied with a gaussian distribution."
    parser.add_argument('-iso', '--isotope',
                        metavar="ISOTOPE",dest="iso",
                        type=str, help=help_string,
                        default=default_iso)
    #add argument for foldder-name and experiment-name
    help_string = "Name of folder for experiment, and name of experiment data-files."
    help_string += "\n\tAn index-value is added to the end of all data-file names."
    parser.add_argument('-f', '--name',
                        metavar="NAME", dest="name",
                        type=str, help=help_string, nargs=2,
                        default=[default_folder_name,default_experiment_name])
    try:
        namespace = parser.parse_args()
    except:
        print "Can't get cmd-line arguments"
        sys.exit("Exiting!")

    n = namespace.N #number of experiments
    s = namespace.sigma #standard deviation
    dt = namespace.dt #timestep length
    iso = namespace.iso #which isotope
    name_strings = namespace.name #folder-name and experiment-name

    case_general(exp_number=n, sigma=s, timestep_length=dt, names=name_strings)
