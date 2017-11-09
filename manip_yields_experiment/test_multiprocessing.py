import sys, os
import multiprocessing as mp
import time as tm

def add_5s():
    """ Global function that keeps adding up a counter for 5 sec. Additor """
    t_0 = tm.time() #[s]
    t_lapsed = t_0 - t_0 #[s]
    t_final = 5.0 #[s]
    counter = 0
    #print "\nAdding 1 for %d seconds..."%t_final
    process_info("Additor")
    while t_lapsed < t_final:
        counter += 1
        t_i = tm.time()
        t_lapsed = t_i - t_0
    print mp.current_process().name + " finished! result=%d"%counter
    
def process_info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()
    print 'name of current process:', mp.current_process().name

"""
### Run additor globally ##
add_5s()

### Spawn a process -> run two additors ###
p_name = "John"
print "\nSpawning new process:", p_name
#process_info("Global main")
add_5s()
proc = mp.Process(target=add_5s, name=p_name)
proc.start()
proc.join()

### Repeat, in tandem ###
print "\n Running processes in tandem"
loa_p_name = ["John"]
loa_p_name += ["Kelly", "Fred", "Linda"]
loa_p_name += ["Locke", "Vale", "Buck"]
doa_proc = {}
for p_name in loa_p_name:
    print "Spawning new process:", p_name
    proc = mp.Process(target=add_5s, name=p_name)
    doa_proc[p_name] = proc
for p_name in loa_p_name:
    print "Starting process:", p_name
    proc = doa_proc[p_name]
    proc.start()
for p_name in loa_p_name:
    print "Joining process:", p_name
    proc = doa_proc[p_name]
    proc.join()
"""

### Find number of CPU's available, fill them ###
n_cpu = mp.cpu_count()
loa_names = ["John", "Kelly", "Fred", "Linda",
             "Locke", "Vale", "Buck",
             "Keyes", "Johnson", "Halsey"]
loa_act_proc = [] #active processes
num_act_proc = 0 #number of active processes

#as long as there are more processes to run, spawn new processes
while loa_names: 
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
    new_name = loa_names.pop(0)
    new_proc = mp.Process(target=add_5s, name=new_name)
    new_proc.start() #start process
    loa_act_proc.append(new_proc)
    num_act_proc += 1
