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

experiment_folder = "MCExperiment_highN_highRes"
plots_folder = "plots_MCExperiment"
isotope = "Re-187"

#get list of filenames in experiment-folder
file_list = os.listdir(experiment_folder)

#get list of filenames with isotope
iso_file_list = [filename for filename in file_list
                 if (isotope in filename)
                 and ("ism" in filename)
                 and ("desc" not in filename) ]

for index in range(len(iso_file_list)):
    if 'timeevol' in iso_file_list[i]:
        id_timeevol = index
    elif 'hist' in iso_file_list[i]:
        id_hist = index

timeevol_matrix = np.load(iso_file_list[id_timeevol])
hist_matrix = np.load(iso_file_list[id_hist])

fig = pl.figure
ax = fig.gca()
ax.grid(True)
ax.plot()
