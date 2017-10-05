"""
This file sets global parameters for best fit between 
'Omega' and 'Eris'.
Firstly the initial parameters are set, 
then the modification can begin.
Lastly the copy-pasted code is presented in the bottom.
"""
import numpy as np #only do this for the default parameters
from directory_master import Foldermap
folder = Foldermap()

### Initialize bestfit-parameters with the initial parameters ###
bestfit_galaxy = 'none'
bestfit_in_out_control=False
bestfit_SF_law=False
bestfit_DM_evolution=False
bestfit_Z_trans=1e-20
bestfit_f_dyn=0.1
bestfit_sfe=0.1
bestfit_outflow_rate=-1.0
bestfit_inflow_rate=-1.0
bestfit_rand_sfh=0.0
bestfit_cte_sfr=1.0
bestfit_m_DM_0=1.0e11 
bestfit_mass_loading=1.0
bestfit_t_star=-1.0
bestfit_sfh_file='none'
bestfit_in_out_ratio=1.0
bestfit_stellar_mass_0=-1.0
bestfit_z_dependent=True
bestfit_exp_ml=2.0
bestfit_nsmerger_bdys=[8,100]
bestfit_imf_type='kroupa'
bestfit_alphaimf=2.35
bestfit_imf_bdys=[0.1, 100]
bestfit_sn1a_rate='power_law'
bestfit_iniZ=0.0
bestfit_dt=1e6
bestfit_special_timesteps=30
bestfit_tend=13e9
bestfit_mgal=1.0e10
bestfit_transitionmass=8
bestfit_iolevel=0
bestfit_ini_alpha=True
bestfit_nb_nsm_per_m=-1.0
bestfit_t_nsm_coal=-1.0
bestfit_table='yield_tables/agb_and_massive_stars_nugrid_MESAonly_fryer12delay.txt'
bestfit_hardsetZ=-1
bestfit_sn1a_on=True
bestfit_nsm_dtd_power=[]
bestfit_sn1a_table='yield_tables/sn1a_t86.txt'
bestfit_ns_merger_on=False
bestfit_f_binary=1.0
bestfit_f_merger=0.0008
bestfit_t_merger_max=1.0e10
bestfit_m_ej_nsm=2.5e-02
bestfit_nsmerger_table='yield_tables/r_process_rosswog_2014.txt'
bestfit_bhns_merger_on=False
bestfit_m_ej_bhnsm=2.5e-02
bestfit_bhnsmerger_table='yield_tables/r_process_rosswog_2014.txt'
bestfit_iniabu_table=''
bestfit_extra_source_on=False
bestfit_extra_source_table=['yield_tables/extra_source.txt']
bestfit_f_extra_source=[1.0]
bestfit_pre_calculate_SSPs=False
bestfit_extra_source_mass_range=[[8,30]]
bestfit_extra_source_exclude_Z=[[]]
bestfit_pop3_table='yield_tables/popIII_heger10.txt'
bestfit_imf_bdys_pop3=[0.1,100]
bestfit_imf_yields_range_pop3=[10,30]
bestfit_starbursts=[]
bestfit_beta_pow=-1.0
bestfit_gauss_dtd=[1e9,6.6e8]
bestfit_exp_dtd=2e9
bestfit_nb_1a_per_m=1.0e-3
bestfit_f_arfo=1
bestfit_t_merge=-1.0
bestfit_imf_yields_range=[1,30]
bestfit_exclude_masses=[]
bestfit_netyields_on=False
bestfit_wiersmamod=False
bestfit_skip_zero=False
bestfit_redshift_f=0.0
bestfit_print_off=False
bestfit_long_range_ref=False
bestfit_f_s_enhance=1.0
bestfit_m_gas_f=-1.0
bestfit_cl_SF_law=False
bestfit_external_control=False
bestfit_calc_SSP_ej=False
bestfit_tau_ferrini=False
bestfit_input_yields=False
bestfit_popIII_on=True
bestfit_t_sf_z_dep=1.0
bestfit_m_crit_on=False
bestfit_norm_crit_m=8.0e+09
bestfit_mass_frac_SSP=0.5
bestfit_sfh_array_norm=-1.0
bestfit_imf_rnd_sampling=False
bestfit_out_follows_E_rate=False
bestfit_r_gas_star=-1.0
bestfit_cte_m_gas=-1.0
bestfit_t_dtd_poly_split=-1.0
bestfit_stellar_param_on=False
bestfit_delayed_extra_log=False
bestfit_bhnsmerger_dtd_array=np.array([])
bestfit_dt_in_SSPs=np.array([])
bestfit_DM_array=np.array([])
bestfit_nsmerger_dtd_array=np.array([])
bestfit_sfh_array=np.array([])
bestfit_ism_ini=np.array([])
bestfit_mdot_ini=np.array([])
bestfit_mdot_ini_t=np.array([])
bestfit_ytables_in=np.array([])
bestfit_zm_lifetime_grid_nugrid_in=np.array([])
bestfit_isotopes_in=np.array([])
bestfit_ytables_pop3_in=np.array([])
bestfit_zm_lifetime_grid_pop3_in=np.array([])
bestfit_ytables_1a_in=np.array([])
bestfit_ytables_nsmerger_in=np.array([])
bestfit_SSPs_in=np.array([])
bestfit_dt_in=np.array([])
bestfit_dt_split_info=np.array([])
bestfit_ej_massive=np.array([])
bestfit_ej_agb=np.array([])
bestfit_ej_sn1a=np.array([])
bestfit_ej_massive_coef=np.array([])
bestfit_ej_agb_coef=np.array([])
bestfit_ej_sn1a_coef=np.array([])
bestfit_dt_ssp=np.array([])
bestfit_yield_interp='lin'
bestfit_mass_sampled=np.array([])
bestfit_scale_cor=np.array([])
bestfit_mass_sampled_ssp=np.array([])
bestfit_scale_cor_ssp=np.array([])
bestfit_poly_fit_dtd_5th=np.array([])
bestfit_poly_fit_range=np.array([])
bestfit_m_tot_ISM_t_in=np.array([])
bestfit_delayed_extra_dtd=np.array([])
bestfit_delayed_extra_dtd_norm=np.array([])
bestfit_delayed_extra_yields=np.array([])
bestfit_delayed_extra_yields_norm=np.array([])

