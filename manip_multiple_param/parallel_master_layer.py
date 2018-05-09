"""
This is the master-script for handling subprocesses of MonteCarlo 
experiment. Performing code exists in bottom if-test.

Stepwise process:
-create subdirectory for all data
-create data-file of all parameters
-create readme-file for subdirectory
-run single experiment and write indeces of datadiles to separate file
-spawn subprocess with experiment until maximum count
-store timing of processes

Experiment:
-get parameters from param-file using process index
-start timing
-start model-calculation
-stop timing
-write to file
-check status?
-return time to master-layer

Input arguments:
parameter-names, parameter-means, parameter-stddev, num-processes,
num-processors, bestfit-namespace,
"""
import sys, os
import time as tm
import multiprocessing as mp

from write_experiment_readme import readme
from parameter_table import make_table, read_table
from grandchild_omega import grandchild_omega

def setup(subdirname, param_filename, readme_filename,
          loa_parameter_tuples, num_experiments,
          num_processors):
    """ function for setting up experiment """
    try:
        os.mkdir(subdirname) #create new subdirectory
    except OSError:
        print "subdir %s already exists"%(subdirname)
        response = raw_input("Continue? (y/n)")
        if response == "n":
            sys.exit("Exiting!")
        elif response == "y":
            pass
        else:
            print "Unintelligable"
            sys.exit("Exiting!")
    os.chdir(subdirname) #change to new directory
    print "Changing to directory: %s"%(os.getcwd())
    
    #create data-file of parameters
    make_table(filename=param_filename,
               loa_parameter_tuples=loa_parameter_tuples,
               N=num_experiments)
    #create readme-file
    readme_object = readme(filename=readme_filename)
    date = tm.asctime(tm.localtime(tm.time()))
    readme_object.add_header(date=date)
    readme_object.add_param_info(filename=param_filename,
                                 parameter_tuples=loa_parameter_tuples)
    readme_object.add_mc_info(num_processes=num_experiments, num_processors=num_processors)
    readme_object.write_new_file()
    return readme_object

def queue_processes(n_procs, n_processors, bestfit_namespace, parameter_filename, data_filename_base):
    """function to spawn new processes in queue-system"""
    t0 = tm.time()
    #list of active processes
    loa_active_procs = []
    max_active_procs = n_processors - 1 #dedicate one processor to master-layer
    #for loop over all processes to be spawned
    for proc_index in range(1,n_procs+1):
        #wait until a process is free (the list of active processes has room for one more process)
        loa_active_procs = wait(loa_active_procs, limit_procs=max_active_procs-1)
        #spawn new process with 'proc_index' and add to list of active processes
        data_filename = data_filename_base + "_pid%d"%proc_index
        arg_tuple = (proc_index, bestfit_namespace, parameter_filename, data_filename) #arguments to pass to experiment
        new_proc = mp.Process(target=experiment_process,
                              name=proc_index, args=arg_tuple)
        new_proc.start() #start process
        loa_active_procs.append(new_proc) #add process to list of active processes
    #wait for all active processes to finish
    loa_active_procs = wait(loa_active_procs, limit_procs=0)
    
    t1 = tm.time()
    return t1 - t0

def wait(loa_active_procs, limit_procs):
    """ Iterately go through a list of active processes,
    kill processes that are finished until the limiting 
    amount ('max_active_procs') is reached.
    Return list of processes """
    while len(loa_active_procs) > limit_procs:
        #loop over all active processes and check activity
        for index_active_proc, active_proc in enumerate(loa_active_procs):
            #check if active process is finished
            if not active_proc.is_alive():
                #kill process
                active_proc.terminate()
                active_proc.join()
                #remove from list
                loa_active_procs.pop(index_active_proc) #remove from list
                #break for loop over all acive processes
                break
            else:
                #check next active process
                continue
    return loa_active_procs

def experiment_process(process_index, bestfit_namespace, parameter_filename, data_filename, write_index_file=False):
    """function to pass to parallel process"""
    #get parameters from P-filename and index
    loa_parameter_tuples = read_table(filename=parameter_filename,
                                     index=process_index)
    #modify bestfit-namespace
    bestfit_namespace, loa_yield_isotopes, loa_yield_values \
        = modify_namespace(bestfit_namespace, loa_parameter_tuples)

    #create omega-instance with bestfit-namespace and fudge-factors
    t0 = tm.time()
    try:
        experiment_object = grandchild_omega(bestfit_namespace,
                                         loa_yield_isotopes,
                                         loa_yield_values)
        #save data
        experiment_object.save2file(data_filename, write_index_file=write_index_file)
        time_string = experiment_object._gettime()
        status_string = "success"
    except:
        time_string = tm.time() - t0
        status_string = "failed"
        raise

    #return time and status and name of filename
    return time_string, status_string, data_filename

