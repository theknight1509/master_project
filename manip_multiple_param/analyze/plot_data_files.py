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

    return doa_figs

def get_timepoint_array(time_array, numpy_matrix, timepoint):
    """ Find closest indeces of time_array closest to timepoint,
    find the appropriate array in numpy_matrix,
    return array of values. """
    if timepoint in time_array: #find exact values
        numpy_array = numpy_matrix[:,timepoint==time_array] #get values
        numpy_array = numpy_array.reshape(len(numpy_array)) #flatten to 1D
    elif (timepoint>time_array[0]) and (timepoint<time_array[-1]): #interpolate
        broken_time_array = np.abs(time_array-timepoint)
        sorted_indeces = np.argsort(broken_time_array) #sorted indeces from timepoint
        interp_indeces = [sorted_indeces[0], sorted_indeces[1]] #indeces of time-array closest to timepoint
        lower_interp_index = min(interp_indeces)
        upper_interp_index = max(interp_indeces)
        
        lower_interp_time = time_array[lower_interp_index] #values of time-array closest to timepoint
        upper_interp_time = time_array[upper_interp_index]
        fraction_interp_time = (timepoint-lower_interp_time)/(upper_interp_time-lower_interp_time) #relative timejump between time-array and timepoint
        
        lower_interp_numpy_array = numpy_matrix[:,lower_interp_index] #values of numpy_matrix closest to timepoint
        upper_interp_numpy_array = numpy_matrix[:,upper_interp_index]
        delta_interp_numpy_array = (upper_interp_numpy_array-lower_interp_numpy_array)*fraction_interp_time #jump in numpy_matrix to timepoint

        numpy_array = lower_interp_numpy_array + delta_interp_numpy_array #interpolated array
    else:
        print "Extrapolation not considered! Fuck off!"
        return False
    return numpy_array

def plot_time_hist(array, label=False):
    """ Make single figure, plot histogram of array onto axis,
    return the n,bins-ararys from the historgram."""
    fig = pl.figure()
    ax = fig.gca(); ax.grid(True)
    n, bins, patches = ax.hist(array, bins=40)
    return fig

def plot_all_time_hist(dir_name, loa_array_strings, timepoint=1.4e+10):
    time_array = get_single_array(dir_name, array_string="time")
    doa_arrays = get_all_arrays(dir_name, loa_array_strings)
    
    doa_stats_arrays = {}
    doa_figs = {}
    for key in loa_array_strings:
        numpy_mat = doa_arrays[key]
        doa_stats_arrays[key] = get_timepoint_array(time_array, numpy_mat, timepoint=timepoint)
        fig = plot_time_hist(doa_stats_arrays[key])
        doa_figs[key] = fig

    return doa_figs

### On direct call! ###
if __name__ == '__main__':
    dir_name = "../test_dir/"
    loa_array_strings = ["num_nsm", "ism_iso_Re-187", "ism_iso_Os-187"]
    plot_all_mean_sigma_extrema(dir_name, loa_array_strings)
