"""
Best mass parameters: m_tot, m_star, sfr, [O/H], [Fe/H]
"""
#get num-timesteps from cmd-line
import sys, os
try:
    n = int(sys.argv[1])
except:
    n = 10

#import class for handling folder structure of project
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
#import GCE-calculation tool
from omega import omega
#import GCE plotting tool
from visualize import visualize
#import bestfit-parameters accumulated over various versions
from bestfit_param_omega.bestfit_file import *
from bestfit_param_omega.find_bestfit_param_v1.summary import *
import matplotlib.pyplot as pl

run1 = False #True
run2 = False #True
run3 = False #True
run4 = True

### Set mass parameters ###
bestfit_out_follows_E_rate = True #Set outflow \propto SNR insteaad of SFR
bestfit_in_out_control=True #make sure 
bestfit_special_timesteps=150 #default timesteps
bestfit_in_out_ratio=0.1 #set inflow proportional to outflow

def set_omega_param(mgal=bestfit_mgal, mass_loading=bestfit_mass_loading,
                    out_follows_E_rate=bestfit_out_follows_E_rate,
                    in_out_ratio=bestfit_in_out_ratio,
                    outflow_rate=-1.0, inflow_rate=-1.0):
    return omega(mgal=mgal,
                 in_out_ratio=in_out_ratio,
                 mass_loading=mass_loading, 
                 out_follows_E_rate=out_follows_E_rate,
                 outflow_rate=outflow_rate,
                 inflow_rate=inflow_rate,
                 galaxy=bestfit_galaxy,in_out_control=bestfit_in_out_control,SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe,rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0,t_star=bestfit_t_star, sfh_file=bestfit_sfh_file,stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, dt=bestfit_dt, special_timesteps=bestfit_special_timesteps, tend=bestfit_tend, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling,r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm)

def visualize_masses(loa_omegas, loa_names, title, run_string):
    save_name = "variable_plots/vary_masses_%s.png"%run_string
    plot_obj = visualize(loa_omegas, loa_names,
                         num_yaxes=5, yields=True)
    plot_obj.add_time_mass("total", index_yaxis=0)
    plot_obj.add_time_mass("locked", index_yaxis=1)
    plot_obj.add_time_relabu("[O/H]", index_yaxis=2)
    plot_obj.add_time_relabu("[Fe/H]", index_yaxis=3)
    plot_obj.add_time_rate("sf", index_yaxis=4)
    plot_obj.finalize(show=False, save=save_name, title=title)
    return plot_obj

###############################
### different variable-runs ###
"""
Keep all parameters constant according to global variables
Run1: vary mass_loading (outflow)
Run2: vary in_out_ratio (inflow)
Run3: vary mgal (initial gas mass)
Run4: vary constant inflow
"""
###############################

### Run1 ###
"""
Vary mass-loading
"""
if run1:
    factors = [0.1, 0.5, 1.0, 2.0, 10.0]
    mass_loading_values = [fac*bestfit_mass_loading for fac in factors]
    loa_omegas = [set_omega_param(mass_loading=ml) for ml in mass_loading_values]
    loa_names = ["M_l=%1.1e"%ml for ml in mass_loading_values]
    title = r"Vary mass-loading \n $M_{tot}(t_0)$=%1.2e $\frac{\dot{M}_{in}}{\dot{M}_{out}}$=%1.2e"%(bestfit_mgal, bestfit_in_out_ratio)
    #plot total_mass, stellar_mass, [O/H], [Fe/H], SFR
    visualize_masses(loa_omegas, loa_names, title=title, run_string="1")

### Run2 ###
"""
Vary in_out_ratio
"""
if run2:
    factors = [0.1, 0.5, 1.0, 2.0, 10.0]
    ratio_values = [fac*bestfit_in_out_ratio for fac in factors]
    loa_omegas = [set_omega_param(in_out_ratio=ratio) for ratio in ratio_values]
    loa_names = ["R_io=%1.1e"%ratio for ratio in ratio_values]
    title = r"Vary $\frac{\dot{M}_{in}}{\dot{M}_{out}}$ \n $M_{tot}(t_0)$=%1.2e mass-loading=%1.2e"%(bestfit_mgal, bestfit_mass_loading)
    #plot total_mass, stellar_mass, [O/H], [Fe/H], SFR
    visualize_masses(loa_omegas, loa_names, title=title, run_string="2")

### Run3 ###
"""
Vary mgal
"""
if run3:
    factors = [0.1, 0.5, 1.0, 2.0, 10.0]
    mgal_values = [fac*bestfit_mgal for fac in factors]
    loa_omegas = [set_omega_param(mgal=mgal) for mgal in mgal_values]
    loa_names = ["M_0=%1.1e"%mgal for mgal in mgal_values]
    title = r"Vary $M_{tot}(t_0)$ \n mass-loading=%1.2e $\frac{\dot{M}_{in}}{\dot{M}_{out}}$=%1.2e"%(bestfit_mass_loading, bestfit_in_out_ratio)
    #plot total_mass, stellar_mass, [O/H], [Fe/H], SFR
    visualize_masses(loa_omegas, loa_names, title=title, run_string="3")

### Run4 ###
"""
Vary constant inflow
"""
if run4:
    factors = [0.1, 0.5, 1.0, 2.0, 10.0]
    inflow_values = [fac*bestfit_inflow_rate for fac in factors]
    loa_omegas = [set_omega_param(inflow_rate=inflow) for inflow in inflow_values]
    loa_names = ["$\dot{M}_{in}$=%1.1e"%inflow for inflow in inflow_values]
    title = r"Vary constant $\dot{M}_{in}$ \n $M_{tot}(t_0)$=%1.2e mass_loading=%1.2e"%(bestfit_mgal, bestfit_mass_loading)
    #plot total_mass, stellar_mass, [O/H], [Fe/H], SFR
    visualize_masses(loa_omegas, loa_names, title=title, run_string="3")
