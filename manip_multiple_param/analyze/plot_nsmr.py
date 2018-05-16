"""
Plot files in pandas-csv files, and store them in the some folder.
"""
import sys
import os
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd

from matplotlib import rcParams
#print rcParams.keys()
rcParams[u"lines.linewidth"] = 2.0

def plot_timeevol(filename_timeevol, ax, plot_string="nsm"):
    pandas_data_frame = pd.read_csv(filename_timeevol)
    time = pandas_data_frame["time"]
    mean = pandas_data_frame["mean"]

    #scale time to Gyr
    time /= 1.0e+6
    ax.set_xlabel("time [Myr]")
    ax.grid(True)

    #calculate rate
    dt = np.copy(time[1:]) - np.copy(time[:-1])
    rate = np.zeros(len(time))
    rate[1:] = mean[1:]/dt
    
    #plot rate and/or cumulative sum
    color_rate = 'b'
    ax.plot(time, rate, color=color_rate, linestyle='-')
    ax.set_ylabel(r"rate $r_{%s}(t)=dN_{%s}/dt$ [$Myr^{-1}$]"%(plot_string, plot_string), 
                  color=color_rate)
    ax.tick_params('y', colors=color_rate)
    ax.ticklabel_format(style='scientific')

    ax_twin = ax.twinx()
    color_sum = 'r'
    ax_twin.plot(time, np.cumsum(mean), color=color_sum, linestyle=':')
    ax_twin.set_ylabel(r"cumulative sum $\int_0^t dN_{%s}$"%(plot_string), color=color_sum)
    ax_twin.tick_params("y", colors=color_sum)
    ax_twin.ticklabel_format(style='scientific')

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

if __name__ == '__main__':
    from directory_master import Foldermap
    result_dir = Foldermap().hume_folder() + "latex/thesis/results/" #.results #.stornext_folder()
    result_dir = result_dir+"MCExperiment_revised_2_nsmtest/"
    loa_fullpaths = get_full_filenames(result_dir)

    print "All paths in %s:"%(result_dir)
    for fullpath in loa_fullpaths:
        print fullpath.split('/')[-1]
    if raw_input("continue? y/n\t") == "y":
        pass
    else:
        sys.exit("Exiting!")

    loa_num_paths = [path for path in loa_fullpaths
                     if "num" in path]
    loa_plot_strings = [path.split("num_")[-1].split("_")[0].split(".")[0] 
                        for path in loa_num_paths] #extract string between 'num_' and '_'/'.'

    for i, num_path in enumerate(loa_num_paths):
        fig = pl.figure()
        ax = fig.gca()
        plot_timeevol(num_path, ax, loa_plot_strings[i])
        fig.tight_layout()
        fig.savefig(result_dir + loa_plot_strings[i] + ".png")

    pl.show()