def modify_namespace(bestfit_namespace, loa_parameter_tuples):
    loa_yield_isotopes = []
    loa_yield_values = []
    for parameter_tuple in loa_parameter_tuples:
        parameter_name = parameter_tuple[0]
        parameter_value = float(parameter_tuple[1])
        if parameter_name == "ej_mass":
            bestfit_namespace.bestfit_m_ej_nsm *= parameter_value
        elif parameter_name == "f_merger":
            bestfit_namespace.bestfit_f_merger *= parameter_value
        # elif parameter_name == "nsm_dtd_slope":
        #     l_dtd = bestfit_namespace.bestfit_nsm_dtd_power #[min,max,slope]
        #     #Choose either -2 or -1 randomly from parameter value
        #     if parameter_value <= 1.0:
        #         l_dtd[2] = -2
        #     else:
        #         l_dtd[2] = -1
        #     #insert list back into namespace
        #     bestfit_namespace.bestfit_nsm_dtd_power = l_dtd
        elif parameter_name == "alphaimf":
            #choose imf-slope from Cote16a
            bestfit_namespace.bestfit_imf_type = "alphaimf"
            bestfit_namespace.bestfit_alphaimf = 2.29
            bestfit_namespace.bestfit_alphaimf *= parameter_value
        elif '-' in parameter_name: #parameter is a isotope-yield
            loa_yield_isotopes.append(parameter_name)
            loa_yield_values.append(parameter_value)
        else:
            print "Warning in 'modify_namespace'! Parameter %s not applied to namespace or yields"%(parameter_name)

    bestfit_namespace.bestfit_special_timesteps = 0
    dt_val = bestfit_namespace.bestfit_dt
    print "Setting special-steps to zero, timestep-size:", dt_val

    return bestfit_namespace, loa_yield_isotopes, loa_yield_values

def param_dict2tuplelist(param_dict):
    """ Turn dictionary of string keys and and string values 
    to list of tuples with gaussian parameters.
    e.g. (param1, mean1, rel_stddev1) """
    param_list = []
    for key in param_dict.keys():
        try:
            val = float(param_dict[key])
            parameter_name = key
            if '-' in parameter_name: #name is a isotope yield
                parameter_name = parameter_name.capitalize()
            param_tuple = (parameter_name, 1.0, val)
            param_list.append(param_tuple)
        except ValueError: #cannot turn value of key to float
            continue
        except: #Any other error
            continue
    return param_list

if __name__ == '__main__':
    ### Get parameters  to omega ###
    import bestfit_param_omega.current_bestfit as CBF
    minimum_dt = 14e+6
    multiple_dt = 2
    CBF.bestfit_dt = multiple_dt*minimum_dt
    print "Using constant timestep with %d times the 'Eris' timestep"%(multiple_dt)

    ### Get experiment setup from config file and parser ###
    loa_config_files = [filename for filename in os.listdir('.')
                        if ('.ini' in filename)]
    print "All config-files: ", loa_config_files
    config_filename = raw_input("Which config-file to use? ")
    import configparser as cp
    config = cp.ConfigParser()
    config.read(config_filename)

    subdir_name = config["montecarlo parameters"]["directory_name"]
    data_files_name = config["montecarlo parameters"]["datafiles_name"]
    parameter_file_name = "parameter_files.dat"
    readme_file_name = "README.md"
    num_experiments = int(config["montecarlo parameters"]["n_experiments"])
    num_processors = int(config["montecarlo parameters"]["n_processors"])

    loa_parameter_tuples = param_dict2tuplelist(config["model parameters"])

    print "Using %s as config file for parameters"%(config_filename)
    
    #Perform 'stepwise process' from doc-string
    #create directory, readme, and paramter-values
    readme_object = setup(subdirname=subdir_name,
                          param_filename=parameter_file_name,
                          readme_filename=readme_file_name,
                          loa_parameter_tuples=loa_parameter_tuples,
                          num_experiments=num_experiments,
                          num_processors=num_processors)
    #Run single experiment with last experiment-index
    experiment_process(process_index=num_experiments,
                       bestfit_namespace=CBF,
                       parameter_filename=parameter_file_name,
                       data_filename=data_files_name + \
                       "_pid%d"%num_experiments,
                       write_index_file=True)
    num_experiments -= 1
    #Run list of subprocesses
    queue_processes(n_procs=num_experiments,
                    n_processors=num_processors,
                    bestfit_namespace=CBF,
                    parameter_filename=parameter_file_name,
                    data_filename_base=data_files_name)
