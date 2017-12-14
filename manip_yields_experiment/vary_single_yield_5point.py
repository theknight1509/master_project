"""
Choose a single isotope and a standard deviation (normally Re-187 and 15%).
Use 'experiment.py' to vary the yield output with +/- one and three sigmas.
Plot [Eu/H] for the all experiments.
"""

### Import ###
import sys, os
import bestfit_param_omega.current_bestfit as current_bestfit
from experiment import experiment
from visualize import visualize

### set global values ###
isotope = "Eu-151"
stddev_ff = 0.15
mean_ff = 1.0
title = ""
experiment_timesteps = 200
#print information

### make all experiments ###
stddev_indeces = [-3,-1,0,1,3]
#list of fudge factors
loa_fudge_factors = [ mean_ff - stddev_ff*index for index in stddev_indeces]
print loa_fudge_factors
#Perform experiments in comprehensive list
loa_experiments = [experiment(isotope, fudge_factor,
                              input_timesteps=experiment_timesteps,
                              bestfit_namespace=current_bestfit)
                   for fudge_factor in loa_fudge_factors]
#list of names of experiments
loa_names = ["'Omega' $\hat{Y}_{%s}$=%1.3f"%(isotope, fudge_factor)
             for fudge_factor in loa_fudge_factors]

### plot with visualize ###
filename = "yield_%s_5point.png"%(isotope)
#plotting object
vis_object = visualize(loa_experiments, loa_names, num_yaxes=1)
#plot spectroscopic abundance
vis_object.add_time_relabu("[Eu/H]")
vis_object.finalize(show=True, save=filename, title=title)
