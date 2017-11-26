"""
General version of 'constant_timestep_omega.py'.
Write a new subclass of 'Omega' designed to test the 
resolution of 'Omega' with respect to different timesteps,
both constant and special(logaritmic).
"""

### Imports and Global statement ###
import sys
import time
import numpy as np

from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
from omega import omega
from bestfit_param_omega.current_bestfit import *
from visualize import omega_data, eris_data
from scipy.interpolate import interp1d

global_endtime = 14e+9
global_spectro_key = "[Eu/H]"

### Subclass of 'Omega' ###
class timesteps_omega(omega):
    """ 
    Get all 'Omega'-arguments from bestfit, except for the the arguments related
    to time-resolution. 
    Redefine a function in 'Omega' so that, for all negative values of special_timesteps,
    the simulation stops after '__copy_sfr_array()
    """
    def __init__(self, special=0, constant=1e+9, t_end=global_endtime):
        """
        Arguments:
        'special' - number of logarithmic timesteps in 'Omega'
        'constant' - length of each constant timestep in 'Omega' [yr]
        't_end' - time after final iteration [yr]

        When 'special' is zero; 
        logarithmic timesteps are deactivated.
        When 'special' is negative; 
        logarithmic timesteps are deactivated, and 'Omega' stops after timesteps are calculated.
        When 'special' is positive;
        logarithmic timesteps are used instead of constant timesteps.
        """
        self.special_timestep = special #store value of special_timestep
        omega.__init__(self,
                       special_timesteps=special,
                       dt=constant,
                       tend=t_end,
                       galaxy=bestfit_galaxy, in_out_control=bestfit_in_out_control, SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe, outflow_rate=bestfit_outflow_rate, inflow_rate=bestfit_inflow_rate, rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0, mass_loading=bestfit_mass_loading, t_star=bestfit_t_star, sfh_file=bestfit_sfh_file, in_out_ratio=bestfit_in_out_ratio, stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, mgal=bestfit_mgal, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_out_follows_E_rate, r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm)

    def _omega__copy_sfr_array(self):

        '''
        See copy_sfr_input() for more info.

        '''
   
        # Variable to keep track of the OMEGA's timestep
        i_dt_csa = 0
        t_csa = 0.0
        nb_dt_csa = self.nb_timesteps + 1
        
        # Variable to keep track of the total stellar mass from the input SFH
        m_stel_sfr_in = 0.0

        # For every timestep given in the array (starting at the second step)
        for i_csa in range(1,len(self.sfh_array)):

            # Calculate the SFR interpolation coefficient
            a_sfr = (self.sfh_array[i_csa][1] - self.sfh_array[i_csa-1][1]) / \
                    (self.sfh_array[i_csa][0] - self.sfh_array[i_csa-1][0])
            b_sfr = self.sfh_array[i_csa][1] - a_sfr * self.sfh_array[i_csa][0]

            # While we stay in the same time bin ...
            while t_csa <= self.sfh_array[i_csa][0]:

                # Interpolate the SFR
                self.sfr_input[i_dt_csa] = a_sfr * t_csa + b_sfr

                # Cumulate the stellar mass formed
                m_stel_sfr_in += self.sfr_input[i_dt_csa] * \
                    self.history.timesteps[i_dt_csa]

                # Exit the loop if the array is full
                if i_dt_csa >= nb_dt_csa:
                    break

                # Calculate the new time
                t_csa += self.history.timesteps[i_dt_csa]
                i_dt_csa += 1

            # Exit the loop if the array is full
            if (i_dt_csa + 1) >= nb_dt_csa:
                break

        # If the array has been read completely, but the sfr_input array is
        # not full, fil the rest of the array with the last read value
        if self.sfh_array[-1][1] == 0.0:
            sfr_temp = 0.0
        else:
            sfr_temp = self.sfr_input[i_dt_csa-1]
        while i_dt_csa < nb_dt_csa - 1:
            self.sfr_input[i_dt_csa] = sfr_temp
            m_stel_sfr_in += self.sfr_input[i_dt_csa] * \
                self.history.timesteps[i_dt_csa]
            t_csa += self.history.timesteps[i_dt_csa]
            i_dt_csa += 1

        # Normalise the SFR in order to be consistent with the integrated
        # input star formation array (no mass loss considered!)
        if self.sfh_array_norm > 0.0:
            norm_sfr_in = self.sfh_array_norm / m_stel_sfr_in
            for i_csa in range(0, nb_dt_csa):
                self.sfr_input[i_csa] = self.sfr_input[i_csa] * norm_sfr_in

        # Fill the missing last entry (extention of the last timestep, for tend)
        # Since we don't know dt starting at tend, it is not part of m_stel_sfr_in
        self.sfr_input[-1] = self.sfr_input[-2]

        #ADD SECTION WHERE NEGATIVE SPECIAL_TIMESTEP STOPS CODE IF IT WORKS
        if self.special_timestep < 0:
            "self.special_timestep is negative, quiting omega early"
            self.external_control = True

