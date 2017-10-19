"""
"""
### import modules ###
import sys
#local module for project
from directory_master import Foldermap 
folder = Foldermap()
folder.activate_environ()
#GCE calculation and local visualization module
from omega import omega 
from visualize import visualize 
#get some bestfit-value from 'Eris'
from bestfit_param_omega.find_bestfit_param_v0.set_param_from_eris import *

#Set cmdline arguments
try:
    n = int(sys.argv[1])
except IndexError:
    n = 10

#Global variables
global M_star_t0_MW, M_gas_t0_MW, M_baryon_t0_MW
plot_dir = "variable_plots/"

def initialize1():
    global M_star_t0_MW, M_gas_t0_MW, M_baryon_t0_MW
    M_star_t0_MW = (6.43e10, 0.63e10) #[M_sol] #http://adsabs.harvard.edu/abs/2011MNRAS.414.2446M
    M_gas_t0_MW = 6.7e9 #[M_sol] #https://ay201b.wordpress.com/2013/01/14/chapter-density-of-the-milky-ways-ism/
    M_baryon_t0_MW = (M_star_t0_MW[0]+M_gas_t0_MW, M_star_t0_MW[1]+M_gas_t0_MW)
def initialize2():
    global M_star_t0_MW, M_gas_t0_MW, M_baryon_t0_MW
    M_star_t0_MW = (54.3e9, 5.7e9) #[M_sol] #http://adsabs.harvard.edu/abs/2017MNRAS.465...76M
    M_gas_t0_MW = 1.2e9 #[M_sol] #https://ui.adsabs.harvard.edu/#abs/2017MNRAS.465...76M/abstract
    M_baryon_t0_MW = (M_star_t0_MW[0]+M_gas_t0_MW, M_star_t0_MW[1]+M_gas_t0_MW)
    
initialize1() #set global variables
t0 = 13.81e+9 #[yr] age of universe today
"""
#vary the initial mass of gas by a few sigmas
M_0 = M_baryon_t0_MW[0] #value of baryonic mass now
S_0 = M_baryon_t0_MW[1] #std-dev of baryonic mass now
factors = range(-2,3) #+/- 2sigmas
M_init = [M_0+fac*S_0 for fac in factors] #+/- 2sigmas
"""
#vary the initial mass by a few dex
M_0 = M_baryon_t0_MW[0]
factors = [0.1, 0.5, 1.0, 2.0, 10.0]
M_init = [fac*M_0 for fac in factors]

#Run calculations of GCE with 'Omega'
timesteps = n
loa_omega_inst = [omega(special_timesteps=timesteps, imf_type=bestfit_imf_type, sfh_array=bestfit_sfh_array, ns_merger_on=bestfit_ns_merger_on, nsmerger_table=bestfit_nsmerger_table)] #empty omega-instance
loa_omega_names = ["default"]
loa_omega_inst += [omega(special_timesteps=timesteps, mgal=mgal, imf_type=bestfit_imf_type, sfh_array=bestfit_sfh_array, ns_merger_on=bestfit_ns_merger_on, nsmerger_table=bestfit_nsmerger_table)
                   for mgal in M_init] #omega-instances with new m_gal
loa_omega_names += ["$M_{gal}$=%1.1f$M_{gal}(t_0)$"%fac for fac in factors]

#visualize masses and sfr with 'visualize'
title = "Vary $M_{gal}$ \n $M_{gal}(t_0)$=%1.2e"%(M_0)
save_name = plot_dir+"varyMgal_mean%1.2e.png"%(M_0)
#plot sfr, ism-mass, locked_mass, total_mass
plot_obj = visualize(loa_omega_inst, loa_omega_names, num_yaxes=4)
plot_obj.add_time_mass("total", index_yaxis=0)
total_mass_t0 = (t0, M_baryon_t0_MW[0])
total_mass_error = M_baryon_t0_MW[1]
plot_obj.add_datapoint(total_mass_t0, linetype='k*',
                       error=(0,total_mass_error), index_yaxis=0)

plot_obj.add_time_mass("ism", index_yaxis=1)
ism_mass_t0 = (t0, M_gas_t0_MW)
plot_obj.add_datapoint(ism_mass_t0, linetype='k*', index_yaxis=1)

plot_obj.add_time_mass("locked", index_yaxis=2)
star_mass_t0 = (t0, M_star_t0_MW[0])
star_mass_error = M_star_t0_MW[1]
plot_obj.add_datapoint(star_mass_t0, linetype='k*',
                       error=(0, star_mass_error), index_yaxis=2)

plot_obj.add_time_rate("sf", index_yaxis=3)

plot_obj.finalize(show=True, title=title, save=save_name)
