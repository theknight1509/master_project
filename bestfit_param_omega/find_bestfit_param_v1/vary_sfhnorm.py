### import modules ###
#local module for project
from directory_master import Foldermap 
folder = Foldermap()
folder.activate_environ()
#GCE calculation and local visualization module
from omega import omega 
from visualize import visualize, eris_data
#get some bestfit-value from 'Eris'
from bestfit_param_omega.find_bestfit_param_v0.set_param_from_eris import *
#get values and filename from document
from read_parameter_space import read_param

#Set cmdline arguments
try:
    from sys import argv
    n = int(argv[1])
except IndexError:
    n = 10
    
#Run calculations of GCE with 'Omega'
timesteps = n
loa_norm_vals, save_name = read_param("sfh_array_norm") #get values from 'parameter_space.txt'
bestfit_mgal = 4.0e+10
loa_omega_inst = [omega(special_timesteps=timesteps, sfh_array_norm=norm,
                        mgal=bestfit_mgal,
                        imf_type=bestfit_imf_type, sfh_array=bestfit_sfh_array,
                        ns_merger_on=bestfit_ns_merger_on, nsmerger_table=bestfit_nsmerger_table)
                   for norm in loa_norm_vals] #omega-instances with new m_gal
loa_omega_names = ["$f_{norm,sfr}$=%1.2f"%norm for norm in loa_norm_vals]
norm_eris = eris_data().sfr["m_growth"][-1]
print norm_eris
loa_omega_inst += [omega(special_timesteps=timesteps, sfh_array_norm=norm_eris,
                        mgal=bestfit_mgal,
                        imf_type=bestfit_imf_type, sfh_array=bestfit_sfh_array,
                        ns_merger_on=bestfit_ns_merger_on, nsmerger_table=bestfit_nsmerger_table)]
loa_omega_names += ["Eris star"]

#visualize masses and sfr with 'visualize'
title = "Vary normalization factor for sfr"
#plot sfr, ism-mass, locked_mass, total_mass
plot_obj = visualize(loa_omega_inst, loa_omega_names, num_yaxes=4)
plot_obj.add_time_mass("total", index_yaxis=0)
plot_obj.add_time_mass("ism", index_yaxis=1)
plot_obj.add_time_mass("locked", index_yaxis=2)
plot_obj.add_time_rate("sf", index_yaxis=3)

plot_obj.finalize(show=True, title=title, save=save_name)
