"""
"""
import os
import matplotlib.pyplot as pl
import numpy as np

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
