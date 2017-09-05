"""
Use 'visualization' and 'Omega' to compare [Eu/H], [Os/H], [Re/H], [Re-187/H], and [Os-187/H]

Description:
"""
################################################
### Import modules and set global parameters ###
################################################
#Get module for handling folders correctly
import sys
import directory_master as dir_m
folder = dir_m.Foldermap() #instance with all the correct folders
#Set environment option for the 'Omega' simulation
import os
os.environ['SYGMADIR'] = folder.nupycee[:-1]
#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs

########################################################
### Run 'Omega' calculation with best-fit parameters ###
""" Best-fit parameters still in progress """
########################################################
num_steps = 140

#get SFR from Shen(2015)/'Eris'
sfh_file_dir = "../reproduce_shen/"
sfh_file_relpath = sfh_file_dir+"time_sfr_Shen_2015.txt"
### make instances of 'Omega' and 'visualize' ###
rncp_omega_obj = om.omega(special_timesteps=num_steps,
                          sfh_file=sfh_file_relpath,
                          imf_type="kroupa93",
                          ns_merger_on=True, f_merger=0.01,
                          nb_nsm_per_m=0.5)
rncp_plot_obj = vs.visualize(rncp_omega_obj, r"$\Omega$",
                             num_yaxes=3, age=0)
#subplot [Eu/H] for all data
rncp_plot_obj.add_time_relabu("[Eu/H]", 0)
#subplot [Eu/H], [Re/H], [Os/H] for 'Omega' data
rncp_plot_obj.add_time_relabu_singleomega("[Eu/H]", 1)
rncp_plot_obj.add_time_relabu_singleomega("[Os/H]", 1)
rncp_plot_obj.add_time_relabu_singleomega("[Re/H]", 1)
#subplot [Eu/H], [Re-187/H], [Os-187/H] for 'Omega' data
rncp_plot_obj.add_time_relabu_singleomega("[Eu/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-187/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Re-187/H]", 2)
#show
rncp_plot_obj.finalize(save="rncp_1.png",
                       title="Rapid Neutron Capture Processes")

### make new plot with new visualize-object ###
rncp_plot_obj = vs.visualize(rncp_omega_obj, r"$\Omega$",
                             num_yaxes=3, age=0)
#subplot [Eu, Re, Os/H] for 'Omega' data
rncp_plot_obj.add_time_relabu_singleomega("[Eu/H]", 0)
rncp_plot_obj.add_time_relabu_singleomega("[Re/H]", 0)
rncp_plot_obj.add_time_relabu_singleomega("[Os/H]", 0)
#subplot [Re, Re-iso/H] for 'Omega' data
rncp_plot_obj.add_time_relabu_singleomega("[Re/H]", 1)
rncp_plot_obj.add_time_relabu_singleomega("[Re-185/H]", 1)
rncp_plot_obj.add_time_relabu_singleomega("[Re-187/H]", 1)
#subplot [Eu/H], [Re-187/H], [Os-187/H] for 'Omega' data
rncp_plot_obj.add_time_relabu_singleomega("[Os/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-184/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-186/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-187/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-188/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-189/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-190/H]", 2)
rncp_plot_obj.add_time_relabu_singleomega("[Os-192/H]", 2)
#show
rncp_plot_obj.finalize(show=True,
                       #save="rncp_2_isotopes.png",
                       title="Rapid Neutron Capture Processes")

#use omega-plotting syntax
rncp_omega_obj.plot_iso_ratio(yaxis="[Re-187/H]", fig=3)
