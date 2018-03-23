Manipulate several 'Omega'-parameters simountanously
===============================================================
This readme is for explaining and presenting the current folder.
The general purpose of this folder is to organize a way to manipulate 'Omega' 
into taking a namespace of bestfit-values. Then multiplying some r-process relevant parameters by a "fudge factor" in order to see what the results are.
This folder is a generalization of the procedures in [manipulate-single-variable](../manip_yields_experiment).

Base 'Omega'-class
--------------------
The One-zone Model for the Evolution of GAlaxies is a simple way of calculating the amount of isotopes
in a galaxy by creating simple stellar populations, and distributing their enriched material into the ISM.
This class inherits chemical evolution from 'chemevol'.

Child 'Omega'-class (nicked 'Experiment')
---------------------------------------------
The self-written child class of 'Omega' takes a single argument,
this argument is a namespace full of input arguments for 'Omega' and they describe a 
bestfit parameter-space to fit to the SPH-simulation 'Eris'.
The class calls the init-function of 'Omega' with all the parameters from the namespace.
There is also a function for writing appropriate results to file.

Grandchild 'Omega'-class
---------------------------
This class takes a bestfit-namespace, like it's parent, and the "fudge factors" for some parameters.
The init-file of this class modifies the bestfit-namespace with "fudge factors", and calls the init of
it's parent, which calls the init of 'Omega'

This class also contains functions that override some functions in 'chemevol'.
This is to make sure the "fudge factors" for the isotope-yields are properly applied.
**Need to fix function to handle lists of multiple isotopes and factors**

Parallelized Monte-Carlo method
--------------------------------
The experiment is parallelized in python by calling a master-process that handles all parameters and processes.
Firstly, and apt folder is created, then all parameters are randomly sampled (within their respectable distributions)
and stored in a file, hence refered to as fudge-factor-parameter-datafile. 

The master process then spawns new processes 
until the number of processes (self included) matches the maximum processes allowed.
Maximum amount of processes is dictated by amount of processors, one process per (virtual) processor
means shortest amount of computing time per process before it finishes.

The new process takes an index, treating it as an identity, 
then picks a set of "fudge factors" from the fudge-factor-parameter-datafile.
The "fudge factors" are used to make an instance of 'Experiment', and the relevant 
data are stored to a 2D-numpy-array, with n number of m long arrays in time.
The new process will return a list of arrays in the data-matrix if the experiment is successful.

Data storage
-------------
All data will be created in the new data-folder!

Each model-calculation yields alot of different arrays in time, all of those that are 
deemed relevant are stored in one big two-dimensional matrix and stored with numpy.save.
They can be retrieved with numpy.load.
At the end of the simulation, the master process will write a file with all array-names 
and their appropriate indeces.

The master process will also write a data-file with status from each process, computing time,
number of processes, processors, mismatch in data-array-format, etc.
After all processes are ended, the master process will exit.
