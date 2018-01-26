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
isotope = "Re-187"
mean_ff = 1.0
stddev_ff = 0.15
rel_stddev_ff = mean_ff + stddev_ff
experiment_timesteps = 500

### make all experiments ###
loa_multiples_sigma = [3, 1, 0, -1, -3]
loa_fudge_factors = [mean_ff + multiple*stddev_ff for multiple in loa_multiples_sigma]
print loa_fudge_factors
#Perform experiments in comprehensive list
loa_experiments = [experiment(isotope, fudge_factor,
                              input_timesteps=experiment_timesteps,
                              bestfit_namespace=current_bestfit)
                   for fudge_factor in loa_fudge_factors]
#list of names of experiments
loa_names = [r"$\hat{Y}_{%s}=%1.2f\sigma$"%(isotope, sigma)
             for sigma in loa_multiples_sigma]

### plot with visualize ###
title = "Spectroscopic abundance of %s with different yield-output"%(isotope)
filename = "yield_%s_5point.png"%(isotope)
#plotting object
vis_object = visualize(loa_experiments, loa_names, num_yaxes=2, yields=True)
#plot spectroscopic abundance
vis_object.add_time_relabu_omegaonly(isotope)
vis_object.add_yields(nuclide=isotope, index_yaxis=1, time="sum", log_bool=False)
vis_object.finalize(show=False, save=filename,
                    title=title, linewidth=3)

title = "%s abundance in proxy-MW by 'Omega'"%(isotope)
filename = "ism_%s_5point.png"%(isotope)
#plot ism-content for isotope in question.
vis_object = visualize(loa_experiments, loa_names, num_yaxes=2)
#plot spectroscopic abundance
vis_object.add_time_ism(isotope)
vis_object.add_eris_sfr(index_yaxis=1)
vis_object.finalize(show=True, save=filename,
                    title=title, linewidth=3)
