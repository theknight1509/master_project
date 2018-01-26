"""

"""
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
from bestfit_param_omega.omega_new import omega_new
import matplotlib.pyplot as pl

#number of timesteps in current model calculations
num_steps = 300
if __name__ == '__main__':
    print "number of timesteps in simulation: ", num_steps

def plot_rates(loa_omegas, loa_omega_names, version_string, expl_string):
    #plot star-formation, kilonova, and supernova rates
    vis_obj = visualize(loa_omegas, loa_omega_names, num_yaxes=3)
    vis_obj.add_time_rate("sf", index_yaxis=0)
    vis_obj.add_time_rate("sn", index_yaxis=1)
    vis_obj.add_time_rate("kn", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/mass_parameters_%s_n%d"%(version_string, num_steps))
    #save data from rates
    for i,rate_key in enumerate(["sf", "sn2", "nsns"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/mass_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("Rate arrays of %s \n%s"%(rate_key, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying mass parameters to 'Eris' parameters")
        save_obj.make_numpy_file(["time", rate_key])

def plot_spectro(loa_omegas, loa_omega_names, version_string, expl_string):
    #Plot spectroscopic data for [O/H], [Fe/H], [Eu/H]
    vis_obj = visualize(loa_omegas, loa_omega_names,
                        num_yaxes=3)
    vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
    vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
    vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/mass_parameters_%s_n%d"%(version_string,num_steps))
    #save data from spectroscopic plots
    for i,spectro_string in enumerate(["[O/H]", "[Fe/H]", "[Eu/H]"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/mass_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("spectroscopic arrays of %s \n%s"%(spectro_string, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying mass parameters to 'Eris' parameters")
        save_obj.make_numpy_file(["time", spectro_string])
        
def plot_mass(loa_omegas, loa_omega_names, version_string, expl_string):
    #plot stellar mass and total mass
    vis_obj = visualize(loa_omegas, loa_omega_names,
                        num_yaxes=2)
    vis_obj.add_time_mass("locked", index_yaxis=0)
    vis_obj.add_time_mass("total", index_yaxis=1)
    vis_obj.add_datapoint((eris_data().mass["time"][0],eris_data().mass["total_mass"][0]),
                          index_yaxis=1, label="M_b(z=0)")
    vis_obj.add_datapoint((eris_data().mass["time"][1],eris_data().mass["total_mass"][1]),
                          index_yaxis=1, label="M_b(z=1)")
    vis_obj.finalize(show=False, save="data/mass_parameters_%s_n%d"%(version_string, num_steps))
    #save "gas_mass" and "m_locked"
    for i,mass_type in enumerate(["gas_mass", "m_locked", "m_tot"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/mass_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("mass arrays of %s \n%s"%(mass_type, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying mass parameters to 'Eris' parameters")
        save_obj.make_numpy_file(["time", mass_type])

######################
### Default models ###
""" Calculate default 'Omega'-models
to compare with the 'Eris' bestfit """
######################
loa_omegas = []; loa_omega_names = []
if __name__ == '__main__' and True:
    from bestfit_param_omega import bestfit_file as clean_slate
    from visualize import eris_data
    reload(clean_slate)
    clean_slate.bestfit_special_timesteps = num_steps
    #set total mass of model equal to final mass of 'Eris'
    clean_slate.bestfit_mgal = eris_data().mass["total_mass"][-1] 
    clean_slate_omega = omega_new(clean_slate) #with default parameters
    clean_slate.bestfit_galaxy = "milky_way"
    milky_way_omega = omega_new(clean_slate) #with milky way default
    clean_slate.bestfit_galaxy = "milky_way_cte"
    milky_way_cte_omega = omega_new(clean_slate) #with milky way default (const. SFH)
    #make list of models
    loa_omegas += [clean_slate_omega, milky_way_omega, milky_way_cte_omega]
    loa_omega_names += ["default w/M_tot('Eris')", "Milky Way default w/M_tot('Eris')",
                        "Milky Way default w/const. SFH  w/M_tot('Eris')"]
    reload(clean_slate) #important for resetting all parameters in bestfit_file

#############################
### Set 'Eris' parameters ###
""" Set initial mass and inflow to 
get an appropriate total and 
stellar mass """
#############################
import bestfit_param_omega.find_bestfit_param_v0.set_param_from_eris as eris_bestfit
eris_bestfit.bestfit_special_timesteps = num_steps
#eris_bestfit.bestfit_dt = 1e+8

from visualize import eris_data, save_data, visualize
eris_bestfit.bestfit_in_out_control = True
eris_bestfit.bestfit_mass_loading = 0.0 #turn off outflow for now

if __name__ == '__main__' and False:
    new_list_of_models = []
    new_list_of_model_names = []

    loa_init_masses = [4.0e+10, 4.4e+10, 4.5e+10, 5e+10]
    loa_inflow_masses = [3,3.7,6,10]
    for init_mass, inflow_mass in \
        zip(loa_init_masses, loa_inflow_masses):
        #set initial mass of gass
        eris_bestfit.bestfit_mgal = init_mass
        #set inflow of gas
        eris_bestfit.bestfit_inflow_rate = inflow_mass
        
        #Make instance of omega model 
        eris_omega = omega_new(eris_bestfit) #with eris parameters

        #add model to list of models
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append(r"'Eris' $M_0$=%1.1e $\dot{M}$=%1.1f"%(init_mass, inflow_mass))

    plot_mass(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
              version_string="v1", expl_string="Setting outflow to zero, adjust initial mass and constant inflow to match 'Eris' datapoints.")
####################
### conclusion 1 ###
eris_bestfit.bestfit_in_out_control = True
eris_bestfit.bestfit_mgal = 4.4e+10
eris_bestfit.bestfit_inflow_rate = 3.7
####################

#Set outflow to follow SNR, not SFR
eris_bestfit.out_follows_E_rate = True #delayed outflow
#add small increase to inflow to counter outflow
eris_bestfit.bestfit_inflow_rate = 4.0

if __name__ == '__main__' and False:
    new_list_of_models = []
    new_list_of_model_names = []
    loa_ml = [0.3, 0.5, 0.7]
    loa_init_mass = [5.6e+10, 6.6e+10, 7.6e+10]
    for ml, init_mass in zip(loa_ml, loa_init_mass):
        #set outflow of gas from mass-loading
        eris_bestfit.bestfit_mass_loading = ml
        #increase initial gas mass to adjust for outflow
        eris_bestfit.bestfit_mgal = init_mass
    
        #Make instance of omega model 
        eris_omega = omega_new(eris_bestfit) #with eris parameters

        #add model to list of models
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append(r"'Eris' ml=%1.1f"%(ml))

    plot_mass(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
              version_string="v2", expl_string="Adding a small contribution to outflow by ML-factor, adjusting the inflow and initial mass accordingly.")
####################
### conclusion 2 ###
eris_bestfit.bestfit_in_out_control = True
eris_bestfit.out_follows_E_rate = True #delayed outflow
eris_bestfit.bestfit_inflow_rate = 4.0
eris_bestfit.bestfit_mgal = 5.6e+10
eris_bestfit.bestfit_mass_loading = 0.3
####################

if __name__ == '__main__' and True:
    print eris_bestfit.bestfit_galaxy
    eris_omega = omega_new(eris_bestfit) #with eris parameters
    
    #add model to list of models
    loa_omegas.append(eris_omega)
    loa_omega_names.append(r"'Eris'")

    plot_rates(loa_omegas=loa_omegas, loa_omega_names=loa_omega_names,
              version_string="v3_rates", expl_string="Incorporating conclusions into one final mass example.\n Inflow=4.0, ML=0.3, M_init=5.6e+10.")
    plot_spectro(loa_omegas=loa_omegas, loa_omega_names=loa_omega_names,
              version_string="v3_spectro", expl_string="Incorporating conclusions into one final mass example.\n Inflow=4.0, ML=0.3, M_init=5.6e+10.")
    plot_mass(loa_omegas=loa_omegas, loa_omega_names=loa_omega_names,
              version_string="v3_masses", expl_string="Incorporating conclusions into one final mass example.\n Inflow=4.0, ML=0.3, M_init=5.6e+10.")

pl.show()
