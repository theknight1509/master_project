"""
Email from cote:

plt.figure(figsize=(7.0,5.3))
# Get the CC SNe and kilona rates
r_sne = o.history.sn2_numbers[1:] / o.history.timesteps
r_kilo = o.history.nsm_numbers[1:] / o.history.timesteps
# Plot results
plt.plot(np.array(o.history.age[1:])/1e9, r_sne, 
color='b', label='CC SNe')
plt.plot(np.array(o.history.age[1:])/1e9, r_kilo, 
color='r', label='Kilonovae')
plt.yscale('log')
plt.ylim(1e-7,1e0)
"""

from directory_master import Foldermap as FM
folder = FM()
folder.activate_environ()
from bestfit_param_omega.current_bestfit import *
import matplotlib.pyplot as pl
from omega import omega

bestfit_special_timesteps = 100
O1 = omega(special_timesteps=bestfit_special_timesteps,
           ns_merger_on=True)
O2 = omega(galaxy=bestfit_galaxy, in_out_control=bestfit_in_out_control, SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe, outflow_rate=bestfit_outflow_rate, inflow_rate=bestfit_inflow_rate, rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0, mass_loading=bestfit_mass_loading, t_star=bestfit_t_star, sfh_file=bestfit_sfh_file, in_out_ratio=bestfit_in_out_ratio, stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, dt=bestfit_dt, special_timesteps=bestfit_special_timesteps, tend=bestfit_tend, mgal=bestfit_mgal, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_out_follows_E_rate, r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm)

pl.figure(figsize=(7.0,5.3)); pl.hold(True)
# Get the CC SNe and kilona rates
r_sne = O1.history.sn2_numbers[1:] / O1.history.timesteps
r_kilo = O1.history.nsm_numbers[1:] / O1.history.timesteps
# Plot results
pl.plot(np.array(O1.history.age[1:])/1e9, r_sne, 
        linestyle='-', color='b', label='CC SNe O1')
pl.plot(np.array(O1.history.age[1:])/1e9, r_kilo, 
        linestyle='-', color='r', label='Kilonovae O1')
r_sne = O2.history.sn2_numbers[1:] / O2.history.timesteps
r_kilo = O2.history.nsm_numbers[1:] / O2.history.timesteps
# Plot results
pl.plot(np.array(O2.history.age[1:])/1e9, r_sne, 
        linestyle=':', color='b', label='CC SNe O2')
pl.plot(np.array(O2.history.age[1:])/1e9, r_kilo, 
        linestyle=':', color='r', label='Kilonovae O2')

pl.yscale('log')
pl.ylim(1e-7,1e0)
pl.ylabel("Rate [1/yr]")
pl.xlabel("Galactic age [Gyr]")
pl.legend()

pl.show()