### Functions for testing, comparing, and plotting ###
def plotting_function(axis, x_list, y_list, constant=False):
    if constant:
        color = "k"
        marker = "o"
        label = "Constant timestep"
    else:
        color = "b"
        marker = "s"
        label = "Logarithmic timestep"
    """
    #set axis-limits
    x_max = max(x_list)
    x_min = min(x_list)
    delta_x = x_max - x_min
    fraction_x = 0.1*delta_x
    x_limits = [x_min - fraction_x, x_max + fraction_x]
    #axis.set_xlim(x_limits)
    """
    axis.plot(x_list, y_list, marker=marker, color=color, label=label, linestyle='None')
    return True

def test_constant_timestep(loa_constant_timesteps):
    #make sure omega stops if succesful also (too much calculation)
    print "Testing constant steplengths"
    special_timesteps = -1
    loa_constant_timesteps = list(loa_constant_timesteps)
    result_list = []#list for storing results
    #for all timestep-values...
    for constant_timestep in loa_constant_timesteps:
        #... check if omega-breaks
        try:
            instance = timesteps_omega(special_timesteps, constant_timestep)
            status = True
            del instance
        except IndexError: #omega breaks down due to error in constant timestep-length
            status = False
        except: #don't know what's wrong
            print "I don't know how, but you f**ked up!"
            sys.exit("Exiting!")
        #... store results as True/False
        print "\tstatus of timestep-length %1.0e: %s"%(constant_timestep, status)
        result_list.append(status)

    #Make table of results
    table = []
    table_name = "Constant_timestep_test_table"
    table_format = (r"$\Delta t$", "Passed?")
    table.append(table_format)
    for i, dt in enumerate(loa_constant_timesteps):
        some_tuple = (dt, result_list[i])
        table.append(some_tuple)
    save_table(table_name, table) #save table of data

    return result_list #list of T/F values

