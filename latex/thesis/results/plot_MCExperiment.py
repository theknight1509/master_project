"""
"""
import os
import matplotlib.pyplot as pl
import numpy as np

from matplotlib import rcParams
#print rcParams.keys()
rcParams[u"lines.linewidth"] = 2.0

def plot_timeevol(filename_timeevol, filename_desc):
    #get strings of description
    with open(filename_desc,'r') as desc_file:
        loa_desc_rows = desc_file.readlines()
    #get all all arrays
    all_arrays = np.load(filename_timeevol)
    time = all_arrays[0,:]
    mean = all_arrays[1,:]
    pos_sigma = all_arrays[2,:]
    neg_sigma = all_arrays[3,:]
    maximum = all_arrays[4,:]
    minimum = all_arrays[5,:]
    
    #make figure
    fig = pl.figure(); ax = fig.gca(); ax.grid(True)

    #scale time to Gyr
    time /= 1.0e+9
    ax.set_xlabel("time [Gyr]")
    
    #plot mean, sigmas, extremas and shaded region
    ax.plot(time, mean, label="<>", color='k')
    ax.fill_between(time, pos_sigma, neg_sigma, color='g')
    loa_surrounding_array = [pos_sigma, neg_sigma, maximum, minimum]
    loa_surrounding_name = [r"+1$\sigma$",r"-1$\sigma$","max","min"]
    for y,y_name in zip(loa_surrounding_array,loa_surrounding_name):
        ax.plot(time, y, linestyle='--', color='g', label=y_name)
    ax.legend(loc="upper left")

    return fig

def plot_hist(filename_hist, filename_desc):
    #get strings of description
    with open(filename_desc,'r') as desc_file:
        loa_desc_rows = desc_file.readlines()
    #get all all arrays
    all_arrays = np.load(filename_hist)
    sos_formation = all_arrays[0,:]
    now = all_arrays[1,:]
    #make figure
    fig = pl.figure()
    loa_ax = fig.subplots(nrows=2,ncols=1, sharex=True)
    for ax, array, label in zip(loa_ax, [sos_formation, now], 
                                 ["t=9.5Gyr","t=14Gyr"]):
        ax.grid(True)
        ax.hist(array, bins=50, label=label)
        ax.axvline(np.mean(array), color='k', 
                   label=r"$\langle X \rangle \pm 1 \sigma$")
        ax.axvline(np.mean(array)-np.std(array), color='k')
        ax.axvline(np.mean(array)+np.std(array), color='k')
        ax.legend(loc=1)
    
    return fig

def get_filenames(experiment_folder, nuclear_quantity, physical_quantity):    
    #get list of filenames in experiment-folder
    file_list = os.listdir(experiment_folder)
    
    #get list of filenames with desired quantities
    quantity_file_list = [filename for filename in file_list
                          if (nuclear_quantity in filename)
                          and (physical_quantity in filename)]
    
    if len(quantity_file_list) != 3:
        print "Error in number of filenames! only %d"%len(quantity_file_list)
        
    for filename in quantity_file_list:
        if 'hist' in filename:
            hist_filename = filename
        elif 'timeevol' in filename:
            timeevol_filename = filename
        elif 'desc' in filename:
            desc_filename = filename
    try:
        return hist_filename, timeevol_filename, desc_filename
    except:
        print "Error in returning filenames! list: %s"%quantity_file_list

def plot_ism_isos(experiment_folder, iso="Re-187", save=False):
    #Plot all instances of ism and desired isotope, both histogram and timeevolution
    hist_filename, timeevol_filename, desc_filename\
        = get_filenames(experiment_folder=experiment_folder, nuclear_quantity=iso, physical_quantity="ism")
    fig_hist = plot_hist(experiment_folder+'/'+hist_filename, 
                         experiment_folder+'/'+desc_filename)
    fig_hist.suptitle("Mass of %s in inter stellar medium"%iso)
    if not save:
        fig_hist.show()
    else: #use save argumnet as filename
        fig_hist.savefig(save+"_hist.png")
    fig_timeevol = plot_timeevol(experiment_folder+'/'+timeevol_filename, 
                                experiment_folder+'/'+desc_filename)
    fig_timeevol.suptitle("Mass of %s in inter stellar medium"%iso)
    if not save:
        fig_hist.show()
    else: #use save argumnet as filename
        fig_hist.savefig(save+"_timeevol.png")
    #raw_input("Waiting for input to quit\n")
    return

experiment_folder = "MCExperiment_highN_highRes"
plots_folder = "plots_MCExperiment"
loa_isos = ["Re-185", "Re-187", "Os-186", "Os-187", "Os-187", "W-184"]

if __name__ == '__main__':
    # hist_filename, timeevol_filename, desc_filename\
    #     = get_filenames(experiment_folder=experiment_folder)
    # fig_hist = plot_hist(experiment_folder+'/'+hist_filename, 
    #                      experiment_folder+'/'+desc_filename)
    # fig_hist.show()
    
    for isotope in loa_isos:
        plot_ism_isos(experiment_folder=experiment_folder, iso=isotope, 
                      save=plots_folder+'/'+experiment_folder+"_ism_%s"%isotope)
