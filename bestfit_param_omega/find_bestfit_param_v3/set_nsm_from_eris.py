"""
#TODO

delay-time distribution of nsm: P(t) \propto t^{-n}, from t_cutoff to t_H
-parameter-values: t_H = 14 Gyr, t_cutoff = [100, 200] Myr, n = [2,1]
-'Omega' parameter input: nsm_dtd_power = [t_cutoff, t_H, -n]
"""
#necessary imports
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
from bestfit_param_omega.omega_new import omega_new
import matplotlib.pyplot as pl
#get eris-parameters from 'sn1a-file'
from bestfit_param_omega.find_bestfit_param_v2.set_sn1a_from_cote import eris_bestfit
from visualize import visualize, save_data

if __name__ == '__main__':
    num_steps = 300
    print "Number of timesteps: ", num_steps

def plot_rates(loa_omegas, loa_omega_names, version_string, expl_string):
    #plot star-formation, kilonova, and supernova rates
    vis_obj = visualize(loa_omegas, loa_omega_names, num_yaxes=3)
    vis_obj.add_time_rate("sf", index_yaxis=0)
    vis_obj.add_time_rate("sn", index_yaxis=1)
    vis_obj.add_time_rate("kn", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/nsm_parameters_%s_n%d"%(version_string, num_steps))
    #save data from rates
    for i,rate_key in enumerate(["sf", "sn2", "nsns"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/nsm_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("Rate arrays of %s \n%s"%(rate_key, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying nsm-parameters to 'Omega' with mass-parameters determined")
        save_obj.make_numpy_file(["time", rate_key])

def plot_spectro(loa_omegas, loa_omega_names, version_string, expl_string):
    #Plot spectroscopic data for [O/H], [Fe/H], [Eu/H]
    vis_obj = visualize(loa_omegas, loa_omega_names,
                        num_yaxes=3)
    vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
    vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
    vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/nsm_parameters_%s_n%d"%(version_string,num_steps))
    #save data from spectroscopic plots
    for i,spectro_string in enumerate(["[O/H]", "[Fe/H]", "[Eu/H]"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/nsm_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("spectroscopic arrays of %s \n%s"%(spectro_string, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying nsm-parameters to 'Omega' with mass-parameters determined")
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

####################################
### Set DTD for BNSM from Shen15 ###
""" 
f_merger, nsm_dtd_power, nb_nsm_per_m, m_ej_nsm, t_nsm_coal"""
####################################
if __name__ == '__main__' and False:
    #try changing dtd
    eris_bestfit.bestfit_special_timesteps = num_steps
    t_H = eris_bestfit.bestfit_tend #hubbletime
    new_list_of_models = []
    new_list_of_model_names = []
    loa_t_min = [50e+6,50e+6,100e+6, 200e+6]
    loa_nsm_pow = [-3,-2,-2,-1]
    for t_min,nsm_pow in zip(loa_t_min, loa_nsm_pow):
        eris_bestfit.bestfit_nsm_dtd_power = [t_min, t_H, nsm_pow]
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/nsm_dtd_pow=[%1.1e,%1.1e,%1.1f]"%(t_min, t_H, nsm_pow))
    eris_bestfit.bestfit_nsm_dtd_power = [] #deactivate

    #look for similar effect in t_nsm_coal
    def_t_coal = eris_bestfit.bestfit_t_nsm_coal#default
    loa_timescale = [1e+7, 1e+8, 1e+9]
    for timescale in loa_timescale:
        eris_bestfit.bestfit_t_nsm_coal = timescale
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/t_nsm_coal=%1.1e"%(timescale))
    eris_bestfit.bestfit_t_nsm_coal =  def_t_coal #return to default

    plot_spectro(loa_omegas=new_list_of_models,
                 loa_omega_names=new_list_of_model_names,
                 version_string="v1",
                 expl_string="Applying different nsm-dtd to 'Eris' parameters")
#conclusions with dtd
#little difference between t_nsm_coal and distributions at those timescales
dtd = [100e+6, eris_bestfit.bestfit_tend, -2] #'Eris' distribution in Shen (2015)
dtd = [50e+6, eris_bestfit.bestfit_tend, -3] #more preferable
dtd = [50e+6, eris_bestfit.bestfit_tend, -2] #'Eris' distribution with earlier minimum time.
coal_time = 1e+7

#Use coal_time for now...
#eris_bestfit.bestfit_t_nsm_coal = coal_time
#use _a_ appropriate dtd
eris_bestfit.bestfit_nsm_dtd_power = dtd

if __name__ == '__main__' and False:
    #try changing ejecta mass
    eris_bestfit.bestfit_special_timesteps = num_steps
    def_ej_mass = eris_bestfit.bestfit_m_ej_nsm
    new_list_of_models = []
    new_list_of_model_names = []
    loa_ejmass = [1e-3, 1e-1, 2e-1, 3e-1, 1.0]
    for ejmass in loa_ejmass:
        eris_bestfit.bestfit_m_ej_nsm = ejmass
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/ej_mass=%1.1e"%(ejmass))
        
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_ejmass",
                 expl_string="Applying different ejecta masses to 'Eris' parameters")
    eris_bestfit.bestfit_m_ej_nsm = def_ej_mass #return to default
#conclusion
#singlehandedly m_ej_nsm needs to be ~ 2-3e-1
    
if __name__ == '__main__' and False:
    #try changing f_merger (merger fraction) to get enough europium and appropriate rates
    eris_bestfit.bestfit_special_timesteps = num_steps
    def_f_merger = eris_bestfit.bestfit_f_merger
    new_list_of_models = []
    new_list_of_model_names = []

    loa_fractions = [7e-4, 9e-4, 1e-3, 7e-3, 1e-2, 1e-1]
    for fraction in loa_fractions:
        eris_bestfit.bestfit_f_merger = fraction
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/f_merger=%1.1e"%(fraction))

    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_mergerfraction_rates",
               expl_string="Applying different merger-fractions to 'Eris' parameters")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_mergerfraction_spectro",
                 expl_string="Applying different merger-fractions to 'Eris' parameters")
    eris_bestfit.bestfit_f_merger = def_f_merger
#conclusion
#singlehandedly f_merger needs to be ~ 1e-2 to reproduce [Eu/H]
#singlehandedly f_merger needs to be ~ 9e-4 to reproduce rates

if __name__ == '__main__' and False:
    #look for similar effect in nb_nsm_per_m (overrides merger-fraction)
    eris_bestfit.bestfit_special_timesteps = num_steps
    def_nb_nsm = eris_bestfit.bestfit_nb_nsm_per_m
    new_list_of_models = []
    new_list_of_model_names = []

    loa_fractions = [2e-6, 1e-5, 2e-5, 3e-5, 1e-4]
    for fraction in loa_fractions:
        eris_bestfit.bestfit_nb_nsm_per_m = fraction
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/(#nsm/m)=%1.1e"%(fraction))

    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_nbnsm_rates",
                 expl_string="Applying different nsm-rates to 'Eris' parameters")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_nbnsm_spectro",
                 expl_string="Applying different nsm-rates to 'Eris' parameters")
    
    eris_bestfit.bestfit_nb_nsm_per_m = def_nb_nsm
#conclusion
#singlehandedly nb_nsm_per_m needs to be ~ 2-3e-5 to reproduce [Eu/H]
#singlehandedly nb_nsm_per_m needs to be ~ 2e-6 to reproduce rates

if __name__ == '__main__' and False:
    #adjust merger-fraction to rates and ejecta-mass to [EU/H]
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    #loa_fractions = [8e-4, 9e-4]
    fraction = 8e-4
    loa_ej_mass = [6e-2, 8e-2, 2e-1, 3e-1]
    #for fraction, ej_mass in zip(loa_fractions, loa_ej_mass):
    for ej_mass in loa_ej_mass:
        eris_bestfit.bestfit_f_merger = fraction
        eris_bestfit.bestfit_m_ej_nsm = ej_mass
        eris_omega = omega_new(eris_bestfit)
        
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit M_ej=%1.1e f_m=%1.1e"%(fraction, ej_mass))

    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v3_rates",
                 expl_string="Combination of KN-rate and spectroscopic fit")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v3_spectro",
                 expl_string="Combination of KN-rate and spectroscopic fit")

#Grand conclusion
#use realistic ejecta mass and appropriate dtd/merger fractions
#eris_bestfit_nsm_dtd_power #already set
eris_bestfit.bestfit_m_ej_nsm = 2e-1
eris_bestfit.bestfit_f_merger = 8e-4
print "The grand NSM conclusion:"
print "Dtd power-law: ", eris_bestfit.bestfit_nsm_dtd_power
print "Relative mass ejecta: ", eris_bestfit.bestfit_m_ej_nsm
print "Merger-fraction: ", eris_bestfit.bestfit_f_merger

if __name__ == '__main__' and True:
    #check grand conclusion
    eris_bestfit.bestfit_special_timesteps = num_steps
    eris_omega = omega_new(eris_bestfit)
    new_list_of_models = [eris_omega]
    new_list_of_model_names = ["'Eris lookalike' from determining NSM parameters"]
    
    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v4_rates",
                 expl_string="Final check for nsm-parameters")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v4_spectro",
                 expl_string="Final check for nsm-parameters")
    
pl.show()
