"""
Set the newest value of parameters that best approximates 'Eris'.
Do this by importing the latest file of parameters.
"""
#import bestfit-file that sets all parameters to default
from bestfit_param_omega.bestfit_file import *

###################
### IMF and SFR ###
###################
"""
'Eris' gives an time-sfr-array that can be read by 'Omega', 
'Eris' also realizes an imf according to Kroupa 1993.
"""
import numpy as np
from directory_master import Foldermap
folder = Foldermap()
bestfit_imf_type='kroupa93'
bestfit_sfh_array = np.loadtxt(folder.eris_sfh_file)

bestfit_popIII_on = True
bestfit_sn1a_on=False

bestfit_mgal = 4.0e+10
bestfit_in_out_control = True
bestfit_out_follows_E_rate = True
bestfit_mass_loading = 0.1
bestfit_inflow_rate = 1.0

bestfit_ns_merger_on=True
bestfit_nsmerger_table='yield_tables/r_process_arnould_2007.txt'
bestfit_bhns_merger_on=True
bestfit_bhnsmerger_table='yield_tables/r_process_arnould_2007.txt'
bestfit_f_merger = 4e-3
bestfit_m_ej_nsm = 1.3e-2
