"""
Set yield-table for massive/agb stars.
Set parameters for population 3 stars.
Fix [O/H] and [Fe/H].
"""
#necessary imports
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
from bestfit_param_omega.omega_new import omega_new
import matplotlib.pyplot as pl
#get eris-parameters from 'mass-file'
from bestfit_param_omega.find_bestfit_param_v1.set_mass_from_eris import eris_bestfit
from visualize import visualize, save_data

if __name__ == '__main__':
    num_steps = 30
    print "Number of timesteps: ", num_steps

def plot_rates(loa_omegas, loa_omega_names, version_string, expl_string):
    #plot star-formation, kilonova, and supernova rates
    vis_obj = visualize(loa_omegas, loa_omega_names, num_yaxes=3,
                        loa_abu=[], loa_spectro_abu=["[O/H]", "[Fe/H]", "[Eu/H]"])
    vis_obj.add_time_rate("sf", index_yaxis=0)
    vis_obj.add_time_rate("sn", index_yaxis=1)
    vis_obj.add_time_rate("kn", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/star_parameters_%s_n%d"%(version_string, num_steps))
    #save data from rates
    for i,rate_key in enumerate(["sf", "sn2", "nsns"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/star_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("Rate arrays of %s \n%s"%(rate_key, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying star-parameters to 'Omega' with mass-parameters determined")
        save_obj.make_numpy_file(["time", rate_key])

def plot_spectro(loa_omegas, loa_omega_names, version_string, expl_string, exclude_eu=False):
    #Plot spectroscopic data for [O/H], [Fe/H], [Eu/H]
    vis_obj = visualize(loa_omegas, loa_omega_names, num_yaxes=3,
                        loa_abu=[], loa_spectro_abu=["[O/H]", "[Fe/H]", "[Eu/H]"])
    vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
    vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
    vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/star_parameters_%s_n%d"%(version_string,num_steps))
    #save data from spectroscopic plots
    for i,spectro_string in enumerate(["[O/H]", "[Fe/H]", "[Eu/H]"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/star_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("spectroscopic arrays of %s \n%s"%(spectro_string, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying star-parameters to 'Omega' with mass-parameters determined")
        save_obj.make_numpy_file(["time", spectro_string])

##############################
### Repeat mass parameters ###
##############################
if __name__ == '__main__' and False:
    eris_bestfit.bestfit_special_timesteps = 30
    eris_omega = omega_new(eris_bestfit)
    vis_obj = visualize(eris_omega, "'Eris' bestfit", num_yaxes=3)
    vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
    vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
    vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
    vis_obj.finalize(show=True)

####################
### Yield-tables ###
####################
if __name__ == '__main__' and False:
    def_yield_table = eris_bestfit.bestfit_table
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    loa_yield_tables = ["agb_and_massive_stars_cnoni.txt", "agb_and_massive_stars_FRUITY_K06.txt", "agb_and_massive_stars_h1.txt", "agb_and_massive_stars_K10_K06.txt","agb_and_massive_stars_nugrid_FRUITY.txt","agb_and_massive_stars_nugrid_K06.txt","agb_and_massive_stars_nugrid_K10.txt","agb_and_massive_stars_nugrid_MESAonly_fryer12delay.txt","agb_and_massive_stars_nugrid_MESAonly_fryer12delay_wind_preexp.txt","agb_and_massive_stars_nugrid_MESAonly_fryer12mix.txt","agb_and_massive_stars_nugrid_MESAonly_fryer12rapid.txt","agb_and_massive_stars_nugrid_MESAonly_ye.txt","agb_and_massive_stars_nugrid_N13.txt","agb_and_massive_stars_portinari98_marigo01_gce2.txt","agb_and_massive_stars_portinari98_marigo01_gce_totalyields.txt","agb_and_massive_stars_portinari98_marigo01_gce.txt","agb_and_massive_stars_portinari98_marigo01_net_yields_all.txt","agb_and_massive_stars_portinari98_marigo01.txt"]

    for table in loa_yield_tables:
        eris_bestfit.bestfit_table = "yield_tables/"+table
        #skip model if the object with H,O,Fe does not execute properly
        try:
            eris_omega = omega_new(eris_bestfit)
            h_index = eris_omega.history.elements.index("H")
            o_index = eris_omega.history.elements.index("O")
            fe_index = eris_omega.history.elements.index("Fe")
            eu_index = eris_omega.history.elements.index("Eu")
            print "Index of H, O, Fe in 'elements': ", h_index, o_index, fe_index, eu_index
        except:
            continue
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append(table)
    if len(new_list_of_model_names) > 0:
        plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                     version_string="v1",
                     expl_string="Various AGB/Massive yield tables")
    eris_bestfit.bestfit_table = def_yield_table #return to default
#Conclusion (based on least amount of iron and most oxygen)
eris_bestfit.bestfit_table="yield_tables/agb_and_massive_stars_nugrid_MESAonly_fryer12delay_wind_preexp.txt"

####################################
### AGB - Massive transitionmass ###
####################################
if __name__ == '__main__' and False:
    eris_bestfit.bestfit_special_timesteps = num_steps
    def_transmass = eris_bestfit.bestfit_transitionmass
    new_list_of_models = []
    new_list_of_model_names = []

    loa_param_value = [7,8,9,10]
    for t_mass in loa_param_value:
        eris_bestfit.bestfit_transitionmass = t_mass
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/t_mass=%1.1f"%t_mass)
    
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2",
                 expl_string="Changing transitionmass")
    
    eris_bestfit.bestfit_transitionmass = def_transmass #return to default
#Conclusion
#Minimal change if any, might depend on support from specific yield tables

#########################
### Pop3 yield tables ###
#########################
if __name__ == '__main__' and False:
    def_yield_table = eris_bestfit.bestfit_pop3_table
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    loa_yield_tables = ["popIII_h1.txt", "popIII_heger10.txt", "popIII_N13.txt"]

    for table in loa_yield_tables:
        eris_bestfit.bestfit_pop3_table = "yield_tables/"+table
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append(table)

    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v3",
                 expl_string="Various Population III yield tables")
    eris_bestfit.bestfit_pop3_table = def_yield_table #return to default
#Conclusion
#no effect!

###########################
### Pop3 imf-boundaries ###
###########################
if __name__ == '__main__' and False:
    def_bounds = eris_bestfit.bestfit_imf_bdys_pop3
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    loa_bounds = []

    # WAYWAY heavy-sided
    bounds = [20.0,100.0]; loa_bounds.append(bounds)
    # heavy-sided
    bounds = [5.0,100.0]; loa_bounds.append(bounds)
    # medium-sided
    bounds = [1.0,20.0]; loa_bounds.append(bounds)
    # light-sided
    bounds = [0.1,20.0]; loa_bounds.append(bounds)

    for bounds in loa_bounds:
        eris_bestfit.bestfit_imf_bdys_pop3 = bounds
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append(r"'Eris' pop3 imf $\in$ %s"%str(bounds))

    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v4",
                 expl_string="Various Population III imf boundaries")
    eris_bestfit.bestfit_imf_bdys_pop3 = def_bounds
#conclusion
#no effect

pl.show()

