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

def plot_timeevol(filename_timeevol, ax, plot_string="nsm", bool_stddev=False):
    pandas_data_frame = pd.read_csv(filename_timeevol)
    time = pandas_data_frame["time"]
    mean = pandas_data_frame["mean"]
    mean_p_sigma = pandas_data_frame["mean+sigma"]
    mean_m_sigma = pandas_data_frame["mean-sigma"]

    #get index of 14Gyr and 9.5Gyr
    index_tnow = np.argmin(np.absolute(time-14e+9))
    index_tsos = np.argmin(np.absolute(time-9.5e+9))

    #scale time to Myr
    time /= 1.0e+6
    ax.set_xlabel("time [Myr]")
    ax.grid(True)

    #calculate rate
    dt = np.copy(time[1:]) - np.copy(time[:-1])
    rate = np.zeros(len(time))
    rate[1:] = mean[1:]/dt
    rate_p_sigma = np.zeros(len(time))
    rate_p_sigma[1:] = mean_p_sigma[1:]/dt
    rate_m_sigma = np.zeros(len(time))
    rate_m_sigma[1:] = mean_m_sigma[1:]/dt
    
    #plot rate and/or cumulative sum
    color_rate = 'b'
    ax.plot(time, rate, color=color_rate, linestyle='-')
    ax.set_ylabel(r"rate $r_{%s}(t)=dN_{%s}/dt$ [$Myr^{-1}$]"%(plot_string, plot_string), 
                  color=color_rate)
    ax.tick_params('y', colors=color_rate)
    ax.ticklabel_format(style='scientific')

    ax_twin = ax.twinx()
    color_sum = 'r'
    int_num = np.cumsum(mean)
    int_num_p_sigma = np.cumsum(mean_p_sigma)
    int_num_m_sigma = np.cumsum(mean_m_sigma)
    ax_twin.plot(time, int_num, color=color_sum, linestyle=':')
    ax_twin.set_ylabel(r"cumulative sum $\int_0^t dN_{%s}$"%(plot_string), color=color_sum)
    ax_twin.tick_params("y", colors=color_sum)
    ax_twin.ticklabel_format(style='scientific')

    if bool_stddev:
        ax.fill_between(time, rate_p_sigma, rate_m_sigma, color=color_rate, alpha=0.5)
        ax_twin.fill_between(time, int_num_p_sigma, int_num_m_sigma, color=color_sum, alpha=0.5)

    #Recalculate sigmas around zero, not mean
    rate_p_sigma -= rate
    rate_m_sigma -= rate
    int_num_p_sigma -= int_num
    int_num_m_sigma -= int_num
    #plot resulting distributions
    print "Finding indeces of %s"%(plot_string)
    print "t_now: index=%d t=%1.2e"%(index_tnow, time[index_tnow])
    print "\t"+"rate=%1.2e +/- %1.2e/%1.2e"%(rate[index_tnow], rate_p_sigma[index_tnow], rate_m_sigma[index_tnow])
    print "\t"+"int_num=%1.2e +/- %1.2e/%1.2e"%(int_num[index_tnow], int_num_p_sigma[index_tnow], int_num_m_sigma[index_tnow])
    print "t_sos: index=%d t=%1.2e"%(index_tsos, time[index_tsos])
    print "\t"+"rate=%1.2e +/- %1.2e/%1.2e"%(rate[index_tsos], rate_p_sigma[index_tsos], rate_m_sigma[index_tsos])
    print "\t"+"int_num=%1.2e +/- %1.2e/%1.2e"%(int_num[index_tsos], int_num_p_sigma[index_tsos], int_num_m_sigma[index_tsos])
    print ""
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
    result_dir = Foldermap().results #.hume_folder() + "latex/thesis/results/" #.stornext_folder() +...
    result_dir = result_dir+"MCExperiment_revised_2_numnsm/"
    loa_fullpaths = get_full_filenames(result_dir)

    print "All paths in %s:"%(result_dir)
    for fullpath in loa_fullpaths:
        print fullpath.split('/')[-1]
    if True:
        #if raw_input("continue? y/n\t") == "y":
        pass
    else:
        sys.exit("Exiting!")

    loa_num_paths = [path for path in loa_fullpaths
                     if "num" in path.split("/")[-1]]
    loa_plot_strings = [path.split("num_")[-1].split("_")[0].split(".")[0] 
                        for path in loa_num_paths] #extract string between 'num_' and '_'/'.'

    for i, num_path in enumerate(loa_num_paths):
        fig = pl.figure()
        ax = fig.gca()
        plot_timeevol(num_path, ax, loa_plot_strings[i],
                      bool_stddev=True)
        fig.tight_layout()
        fig.savefig(result_dir + loa_plot_strings[i] + ".png")

    pl.show()
