"""
This script plots all the data from fitting-process of 'Eris'.
"""
####################################
### Imports and global variables ###
####################################
import numpy as np
import matplotlib.pyplot as pl
from visualize import eris_data
eris_data_inst = eris_data()
#directories for data and plots
data_dir = "data_fitting/"
plot_dir = "plots_fitting/"
#boolean switches
plot_all = True #plot all data
locked_param = False #plot all data from version 0
mass_param = False #plot all data from version 1
star_param = False #plot all data from version 2
nsm_param = False #plot all data from version 3

############################
### plots from version 0 ###
############################
if plot_all or locked_param or True:
    print "plotting version 0"
    data_filename = lambda param_type: data_dir + "highres_eris_parameters_%s.npy"%param_type
    #plot_filename = ?
    
    #plot sfr of defaults+'Eris lookalike'+'Eris'
    #plot spectroscopic data of defaults+'Eris lookalike'+'Eris'
    #plot stellar mass and ISM mass of defaults+'Eris lookalike'+'Eris'

"""
    #get arrays from data-file for plotting star formation rate
    filename_sfr = data_dir + filename + "rates0.npy"
    array_sfr = np.load(filename_sfr)
    time = array_sfr[4]
    eris_fit = array_sfr[0]
    default = array_sfr[1]
    mw = array_sfr[2]
    mw_cte = array_sfr[3]
    #adjust lengths
    time = time[:-1]

    #get star-formation rate from 'Eris'-data
    eris_sfr = eris_data_inst.sfr["sfr"]
    eris_time = eris_data_inst.sfr["time"]

    #plot
    pl.grid(True)
    pl.plot(time, eris_fit, label="Eris fit")
    pl.plot(time, default, label="Omega")
    pl.plot(time, mw, label="MW")
    pl.plot(time, mw_cte, label="MW cte")
    pl.plot(eris_time, eris_sfr, label="'Eris' sim")
    pl.legend()
    pl.savefig(plot_dir + "sfr_set_eris_param.png")
    pl.show()

"""

############################
### plots from version 1 ###
############################
if plot_all or mass_param or True:
    None
    #plot stellar mass and total mass with new initial mass and constant inflow
    #plot stellar mass and total mass with added outflow
    #plot total comparison with defaults+'Eris lookalike'+'Eris'
    #-stellar mass
    #-total mass
    #-spectroscopic data
    #-rates    

############################
### plots from version 2 ###
############################
if plot_all or star_param or True:
    None
    #SN1a dtd's
    #SN1a numbers

############################
### plots from version 3 ###
############################
if plot_all or nsm_param or True:
    None
    #dtd
    #ejecta mass
    #merger-fraction/nsm per mass
    #end results

pl.show()
