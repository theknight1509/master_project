"""
Go through /stornext/-directories and plot various data-sets
with mean + regions and such.
Decide which data is to be stored in /results/
"""
from directory_master import Foldermap
from plot_data_files import plot_all_mean_sigma_extrema, plot_all_time_hist
import matplotlib.pyplot as pl

#Get relevant directory-names for uio-systems
folder_instance = Foldermap()
dir_stornext = folder_instance.stornext_folder()
dir_hume = folder_instance.hume_folder()

#decide on variables to plot!
loa_elem = ["Re", "Os"]
loa_re_isos = ["Re-187", "Re-185"]
loa_os_isos = ["Os-187", "Os-188"]
loa_ism_isos = ["ism_iso_"+iso for iso
                in loa_re_isos+loa_os_isos]
loa_ism_elem = ["ism_elem_"+elem for elem in loa_elem]
loa_yield_isos = ["yield_"+iso for iso
                  in loa_re_isos+loa_os_isos]
loa_array_strings = ["num_nsm", "m_locked"] + \
                    loa_ism_elem + \
                    loa_ism_isos + \
                    loa_yield_isos

if __name__ == '__main__':
    print "Plotting data for the following arrays:"
    print loa_array_strings

    dir_experiment = dir_stornext + "MCExperiment1/"

    doa_figs_spread = plot_all_mean_sigma_extrema(dir_experiment,
                                                  loa_array_strings)
    doa_figs_hist = plot_all_time_hist(dir_experiment,
                                       loa_array_strings)
    for key in loa_array_strings:
        fig = doa_figs_spread[key]; ax = fig.gca()
        ax.set_xlabel("time [yr]")
        ax.set_title(key)
        fig.savefig("temp_check_images/spread_%s.png"%(key))
        fig = doa_figs_hist[key]; ax = fig.gca()
        ax.set_title(key)
        fig.savefig("temp_check_images/hist_%s.png"%(key))
    pl.show()
    
