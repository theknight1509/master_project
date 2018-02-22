"""
Calculate the chi^2 parameter between one set of 'Eris' arrays and matching set of 'Omega' arrays
"""

### Imports and Global statement ###
import sys
import numpy as np
from scipy.interpolate import interp1d

def pearson_chi2(observed, expected):
    #sources for statistic:
    #http://www.economics.soton.ac.uk/staff/aldrich/1900.pdf p.165
    #https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test
    chi2 = (observed-expected)**2/expected
    return np.sum(chi2)

def chi2_eris_omega(x_eris, y_eris, x_omega, y_omega):
    """
    Make an interpolation function to map the omega-data
    onto the eris-data, y'_omega=y_omega(x_eris).
    Then calculate the pearson chi^2 parameter between
    y_eris and y'_omega.
    """
    #make mask for removing inf-values in y_omega
    inf_mask = np.logical_not(np.isinf(y_omega))
    #make interpolation function with scipy
    interpolation_omega = interp1d(x=x_omega[inf_mask], y=y_omega[inf_mask],
                                   bounds_error=False, fill_value="extrapolate")
    #map y_omega to x_eris values
    y_omega_onto_eris = interpolation_omega(x_eris)
    chi2_value = pearson_chi2(y_omega_onto_eris, y_eris)
    return chi2_value
