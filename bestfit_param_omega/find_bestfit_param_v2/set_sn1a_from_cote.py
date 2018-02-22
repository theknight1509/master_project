"""
Set delay-time distribution and relative amount of type 1a SN.
Compare [Fe/H] and [O/H] between 'Omega' and 'Eris'.
"""
#necessary imports
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ()
from bestfit_param_omega.omega_new import omega_new
import matplotlib.pyplot as pl
#get eris-parameters from 'mass-file'
from bestfit_param_omega.find_bestfit_param_v2.set_stars import eris_bestfit
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
    vis_obj.finalize(show=False, save="data/sn1a_parameters_%s_n%d"%(version_string, num_steps))
    #save data from rates
    for i,rate_key in enumerate(["sf", "sn2", "nsns"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/sn1a_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("Rate arrays of %s \n%s"%(rate_key, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying sn1a-parameters to 'Omega' with mass-parameters determined")
        save_obj.make_numpy_file(["time", rate_key])

def plot_spectro(loa_omegas, loa_omega_names, version_string, expl_string):
    #Plot spectroscopic data for [O/H], [Fe/H], [Eu/H]
    vis_obj = visualize(loa_omegas, loa_omega_names,
                        num_yaxes=3)
    vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
    vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
    vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
    vis_obj.finalize(show=False, save="data/sn1a_parameters_%s_n%d"%(version_string,num_steps))
    #save data from spectroscopic plots
    for i,spectro_string in enumerate(["[O/H]", "[Fe/H]", "[Eu/H]"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames("data/sn1a_parameters_%s_%d_n%d"%(version_string,i,num_steps))
        save_obj.make_explanatory_file("spectroscopic arrays of %s \n%s"%(spectro_string, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Applying sn1a-parameters to 'Omega' with mass-parameters determined")
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

##########################

### Set number of SN1a ###
##########################
if __name__ == '__main__' and False:
    #use nb_1a_per_m to scale number of SN1a
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    loa_nb = [1e-5, 8e-4, 1e-3, 1.5e-3, 2e-3, 3e-3, 1e-1, 1.0]
    for nb_1a in loa_nb:
        eris_bestfit.bestfit_nb_1a_per_m = nb_1a
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/nb1a_per_m=%1.1e"%nb_1a)
    
    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v1_rates",
                 expl_string="Number of SN1a per mass")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v1_spectro",
                 expl_string="Number of SN1a per mass")
#Conclusion
eris_bestfit.bestfit_nb_1a_per_m = 1e-3

#####################################
### Set DTD for sn1a from cote16a ###
""" Set sn1a_rate to power-law, gaussian or exponential,
and probe different expoent values for all three. """
#####################################

#Power-law dtd
if __name__ == '__main__' and False:
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    eris_bestfit.bestfit_sn1a_rate = "power_law"
    def_beta = eris_bestfit.bestfit_beta_pow
    loa_beta = [-5,-3.5,-1.0,-0.1]
    for beta_pow in loa_beta:
        print "power-law sn1a dtd: beta=", beta_pow
        eris_bestfit.bestfit_beta_pow = beta_pow
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/sn1a power=%1.1f"%beta_pow)
    eris_bestfit.bestfit_beta_pow = def_beta #return to default

    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_powerlaw_rates",
                 expl_string="Applying different power-law dtd to 'Eris' parameters")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_powerlaw_spectro",
                 expl_string="Applying different power-law dtd to 'Eris' parameters")

#Gaussian dtd
if __name__ == '__main__' and False:
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    eris_bestfit.bestfit_sn1a_rate = "gauss"
    def_gauss_dtd = eris_bestfit.bestfit_gauss_dtd
    loa_gaussian_dtd = []
    
    #long mean, small spread gaussian
    gauss_dtd = [1e+10, 1e+8]
    loa_gaussian_dtd.append(gauss_dtd)
    #long mean, wide spread gaussian
    gauss_dtd = [1e+10, 1e+10]
    loa_gaussian_dtd.append(gauss_dtd)
    #short mean, small spread gaussian
    gauss_dtd = [1e+8, 5e+7]
    loa_gaussian_dtd.append(gauss_dtd)
    #short mean, wide spread gaussian
    gauss_dtd = [1e+8, 1e+10]
    loa_gaussian_dtd.append(gauss_dtd)

    for new_gauss_dtd in loa_gaussian_dtd:
        print "gaussian sn1a dtd: [%1.1e,%1.1e]"%tuple(new_gauss_dtd)
        eris_bestfit.bestfit_gauss_dtd = new_gauss_dtd
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/sn1a gauss=[%1.1e,%1.1e]"%tuple(new_gauss_dtd))
    
    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_gauss_rates",
                 expl_string="Applying different gaussian SN1a-dtd to 'Eris' parameters")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_gauss_spectro",
                 expl_string="Applying different gaussian SN1a-dtd to 'Eris' parameters")
    
    eris_bestfit.bestfit_gauss_dtd = def_gauss_dtd #revert back to default

#Exponential dtd
if __name__ == '__main__' and False:
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    eris_bestfit.bestfit_sn1a_rate = "exp"
    def_exp_dtd = eris_bestfit.bestfit_exp_dtd
    loa_timescales = [1e+6, 5e+6, 5.1e+6, 5.2e+6, 5.3e+6, 5.4e+6, 5.5e+6, 6e+6, 1e+8]
    for timescale in loa_timescales:
        #use timescale as exponential e-folding rate
        print "e-folding rate: %1.1e"%timescale
        eris_bestfit.bestfit_exp_dtd = timescale
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/sn1a exp=%1.1e[yr]"%timescale)

    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_exp_rates",
                 expl_string="Applying different exponential SN1a-dtd to 'Eris' parameters")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v2_exp_spectro",
                 expl_string="Applying different exponential SN1a-dtd to 'Eris' parameters")
    
    eris_bestfit.bestfit_exp_dtd = def_exp_dtd#revert back to default

