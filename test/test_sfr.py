"""
Description: Test various ways of inserting the 'Eris'-sfr
into the 'Omega'-calculation. This is done by a sfh-file, 
and a sfh-array from the data in 'reproduce_shen'-directory.
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
import os
os.environ['SYGMADIR'] = folder.nupycee[:-1]
#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs
import sys
import numpy as np
import matplotlib.pyplot as pl

###############################################
### Get boolean test-switches from cmd-line ###
###############################################

print "Using boolean cmd-line args: *all* *test1* *test2* etc."
try:
    test_all = bool(int(sys.argv[1]))
except:
    test_all = True
try:
    test_array_bool = [bool(int(arg)) for arg in sys.argv[2:]]
except:
    test_array_bool = []
    
num_tests = 3
while len(test_array_bool) < num_tests:
    test_array_bool.append(False)
num_steps = 350

###########################################
### Tests various ways of inserting SFR ###
###########################################

#relative path to sfh-file from 'NuPyCEE'-directory
sfh_file_dir = "../reproduce_shen/"
sfh_file_relpath1 = sfh_file_dir+"time_sfr_Shen_2015.txt"
sfh_file_relpath2 = sfh_file_dir+"timegal5e8_sfr_Shen_2015.txt"

if test_all or test_array_bool[0]:
    print "First test, vanilla 'Omega'"
    om.omega(special_timesteps=num_steps)

if test_all or test_array_bool[1]:
    print "Second test, sfh-file"
    sfh_file_omega = om.omega(special_timesteps=num_steps,
                              sfh_file=sfh_file_relpath1)
    #plot sfr
    plotting_object = vs.visualize(sfh_file_omega,
                                   "Omega(sfh-file)",
                                   age=0)
    plotting_object.add_time_sfr()
    #plotting_object.add_tbirth()
    plotting_object.finalize(show=True)

    
if test_all or test_array_bool[2]:
    print "Third test, sfh-array"
    sfh_array = np.loadtxt(folder.nupycee + sfh_file_relpath1)
    sfh_array_omega = om.omega(special_timesteps=num_steps,
                               sfh_array=sfh_array)
    #plot sfr
    plotting_object = vs.visualize(sfh_array_omega,
                                   "Omega(sfh-array)")
    plotting_object.add_time_sfr()
    #plotting_object.add_tbirth()
    plotting_object.finalize(show=True)

"""
def __init__(self, 

galaxy='none', in_out_control=False, SF_law=False, \
DM_evolution=False, Z_trans=1e-20, f_dyn=0.1, sfe=0.1, \
outflow_rate=-1.0, inflow_rate=-1.0, rand_sfh=0.0, cte_sfr=1.0, \
m_DM_0=1.0e11, mass_loading=1.0, t_star=-1.0, sfh_file='none', \
in_out_ratio=1.0, stellar_mass_0=-1.0, \
z_dependent=True, exp_ml=2.0, nsmerger_bdys=[8, 100], \
imf_type='kroupa', alphaimf=2.35, imf_bdys=[0.1,100], \
sn1a_rate='power_law', iniZ=0.0, dt=1e6, special_timesteps=30, \
tend=13e9, mgal=1.0e10, transitionmass=8, iolevel=0, \
ini_alpha=True, nb_nsm_per_m=-1.0, t_nsm_coal=-1.0,\
table='yield_tables/agb_and_massive_stars_nugrid_MESAonly_fryer12delay.txt', \
hardsetZ=-1, sn1a_on=True, nsm_dtd_power=[],\
sn1a_table='yield_tables/sn1a_t86.txt',\
ns_merger_on=False, f_binary=1.0, f_merger=0.0008,\
t_merger_max=1.0e10, m_ej_nsm = 2.5e-02, \
nsmerger_table = 'yield_tables/r_process_rosswog_2014.txt', \
bhns_merger_on=False, m_ej_bhnsm=2.5e-02, \
bhnsmerger_table = 'yield_tables/r_process_rosswog_2014.txt', \
iniabu_table='', extra_source_on=False, \
extra_source_table=['yield_tables/extra_source.txt'], \
f_extra_source=[1.0], pre_calculate_SSPs=False, \
extra_source_mass_range=[[8,30]], \
extra_source_exclude_Z=[[]], \
pop3_table='yield_tables/popIII_heger10.txt', \
imf_bdys_pop3=[0.1,100], imf_yields_range_pop3=[10,30], \
starbursts=[], beta_pow=-1.0, gauss_dtd=[1e9,6.6e8],exp_dtd=2e9,\
nb_1a_per_m=1.0e-3, f_arfo=1, t_merge=-1.0,\
imf_yields_range=[1,30],exclude_masses=[], \
netyields_on=False,wiersmamod=False,skip_zero=False,\
redshift_f=0.0,print_off=False,long_range_ref=False,\
f_s_enhance=1.0,m_gas_f=-1.0, cl_SF_law=False,\
external_control=False, calc_SSP_ej=False, tau_ferrini=False,\
input_yields=False, popIII_on=True, t_sf_z_dep = 1.0,\
m_crit_on=False, norm_crit_m=8.0e+09, mass_frac_SSP=0.5,\
sfh_array_norm=-1.0, imf_rnd_sampling=False,\
out_follows_E_rate=False,\
r_gas_star=-1.0, cte_m_gas = -1.0, t_dtd_poly_split=-1.0,\
stellar_param_on=False, delayed_extra_log=False,\
bhnsmerger_dtd_array=np.array([]), dt_in_SSPs=np.array([]), \
DM_array=np.array([]), nsmerger_dtd_array=np.array([]),\
sfh_array=np.array([]),ism_ini=np.array([]),\
mdot_ini=np.array([]), mdot_ini_t=np.array([]),\
ytables_in=np.array([]), zm_lifetime_grid_nugrid_in=np.array([]),\
isotopes_in=np.array([]), ytables_pop3_in=np.array([]),\
zm_lifetime_grid_pop3_in=np.array([]), ytables_1a_in=np.array([]),\
ytables_nsmerger_in=np.array([]), SSPs_in=np.array([]),\
dt_in=np.array([]), dt_split_info=np.array([]),\
ej_massive=np.array([]), ej_agb=np.array([]),\
ej_sn1a=np.array([]), ej_massive_coef=np.array([]),\
ej_agb_coef=np.array([]), ej_sn1a_coef=np.array([]),\
dt_ssp=np.array([]),yield_interp='lin',\
mass_sampled=np.array([]), scale_cor=np.array([]),\
mass_sampled_ssp=np.array([]), scale_cor_ssp=np.array([]),\
poly_fit_dtd_5th=np.array([]), poly_fit_range=np.array([]),\
m_tot_ISM_t_in=np.array([]),\
delayed_extra_dtd=np.array([]), delayed_extra_dtd_norm=np.array([]), \
delayed_extra_yields=np.array([]), delayed_extra_yields_norm=np.array([])):
"""
