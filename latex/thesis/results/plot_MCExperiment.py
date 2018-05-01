"""
"""
import os
import matplotlib.pyplot as pl
import numpy as np

from matplotlib import rcParams
print rcParams.keys()
rcParams[u"lines.linewidth"] = 2.0

def plot_timeevol(filename_timeevol, filename_desc):
    #get strings of description
    with open(filename_desc,'r') as desc_file:
        loa_desc_rows = desc_file.readlines()
    #get all all arrays
    all_arrays = np.load(filename)
    time = all_arrays[0,:]
    mean = all_arrays[1,:]
    pos_sigma = all_arrays[2,:]
    neg_sigma = all_arrays[3,:]
    maximum = all_arrays[4,:]
    minimum = all_arrays[5,:]
    
    #make figure
    fig = pl.figure(); ax = fig.gca(); ax.grid(True)

    ax.plot(time, mean, label="<>", color='k')
    ax.fill_between(time, pos_sigma, neg_sigma, color='g')
    loa_surrounding_array = [pos_sigma, neg_sigma, maximum, minimum]
    loa_surrounding_name = [r"+1$\sigma$",r"-1$\sigma$","max","min"]
    for y,y_name in zip(loa_surrounding_array,loa_surrounding_name):
        ax.plot(time, y, linestyle='--', color='g', label=y_name)

    return fig

def plot_hist(filename_hist, filename_desc):
    #get strings of description
    with open(filename_desc,'r') as desc_file:
        loa_desc_rows = desc_file.readlines()
    #get all all arrays
    all_arrays = np.load(filename)
    sos_formation = all_arrays[0,:]
    now = all_arrays[1,:]
    #make figure
    fig = pl.figure()
    loa_ax = fig.subplots(nrows=2,ncols=1)
    loa_ax[0].grid(True)
    loa_ax[0].hist(sos_formation, nbins=50, label="t=9.5Gyr")
    loa_ax[0].legend(loc=1)
    loa_ax[1].grid(True)
    loa_ax[1].hist(now, nbins=50, label="t=14Gyr")
    loa_ax[1].legend(loc=1)
    
    return fig

def get_filenames(experiment_folder):
    #decide on isotope_ism, isotope_yield, element_ism, num_nsm
    nuclear_quantity = "Re-187" #isotope or element
    physical_quantity = "ism" #ism or yield
    
    #get list of filenames in experiment-folder
    file_list = os.listdir(experiment_folder)
    
    #get list of filenames with desired quantities
    quantity_file_list = [filename for filename in file_list
                          if (nuclear_quantity in filename)
                          and (physical_quantity in filename)]
    
    if len(quantity_file_list) != 3:
        print "Error in number of filenames! only %d"len(quantity_file_list)
        
    for filename in quantity_file_list:
        if 'hist' in filename:
            hist_filename = filename
        elif 'timeevol' in filename:
            timeevol_filename = filename
        elif 'desc' in filename:
            desc_filename = filename

    return hist_filename, timeevol_filename, desc_filename

experiment_folder = "MCExperiment_highN_highRes"
plots_folder = "plots_MCExperiment"

if __name__ == '__main__':
    hist_filename, timeevol_filename, desc_filename\
        = get_filenames(experiment_folder=experiment_folder)
    fig_hist = plot_hist(hist_filename, desc_filename)
    fig_hist.show()
