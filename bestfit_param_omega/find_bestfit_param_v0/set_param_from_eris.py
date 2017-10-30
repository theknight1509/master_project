"""
From looking at 'Eris'(Shen et.al.2015) the Initial Mass Function and Star Formation Rate can be 
determined, also the Compact Object Merger tables must be From Arnould 2007.
"""
from bestfit_param_omega.bestfit_file import *
import numpy as np
from directory_master import Foldermap
folder = Foldermap()

###################
### IMF and SFR ###
###################
"""
'Eris' gives an time-sfr-array that can be read by 'Omega', 
'Eris' also realizes an imf according to Kroupa 1993.
"""
bestfit_imf_type='kroupa93'
bestfit_sfh_array = np.loadtxt(folder.eris_sfh_file)

########################
### r-process tables ###
########################
"""
Only the r-process tables from Arnould et.al. 2007 have contributions
from Re-187 (which is essential for this project)
"""
bestfit_ns_merger_on=True
bestfit_nsmerger_table='yield_tables/r_process_arnould_2007.txt'
bestfit_bhns_merger_on=True
bestfit_bhnsmerger_table='yield_tables/r_process_arnould_2007.txt'

if __name__ == '__main__':
    """
    Use visualize to show how the parameters presented affect 'Omega'.
    Show one set of data from 'Eris', one set of data from _default_ 'Omega',
    and one set of data from 'Omega' with the new parameters.
    """
    folder.activate_environ()
    from omega import omega

    n = 150
    default_omega = omega(special_timesteps=n)
    new_omega = omega(special_timesteps=n,
                      imf_type=bestfit_imf_type,
                      sfh_array=bestfit_sfh_array,
                      ns_merger_on=bestfit_ns_merger_on,
                      bhns_merger_on=bestfit_bhns_merger_on,
                      nsmerger_table=bestfit_nsmerger_table,
                      bhnsmerger_table=bestfit_bhnsmerger_table)

    #compare with visualize 
    from visualize import visualize
    #plot [Fe/H], [O/H], [Eu/H]
    plot_spectro_shen = visualize([default_omega, new_omega],
                                  ["default", "bestfit"],
                                  num_yaxes=3)
    plot_spectro_shen.add_time_relabu("[Fe/H]", index_yaxis=0)
    plot_spectro_shen.add_time_relabu("[O/H]", index_yaxis=1)
    plot_spectro_shen.add_time_relabu("[Eu/H]", index_yaxis=2)
    ylim_spectro = [-5,1]
    plot_spectro_shen.zoom(loa_ylimlist=[ylim_spectro,ylim_spectro,
                                         ylim_spectro])
    plot_spectro_shen.finalize(title="Bestfit parameters from 'Eris'", show=False, save="bestfit_param_eris_spectroplot.png")
    #plot SN-rate, NS-rate, SF-rate
    plot_rates_shen = visualize([default_omega, new_omega],
                                ["default", "bestfit"],
                                num_yaxes=3)
    plot_rates_shen.add_time_rate(rate="sn", index_yaxis=0,
                                  rate_type="sum")
    plot_rates_shen.add_time_rate(rate="sf", index_yaxis=1,
                                  rate_type="sum")
    plot_rates_shen.add_time_rate(rate="kn", index_yaxis=2,
                                  rate_type="sum")
    plot_rates_shen.finalize(title="Bestfit parameters from 'Eris'", show=True, save="bestfit_param_eris_rateplot.png")

del folder #remove the instance of 'directory_master', just because.
