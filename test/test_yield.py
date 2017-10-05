"""
Description: Test various ways of making an 'Experiment'-class that will fuck with the yields of a specific isotope.
TODO:
"""
################################################
### Import modules and set global parameters ###
################################################
#Get module for handling folders correctly
import sys
import directory_master as dir_m
folder = dir_m.Foldermap() #instance with all the correct folders
#Set environment option for the 'Omega' simulation
folder.activate_environ()

#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs
import sys
import numpy as np

#get sfr from Eris-datafile and store as 2D-array
sfh_array = np.loadtxt(folder.eris_sfh_file)

#run a omega simulation
omega_inst = om.omega(special_timesteps=500, sfh_array=sfh_array,
                      inflow_rate=3.0, mass_loading=0.003,
                      sn1a_on=False, ns_merger_on=True,
                      f_binary=1.0, f_merger=0.0008,
                      m_ej_nsm=5.0e-2, mgal=1e11)

#visualize yields with 'visualize.py'
plot_inst = vs.visualize(omega_inst, "Omega",
                         yields=True, num_yaxes=1)
plot_inst.add_yields_single_omega(index_yaxis=0,
                                  nuc_bound=["Re-187", "Os-187",
                                             "Eu-151", "Eu-153"])
plot_inst.finalize(show=False, save="yields_galaxylunch.png")
#visualize spectroscopic evolution between 'Omega' and 'Eris'
plot_inst = vs.visualize(omega_inst, "Omega",
                         num_yaxes=3)
plot_inst.add_time_relabu("[O/H]", index_yaxis=0)
plot_inst.add_time_relabu("[Fe/H]", index_yaxis=1)
plot_inst.add_time_relabu("[Eu/H]", index_yaxis=2)
ylim = [-3,1]
plot_inst.zoom(loa_ylimlist=[ylim,ylim,ylim])
plot_inst.finalize(show=False, save="spectro_galaxylunch.png")
#visualize rates
plot_inst = vs.visualize(omega_inst, "Omega",
                         num_yaxes=3)
plot_inst.add_time_rate("sf", index_yaxis=0)
plot_inst.add_time_rate("ns", index_yaxis=1)
plot_inst.add_time_rate("sn", index_yaxis=2)
plot_inst.finalize(show=True, save="rates_galaxylunch.png")