def resolution_function(loa_constant_timesteps, loa_special_timesteps):
    """
    Resolution is calculated by choosing a timestep for omega and calculate the spectrographic
    data. The data are used to calculate a interpolation function.
    The chi^2-values for all interpolation functions is calculated using a separate time-array
    with twice as many time-points as the omega data with the most time-points.
    This is done for both special timesteps and constant timesteps.
    """
    loa_const_tuples = []
    loa_special_tuples = []
    max_n = 0 #maximum number of data points among all simulations

    # calculate resolution for the list of special timesteps

    #loop over all special timestep values...
    for special_timestep in loa_special_timesteps:
        #tuple (special_n, I(t), n_points, calc_time)
        some_tuple = get_single_interpolation(special_timestep=special_timestep)
        #print "resolution-function() - 1st special forloop - tuple: \n\t", some_tuple
        n = some_tuple[2]
        if n > max_n:
            max_n = n
        loa_special_tuples.append(some_tuple)
    eris_interpolation = get_eris_interpolation() # interpolation function for eris data
    interpolation_time = np.linspace(0, global_endtime, 2*max_n) #interpolation time-axis
    eris_interpolated = eris_interpolation(interpolation_time) #interpolated array

    special_table_format = ("n", pearson_chi2.__name__, astro_chi2.__name__,
                             relative_chi2.__name__, "time-points", "calculation-time")
    #print "resolution-function() - special table format - tuple: \n\t", special_table_format
    special_table = []
    special_table.append(special_table_format)
    #loop over special timestep tuple...
    for timestep_tuple in loa_special_tuples:
        #unpack tuple (n, I(t), n_points, calc_time)
        n, interpolation_function, n_points, calc_time = timestep_tuple
        #... calculate all chi2-values
        omega_interpolated = interpolation_function(interpolation_time)        
        chi2_p = pearson_chi2(omega_interpolated, eris_interpolated)
        chi2_a = astro_chi2(omega_interpolated, eris_interpolated)
        chi2_r = relative_chi2(omega_interpolated, eris_interpolated)
        #... make new tuple of results (dt, chi2_p, chi2_a, chi2r, n_points, calc_time)
        result_tuple = (n, chi2_p, chi2_a, chi2_r, n_points, calc_time)
        #print "resolution-function() - 2nd special forloop - tuple: \n\t", result_tuple
        #... add tuple of results to table
        special_table.append(result_tuple)

    # calculate resolution for the list of constant timesteps
    
    #loop over all constant timestep values...
    for constant_timestep in loa_constant_timesteps:
        #tuple (dt, I(t), n_points, calc_time)
        some_tuple = get_single_interpolation(constant_timestep=constant_timestep)
        #print "resolution-function() - 1st constant forloop - tuple: \n\t", some_tuple
        n = some_tuple[2]
        if n > max_n:
            max_n = n
        loa_const_tuples.append(some_tuple)

    constant_table_format = ("dt", pearson_chi2.__name__, astro_chi2.__name__,
                             relative_chi2.__name__, "time-points", "calculation-time")
    #print "resolution-function() - constant table format - tuple: \n\t", constant_table_format
    constant_table = []
    constant_table.append(constant_table_format)
    #loop over constant timestep tuple...
    for timestep_tuple in loa_const_tuples:
        #unpack tuple (dt, I(t), n_points, calc_time)
        dt, interpolation_function, n_points, calc_time = timestep_tuple
        #... calculate all chi2-values
        omega_interpolated = interpolation_function(interpolation_time)
        chi2_p = pearson_chi2(omega_interpolated, eris_interpolated)
        chi2_a = astro_chi2(omega_interpolated, eris_interpolated)
        chi2_r = relative_chi2(omega_interpolated, eris_interpolated)
        #... make new tuple of results (dt, chi2_p, chi2_a, chi2r, n_points, calc_time)
        result_tuple = (dt, chi2_p, chi2_a, chi2_r, n_points, calc_time)
        #print "resolution-function() - 2nd constant forloop - tuple: \n\t", result_tuple
        #... add tuple of results to table
        constant_table.append(result_tuple)

    return constant_table, special_table

def save_table(filename, table):
    #pure data file
    with open(filename+".dat", 'w') as outfile:
        for row_tuple in table:
            #turn all elements into strings
            row = [str(row_elem) for row_elem in row_tuple]
            outfile.write( ' '.join(row) + '\n' )

    #latex file
    table_string = ""
    for row_tuple in table:
        row = [str(row_elem) for row_elem in row_tuple]
        row_string = " & ".join(row)
        table_string += row_string + " \\ \n"
    #fill in latex-syntax around table
    latex_string = r"\begin{table}[]"+'\n'
    latex_string += r"\centering"+'\n'
    latex_string += r"\caption{Table for resolution of 'Omega'-calculations}"+'\n'
    latex_string += r"\label{tab:omega-timestep}"+'\n'
    latex_string += r"\begin{tabular}{cccc}"+'\n'
    latex_string += table_string
    latex_string += r"\end{tabular}"+'\n'
    latex_string += r"\end{table}"+'\n'
    with open(filename+".tex", 'w') as outfile:
        outfile.write(latex_string)
    return True