##################################
### Modify best-fit parameters ###
""" 
Include documentation/reasoning for 
modification
"""
##################################
#input 'Eris'
"""
Taken directly from 'Eris' data
"""
bestfit_imf_type='kroupa93'
sfh_file_dir = "../reproduce_shen/"
sfh_file_relpath = sfh_file_dir+"time_sfr_Shen_2015.txt"
#bestfit_sfh_file=sfh_file_relpath
#get array of time-sfr from sfh-file
bestfit_sfh_array = np.loadtxt(folder.eris_sfh_file)

#present mass values in galaxy
"""
tested in 'test/test_bestfitfile.py'
"""
bestfit_stellar_mass_0=2.0e10 #-1.0
bestfit_m_gas_f=2.0e11 #-1.0
#bestfit_mgal = 
#flows
"""
tested in 'test/test_bestfitfile.py'
"""
bestfit_in_out_control=True #False
bestfit_inflow_rate=3.0 #-1.0 
bestfit_out_follows_E_rate=False
bestfit_mass_loading=0.003 #1.0
#supernovas and kilonovas
"""
Use only CCSN and NS-NSM, same as 'Eris'.
Parameters have been tested in 'test/test_bestfitfile.py'
"""
bestfit_sn1a_on=False #True
bestfit_ns_merger_on=True #False
bestfit_f_binary=1.0 #1.0
bestfit_f_merger=0.0008
bestfit_m_ej_nsm=5.0e-02 #2.5e-5
#control calculation
"""
Modify time, stepnumber and external control
"""
bestfit_dt=1e6
bestfit_special_timesteps=30
bestfit_tend=13e9
bestfit_external_control=False

if __name__ == '__main__': #test the current bestfit parameters
    ### Set cmd-line parameters ###
    from sys import argv
    num_cmdline = len(argv)
    self_name = argv[0]
    n = 20 #number of timesteps
    if num_cmdline >= 2:
        n = int(argv[1])

    #Get module for handling folders correctly
    import directory_master as dir_m
    folder = dir_m.Foldermap() #instance with all the correct folders
    folder.activate_environ() #activate correct global_path in omega
    bestfit_special_timesteps = n #set number timesteps to cmdline
    
    ### Make omega-objects ###
    import NuPyCEE.omega as om
    loa_bestfit_omegas = [om.omega(galaxy=bestfit_galaxy, in_out_control=bestfit_in_out_control, SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe, outflow_rate=bestfit_outflow_rate, inflow_rate=bestfit_inflow_rate, rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0, mass_loading=bestfit_mass_loading, t_star=bestfit_t_star, sfh_file=bestfit_sfh_file, in_out_ratio=bestfit_in_out_ratio, stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, dt=bestfit_dt, special_timesteps=bestfit_special_timesteps, tend=bestfit_tend, mgal=bestfit_mgal, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_out_follows_E_rate, r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm)]
    loa_bestfit_names = ["best fit"]
    
    ###plot with visualize ###
    import visualize as vs
    image_location = folder() + "bestfit_param_omega/"
    plot_spectros = vs.visualize(loa_bestfit_omegas, loa_bestfit_names, num_yaxes=3)
    plot_spectros.add_time_relabu('[O/H]', index_yaxis=0)
    plot_spectros.add_time_relabu('[Fe/H]', index_yaxis=1)
    plot_spectros.add_time_relabu('[Eu/H]', index_yaxis=2)
    plot_spectros.zoom([[-4,1],[-4,1],[-4,1]])
    image_filename = image_location + "bestfit_omega_eris_spectro_n%d"%n
    plot_spectros.finalize(title="Spectroscopic data of bestfit parameters",
                           save=image_filename)
    plot_rates = vs.visualize(loa_bestfit_omegas, loa_bestfit_names, num_yaxes=3)
    plot_rates.add_time_rate('kn',index_yaxis=0,rate_type='one')
    plot_rates.add_time_rate('sn',index_yaxis=1,rate_type='one')
    plot_rates.add_time_rate('sf',index_yaxis=2)
    image_filename = image_location + "bestfit_omega_eris_rates_n%d"%n
    plot_rates.finalize(show=True,
                        title="Rate data of bestfit parameters",
                        save=image_filename)

