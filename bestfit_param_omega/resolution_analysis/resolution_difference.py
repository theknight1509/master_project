"""
This script compares the resolution of logarithmic timesteps and constant timesteps.
Using both log. and const. steplengths, the pearson chi squared parameter(chi^2_p) is calculated 
between the eris-data and omega-data. The chi^2_p-value is calculated for
sfr, [O/H], [Fe/H], and [Eu/H].

Procedure:
for a given type and number of steplengths:
-calculate the omega-model
-get the desired arrays from omega-model (time, sfr, [O/H], [Fe/H], and [Eu/H])
-calculate the interpolation-functions from omega-arrays over time (use scipy.interpolate.interp1d)
-calculate the chi^2-value between the eris-data and the interpolated omega-data _ONTO_ the eris-data
-store chi^2-values
"""
### Import modules ###
import sys
import os
import numpy as np

#use omega_new and current_bestfit from 'bestfit'-directory.
from bestfit_param_omega import current_bestfit as cbf
from bestfit_param_omega.omega_new import omega_new

#use data-classes from visualize-script
from visualize import eris_data, omega_data

#interpolation-function
from scipy.interpolate import interp1d

### Procedure for a given instance of omega ###
def calculate_chi2_values(omega_inst):
    """ Calc. chi^2_p values between omega and eris 
    for sfr, [Z/H] interpolated against time. """
    loa_spectro = ["[O/H]","[Fe/H]","[Eu/H]"] #list of [Z/H]
    #get data from omega
    Odata_obj = omega_data(omega_inst, loa_abu=[],
                           loa_spectro_abu=loa_spectro)
    #get data from eris
    Edata_obj = eris_data()

    #dictionary to store pearson chi^2 values per array
    doa_chi2_values = {}

    #first do sfr arrays
    #get time and array from omega
    Odata_time = Odata_obj.get_dictionary()["time_rate"]
    Odata_array = Odata_obj.get_dictionary()["sf"]
    #make interpolation-function from time and array of omega
    Odata_intpol = make_interpolation_object(Odata_time,
                                             Odata_array)
    #get time and array from eris
    Edata_time = eris_data().sfr["time"]
    Edata_array = eris_data().sfr["sfr"]
    #calculate array of omega, interpolated onto time-array of eris
    Ointerp_array = Odata_intpol(Edata_time)
    #calculate chi^2_p of array from eris-data and interpolated omega-data
    chi2_p = pearson_chi2(Ointerp_array, Edata_array)
    #store chi^2_p in dictionary
    doa_chi2_values["sfr"] = chi2_p

    #loop over spectroscopic arrays
    for array_key in loa_spectro:
        #get time and array from omega
        Odata_time = Odata_obj.get_dictionary()["time"]
        Odata_array = Odata_obj.get_dictionary()[array_key]
        #make interpolation-function from time and array of omega
        Odata_intpol = make_interpolation_object(Odata_time,
                                                 Odata_array)
        #use sfgas-dictionary in 'eris_data
        Edata_time = eris_data().sfgas["time"]
        Edata_array = eris_data().sfgas[array_key]
        
        #calculate array of omega, interpolated onto time-array of eris
        Ointerp_array = Odata_intpol(Edata_time)
        #calculate chi^2_p of array from eris-data and interpolated omega-data
        chi2_p = pearson_chi2(Ointerp_array, Edata_array)
        #store chi^2_p in dictionary
        doa_chi2_values[array_key] = chi2_p

    return doa_chi2_values

def pearson_chi2(O,E):
    #remove any zeros from 'E'
    zero_mask = (E != 0.0) #mask away values where E is zero
    E_masked = E[zero_mask]
    O_masked = O[zero_mask]
    inf_mask = np.logical_not(np.isinf(E)) #mask away values where E is inf
    E_masked = E[inf_mask]
    O_masked = O[inf_mask]
    chi2 = (O_masked - E_masked)**2/E_masked
    chi2 = np.sum(chi2)
    return chi2

def make_interpolation_object(time, array):
    #create mask to remove inf-values
    inf_mask = np.logical_not(np.isinf(array))
    interpolation_function = interp1d(x=time[inf_mask],
                                      y=array[inf_mask],
                                      bounds_error=False,
                                      fill_value="extrapolate")
    return interpolation_function

def save_table_datafile(loa_data_strings, filename):
    with open(filename+".dat", 'w') as outfile:
        for line in loa_data_strings:
            outfile.write(line + '\n')
    return

def save_table_markdown(loa_data_strings, filename):
    sep = "|" #markdown table separator
    #fetch header from first element in list
    header = loa_data_strings.pop(0)
    n_comma = header.count(",")
    header = sep + sep.join(header.split(",")) + sep
    #make row (horizontal line) that separates header from table
    horiz = "---".join([sep]*(n_comma+2))
    with open(filename+".md", 'w') as outfile:
        outfile.write(header + '\n')
        outfile.write(horiz + '\n')
        for line in loa_data_strings:
            #replace strings with markdown-separator
            modified_line = sep + sep.join(line.split(",")) + sep
            outfile.write(modified_line + '\n')
    return

