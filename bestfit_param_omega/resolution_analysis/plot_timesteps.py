"""
Plot the timestep data-tables
"""
#import matplotlib.pyplot as pl
from matplotlib import pyplot as plt
import os, sys

# get list of tables
loa_filenames = ["resolutiontable_constant.dat", "resolutiontable_special.dat"]
response = raw_input("The data files are: %s \n is this okay? (y/n)\t"%loa_filenames)
if response == "y":
    pass
elif response == "n":
    print "Then f***ing fix it yourself!"
    sys.exit("Exiting!")
else:
    print "Unintelligeble response"
    sys.exit("Exiting!")

#Extract data from filenames
doa_data = {}
for filename in loa_filenames:
    current_data_dict = {}
    #read from file
    with open(filename, 'r') as infile:
        title_row = infile.readline().split()
        loa_rows = infile.readlines()
    #make empty list for each title
    for title in title_row:
        current_data_dict[title] = []
    #fill lists appropriately
    for row in loa_rows:
        words = row.split()
        for i, title in enumerate(title_row):
            if (title == "n") or (title == "time-points"):
                current_val = int(words[i])
            else:
                current_val = float(words[i])
            current_data_dict[title].append(current_val)
    doa_data[filename] = current_data_dict
#Done extracting data into two nested dictionaries

#plot into three figures, one for each chi^2 method

fig_type = "pearson_chi2" 
fig_type = "astro_chi2" 
fig_type = "relative_chi2"

"""
for i in range(len(fig_name_list)):
    fig = pl.figure(fig_name_list[i])
    
    constant_axis = fig.add_subplot(111)
    plotting_function(constant_axis, constant_dt_values,
    constant_value_list[i], fig_str_list[i],
    constant=True)
    #make a new axis, inverted, on top
    special_axis = constant_axis.twiny()
    special_axis.invert_xaxis()
    special_axis.set_xscale('log')
    special_axis.xaxis.tick_top()
    plotting_function(special_axis, special_dt_values,
    special_value_list[i], fig_str_list[i],
    constant=False)
    
    axis = fig.add_subplot(111)
    axis.grid(True)
    axis.set_title("Resolution of 'Omega' compared to 'Eris'")
    axis.set_xlabel("number of timepoints")
    axis.set_ylabel(fig_str_list[i])
    axis.set_xscale('log')
    plotting_function(axis, constant_n_values,
                      constant_value_list[i],
                      constant=True)
    plotting_function(axis, special_n_values,
                      special_value_list[i],
                      constant=False)
    axis.legend(numpoints=1, loc='best')
    #save figures
    figname = "timestep_resolution_" + fig_name_list[i] + ".png"
    fig.savefig(figname)
pl.show()
"""