################################################
### Insert this into the omega-initalization ###
################################################
""" 
galaxy=bestfit_galaxy,
in_out_control=bestfit_in_out_control,
SF_law=bestfit_SF_law,
DM_evolution=bestfit_DM_evolution,
Z_trans=bestfit_Z_trans,
f_dyn=bestfit_f_dyn,
sfe=bestfit_sfe,
outflow_rate=bestfit_outflow_rate,
inflow_rate=bestfit_inflow_rate,
rand_sfh=bestfit_rand_sfh,
cte_sfr=bestfit_cte_sfr,
m_DM_0=bestfit_m_DM_0,
mass_loading=bestfit_mass_loading,
t_star=bestfit_t_star,
sfh_file=bestfit_sfh_file,
in_out_ratio=bestfit_in_out_ratio,
stellar_mass_0=bestfit_stellar_mass_0,
z_dependent=bestfit_z_dependent,
exp_ml=bestfit_exp_ml,
nsmerger_bdys=bestfit_nsmerger_bdys,
imf_type=bestfit_imf_type,
alphaimf=bestfit_alphaimf,
imf_bdys=bestfit_imf_bdys,
sn1a_rate=bestfit_sn1a_rate,
iniZ=bestfit_iniZ,
dt=bestfit_dt,
special_timesteps=bestfit_special_timesteps,
tend=bestfit_tend,
mgal=bestfit_mgal,
transitionmass=bestfit_transitionmass,
iolevel=bestfit_iolevel,
ini_alpha=bestfit_ini_alpha,
nb_nsm_per_m=bestfit_nb_nsm_per_m,
t_nsm_coal=bestfit_t_nsm_coal,
table=bestfit_table,
hardsetZ=bestfit_hardsetZ,
sn1a_on=bestfit_sn1a_on,
nsm_dtd_power=bestfit_nsm_dtd_power,
sn1a_table=bestfit_sn1a_table,
ns_merger_on=bestfit_ns_merger_on,
f_binary=bestfit_f_binary,
f_merger=bestfit_f_merger,
t_merger_max=bestfit_t_merger_max,
m_ej_nsm=bestfit_m_ej_nsm,
nsmerger_table=bestfit_nsmerger_table,
bhns_merger_on=bestfit_bhns_merger_on,
m_ej_bhnsm=bestfit_m_ej_bhnsm,
bhnsmerger_table=bestfit_bhnsmerger_table,
iniabu_table=bestfit_iniabu_table,
extra_source_on=bestfit_extra_source_on,
extra_source_table=bestfit_extra_source_table,
f_extra_source=bestfit_f_extra_source,
pre_calculate_SSPs=bestfit_pre_calculate_SSPs,
extra_source_mass_range=bestfit_extra_source_mass_range,
extra_source_exclude_Z=bestfit_extra_source_exclude_Z,
pop3_table=bestfit_pop3_table,
imf_bdys_pop3=bestfit_imf_bdys_pop3,
imf_yields_range_pop3=bestfit_imf_yields_range_pop3,
starbursts=bestfit_starbursts,
beta_pow=bestfit_beta_pow,
gauss_dtd=bestfit_gauss_dtd,
exp_dtd=bestfit_exp_dtd,
nb_1a_per_m=bestfit_nb_1a_per_m,
f_arfo=bestfit_f_arfo,
t_merge=bestfit_t_merge,
imf_yields_range=bestfit_imf_yields_range,
exclude_masses=bestfit_exclude_masses,
netyields_on=bestfit_netyields_on,
wiersmamod=bestfit_wiersmamod,
skip_zero=bestfit_skip_zero,
redshift_f=bestfit_redshift_f,
print_off=bestfit_print_off,
long_range_ref=bestfit_long_range_ref,
f_s_enhance=bestfit_f_s_enhance,
m_gas_f=bestfit_m_gas_f,
cl_SF_law=bestfit_cl_SF_law,
external_control=bestfit_external_control,
calc_SSP_ej=bestfit_calc_SSP_ej,
tau_ferrini=bestfit_tau_ferrini,
input_yields=bestfit_input_yields,
popIII_on=bestfit_popIII_on,
t_sf_z_dep=bestfit_t_sf_z_dep,
m_crit_on=bestfit_m_crit_on,
norm_crit_m=bestfit_norm_crit_m,
mass_frac_SSP=bestfit_mass_frac_SSP,
sfh_array_norm=bestfit_sfh_array_norm,
imf_rnd_sampling=bestfit_imf_rnd_sampling,
out_follows_E_rate=bestfit_out_follows_E_rate,
r_gas_star=bestfit_r_gas_star,
cte_m_gas=bestfit_cte_m_gas,
t_dtd_poly_split=bestfit_t_dtd_poly_split,
stellar_param_on=bestfit_stellar_param_on,
delayed_extra_log=bestfit_delayed_extra_log,
bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array,
dt_in_SSPs=bestfit_dt_in_SSPs,
DM_array=bestfit_DM_array,
nsmerger_dtd_array=bestfit_nsmerger_dtd_array,
sfh_array=bestfit_sfh_array,
ism_ini=bestfit_ism_ini,
mdot_ini=bestfit_mdot_ini,
mdot_ini_t=bestfit_mdot_ini_t,
ytables_in=bestfit_ytables_in,
zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in,
isotopes_in=bestfit_isotopes_in,
ytables_pop3_in=bestfit_ytables_pop3_in,
zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in,
ytables_1a_in=bestfit_ytables_1a_in,
ytables_nsmerger_in=bestfit_ytables_nsmerger_in,
SSPs_in=bestfit_SSPs_in,
dt_in=bestfit_dt_in,
dt_split_info=bestfit_dt_split_info,
ej_massive=bestfit_ej_massive,
ej_agb=bestfit_ej_agb,
ej_sn1a=bestfit_ej_sn1a,
ej_massive_coef=bestfit_ej_massive_coef,
ej_agb_coef=bestfit_ej_agb_coef,
ej_sn1a_coef=bestfit_ej_sn1a_coef,
dt_ssp=bestfit_dt_ssp,
yield_interp=bestfit_yield_interp,
mass_sampled=bestfit_mass_sampled,
scale_cor=bestfit_scale_cor,
poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th,
poly_fit_range=bestfit_poly_fit_range,
m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in,
delayed_extra_dtd=bestfit_delayed_extra_dtd,
delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm,
delayed_extra_yields=bestfit_delayed_extra_yields,
delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm
"""

