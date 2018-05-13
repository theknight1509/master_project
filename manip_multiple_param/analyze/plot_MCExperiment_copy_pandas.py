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

def plot_timeevol(filename_timeevol, ax, plot_string="f_{187}"):
    pandas_data_frame = pd.read_csv(filename_timeevol)
    time = pandas_data_frame["time"]
    mean = pandas_data_frame["mean"]
    pos_sigma = pandas_data_frame["mean+sigma"]
    neg_sigma = pandas_data_frame["mean-sigma"]
    maximum = pandas_data_frame["maximum"]
    minimum = pandas_data_frame["minimum"]
    
    #scale time to Gyr
    time /= 1.0e+9
    ax.set_xlabel("time [Gyr]")
    ax.grid(True)
    
    #plot mean, sigmas, extremas and shaded region
    ax.plot(time, mean, color='b', 
            label=r"$\langle %s \rangle$"%plot_string)
    ax.fill_between(time, pos_sigma, neg_sigma, color='g', alpha=0.8, 
                    label=r"$\langle %s \rangle \pm \sigma$"%plot_string)
    loa_surrounding_array = [maximum, minimum] #pos_sigma, neg_sigma, 
    loa_surrounding_name = ["max($%s$)"%plot_string,"min($%s$)"%plot_string] #r"+1$\sigma$",r"-1$\sigma$",
    for y,y_name in zip(loa_surrounding_array,loa_surrounding_name):
        ax.plot(time, y, linestyle='--', color='g', label=y_name)
    ax.legend(loc="upper left")

    return

def plot_hist(filename_hist, loa_ax):
    pandas_data_frame = pd.read_csv(filename_hist)
    keys = [key for key in pandas_data_frame.keys()
            if ("t=" in key)]

    for ax, key in zip(loa_ax, keys):
        array = pandas_data_frame[key]
        ax.grid(True)
        ax.hist(array, bins=50, label=key)
        ax.axvline(np.mean(array), color='k', 
                   label=r"$\langle X \rangle \pm 1 \sigma$")
        ax.axvline(np.mean(array)-np.std(array), color='k')
        ax.axvline(np.mean(array)+np.std(array), color='k')
        ax.legend(loc=1)
    
    return

def plot_hist_vertical(filename_hist, loa_ax):
    pandas_data_frame = pd.read_csv(filename_hist)
    keys = [key for key in pandas_data_frame.keys()
            if ("t=" in key)]
    colors = ["k", "k"]
    color = {key: color for color, key in zip(colors,keys)}

    for ax, key in zip(loa_ax, keys):
        array = pandas_data_frame[key]
        ax.grid(True)
        ax.hist(array, bins=50, label=key, orientation="horizontal", color=color[key])
        ax.set_title("%s"%(key))
        # ax.axhline(np.mean(array), color='k', 
        #            label=r"$\langle X \rangle \pm 1 \sigma$")
        # ax.axhline(np.mean(array)-np.std(array), color='k')
        # ax.axhline(np.mean(array)+np.std(array), color='k')
        # ax.legend(loc=1)
    return


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

def plot_all_single_paths(loa_fullpaths):
    for fullpath in loa_fullpaths:
        fig = pl.figure()
        if "hist" in fullpath:
            loa_ax = fig.subplots(nrows=2, ncols=1, sharex=True)
            plot_hist(fullpath, loa_ax)
            ax = loa_ax[0]
        elif "timeevol" in fullpath:
            ax = fig.gca()
            plot_timeevol(fullpath, ax)
        else:
            print "(/) Error! neither 'hist' not 'timeevol' present"

        ax.set_title(fullpath.split('/')[-1])

        save_name = fullpath[:-len(".csv")] + ".png"
        fig.savefig(save_name)
    return fig

def plot_combined_plots(loa_fullpaths):
    doa_fullpaths = sort_paths(loa_fullpaths=loa_fullpaths)

    #get paths of timeevol and hist
    loa_paths = doa_fullpaths["div"]
    #make master-figure
    fig = pl.figure(dpi=100)
    ax1, ax2, ax3 = fig.subplots(nrows=1, ncols=3,
                            gridspec_kw={"width_ratios":[5,1,1]})
    #sort paths into timeevol and hist
    for path in loa_paths:
        if "timeevol" in path: 
            plot_timeevol(path, ax1)
        elif "hist" in path: 
            plot_hist_vertical(path, [ax3,ax2])
    
    #draw vertical line for histograms
    ax1.axvline(9.5, color='k')
    ax1.axvline(14, color='k')
    ax1.set_title(r"$f_{187} = ^{187}Os/^{187}Re $")
    
    fig.tight_layout()

    return fig

def sort_paths(loa_fullpaths, check=True):
    div = "div"
    re187 = "Re-187"
    os187 = "Os-187"
    keys = [div, re187, os187]
    doa_fullpaths = {key:[] for key in keys}
    
    while len(loa_fullpaths) > 0:
        for i, path in enumerate(loa_fullpaths):
            if div in path:
                doa_fullpaths[div].append(path)
                loa_fullpaths.pop(i)
            elif re187 in path:
                doa_fullpaths[re187].append(path)
                loa_fullpaths.pop(i)
            elif os187 in path:
                doa_fullpaths[os187].append(path)
                loa_fullpaths.pop(i)
            else:
                print "(/) Error in sort_paths()!"
                print "\t", "path doesn't match any key %s"%keys
                print "\t", path

    if check: #check lengths of lists
        all_good = True
        desired_length = 2
        for key in doa_fullpaths.keys():
            if not (len(doa_fullpaths[key]) == desired_length):
                all_good = False
        if not all_good:
            print "sort_paths()! Check of lists failed"
            print doa_fullpaths
        else:
            print "sort_paths()! Check of lists succeded"

    return doa_fullpaths

if __name__ == '__main__':
    loa_fullpaths = get_full_filenames(subdir_name)

    print "All paths:"
    for fullpath in loa_fullpaths:
        print fullpath.split('/')[-1]
    if raw_input("continue? y/n\t") == "y":
        pass
    else:
        sys.exit("Exiting!")

    # plot_all_single_paths(loa_fullpaths=loa_fullpaths)
    fig = plot_combined_plots(loa_fullpaths=loa_fullpaths)
    fig.show()
