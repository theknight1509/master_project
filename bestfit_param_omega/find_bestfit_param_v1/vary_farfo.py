### import modules ###
#local module for project
from directory_master import Foldermap 
folder = Foldermap()
folder.activate_environ()
#GCE calculation and local visualization module
from omega import omega 
from visualize import visualize 
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
loa_fraction_vals, save_name = read_param("f_arfo") #get values from 'parameter_space.txt'
bestfit_mgal = 3.5e+10
loa_omega_inst = [omega(special_timesteps=timesteps, f_arfo=fraction,
                        imf_type=bestfit_imf_type,
                        sfh_array=bestfit_sfh_array,
                        ns_merger_on=bestfit_ns_merger_on,
                        nsmerger_table=bestfit_nsmerger_table,
                        mgal=bestfit_mgal)
                   for fraction in loa_fraction_vals] #omega-instances with new m_gal
loa_omega_names = ["f=%1.2e"%fraction for fraction in loa_fraction_vals]

#visualize masses and sfr with 'visualize'
title = "Vary fractional yield of massive stars"
#plot sfr, ism-mass, locked_mass, total_mass
plot_obj = visualize(loa_omega_inst, loa_omega_names,
                     num_yaxes=4, yields=True)
plot_obj.add_yields("O", index_yaxis=0, time="sum")
plot_obj.add_yields("Eu", index_yaxis=1, time="sum")
plot_obj.add_time_mass("locked", index_yaxis=2)
plot_obj.add_time_rate("sf", index_yaxis=3)

plot_obj.finalize(show=True, title=title, save=save_name)