""" 
galaxy=bestfit_galaxy, in_out_control=bestfit_in_out_control, SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe, outflow_rate=bestfit_outflow_rate, inflow_rate=bestfit_inflow_rate, rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0, mass_loading=bestfit_mass_loading, t_star=bestfit_t_star, sfh_file=bestfit_sfh_file, in_out_ratio=bestfit_in_out_ratio, stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, dt=bestfit_dt, special_timesteps=bestfit_special_timesteps, tend=bestfit_tend, mgal=bestfit_mgal, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_out_follows_E_rate, r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm 
"""

#Some details regarding __history()
""" 
self.age = []
self.sfr = []
self.gas_mass = []
self.metallicity = []
self.ism_iso_yield = []
self.ism_iso_yield_agb = []
self.ism_iso_yield_massive = []
self.ism_iso_yield_1a = []
self.ism_iso_yield_nsm = []
self.ism_iso_yield_bhnsm = []
self.isotopes = []
self.elements = []
self.ism_elem_yield = []
self.ism_elem_yield_agb = []
self.ism_elem_yield_massive = []
self.ism_elem_yield_1a = []
self.ism_elem_yield_nsm = []
self.ism_elem_yield_bhnsm = []
self.sn1a_numbers = []
self.nsm_numbers = []
self.bhnsm_numbers = []
self.sn2_numbers = []
self.t_m_bdys = []

# Add the evolution arrays to the history class
self.history.m_DM_t = self.m_DM_t
self.history.m_tot_ISM_t = self.m_tot_ISM_t
self.history.m_outflow_t = self.m_outflow_t
self.history.m_inflow_t = self.m_inflow_t
self.history.eta_outflow_t = self.eta_outflow_t
self.history.t_SF_t = self.t_SF_t
self.history.redshift_t = self.redshift_t

# If external control ...
if self.external_control:
self.history.sfr_abs[i] = self.history.sfr_abs[i-1]
"""