def save_table_latex(loa_data_string, filename):
    latex_col_sep = r" & "
    latex_row_sep = r" \\"
    hline = r"\hline"
    #fetch header from first element in list
    header = loa_data_strings.pop(0)
    n_comma = header.count(",")
    header = hline + '\n' + \
             r"$" + \
             (r"$"+latex_col_sep+r"$").join(header.split(",")) + \
             r"$" + latex_row_sep
    #make row (horizontal line) that separates header from table
    horiz = r"\hline"
    with open(filename+".tex", 'w') as outfile:
        outfile.write(r"\begin{table}" + '\n')
        outfile.write(r"\begin{tabular}" + '\n')
        outfile.write(header + '\n')
        outfile.write(horiz + '\n')
        for line in loa_data_strings:
            modified_line = latex_col_sep.join(line.split(",")) \
                            + latex_row_sep
            outfile.write(modified_line + '\n')
        outfile.write(r"\end{tabular}" + '\n')
        outfile.write(r"\end{table}" + '\n')
    return


if __name__ == '__main__':
    #Execute analysis of difference in resolution!
    
    #make list of appropriate timestep-values (constant and special) from test_const_dt
    loa_const_dt_values = [1.6e+7, 2.0e+7, 2.5e+7, 2.8e+7, 4.0e+7,
                           5.0e+7, 7.0e+7, 8.0e+7, 1.0e+8, 2.0e+8,
                           4.0e+8, 5.0e+8, 7.0e+8, 1.0e+9, 2.0e+9, 7.0e+9] 
    loa_const_dt_values = loa_const_dt_values[::-1] #reverse order
    loa_special_timestep_numbers = [] #fill while calculating constant timesteps

    #loop over all __constant__ timestep number
    loa_data_strings = [r"n, \chi^2_{sfr}, \chi^2_{[O/H]}, \chi^2_{[Fe/H]}, \chi^2_{[Eu/H]}, t_{calc}"]
    for constdt in loa_const_dt_values:
        print "constant timestep: %1.4e yr"%constdt
        #set timesteps
        cbf.bestfit_special_timesteps = 0
        cbf.bestfit_dt = constdt
        #calculate omega-model
        omega_obj = omega_new(cbf)
        n_time = len(omega_obj.history.age) #number of timesteps
        time_str = omega_obj._gettime() #get current calculation time
        doa_chi2_values = calculate_chi2_values(omega_obj)
        #make data-string with age-length, chi^2_p-values, time_str
        data_tuple = (n_time, doa_chi2_values["sfr"], doa_chi2_values["[O/H]"],
                      doa_chi2_values["[Fe/H]"], doa_chi2_values["[Eu/H]"], time_str)
        data_str = "%d, %1.4e, %1.4e, %1.4e, %1.4e, %s"%data_tuple
        loa_data_strings.append(data_str)
        loa_special_timestep_numbers.append(n_time) #reuse number of timesteps
    #write data-file from list of all data-strings
    fname = sys.argv[0].split('.')[0] + "_constdt" #use self-filename
    save_table_datafile(loa_data_strings, fname)
    save_table_markdown(loa_data_strings, fname)
    save_table_latex(loa_data_strings, fname)
    
    #loop over all __special__ timestep number
    loa_data_strings = [r"n, \chi^2_{sfr}, \chi^2_{[O/H]}, \chi^2_{[Fe/H]}, \chi^2_{[Eu/H]}, t_{calc}"]
    for num_dt in loa_special_timestep_numbers:
        print "logarithmic timestep: %d timesteps"%num_dt
        #set timesteps
        cbf.bestfit_special_timesteps = num_dt
        #calculate omega-model
        omega_obj = omega_new(cbf)
        n_time = len(omega_obj.history.age) #number of timesteps
        time_str = omega_obj._gettime() #get current calculation time
        doa_chi2_values = calculate_chi2_values(omega_obj)
        #make data-string with age-length, chi^2_p-values, time_str
        data_tuple = (n_time, doa_chi2_values["sfr"], doa_chi2_values["[O/H]"],
                      doa_chi2_values["[Fe/H]"], doa_chi2_values["[Eu/H]"], time_str)
        data_str = r"%d, %1.4e, %1.4e, %1.4e, %1.4e, %s"%data_tuple
        loa_data_strings.append(data_str)
    #write data-file from list of all data-strings 
    fname = sys.argv[0].split('.')[0] + "_logdt" #use self-filename
    save_table_datafile(loa_data_strings, fname)
    save_table_markdown(loa_data_strings, fname)
    save_table_latex(loa_data_strings, fname)