#conclusion
eris_bestfit.bestfit_sn1a_rate = "exp"
eris_bestfit.bestfit_exp_dtd = 5.5e+6

##################################################
### Use a yield table with better O/Fe balance ###
##################################################
if __name__ == '__main__' and False:
    def_yield_table = eris_bestfit.bestfit_sn1a_table
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    #see yield_table_contents for O-Fe in yield-tables
    loa_yield_tables_available = ["sn1a_i99_CDD1.txt", "sn1a_i99_CDD2.txt", "sn1a_i99_W7.txt", "sn1a_ivo12_mix_z.txt", "sn1a_ivo12_stable_z.txt", "sn1a_ivo13_mix_z.txt", "sn1a_ivo13_stable_z.txt", "sn1a_t03.txt", "sn1a_t86.txt"]
    
    for table in loa_yield_tables_available:
        eris_bestfit.bestfit_sn1a_table = "yield_tables/"+table
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append(table)

    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v3_spectro",
                 expl_string="Various sn1a yield tables")
    eris_bestfit.bestfit_sn1a_table = def_yield_table #return to default
#Conclusion
eris_bestfit.bestfit_sn1a_table = "yield_tables/sn1a_ivo13_stable_z.txt" #less iron, more oxygen, VERY little effect

############################################
### Set number of SN1a a new to rescale! ###
############################################
if __name__ == '__main__' and False:
    #use nb_1a_per_m to scale number of SN1a
    eris_bestfit.bestfit_special_timesteps = num_steps
    new_list_of_models = []
    new_list_of_model_names = []

    loa_nb = [8e-4, 9e-4, 1e-3, 2e-3, 3e-3]
    for nb_1a in loa_nb:
        eris_bestfit.bestfit_nb_1a_per_m = nb_1a
        eris_omega = omega_new(eris_bestfit)
        new_list_of_models.append(eris_omega)
        new_list_of_model_names.append("'Eris' bestfit w/nb1a_per_m=%1.1e"%nb_1a)
    plot_rates(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v4_rates",
                 expl_string="Changing sn1a-numbers after fitting sn1a")
    plot_spectro(loa_omegas=new_list_of_models, loa_omega_names=new_list_of_model_names,
                 version_string="v4_spectro",
                 expl_string="Changing sn1a-numbers after fitting sn1a")
#Conclusion
eris_bestfit.bestfit_nb_1a_per_m = 1e-3

pl.show()
