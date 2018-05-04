import bestfit_param_omega.current_bestfit as eris_bestfit
from bestfit_param_omega.omega_new import omega_new
from visualize import visualize, eris_data, save_data
from matplotlib.pyplot import show

#make functions for plotting and saving data
def plot_mass(loa_omegas, loa_omega_names, expl_string):
    filename = "masses_n%d"%(num_steps)
    #plot stellar mass and total mass
    vis_obj = visualize(loa_omegas, loa_omega_names,
                        num_yaxes=2)
    vis_obj.add_time_mass("locked", index_yaxis=0)
    vis_obj.add_time_mass("total", index_yaxis=1)
    vis_obj.add_datapoint((eris_data().mass["time"][0],eris_data().mass["total_mass"][0]),
                          index_yaxis=1, label="M_b(z=0)")
    vis_obj.add_datapoint((eris_data().mass["time"][1],eris_data().mass["total_mass"][1]),
                          index_yaxis=1, label="M_b(z=1)")
    vis_obj.finalize(show=False, save=filename+".png")
    #save "gas_mass" and "m_locked"
    for i,mass_type in enumerate(["gas_mass", "m_locked", "m_tot"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames(filename+"_param%d"%i)
        save_obj.make_explanatory_file("mass arrays of %s \n%s"%(mass_type, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Final 'Eris'-bestfit of 'Omega'")
        save_obj.make_numpy_file(["time", mass_type])

def plot_rates(loa_omegas, loa_omega_names, expl_string):
    filename = "rates_n%d"%(num_steps)
    #plot star-formation, kilonova, and supernova rates
    vis_obj = visualize(loa_omegas, loa_omega_names, num_yaxes=3)
    vis_obj.add_time_rate("sf", index_yaxis=0)
    vis_obj.add_time_rate("sn", index_yaxis=1)
    vis_obj.add_time_rate("kn", index_yaxis=2)
    vis_obj.finalize(show=False, save=filename+".png")
    #save data from rates
    for i,rate_key in enumerate(["sf", "sn2", "nsns"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames(filename+"_param%d"%i)
        save_obj.make_explanatory_file("Rate arrays of %s \n%s"%(rate_key, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Final 'Eris'-bestfit of 'Omega'")
        save_obj.make_numpy_file(["time", rate_key])

def plot_spectro(loa_omegas, loa_omega_names, expl_string):
    filename = "spectro_n%d"%(num_steps)
    #Plot spectroscopic data for [O/H], [Fe/H], [Eu/H]
    vis_obj = visualize(loa_omegas, loa_omega_names,
                        num_yaxes=3)
    vis_obj.add_time_relabu("[O/H]", index_yaxis=0)
    vis_obj.add_time_relabu("[Fe/H]", index_yaxis=1)
    vis_obj.add_time_relabu("[Eu/H]", index_yaxis=2)
    vis_obj.finalize(show=False, save=filename+".png")
    #save data from spectroscopic plots
    for i,spectro_string in enumerate(["[O/H]", "[Fe/H]", "[Eu/H]"]):
        save_obj = save_data(loa_omegas)
        save_obj.make_filenames(filename+"_param%d"%i)
        save_obj.make_explanatory_file("spectroscopic arrays of %s \n%s"%(spectro_string, expl_string),
                                       ["time"]+loa_omega_names,
                                       "Final 'Eris'-bestfit of 'Omega'")
        save_obj.make_numpy_file(["time", spectro_string])

#set number of special timesteps
try: #check input
    import sys
    input_arg = sys.argv[1]
    num_steps = int(input_arg)
except IndexError: #no input-arguments given
    num_steps = 10
except:
    num_steps = int(input("How many timesteps do you want?"))
print "Number of timesteps: ", num_steps
eris_bestfit.bestfit_special_timesteps = num_steps

#make instance of omega with the bestfit parameter space to eris.
loa_omega = [omega_new(eris_bestfit)]
loa_omega_name = ["'Omega' w/'Eris'-bestfit"]

plot_rates(loa_omega, loa_omega_name, expl_string="")
plot_spectro(loa_omega, loa_omega_name, expl_string="")
plot_mass(loa_omega, loa_omega_name, expl_string="")

show()
