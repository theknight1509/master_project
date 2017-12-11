"""
Plot the timestep data-tables
"""
#import matplotlib.pyplot as pl
import matplotlib.pyplot as pl
import os, sys
program_index = "2"

# get list of tables
loa_filetypes = ["constant", "special"]
filename = lambda filetype: "resolutiontable%s_%s.dat"%(program_index, filetype)
loa_filenames = [filename(filetype) for filetype in loa_filetypes]
#get response from user
if len(sys.argv) == 2:
    response = sys.argv[1]
else:
    response = raw_input("The data files are: %s \n is this okay? (y/n)\t"%loa_filenames)
#act on response
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
for filetype in loa_filetypes:
    current_data_dict = {}
    #read from file
    with open(filename(filetype), 'r') as infile:
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
    doa_data[filetype] = current_data_dict
#Done extracting data into two nested dictionaries

#make function for plottong two different plots in the same eaxis-object
def plot_resolution(axis, loa_x_axis, loa_y_axis, loa_labels,
                    color='r', loa_line=["s", "*"], eris=False):
    axis.grid(True)
    axis.hold(True)
    #plot all arrays in order
    for index, label in enumerate(loa_labels):
        axis.plot(loa_x_axis[index], loa_y_axis[index], loa_line[index], color=color, label=label)
        
    if eris:
        #add 'Eris' vertical line
        eris_num_timepoints = 1001
        axis.axvline(x=eris_num_timepoints, color='k', label="Eris")

def plot_2in1_filetype(fig_type):
    """
    For a given *fig_type*; make an Figure-object and plot chi^2 against timesteps on one axis,
    flip the axis and plot calc-time against timesteps on the other axis.
    """
    toilet = "Resolution of 'Omega' compared to 'Eris'"
    fig, ax = pl.subplots()
    ax.set_title(toilet)
    
    #plot chi^2 against number of timesteps
    key_timesteps = "time-points"
    loa_timepoints = [doa_data[filetype][key_timesteps] for filetype in loa_filetypes]
    
    loa_chi2 = [doa_data[filetype][fig_type] for filetype in loa_filetypes]
    loa_labels = [filetype + " timesteps" for filetype in loa_filetypes]
    y_limits = [10**3, 10**6]
    plot_resolution(ax, loa_timepoints, loa_chi2, loa_labels, color='r', eris=True)
    ax.tick_params(axis='y', colors='r')
    ax.spines['left'].set_color('r')
    ax.yaxis.label.set_color('r')
    ax.legend(numpoints=1)
    ax.set_xlabel(key_timesteps)
    ax.set_xscale('log')
    ax.set_ylabel(fig_type)
    ax.set_yscale("log")
    #ax.set_ylim(y_limits)

    #plot calculation time against number of timesteps
    ax2 = ax.twinx()
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    key_calctime = "calculation-time"
    loa_calctime = [doa_data[filetype][key_calctime] for filetype in loa_filetypes]
    plot_resolution(ax2, loa_timepoints, loa_calctime, loa_labels, color='b', eris=False)
    ax2.tick_params(axis='y', colors='b')
    ax2.spines['right'].set_color('b')
    ax2.yaxis.label.set_color('b')
    ax2.set_ylabel(key_calctime + " [s]")
    ax.set_yscale("log")
    fig.savefig("doubleyaxis%s_%s_calctime.png"%(program_index, fig_type))

def plot_filetype(fig_type, activate_ylim=False):
    """
    For a given *fig_type*; make an Figure-object and plot chi^2 against timesteps.
    """
    toilet = "Resolution of 'Omega' compared to 'Eris'"
    fig, ax = pl.subplots()
    ax.set_title(toilet)
    
    #plot chi^2 against number of timesteps
    key_timesteps = "time-points"
    loa_timepoints = [doa_data[filetype][key_timesteps] for filetype in loa_filetypes]
    
    loa_chi2 = [doa_data[filetype][fig_type] for filetype in loa_filetypes]
    loa_labels = [filetype + " timesteps" for filetype in loa_filetypes]
    y_limits = [10**3, 10**6]
    
    plot_resolution(ax, loa_timepoints, loa_chi2, loa_labels, color=None, eris=True)

    ax.legend(numpoints=1)
    ax.set_xlabel(key_timesteps)
    ax.set_xscale('log')
    ax.set_ylabel(fig_type)
    ax.set_yscale("log")
    if activate_ylim:
        ax.set_ylim(y_limits)

    fig.savefig("singleyaxis%s_%s.png"%(program_index, fig_type))

def plot_calctime():
    """
    For a given *fig_type*; make an Figure-object and plot chi^2 against timesteps on one axis,
    flip the axis and plot calc-time against timesteps on the other axis.
    """
    toilet = "Resolution of 'Omega' compared to 'Eris'"
    fig, ax = pl.subplots()
    ax.set_title(toilet)
    
    #plot chi^2 against number of timesteps
    loa_labels = [filetype + " timesteps" for filetype in loa_filetypes]
    y_limits = [10**3, 10**6]
    
    key_timesteps = "time-points"
    loa_timepoints = [doa_data[filetype][key_timesteps] for filetype in loa_filetypes]

    key_calctime = "calculation-time"
    loa_calctime = [doa_data[filetype][key_calctime] for filetype in loa_filetypes]
    plot_resolution(ax, loa_timepoints, loa_calctime, loa_labels, color=None, eris=False)
    
    ax.set_yscale("log")
    ax.legend(numpoints=1)
    ax.set_xlabel(key_timesteps)
    ax.set_xscale('log')
    ax.set_ylabel(key_calctime + " [s]")
    ax.set_yscale("log")
    fig.savefig("singleyaxis%s_calctime.png"%program_index)

if True:
    ### plot into three figures, one for each chi^2 method ###

    loa_fig_types = ["pearson_chi2", "astro_chi2", "relative_chi2"]
    loa_activate_ylim = [True, True, False]
    for i in range(3):
        plot_filetype(fig_type=loa_fig_types[i], activate_ylim=loa_activate_ylim[i])
        plot_2in1_filetype(fig_type=loa_fig_types[i])
        #pass
    plot_calctime()

if False:
    pl.show()
