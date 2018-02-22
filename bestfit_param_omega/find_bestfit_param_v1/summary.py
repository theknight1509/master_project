"""
Summarize what is learned about parameter-space
"""
from bestfit_param_omega.bestfit_file import *
from bestfit_param_omega.find_bestfit_param_v0.set_param_from_eris import *

#initial mass will be modified by gasflow,
#however set a better starting point
bestfit_mgal = 4.0e+10
bestfit_sfh_array_norm = 38914300000.0 #final M_* of 'Eris'
bestfit_in_out_control = True
bestfit_mass_loading = 0.1 #use mass_loading to determine outflow
bestfit_out_follows_E_rate = False
bestfit_inflow_rate = 10.0
#f_binary is unchanged
bestfit_f_merger = 8e-3
bestfit_m_ej_nsm = 2.5e-2
bestfit_t_merger_max = 1.0e+8
bestfit_t_nsm_coal = 1.0e+6
#imf_bdys is unchanged
#f_arfo is unchanged

import sys
sys.exit("This module is currently outdated!")

