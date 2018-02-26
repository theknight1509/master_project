"""
Choose a single isotope and a standard deviation (normally Re-187 and 15%).
Use 'experiment.py' to vary the yield output with +/- one and three sigmas.
Plot [Eu/H] for the all experiments.
"""

### Import ###
import sys, os
import bestfit_param_omega.current_bestfit as cbf
from experiment import experiment
from visualize import visualize

### Global values for controlling experiment ###
global_special_timestep = 0
global_constant_timestep = cbf.bestfit_dt

### Functions for running experiment ###
def get_relative_yields(filename):
    """
    Read 'filename' with isotope, standard value, min and max values.
    Return a dictionary with isotope-keys and a list of 0, +/- sigma, 
    and +/- two sigma.
    """
    doa_iso_yields = {}
    with open(filename, 'r') as infile:
        loa_datarows = infile.readlines() #get list of rows
        loa_datarows.pop(0) #remove header
        for row in loa_datarows:
            col_values = row.split(' ') #split into words
            isotope = col_values.pop(0) #remove iso-string
            col_values = [float(col_value) for col_value in col_values]
            rel_diff_with_index0 = [(val - col_values[0])/col_values[0]
                                    for val in col_values]
            #make list of relative yield uncertainties
            loa_rel_diff = [2*min(rel_diff_with_index0),
                            min(rel_diff_with_index0),
                            0, max(rel_diff_with_index0),
                            2*max(rel_diff_with_index0)]
            doa_iso_yields[isotope] = loa_rel_diff
    return doa_iso_yields

def experiment_with_fudge_factors(isotope, loa_fudge_factors):
    #Perform experiments in comprehensive list
    loa_experiments = [experiment(isotope, fudge_factor,
                                  input_timesteps=global_special_timestep,
                                  dt=global_constant_timestep
                                  bestfit_namespace=cbf)
                   for fudge_factor in loa_fudge_factors]
    #list of names of experiments
    loa_names = [r"$\hat{Y}_{%s}=%1.2f\sigma$"%(isotope, sigma)
                 for sigma in loa_multiples_sigma]

    #save figure
    title = "%s abundance in proxy-MW by 'Omega'"%(isotope)
    filename = "ism_%s_5point.png"%(isotope)
    #plot ism-content for isotope in question.
    vis_object = visualize(loa_experiments, loa_names, num_yaxes=2)
    #plot spectroscopic abundance
    vis_object.add_time_ism(isotope, index_yaxis_0)
    vis_object.finalize(show=True, save=filename,
                        title=title, linewidth=3)
    vis_object.add_yields(nuclide=isotope, index_yaxis=1, time="sum", log_bool=False)


