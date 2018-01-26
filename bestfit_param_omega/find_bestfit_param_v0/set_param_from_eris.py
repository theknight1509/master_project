"""
From looking at 'Eris'(Shen et.al.2015) the Initial Mass Function and Star Formation Rate can be 
determined, also the Compact Object Merger tables must be From Arnould 2007.
"""
from bestfit_param_omega.bestfit_file import *
import numpy as np

###################
### IMF and SFR ###
###################
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
bestfit_bhns_merger_on=False #not present in 'Eris'
bestfit_bhnsmerger_table='yield_tables/r_process_arnould_2007.txt'

###
### Other
###
bestfit_sn1a_on = True
bestfit_tend = 14e+9 #14Gyr simulation

if __name__ == '__main__':
    from directory_master import Foldermap
    folder = Foldermap()
    folder.activate_environ()
    import matplotlib.pyplot as pl
    import sys

    from bestfit_param_omega.omega_new import omega_new
    from visualize import visualize, save_data
    
    "Compare 'Omega' with 'Eris'-parameters, clean slate and milky_way-parameters, milky_way_cte-parameters. Make instances of 'Omega'"
    import bestfit_param_omega.bestfit_file as clean_slate

    #Add an high-res option from cmd-line
    highres_string = ""
    num_time = 5
    try:
        if sys.argv[1] == "highres":
            highres_string = "highres_"
            num_time = 500
    except IndexError: #cmd-line argument does not exist
        pass
    
    clean_slate.bestfit_special_timesteps = num_time
    clean_slate_omega = omega_new(clean_slate)
    
    clean_slate.bestfit_galaxy = "milky_way"
    milky_way_omega = omega_new(clean_slate)
    
    clean_slate.bestfit_galaxy = "milky_way_cte"
    milky_way_cte_omega = omega_new(clean_slate)

    #add current bestfit_parameters to a new namespace
    eris_bestfit = reload(clean_slate)
    eris_bestfit.bestfit_special_timesteps = num_time
    eris_bestfit.bestfit_imf_type = bestfit_imf_type
    eris_bestfit.bestfit_sfh_array = bestfit_sfh_array
    eris_bestfit.bestfit_tend = bestfit_tend
    eris_bestfit.bestfit_ns_merger_on = bestfit_ns_merger_on
    eris_bestfit.bestfit_nsmerger_table = bestfit_nsmerger_table
    eris_bestfit.bestfit_bhns_merger_on = bestfit_bhns_merger_on
    eris_bestfit.bestfit_bhnsmerger_table = bestfit_bhnsmerger_table
    eris_bestfit.bestfit_sn1a_on = bestfit_sn1a_on
    eris_omega = omega_new(eris_bestfit)

    #Make list of all 'Omega' instances and appr. names
    loa_omegas = [eris_omega, clean_slate_omega,
                  milky_way_omega, milky_way_cte_omega]
    loa_omega_names = ["'Eris'", "deafult", "Milky Way default",
                       "Milky Way cte default"]

    if True:
        #plot star-formation, kilonova, and supernova rates
        vis_obj = visualize(loa_omegas, loa_omega_names, num_yaxes=3)
        vis_obj.add_time_rate("sf", index_yaxis=0)
        vis_obj.add_time_rate("sn", index_yaxis=1)
        vis_obj.add_time_rate("kn", index_yaxis=2)
        vis_obj.finalize(show=False, save="data/%seris_parameters_rates"%highres_string)
        #save data from rates
        for i,rate_key in enumerate(["sf", "sn2", "nsns"]):
            save_obj = save_data(loa_omegas)
            save_obj.make_filenames("data/%seris_parameters_rates%d"%(highres_string, i))
            save_obj.make_explanatory_file("File contains rate-arrays of %s"%rate_key,
                                           ["time"]+loa_omega_names,
                                           "Applying 'Eris' to default")
            save_obj.make_numpy_file(["time", rate_key])

    if True:
        #Plot spectroscopic data for [O/H], [Fe/H], [Eu/H]
        vis_obj = visualize(loa_omegas, loa_omega_names,
                            num_yaxes=3)
        vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
        vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
        vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
        vis_obj.finalize(show=False, save="data/%seris_parameters_spectro"%highres_string)
        #save data from spectroscopic plots
        for i,spectro_string in enumerate(["[O/H]", "[Fe/H]", "[Eu/H]"]):
            save_obj = save_data(loa_omegas)
            save_obj.make_filenames("data/%seris_parameters_spectro%d"%(highres_string,i))
            save_obj.make_explanatory_file("File contains spectroscopic arrays for %s"%spectro_string,
                                       ["time"]+loa_omega_names,
                                       "Applying 'Eris' to default")
            save_obj.make_numpy_file(["time", spectro_string])

    if True:
        #plot stellar mass and ism mass
        vis_obj = visualize(loa_omegas, loa_omega_names,
                            num_yaxes=2)
        vis_obj.add_time_mass("locked", index_yaxis=0)
        vis_obj.add_time_mass("gas_mass", index_yaxis=1)
        vis_obj.finalize(show=False, save="data/%seris_parameters_mass"%highres_string)
        #save "gas_mass" and "m_locked"
        for mass_type in ["gas_mass", "m_locked"]:
            save_obj = save_data(loa_omegas)
            save_obj.make_filenames("data/%seris_parameters_%s"%(highres_string,mass_type))
            save_obj.make_explanatory_file("%s measured in solar masses"%mass_type,
                                           ["time"]+loa_omega_names,
                                           "Applying 'Eris' to default")
            save_obj.make_numpy_file(["time", mass_type])

    pl.show()
