"""
This is the master-script for handling subprocesses of MonteCarlo 
experiment. Performing code exists in bottom if-test.

Stepwise process:
-create subdirectory for all data
-create data-file of all parameters
-create readme-file for subdirectory
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

def experiment_process(process_index, bestfit_namespace, parameter_filename, data_filename):
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
        experiment_object.save2file(data_filename)
        time_string = experiment_object.chemevol_gettime()
        status_string = "success"
    except:
        time_string = tm.time() - t0
        status_string = "failed"

    #return time and status and name of filename
    return time_string, status_string, data_filename

def modify_namespace(bestfit_namespace, loa_parameter_tuples):
    sys.exit("Exiting!")
    loa_yield_isotopes = []
    loa_yield_values = []
    for parameter_tuple in loa_parameter_tuples:
        continue
    return bestfit_namespace, loa_yield_isotopes, loa_yield_values

if __name__ == '__main__':
    import bestfit_param_omega.current_bestfit as CBF 
    #Perform 'stepwise process' from doc-string

    readme_object = setup(subdirname="test",
                          param_filename="",
                          readme_filename="",
                          loa_parameter_tuples="",
                          num_experiments="",
                          num_processors="")
    sys.exit()
    queue_processes(n_procs=5, n_processors=3, bestfit_namespace=CBF,
                    parameter_filename="test", data_filename_base="test")