def get_single_interpolation(special_timestep=0, constant_timestep=1e+9):
    #start timing
    t0 = time.clock()
    #make instance of omega-subclass
    instance = timesteps_omega(special_timestep, constant_timestep)
    #stop timing
    t1 = time.clock()
    t_gce = t1 - t0
    #make interpolation function from data in omega-subclass
    interpolation_function, n = get_interpolation_function(instance)
    #make tuple of relevant data
    if special_timestep == 0:
        resolution = constant_timestep
    else:
        resolution = special_timestep
    tuple_of_relevant_data = (resolution, interpolation_function, n, t_gce)
    return tuple_of_relevant_data

def get_interpolation_function(omega_instance):
    #get dictionary of data from omega-instance
    omega_data_instance = omega_data(omega_instance)
    data_dict = omega_data_instance.get_dictionary()
    #get time and spectrographic arrays from dictionary
    time_array = data_dict["time"]
    spectro_array = data_dict[global_spectro_key]
    #delete unnecessary objects
    del omega_instance
    del omega_data_instance
    del data_dict
    #make mask for removing inf-values
    mask_of_infvalues = np.logical_not(np.isinf(spectro_array))
    #make interpolation function with scipy
    interpolation_function = interp1d(x=time_array[mask_of_infvalues],
                                      y=spectro_array[mask_of_infvalues],
                                      bounds_error=False,
                                      fill_value="extrapolate")
    return interpolation_function, len(time_array)

def get_eris_interpolation():
    #get data from 'Eris'
    eris_instance = eris_data()
    eris_dict = eris_instance.sfgas #spectrographic data from Eris
    #get spectro_array
    time_array = eris_dict["time"]
    spectro_array = eris_dict[global_spectro_key]
    #delete unnecessary objects
    del eris_instance; del eris_dict
    #make interpolation_function that are not 'inf'
    mask_of_infvalues = np.logical_not(np.isinf(spectro_array))
    interpolation_function = interp1d(x=time_array[mask_of_infvalues],
                                      y=spectro_array[mask_of_infvalues],
                                      bounds_error=False,
                                      fill_value="extrapolate")
    return interpolation_function


### Independant functions ###
def pearson_chi2(O,E):
    chi2 = (O - E)**2/np.abs(E)
    chi2 = np.sum(chi2)
    #print O,E
    #sys.exit()
    return chi2

pearson_chi2.__str__ = r"Pearson $\chi^2$"
def astro_chi2(O,E):
    chi2 = (O - E)**2
    chi2 = np.sum(chi2)
    return chi2

astro_chi2.__str__ = r"Astrophysical $\chi^2$"
def relative_chi2(O,E):
    chi2 = (O - E)**2/len(E)
    chi2 = np.sum(chi2)
    return chi2

relative_chi2.__str__ = r"Relative $\chi^2$"

