"""
Plot files in pandas-csv files, and store them in the some folder.
"""
import sys
import os
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd

import configparser as cp
config_filename = "../config_beehive_revised.ini"
config = cp.ConfigParser()
config.read(config_filename)
subdir_name = config["montecarlo parameters"]["directory_name"]
print "Working in directory: %s"%(subdir_name)

from matplotlib import rcParams
#print rcParams.keys()
rcParams[u"lines.linewidth"] = 2.0

def plot_timeevol(filename_timeevol):
    pandas_data_frame = pd.read_csv(filename_timeevol)
    time = pandas_data_frame["time"]
    mean = pandas_data_frame["mean"]
    pos_sigma = pandas_data_frame["mean+sigma"]
    neg_sigma = pandas_data_frame["mean-sigma"]
    maximum = pandas_data_frame["maximum"]
    minimum = pandas_data_frame["minimum"]
    
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

def plot_hist(filename_hist):
    pandas_data_frame = pd.read_csv(filename_hist)
    keys = [key for key in pandas_data_frame.keys()
            if ("t=" in key)]
    fig = pl.figure()
    loa_ax = fig.subplots(nrows=2,ncols=1, sharex=True)
    for ax, key in zip(loa_ax, keys):
        array = pandas_data_frame[key]
        ax.grid(True)
        ax.hist(array, bins=50, label=key)
        ax.axvline(np.mean(array), color='k', 
                   label=r"$\langle X \rangle \pm 1 \sigma$")
        ax.axvline(np.mean(array)-np.std(array), color='k')
        ax.axvline(np.mean(array)+np.std(array), color='k')
        ax.legend(loc=1)
    
    return fig

def get_full_filenames(experiment_folder):
    """ Return list of csv-filenames in experiment-folder with full path. """
    #get list of filenames in experiment-folder
    file_list = os.listdir(experiment_folder)

    #add '/' to experiment_folder if necessary
    if experiment_folder[-1] != '/':
        experiment_folder = experiment_folder + '/'
    
    #get list of filenames with desired quantities
    csv_file_list = [experiment_folder + filename for filename in file_list
                     if (".csv" in filename)]

    return csv_file_list



if __name__ == '__main__':
    loa_fullpaths = get_full_filenames(subdir_name)

    for fullpath in loa_fullpaths:
        print fullpath.split('/')[-1]
    if raw_input("continue? y/n\t") == "y":
        pass
    else:
        sys.exit("Exiting!")

    for fullpath in loa_fullpaths:
        if "hist" in fullpath:
            fig = plot_hist(fullpath)
        elif "timeevol" in fullpath:
            fig = plot_timeevol(fullpath)
        else:
            print "(/) Error! neither 'hist' not 'timeevol' present"

        ax = fig.gca()
        ax.set_title(fullpath.split('/')[-1])

        save_name = fullpath[:-len(".csv")] + ".png"
        fig.savefig(save_name)
        fig.show()
