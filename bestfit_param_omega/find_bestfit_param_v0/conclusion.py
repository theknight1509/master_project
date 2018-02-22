"""
Set all parameters determined in 'set_param_from_eris'
"""
from directory_master import Foldermap
folder = Foldermap()
import numpy as np

bestfit_imf_type='kroupa93'
bestfit_sfh_array = np.loadtxt(folder.eris_sfh_file)

bestfit_ns_merger_on = True
bestfit_bhns_merger_on = True
bestfit_nsmerger_table = 'yield_tables/r_process_arnould_2007.txt'
bestfit_sn1a_on = True
bestfit_tend = 14e+9 #14Gyr simulation
bestfit_dt = 14e+6 #only activated when special_timesteps=0 #1000 constant timesteps