### Program action ###
if __name__ == '__main__':
    import matplotlib.pyplot as pl

    #set resolution-parameters by default
    loa_test_constant_timesteps = []
    loa_test_constant_timesteps += range(int(1e+9), int(1e+10), int(1e+9))
    loa_test_constant_timesteps += range(int(1e+8), int(1e+9), int(1e+8))
    loa_test_constant_timesteps += range(int(1e+7), int(1e+8), int(1e+7))
    loa_test_constant_timesteps += range(int(1e+6), int(1e+7), int(1e+6))
    loa_test_constant_timesteps += range(int(1e+5), int(1e+6), int(1e+5))
    constant_timesteps = [2e+7, 4e+7, 5e+7, 7e+7, 8e+7, 1e+8, 2e+8, 4e+8, 5e+8, 7e+8, 1e+9, 2e+9]
    special_timesteps = [5, 10, 20, 30, 40, 50, 100, 150, 200, 500]

    #get cmd-line arguments
    num_arg = len(sys.argv)
    if num_arg == 3:
        first_arg = eval(sys.argv[1])
        second_arg = eval(sys.argv[2])
        if isinstance(first_arg, list) and isinstance(second_arg, list):
            #two lists, use them as constant and special
            constant_timesteps = first_arg
            special_timesteps = second_arg
    elif num_arg == 2:
        first_arg = sys.argv[1]
        if first_arg.lower() == "test":
            print "Would you like to test the following constant timesteps?"
            print loa_test_constant_timesteps
            response = raw_input("y/n\n")
            if response == "y":
                loa_test_results = test_constant_timestep(loa_test_constant_timesteps)
            elif response == "n":
                response = raw_input("please give list of timesteps\n")
                loa_test_constant_timesteps = eval(response)
                loa_test_results = test_constant_timestep(loa_test_constant_timesteps)
            else:
                print "What??"
                raise Exception
    elif num_arg == 1:
        print "would you like to proceed with these lists?"
        print "constant_timesteps; ", constant_timesteps
        print "special_timesteps; ", special_timesteps
        response = raw_input("y/n\n")
        if response == "y":
            pass
        elif response == "n":
            sys.exit("Exiting!")
        else:
            print "What??"
            raise Exception

    #calculate resolution-data
    #table-format (dt/n, chi2_p, chi2_a, chi2_r, n_points, calc_time)
    constant_table, special_table = resolution_function(constant_timesteps, special_timesteps)
    #save data
    table_filename = "resolutiontable"
    save_table(table_filename+"_constant", constant_table)
    save_table(table_filename+"_special", special_table)
    #calculate "plotables" from data, extract sublists from tables and name them appropriately
    constant_dt_values = [row[0] for row in constant_table[1:]]
    constant_n_values = [row[4] for row in constant_table[1:]]
    constant_chi2_p_values = [row[1] for row in constant_table[1:]]
    constant_chi2_a_values = [row[2] for row in constant_table[1:]]
    constant_chi2_r_values = [row[3] for row in constant_table[1:]]
    special_n_values = [row[4] for row in special_table[1:]]
    special_chi2_p_values = [row[1] for row in special_table[1:]]
    special_chi2_a_values = [row[2] for row in special_table[1:]]
    special_chi2_r_values = [row[3] for row in special_table[1:]]
    #make figures and axes objects for plotting difference
    fig_name_list = [pearson_chi2.__name__, astro_chi2.__name__, relative_chi2.__name__]
    fig_str_list = [pearson_chi2.__str__, astro_chi2.__str__, relative_chi2.__str__]
    constant_value_list = [constant_chi2_p_values, constant_chi2_a_values, constant_chi2_r_values]
    special_value_list = [special_chi2_p_values, special_chi2_a_values, special_chi2_r_values]
    default_rectangle = (0,0,1,1) #(left, bottom, width, height) #fraction of figure dims
    for i in range(len(fig_name_list)):
        fig = pl.figure(fig_name_list[i])
        """
        constant_axis = fig.add_subplot(111)
        plotting_function(constant_axis, constant_dt_values,
                          constant_value_list[i], fig_str_list[i],
                          constant=True)
        #make a new axis, inverted, on top
        special_axis = constant_axis.twiny()
        special_axis.invert_xaxis()
        special_axis.set_xscale('log')
        special_axis.xaxis.tick_top()
        plotting_function(special_axis, special_dt_values,
                          special_value_list[i], fig_str_list[i],
                          constant=False)
        """
        axis = fig.add_subplot(111)
        axis.grid(True)
        axis.set_title("Resolution of 'Omega' compared to 'Eris'")
        axis.set_xlabel("number of timepoints")
        axis.set_ylabel(fig_str_list[i])
        plotting_function(axis, constant_n_values,
                          constant_value_list[i],
                          constant=True)
        plotting_function(axis, special_n_values,
                          special_value_list[i],
                          constant=False)
        axis.legend(numpoints=1, loc='best')
        #save figures
        figname = "timestep_resolution_" + fig_name_list[i] + ".png"
        fig.savefig(figname)
    pl.show()
