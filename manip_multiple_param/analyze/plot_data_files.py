""" Make functions for plotting various components of simulation
in order to find good representation of data.
Also store the well represented data as numpy-arrays. """
import numpy as np
import matplotlib.pyplot as pl
from handle_data_files import get_all_arrays, get_single_array

def get_mean_sigma_extrema(numpy_matrix):
    axis = 0
    mean = np.mean(numpy_matrix, axis=axis)
    sigma = np.std(numpy_matrix, axis=axis)
    pos_sigma = mean + sigma
    neg_sigma = mean - sigma
    maxima = np.amax(numpy_matrix, axis=axis)
    minima = np.amin(numpy_matrix, axis=axis)
    return mean, pos_sigma, neg_sigma, maxima, minima

def plot_mean_sigma_extrema(time_array, toa_arrays,
                            toa_labels=False):
    fig = pl.figure()
    ax = fig.gca(); ax.grid(True)
    for array in toa_arrays:
        ax.plot(time_array, array)
    if toa_labels:
        ax.legend(toa_labels, numpoints=1, loc='lower right')
    return fig

def plot_all_mean_sigma_extrema(dir_name, loa_array_strings):
    time_array = get_single_array(dir_name, array_string="time")
    doa_arrays = get_all_arrays(dir_name, loa_array_strings)
    
    doa_stats_arrays = {}
    doa_figs = {}
    for key in loa_array_strings:
        numpy_mat = doa_arrays[key]
        doa_stats_arrays[key] = get_mean_sigma_extrema(numpy_mat)
        fig = plot_mean_sigma_extrema(time_array,doa_stats_arrays[key])
        doa_figs[key] = fig

    return loa_figs

### On direct call! ###
if __name__ == '__main__':
    dir_name = "../test_dir/"
    loa_array_strings = ["num_nsm", "ism_iso_Re-187", "ism_iso_Os-187"]
    plot_all_mean_sigma_extrema(dir_name, loa_array_strings)
