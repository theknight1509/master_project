"""
With the current bestfit values for omega, 
perform several omega-calculations with different dt-values.
Use interpolatation to plot chi-squared with respect to the [Eu/H]
abundance in 'Eris'.
"""

#Necessary modules
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
from omega import omega
from bestfit_param_omega.current_bestfit import *
from visualize import omega_data, eris_data
import numpy as np
import matplotlib.pyplot as pl
from scipy.interpolate import interp1d, CubicSpline
import time, sys

#Make GCE-instances for different dt-values
eris_dict = eris_data().sfgas #spectrographic data from Eris
t_end = 14e+9
loa_dt_values = [2e+7, 4e+7, 5e+7, 7e+7, 8e+7, 1e+8, 2e+8, 4e+8, 5e+8, 7e+8, 1e+9, 2e+9]
loa_dt_values = loa_dt_values[::-1]
loa_omega_dicts = []
loa_omega_timing = []
loa_omega_length = []
for dt_value in loa_dt_values:
    t0 = time.clock()
    try:
        print "testing: %e"%dt_value
        instance = omega(special_timesteps=0,
                         dt=dt_value,
                         tend=t_end,
                         galaxy=bestfit_galaxy, in_out_control=bestfit_in_out_control, SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe, outflow_rate=bestfit_outflow_rate, inflow_rate=bestfit_inflow_rate, rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0, mass_loading=bestfit_mass_loading, t_star=bestfit_t_star, sfh_file=bestfit_sfh_file, in_out_ratio=bestfit_in_out_ratio, stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, mgal=bestfit_mgal, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_out_follows_E_rate, r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm)
    except IndexError: #Don't ask!
        print "%e did not work"%dt_value
        instance = False
    t1 = time.clock()
    #data_dict = omega_data(instance).get_dictionary()
    #loa_omega_dicts.append(data_dict) #store data from omega
    #loa_omega_timing.append(t1-t0)
    #loa_omega_length.append(len(data_dict["time"]))

#Interpolate [Eu/H] over a common time-array
mask_of_infvalues = np.logical_not(np.isinf(eris_dict["[Eu/H]"]))
func_europium_eris = interp1d(x=eris_dict["time"][mask_of_infvalues],
                              y=eris_dict["[Eu/H]"][mask_of_infvalues],
                              bounds_error=False,
                              fill_value="extrapolate")
loa_func_europium_omega = []
for omega_dict in loa_omega_dicts:
    mask_of_infvalues = np.logical_not(np.isinf(omega_dict["[Eu/H]"]))
    func = interp1d(x=omega_dict["time"][mask_of_infvalues],
                    y=omega_dict["Eu/H"][mask_of_infvalues],
                    bounds_error=False,
                    fill_value="extrapolate")
    loa_func_europium_omega.append(func)
#make time-array twice as long as longest time-array
num_t_max = max([len(omega_dict["time"])
                 for omega_dict
                 in loa_omega_dicts]) #length of longest time-array
num_t_common = 2*num_t_max #twice as many timesteps as maximum
num_t_common = 1e+5
common_t_array = np.linspace(0,t_end, num_t_common)
#make europium-arrays from interpolation function and common time
europium_eris = func_europium_eris(common_t_array)
loa_europium_omega = [func(common_t_array) for func
                      in loa_func_europium_omega]

###Calculate chi-squared between omegas and eris###
loa_europium_chi2 = []
for europium_omega in loa_europium_omega:
    #Using Pearson's cumulative test-statistic
    #Source: _wikipedia_/wiki/Chi-squared_distribution
    O = europium_omega
    E = europium_eris
    chi2 = np.sum( (O-E)**2/E )
    loa_europium_chi2.append(chi2)

###Make table###
table = []
table.append([r"$\Delta t$ [yr]", r"n",
              r"$\chi^2$", r"$t_{calc}$ [s]"])
for i in range(len(loa_dt_values)):
    row = ["%1.8e"%(loa_dt_values[i]),
           "%d"%(loa_omega_length[i]),
           "%1.2e"%(loa_europium_chi2[i]),
           "%1.2e"%(loa_omega_timing[i])]
    table.append(row)
#save table to data-file
with open("table.dat", 'w') as outfile:
    for row in table:
        new_line = ""
        for row_elem in row:
            new_line += row_elem + ' '
        new_line += '\n'
        outfile.write(new_line)
#write table with latex syntax
table_string = ""
for row in table:
    for row_elem in row[:-1]:
        table_string += row_elem + r" & "
    table_string += row[-1] + r" \\" + '\n'
#fill in latex-syntax around table
latex_string = r"\begin{table}[]"+'\n'
latex_string += r"\centering"+'\n'
latex_string += r"\caption{Table for resolution of 'Omega'-calculations}"+'\n'
latex_string += r"\label{tab:omega-timestep}"+'\n'
latex_string += r"\begin{tabular}{cccc}"+'\n'
latex_string += table_string
latex_string += r"\end{tabular}"+'\n'
latex_string += r"\end{table}"+'\n'
#write table to tex-file and txt-file
with open("table.tex", 'w') as outfile:
    outfile.write(latex_string)

###Plot chi-squared vs. timestep###
pl.figure(); pl.grid(True)
pl.plot(loa_dt_values, loa_europium_chi2, 'k*')
pl.xlabel(r"timestep $\Delta t$ [yr]")
pl.ylabel(r"$\chi^2 = \Sigma_i \frac{(O_i-E_i)^2}{E_i}$")
pl.legend(loc="best", num_points=1)
pl.savefig("timestep_chisquared.png")
pl.show()
