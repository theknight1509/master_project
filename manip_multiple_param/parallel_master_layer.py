"""
This is the master-script for handling subprocesses of MonteCarlo 
experiment.

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
