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
from bestfit_param_omega.bestfit_file import *

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
sfh_file_dir = "bestfit_param_omega/"
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
