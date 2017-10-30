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
loa_outflow_vals, save_name = read_param("outflow_rate") #get values from 'parameter_space.txt'
bestfit_mgal = 4.0e+10
loa_omega_inst = [omega(special_timesteps=timesteps,
                        in_out_control=True,
                        outflow_rate=outflow,
                        out_follows_E_rate=False,
                        in_out_ratio=0.0,
                        imf_type=bestfit_imf_type, sfh_array=bestfit_sfh_array,
                        ns_merger_on=bestfit_ns_merger_on, nsmerger_table=bestfit_nsmerger_table,
                        mgal=bestfit_mgal)
                  for outflow in loa_outflow_vals] #omega-instances with new outflow
loa_omega_names = ["$\dot{M}_{out}$=%1.2e"%outflow for outflow in loa_outflow_vals]

#visualize masses and sfr with 'visualize'
title = "Vary constant outflow $\dot{M}_{out}$ \n $M_{gal}(t_0)$=%1.1e"%(bestfit_mgal)
#plot sfr, ism-mass, locked_mass, total_mass
plot_obj = visualize(loa_omega_inst, loa_omega_names, num_yaxes=4)
plot_obj.add_time_mass("total", index_yaxis=0)
plot_obj.add_time_mass("outflow", index_yaxis=1)
plot_obj.add_time_mass("locked", index_yaxis=2)
plot_obj.add_time_rate("sf", index_yaxis=3)

plot_obj.finalize(show=True, title=title, save=save_name)
