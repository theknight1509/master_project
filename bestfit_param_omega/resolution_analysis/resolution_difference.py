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

#use new_omega and current_bestfit from 'bestfit'-directory.

#Procedure for a given instance of omega
def todo(omega_inst):
    #get data from omega
    #get data from eris

    #dictionary to store pearson chi^2 values per array

    #loop over desired arrays
    for TODO:
        #get time and array from omega
        #make interpolation-function from time and array of omega
        #get time and array from eris
        #TODO REMEMBER SFR/SFGAS SPECIAL CASE IN ERIS

        #calculate array of omega, interpolated onto time-array of eris
        #calculate chi^2_p of array from eris-data and interpolated omega-data
        #store chi^2_p in dictionary

    return doa_chi2_values

