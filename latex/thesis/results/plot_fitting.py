"""
This script plots all the data from fitting-process of 'Eris'.
"""
####################################
### Imports and global variables ###
####################################
import numpy as np
import matplotlib.pyplot as pl
from visualize import eris_data
eris_data_inst = eris_data()
#directories for data and plots
data_dir = "data_fitting/"
plot_dir = "plots_fitting/"
#boolean switches
plot_all = False #plot all data
locked_param = False #plot all data from version 0
mass_param = False #plot all data from version 1
star_param = False #plot all data from version 2
nsm_param = True #plot all data from version 3
cbf = False #plot current bestfit
timestep = False #plot timestep analysis

#Set matplotlib-parameters
try:
    from matplotlib import rcParams
    rcParams["axes.labelsize"] = 16
    rcParams["axes.titlesize"] = 14
    rcParams["figure.titlesize"] = 14
    rcParams["legend.fontsize"] = 14
    rcParams["lines.linewidth"] = 2
    """
    [u'agg.path.chunksize', u'animation.avconv_args', u'animation.avconv_path', u'animation.bitrate', u'animation.codec', u'animation.convert_args', u'animation.convert_path', u'animation.ffmpeg_args', u'animation.ffmpeg_path', u'animation.frame_format', u'animation.html', u'animation.mencoder_args', u'animation.mencoder_path', u'animation.writer', u'axes.axisbelow', u'axes.edgecolor', u'axes.facecolor', u'axes.formatter.limits', u'axes.formatter.use_locale', u'axes.formatter.use_mathtext', u'axes.formatter.useoffset', u'axes.grid', u'axes.grid.axis', u'axes.grid.which', u'axes.hold', u'axes.labelcolor', u'axes.labelpad', u'axes.labelsize', u'axes.labelweight', u'axes.linewidth', u'axes.prop_cycle', u'axes.spines.bottom', u'axes.spines.left', u'axes.spines.right', u'axes.spines.top', u'axes.titlesize', u'axes.titleweight', u'axes.unicode_minus', u'axes.xmargin', u'axes.ymargin', u'axes3d.grid', u'backend', u'backend.qt4', u'backend.qt5', u'backend_fallback', u'boxplot.bootstrap', u'boxplot.boxprops.color', u'boxplot.boxprops.linestyle', u'boxplot.boxprops.linewidth', u'boxplot.capprops.color', u'boxplot.capprops.linestyle', u'boxplot.capprops.linewidth', u'boxplot.flierprops.color', u'boxplot.flierprops.linestyle', u'boxplot.flierprops.linewidth', u'boxplot.flierprops.marker', u'boxplot.flierprops.markeredgecolor', u'boxplot.flierprops.markerfacecolor', u'boxplot.flierprops.markersize', u'boxplot.meanline', u'boxplot.meanprops.color', u'boxplot.meanprops.linestyle', u'boxplot.meanprops.linewidth', u'boxplot.medianprops.color', u'boxplot.medianprops.linestyle', u'boxplot.medianprops.linewidth', u'boxplot.notch', u'boxplot.patchartist', u'boxplot.showbox', u'boxplot.showcaps', u'boxplot.showfliers', u'boxplot.showmeans', u'boxplot.vertical', u'boxplot.whiskerprops.color', u'boxplot.whiskerprops.linestyle', u'boxplot.whiskerprops.linewidth', u'boxplot.whiskers', u'contour.corner_mask', u'contour.negative_linestyle', u'datapath', u'docstring.hardcopy', u'errorbar.capsize', u'examples.directory', u'figure.autolayout', u'figure.dpi', u'figure.edgecolor', u'figure.facecolor', u'figure.figsize', u'figure.frameon', u'figure.max_open_warning', u'figure.subplot.bottom', u'figure.subplot.hspace', u'figure.subplot.left', u'figure.subplot.right', u'figure.subplot.top', u'figure.subplot.wspace', u'figure.titlesize', u'figure.titleweight', u'font.cursive', u'font.family', u'font.fantasy', u'font.monospace', u'font.sans-serif', u'font.serif', u'font.size', u'font.stretch', u'font.style', u'font.variant', u'font.weight', u'grid.alpha', u'grid.color', u'grid.linestyle', u'grid.linewidth', u'image.aspect', u'image.cmap', u'image.composite_image', u'image.interpolation', u'image.lut', u'image.origin', u'image.resample', u'interactive', u'keymap.all_axes', u'keymap.back', u'keymap.forward', u'keymap.fullscreen', u'keymap.grid', u'keymap.home', u'keymap.pan', u'keymap.quit', u'keymap.save', u'keymap.xscale', u'keymap.yscale', u'keymap.zoom', u'legend.borderaxespad', u'legend.borderpad', u'legend.columnspacing', u'legend.edgecolor', u'legend.facecolor', u'legend.fancybox', u'legend.fontsize', u'legend.framealpha', u'legend.frameon', u'legend.handleheight', u'legend.handlelength', u'legend.handletextpad', u'legend.isaxes', u'legend.labelspacing', u'legend.loc', u'legend.markerscale', u'legend.numpoints', u'legend.scatterpoints', u'legend.shadow', u'lines.antialiased', u'lines.color', u'lines.dash_capstyle', u'lines.dash_joinstyle', u'lines.linestyle', u'lines.linewidth', u'lines.marker', u'lines.markeredgewidth', u'lines.markersize', u'lines.solid_capstyle', u'lines.solid_joinstyle', u'markers.fillstyle', u'mathtext.bf', u'mathtext.cal', u'mathtext.default', u'mathtext.fallback_to_cm', u'mathtext.fontset', u'mathtext.it', u'mathtext.rm', u'mathtext.sf', u'mathtext.tt', u'nbagg.transparent', u'patch.antialiased', u'patch.edgecolor', u'patch.facecolor', u'patch.linewidth', u'path.effects', u'path.simplify', u'path.simplify_threshold', u'path.sketch', u'path.snap', u'pdf.compression', u'pdf.fonttype', u'pdf.inheritcolor', u'pdf.use14corefonts', u'pgf.debug', u'pgf.preamble', u'pgf.rcfonts', u'pgf.texsystem', u'plugins.directory', u'polaraxes.grid', u'ps.distiller.res', u'ps.fonttype', u'ps.papersize', u'ps.useafm', u'ps.usedistiller', u'savefig.bbox', u'savefig.directory', u'savefig.dpi', u'savefig.edgecolor', u'savefig.facecolor', u'savefig.format', u'savefig.frameon', u'savefig.jpeg_quality', u'savefig.orientation', u'savefig.pad_inches', u'savefig.transparent', u'svg.fonttype', u'svg.image_inline', u'svg.image_noscale', u'text.antialiased', u'text.color', u'text.dvipnghack', u'text.hinting', u'text.hinting_factor', u'text.latex.preamble', u'text.latex.preview', u'text.latex.unicode', u'text.usetex', u'timezone', u'tk.window_focus', u'toolbar', u'verbose.fileo', u'verbose.level', u'webagg.open_in_browser', u'webagg.port', u'webagg.port_retries', u'xtick.color', u'xtick.direction', u'xtick.labelsize', u'xtick.major.pad', u'xtick.major.size', u'xtick.major.width', u'xtick.minor.pad', u'xtick.minor.size', u'xtick.minor.visible', u'xtick.minor.width', u'ytick.color', u'ytick.direction', u'ytick.labelsize', u'ytick.major.pad', u'ytick.major.size', u'ytick.major.width', u'ytick.minor.pad', u'ytick.minor.size', u'ytick.minor.visible', u'ytick.minor.width']
    """
except:
    print "Unable to change rcParameters for matplotlib!"

############################
### plots from version 0 ###
############################
"""
Uses boolean switch: 'locked_param'.
Warning from original writer: for some files the data-order and length of time-arrays got mucked up, thats why the ordering and slicing is present.
"""

def v0_sfr():
    data_filename_lambdafunc = lambda param_type: data_dir + "highres_eris_parameters_%s.npy"%param_type
    plot_filename = plot_dir + "set_sfr_plot_sfr.png"
    print "plotting sfr of v0 into filename: ", plot_filename
    
    # plot sfr of defaults+'Eris lookalike'+'Eris'
    data_filename = data_filename_lambdafunc("rates0")
    eris_fit, default, mw, mw_cte, time = np.load(data_filename)
    time = time[:-1] #adjust lengths of time-array
    timescale = 1e+9 #measure time in Gyr
    time /= timescale 
    #get star-formation rate from 'Eris'-data
    eris_sfr = eris_data_inst.sfr["sfr"]
    eris_time = eris_data_inst.sfr["time"]/timescale
    #plot data    
    pl.figure()
    pl.plot(time, eris_fit, '--', label="'Omega' w/'Eris'-SFR")
    pl.plot(time, default, '-.', label="'Omega' default")
    pl.plot(time, mw, '--', label="'Omega' MW")
    pl.plot(time, mw_cte, '-.', label="'Omega' MW cte")
    pl.plot(eris_time, eris_sfr, 'k', label="'Eris'")
    pl.grid(True)
    pl.legend()
    #set title/axis/legend and such here!
    pl.title("Comparison of 'Omega' models")
    pl.xlabel("time [Gyr]")
    pl.ylabel("star formation rate [$M_\odot$/yr]")
    pl.savefig(plot_filename)

def v0_mass():
    print "plot stellar and ism mass from v0"
    data_filename_lambdafunc = lambda param_type: data_dir + "highres_eris_parameters_%s.npy"%param_type
    plot_filename_lambdafunc = lambda param_type: plot_dir + "set_sfr_plot_%s_mass.png"%param_type
    
    #plot stellar mass and ISM mass of defaults+'Eris lookalike'+'Eris'
    timescale = 1e+9 #scale time-axes to Gyr
    #get stellar mass from 'Eris'-data
    eris_stellar = eris_data_inst.sfr["m_cum"]
    eris_time = eris_data_inst.sfr["time"]
    eris_time /= timescale #scale to Gyr
    
    data_filename_ism = data_filename_lambdafunc("gas_mass")
    fig = pl.figure()
    ax = fig.gca()
    eris_fit, default, mw, mw_cte, time = np.load(data_filename_ism)
    time /= timescale #scale timeaxis to Gyr
    #plot data
    ax.plot(time, eris_fit, '--', label="'Omega' w/'Eris'-SFR")
    ax.plot(time, default, '-.', label="'Omega' default")
    ax.plot(time, mw, '--', label="'Omega' MW")
    ax.plot(time, mw_cte, '-.', label="'Omega' MW cte")
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel("$M_{ISM} [M_\odot]$")
    fig.suptitle("Comparison of 'Omega' models")
    fig.savefig(plot_filename_lambdafunc('gas'))

    data_filename_stellar = data_filename_lambdafunc("m_locked")
    fig = pl.figure()
    ax = fig.gca()
    time, eris_fit, default, mw, mw_cte = np.load(data_filename_stellar)
    time /= timescale #scale time-axis to Gyr
    #calculate cumulative sum of stellar masses
    eris_fit = np.cumsum(eris_fit)
    default = np.cumsum(default)
    mw = np.cumsum(mw)
    mw_cte = np.cumsum(mw_cte)
    #plot data
    ax.plot(time, eris_fit, '--', label="'Omega' w/'Eris'-SFR")
    ax.plot(time, default, '-.', label="'Omega' default")
    ax.plot(time, mw, '--', label="'Omega' MW")
    ax.plot(time, mw_cte, '-.', label="'Omega' MW cte")
    ax.plot(eris_time, eris_stellar, 'k-', label="'Eris' sim")
    ax.grid(True)
    ax.legend(loc='center right', bbox_to_anchor=(1.0, 0.6))
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel("$M_{*,cum.} [M_\odot]$")
    fig.suptitle("Comparison of 'Omega' models")
    fig.savefig(plot_filename_lambdafunc('stellar'))

def v0_spectro():
    print "plot spectroscopic data for v0"
    data_filename_lambdafunc = lambda param_type: data_dir + "highres_eris_parameters_%s.npy"%param_type
    plot_filename = plot_dir + "set_sfr_plot_spectro.png"
    
    #Plot spectroscopic data of defaults+'Eris lookalike'+'Eris'
    timescale = 1e+9 #scale time-axes to Gyr
    eris_time = eris_data().sfgas["time"] #time-axis from 'Eris'-simulation
    eris_time /= timescale #scale time
    fig, loa_axes = pl.subplots(3, sharex=True) #make figure with 3 subplots

    #[O/H] on top
    oxy_index = 0
    eris_fit, default, mw, mw_cte, time = np.load(data_filename_lambdafunc("spectro0"))
    time /= timescale #scale to timescale
    eris_oxy = eris_data().sfgas["[O/H]"]
    loa_axes[oxy_index].plot(time, eris_fit, '--', label="'Omega' w/'Eris'-SFR")
    loa_axes[oxy_index].plot(time, default, '-.', label="'Omega' default")
    loa_axes[oxy_index].plot(time, mw, '--', label="'Omega' MW")
    loa_axes[oxy_index].plot(time, mw_cte, '-.', label="'Omega' MW cte")
    loa_axes[oxy_index].plot(eris_time, eris_oxy, 'k-', label="'Eris'")
    #loa_axes[oxy_index].legend()
    loa_axes[oxy_index].grid(True)
    
    #[Fe/H] in the middle
    iron_index = 1
    eris_fit, default, mw, mw_cte, time = np.load(data_filename_lambdafunc("spectro1"))
    time /= timescale #scale to timescale
    eris_iron = eris_data().sfgas["[Fe/H]"]
    loa_axes[iron_index].plot(time, eris_fit, '--')#, label="'Omega' w/'Eris'-SFR")
    loa_axes[iron_index].plot(time, default, '-.')#, label="'Omega' default")
    loa_axes[iron_index].plot(time, mw, '--')#, label="'Omega' MW")
    loa_axes[iron_index].plot(time, mw_cte, '-.')#, label="'Omega' MW cte")
    loa_axes[iron_index].plot(eris_time, eris_iron, 'k-')#, label="'Eris'")
    #loa_axes[iron_index].legend()
    loa_axes[iron_index].grid(True)

    #[Eu/H] on bottom
    euro_index = 2
    eris_fit, default, mw, mw_cte, time = np.load(data_filename_lambdafunc("spectro2"))
    time /= timescale #scale to timescale
    eris_euro = eris_data().sfgas["[Eu/H]"]
    loa_axes[euro_index].plot(time, eris_fit, '--')#, label="'Omega' w/'Eris'-SFR")
    loa_axes[euro_index].plot(time, default, '-.')#, label="'Omega' default")
    loa_axes[euro_index].plot(time, mw, '--')#, label="'Omega' MW")
    loa_axes[euro_index].plot(time, mw_cte, '-.')#, label="'Omega' MW cte")
    loa_axes[euro_index].plot(eris_time, eris_euro, 'k-')#, label="'Eris'")
    #loa_axes[euro_index].legend()
    loa_axes[euro_index].grid(True)

    #TODO add title and such here
    loa_axes[oxy_index].set_ylabel("[O/H]")
    loa_axes[iron_index].set_ylabel("[Fe/H]")
    loa_axes[euro_index].set_ylabel("[Eu/H]")
    loa_axes[2].set_xlabel("time [Gyr]")
    loa_axes[0].legend(["'Omega' w/'Eris'-SFR", "'Omega' default", "'Omega' MW", "'Omega' MW cte","'Eris'"],
                       loc="upper right", fontsize=10, bbox_to_anchor=(1.0,0.7))
    for ax in loa_axes: #set y-axis limits
        ax.set_ylim([-5,2])
    fig.savefig(plot_filename)

if plot_all or locked_param or False:
    if True:
        v0_sfr()
    if True:
        v0_mass()
    if True:
        v0_spectro()

############################
### plots from version 1 ###
############################
"""
Uses boolean switch: 'mass_param'.
"""
def v1_minit_minf():
    print "plotting total mass and inflow from v1"
    data_filename_lambdafunc = lambda param_type: data_dir + "mass_parameters_v1_%s.npy"%param_type
    plot_filename_lambdafunc = lambda param_type: plot_dir + "set_mass_1_plot_%s.png"%param_type
    timescale = 1e+9 #scale time to Gyrs
    
    #### plot stellar mass and total mass with new initial mass and constant inflow ###
    #from explanatory files
    omega1_desc = r"$M_0$=4.0e+10 $\dot{M}$=3.0"
    omega2_desc = r"$M_0$=4.4e+10 $\dot{M}$=3.7"
    omega3_desc = r"$M_0$=4.5e+10 $\dot{M}$=6.0"
    omega4_desc = r"$M_0$=5.0e+10 $\dot{M}$=10.0"

    #plot stellar mass of 'Eris' and all models
    eris_mass = eris_data_inst.sfr["m_cum"]
    eris_time = eris_data_inst.sfr["time"]
    eris_time /= timescale #scale to Gyr
    time, omega1, omega2, omega3, omega4 \
        = np.load(data_filename_lambdafunc("1_n1100"))
    time /= timescale #scale time to Gyrs
    #calculate cumulative stellar mass to compare with 'Eris'
    omega1, omega2, omega3, omega4 \
        = np.cumsum(omega1), np.cumsum(omega2), \
        np.cumsum(omega3), np.cumsum(omega4)
    #make plot-object
    fig = pl.figure("v1.1.1")
    fig.suptitle("Initial mass of gas and constant inflow rate")
    ax = fig.gca()
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel(r"$M_{\star, cum}$ [$M_\odot$]")
    ax.grid(True)
    ax.plot(eris_time, eris_mass, 'k-', label="'Eris'")
    ax.plot(time, omega1, '--', label=omega1_desc)
    ax.plot(time, omega2, '-.', label=omega2_desc)
    ax.plot(time, omega3, '-', label=omega3_desc)
    ax.plot(time, omega4, '-.', label=omega4_desc)
    #ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.0))
    ax.legend(loc="best")
    fig.savefig(plot_filename_lambdafunc("stellar_mass"))
    
    #plot total mass of 'Eris' and all models
    eris_mass = eris_data_inst.mass["total_mass"]
    eris_time = eris_data_inst.mass["time"]
    eris_time /= timescale #scale to Gyr
    time, omega1, omega2, omega3, omega4 \
        = np.load(data_filename_lambdafunc("2_n1100"))
    time /= timescale
    
    fig = pl.figure("v1.1.2")
    fig.suptitle("Initial mass of gas and constant inflow rate")
    ax = fig.gca()
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel(r"$M_{tot}$ [$M_\odot$]")
    ax.grid(True)
    ax.plot(eris_time, eris_mass, 'k.', label="'Eris'")
    ax.plot(time, omega1, '--', label=omega1_desc)
    ax.plot(time, omega2, '-.', label=omega2_desc)
    ax.plot(time, omega3, '-.', label=omega3_desc)
    ax.plot(time, omega4, '-.', label=omega4_desc)
    #ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.0))
    ax.legend(loc="best")
    fig.savefig(plot_filename_lambdafunc("total_mass"))

def v1_mout(plot_arg="all"):
    print "plotting outflow from v1"
    data_filename_lambdafunc = lambda param_type: data_dir + "mass_parameters_v2_%s.npy"%param_type
    plot_filename_lambdafunc = lambda param_type: plot_dir + "set_mass_2_plot_%s.png"%param_type
    timescale = 1e+9 #scale time to Gyrs
    
    ### plot stellar mass and total mass with added outflow ###
    #from explanatory files
    omega1_desc = r"$M_{loading}$=0.3, $M_0$=5.4e+10, $\dot{M}_{in}$=4.3"
    omega2_desc = r"$M_{loading}$=0.4, $M_0$=5.6e+10, $\dot{M}_{in}$=4.6"
    omega3_desc = r"$M_{loading}$=0.5, $M_0$=5.4e+10, $\dot{M}_{in}$=4.0"
    omega4_desc = r"$M_{loading}$=0.2, $M_0$=5.4e+10, $\dot{M}_{in}$=4.6"
    omega5_desc = r"$M_{loading}$=0.5, $M_0$=5.6e+10, $\dot{M}_{in}$=4.2"
    omega6_desc = r"$M_{loading}$=0.2, $M_0$=5.6e+10, $\dot{M}_{in}$=5.2" 
    omega7_desc = r"$M_{loading}$=0.3, $M_0$=6.0e+10, $\dot{M}_{in}$=3.7"
    omega8_desc = r"$M_{loading}$=0.5, $M_0$=6.0e+10, $\dot{M}_{in}$=3.7"
    omega9_desc = r"$M_{loading}$=0.7, $M_0$=6.0e+10, $\dot{M}_{in}$=3.7"
    omega10_desc = r"$M_{loading}$=0.9, $M_0$=6.0e+10, $\dot{M}_{in}$=3.7"
    omega11_desc = r"$M_{loading}$=1.5, $M_0$=6.0e+10, $\dot{M}_{in}$=3.7"
    omega12_desc = r"$M_{loading}$=2.0, $M_0$=6.0e+10, $\dot{M}_{in}$=3.7"

    if plot_arg in ["all", "1"]:
        #plot stellar mass
        eris_mass = eris_data_inst.sfr["m_cum"]
        eris_time = eris_data_inst.sfr["time"]
        eris_time /= timescale #scale to Gyr
        time, omega1, omega2, omega3, omega4, omega5, \
            omega6,  omega7,  omega8,  omega9,  omega10, \
            omega11,  omega12 \
            = np.load(data_filename_lambdafunc("mass_1_n300"))
        time /= timescale #scale time to Gyrs
        #calculate cumulative stellar mass to compare with 'Eris'
        omega1, omega2, omega3, omega4, omega5, \
            omega6,  omega7,  omega8,  omega9,  omega10, \
            omega11,  omega12 \
            = np.cumsum(omega1), np.cumsum(omega2), \
            np.cumsum(omega3), np.cumsum(omega4), \
            np.cumsum(omega5), np.cumsum(omega6), \
            np.cumsum(omega7), np.cumsum(omega8), \
            np.cumsum(omega9), np.cumsum(omega10), \
            np.cumsum(omega11), np.cumsum(omega12)
        #make plot-object
        fig = pl.figure("v1.2.1")
        fig.suptitle("Outflow proportional to SNR")
        ax = fig.gca()
        ax.set_xlabel("time [Gyr]")
        ax.set_ylabel(r"$M_{\star, cum}$ [$M_\odot$]")
        ax.grid(True)
        ax.plot(eris_time, eris_mass, 'k-', label="'Eris'")
        ax.plot(time, omega1, '--', label=omega1_desc)
        ax.plot(time, omega2, '-.', label=omega2_desc)
        ax.plot(time, omega3, ':', label=omega3_desc)
        ax.plot(time, omega4, '--', label=omega4_desc)
        ax.plot(time, omega5, '-.', label=omega5_desc)
        ax.plot(time, omega6, ':', label=omega6_desc)
        ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.0))
        #ax.legend(loc="best")
        fig.savefig(plot_filename_lambdafunc("stellar_mass"))

    if plot_arg in ["all", "2"]:
        #plot total mass of 'Eris' and all models
        eris_mass = eris_data_inst.mass["total_mass"]
        eris_time = eris_data_inst.mass["time"]
        eris_time /= timescale #scale to Gyr
        time, omega1, omega2, omega3 , omega4, omega5, \
            omega6,  omega7,  omega8,  omega9,  omega10, \
            omega11,  omega12 \
            = np.load(data_filename_lambdafunc("mass_2_n300"))
        time /= timescale
        
        fig = pl.figure("v1.1.2")
        fig.suptitle("Outflow proportional to SNR")
        ax = fig.gca()
        ax.set_xlabel("time [Gyr]")
        ax.set_ylabel(r"$M_{tot}$ [$M_\odot$]")
        ax.grid(True)
        ax.plot(eris_time, eris_mass, 'ko', label="'Eris'")
        ax.plot(time, omega1, '--', label=omega1_desc)
        ax.plot(time, omega2, '-.', label=omega2_desc)
        ax.plot(time, omega3, ':', label=omega3_desc)
        ax.plot(time, omega4, '--', label=omega4_desc)
        ax.plot(time, omega5, '-.', label=omega5_desc)
        ax.plot(time, omega6, ':', label=omega6_desc)
        ax.set_ylim((0,1.1*max(eris_mass)))
        ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.0))
        fig.savefig(plot_filename_lambdafunc("total_mass"))

    if plot_arg in ["all", "3"]:
        #plot [Fe/H] of 'Eris' and some omega models
        #show that variation in outflow does not reproduce 'dips' (omega7-12)
        eris_mass = eris_data_inst.sfgas["[Fe/H]"]
        eris_time = eris_data_inst.sfgas["time"]
        eris_time /= timescale #scale to Gyr
        time, omega1, omega2, omega3 , omega4, omega5, \
            omega6,  omega7,  omega8,  omega9,  omega10, \
            omega11,  omega12 \
            = np.load(data_filename_lambdafunc("spectro_1_n300"))
        time /= timescale
        
        fig = pl.figure("v1.1.3")
        fig.suptitle("Outflow proportional to SNR")
        ax = fig.gca()
        ax.set_title(omega7_desc[19:])
        ax.set_xlabel("time [Gyr]")
        ax.set_ylabel(r"[Fe/H]")
        ax.grid(True)
        ax.plot(eris_time, eris_mass, 'k-', label="'Eris'")
        #plot last six models, without the 'emptied ones', remove initial and inflow from legendtext
        ax.plot(time, omega7, '--', label=omega7_desc[:17]) 
        ax.plot(time, omega8, '-.', label=omega8_desc[:17])
        ax.plot(time, omega9, '--', label=omega9_desc[:17])
        ax.plot(time, omega10, '-.', label=omega10_desc[:17])
        #ax.plot(time, omega11, '--', label=omega11_desc)
        #ax.plot(time, omega12, '-.', label=omega12_desc)
        ax.set_ylim((-3,0))
        ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.0))
        #ax.legend(loc="best")
        fig.savefig(plot_filename_lambdafunc("iron"))

def v1_final(plot_arg="all"):
    print "plotting final parameters of v1"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "mass_parameters_v3_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_mass_3_plot_%s.png"%file_str
    """Incorporating conclusions into one final mass example.
    Inflow=4.0, ML=0.3, M_init=5.6e+10..
    zeroth array: time 
    first array: default w/M_tot('Eris') 
    second array: Milky Way default w/M_tot('Eris') 
    third array: Milky Way default w/const. SFH  w/M_tot('Eris') 
    fourth array: 'Eris'"""
    
    omega1_desc = "'Omega' default"
    omega2_desc = "'Omega' MW"
    omega3_desc = "'Omega' MW cte"
    omega4_desc = "Fiducial 'Omega'"
    filenames = ["masses_1_n300", "masses_2_n300", "rates_0_n300", "spectro_0_n300", "spectro_1_n300"]
    timescale = 1e+9 #scale time to Gyrs

    
    if plot_arg in ["all", "1"]:
        ### plot stellar mass ###
        eris_mass = eris_data_inst.sfr["m_cum"]
        eris_time = eris_data_inst.sfr["time"]
        eris_time /= timescale #scale to Gyr
        time, omega1, omega2, omega3, omega4 \
            = np.load(data_filename_lambdafunc( filenames[0] ))
        time /= timescale #scale time to Gyrs
        #calculate cumulative stellar mass to compare with 'Eris'
        omega1, omega2, omega3, omega4\
            = np.cumsum(omega1), np.cumsum(omega2), \
            np.cumsum(omega3), np.cumsum(omega4)
        #make plot-object
        fig = pl.figure("v1.3.1")
        fig.suptitle("Fitting of Fiducial Omega to mass content")
        ax = fig.gca()
        ax.set_xlabel("time [Gyr]")
        ax.set_ylabel(r"$M_{\star, cum}$ [$M_\odot$]")
        ax.grid(True)
        ax.plot(eris_time, eris_mass, 'k-', label="'Eris'")
        # ax.plot(time, omega1, '--', label=omega1_desc)
        # ax.plot(time, omega2, '-.', label=omega2_desc)
        # ax.plot(time, omega3, '--', label=omega3_desc)
        ax.plot(time, omega4, '-.', label=omega4_desc)
        #ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.0))
        ax.legend(loc="best")
        fig.savefig(plot_filename_lambdafunc("stellar_mass"))
        print plot_filename_lambdafunc("stellar_mass")

    if plot_arg in ["all", "2"]:
        ### plot total mass ###
        print "Warning! total mass does not reproduce github!"
        eris_mass = eris_data_inst.mass["total_mass"]
        eris_time = eris_data_inst.mass["time"]
        eris_time /= timescale #scale to Gyr
        time, omega1, omega2, omega3, omega4 \
            = np.load(data_filename_lambdafunc( filenames[1] ))
        time /= timescale #scale time to Gyrs
        #make plot-object
        fig = pl.figure("v1.3.2")
        fig.suptitle("Fitting of Fiducial Omega to mass content")
        ax = fig.gca()
        ax.set_xlabel("time [Gyr]")
        ax.set_ylabel(r"$M_{tot}$ [$M_\odot$]")
        ax.grid(True)
        ax.plot(eris_time, eris_mass, 'k.', label="'Eris'")
        # ax.plot(time, omega1, '--', label=omega1_desc)
        # ax.plot(time, omega2, '-.', label=omega2_desc)
        # ax.plot(time, omega3, '--', label=omega3_desc)
        ax.plot(time, omega4, '--', label=omega4_desc)
        #ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.0))
        ax.legend(loc="best")
        fig.savefig(plot_filename_lambdafunc("total_mass"))
        print plot_filename_lambdafunc("total_mass")

    """
    if plot_arg in ["all", "3"]:
    ### plot sfr ###
    eris_sfr = eris_data_inst.sfr["sfr"]
    eris_time = eris_data_inst.sfr["time"]
    eris_time /= timescale #scale to Gyr
    time, omega1, omega2, omega3, omega4 \
        = np.load(data_filename_lambdafunc( filenames[2] ))
    time /= timescale #scale time to Gyrs
    #make plot-object
    fig = pl.figure("v1.3.3")
    fig.suptitle("Comparison of models")
    ax = fig.gca()
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel(r"Star formation rate [$M_\odot$/yr]")
    ax.grid(True)
    ax.plot(time, omega1, '--', label=omega1_desc)
    ax.plot(time, omega2, '-.', label=omega2_desc)
    ax.plot(time, omega3, '--', label=omega3_desc)
    ax.plot(time, omega4, '-.', label=omega4_desc)
    ax.plot(eris_time, eris_sfr, 'k-', label="'Eris'")
    #ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.0))
    ax.legend(loc="best")
    fig.savefig(plot_filename_lambdafunc("sfr"))

    if plot_arg in ["all", "4"]:
    ### plot [O/H] ###
    eris_oxy = eris_data_inst.sfgas["[O/H]"]
    eris_time = eris_data_inst.sfgas["time"]
    eris_time /= timescale #scale to Gyr
    time, omega1, omega2, omega3, omega4 \
        = np.load(data_filename_lambdafunc( filenames[3] ))
    time /= timescale #scale time to Gyrs
    #make plot-object
    fig = pl.figure("v1.3.4")
    fig.suptitle("Comparison of models")
    ax = fig.gca()
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel(r"[O/H]")
    ax.grid(True)
    ax.plot(time, omega1, '--', label=omega1_desc)
    ax.plot(time, omega2, '-.', label=omega2_desc)
    ax.plot(time, omega3, '--', label=omega3_desc)
    ax.plot(time, omega4, '-.', label=omega4_desc)
    ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.2))
    #ax.legend(loc="best")
    ax.set_ylim((-5,2))
    fig.savefig(plot_filename_lambdafunc("spectro_oxy"))

    if plot_arg in ["all", "5"]:    
    ### plot [Fe/H] ###
    eris_oxy = eris_data_inst.sfgas["[Fe/H]"]
    eris_time = eris_data_inst.sfgas["time"]
    eris_time /= timescale #scale to Gyr
    time, omega1, omega2, omega3, omega4 \
        = np.load(data_filename_lambdafunc( filenames[4] ))
    time /= timescale #scale time to Gyrs
    #make plot-object
    fig = pl.figure("v1.3.5")
    fig.suptitle("Comparison of models")
    ax = fig.gca()
    ax.set_xlabel("time [Gyr]")
    ax.set_ylabel(r"[O/H]")
    ax.grid(True)
    ax.plot(time, omega1, '--', label=omega1_desc)
    ax.plot(time, omega2, '-.', label=omega2_desc)
    ax.plot(time, omega3, '--', label=omega3_desc)
    ax.plot(time, omega4, '-.', label=omega4_desc)
    ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.2))
    #ax.legend(loc="best")
    ax.set_ylim((-5,2))
    fig.savefig(plot_filename_lambdafunc("spectro_iron"))
    """

if plot_all or mass_param or False:
    if False:
        v1_minit_minf()
    if False:
        v1_mout(plot_arg="all")
    if True:
        v1_final()

############################
### plots from version 2 ###
############################
def v2_star_useless(plot_arg="all"):
    """ Plot the useless data from star-files """
    print "plotting the '%s'pop III figures"%plot_arg
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "star_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_star_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_time = eris_data().sfgas["time"]
    eris_oxy = eris_data().sfgas["[O/H]"]
    eris_iron = eris_data().sfgas["[Fe/H]"]
    eris_time /= timescale #scale with timescale

    if plot_arg in ["all", "1"]:
        #plot spectroscopic data with change in transitionmass #[Fe/H]
        filename = data_filename_lambdafunc("v2_1_n30")
        fig = pl.figure("v2.1.1"); 
        fig.suptitle("Transitionmass between AGB-stars and Massive stars")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        omega_desc = ["7.0","8.0","9.0","10.0"]
        ax.plot(time, omega1, '--', label="$M_{trans.}=%sM_\odot$"%omega_desc[0])
        ax.plot(time, omega2, '-.', label="$M_{trans.}=%sM_\odot$"%omega_desc[1])
        ax.plot(time, omega3, '--', label="$M_{trans.}=%sM_\odot$"%omega_desc[2])
        ax.plot(time, omega4, '-.', label="$M_{trans.}=%sM_\odot$"%omega_desc[3])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("transmass")
        fig.savefig(filename)
        

    if plot_arg in ["all", "2"]:
        #plot spectroscopic data with change in pop3 yield tables
        #[O/H]
        filename = data_filename_lambdafunc("v3_0_n300")
        fig = pl.figure("v2.1.2"); ax = fig.gca(); ax.grid(True); ax.hold(True)
        fig.suptitle("Yield table for Population III stars"); ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        time, omega1, omega2, omega3 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label="Heger & Woosley (2010)")
        ax.plot(time, omega2, '-.', label="Heger & Woosley (2010)")
        ax.plot(time, omega3, ':', label="Nomoto 2013")
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("pop3_yt_oxy")
        fig.savefig(filename)

    if plot_arg in ["all", "3"]:
        #[Fe/H]
        filename = data_filename_lambdafunc("v3_1_n300")
        fig = pl.figure("v2.1.3"); ax = fig.gca(); ax.grid(True); ax.hold(True)
        fig.suptitle("Yield table for Population III stars"); ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label="Heger & Woosley (2010)")
        ax.plot(time, omega2, '-.', label="Heger & Woosley (2010)")
        ax.plot(time, omega3, ':', label="Nomoto 2013")
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("pop3_yt_iron")
        fig.savefig(filename)

    if plot_arg in ["all", "4"]:
        #plot spectroscopic data with change in pop3 imf boundaries
        #[O/H]
        filename = data_filename_lambdafunc("v4_0_n300")
        fig = pl.figure("v2.1.4"); ax = fig.gca(); ax.grid(True); ax.hold(True)
        fig.suptitle("IMF boundaries for populaation III stars"); ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=r"imf $\in$ [20.0, 100.0]")
        ax.plot(time, omega2, '-.', label="imf $\in$ [5.0, 100.0]")
        ax.plot(time, omega3, '--', label="imf $\in$ [1.0, 20.0]")
        ax.plot(time, omega3, '-.', label="imf $\in$ [0.1, 20.0]")
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("pop3_bound_oxy")
        fig.savefig(filename)

    if plot_arg in ["all", "5"]:
        #[Fe/H]
        filename = data_filename_lambdafunc("v4_0_n300")
        fig = pl.figure("v2.1.5"); ax = fig.gca(); ax.grid(True); ax.hold(True)
        fig.suptitle("IMF boundaries for populaation III stars"); ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=r"imf $\in$ [20.0, 100.0]")
        ax.plot(time, omega2, '-.', label="imf $\in$ [5.0, 100.0]")
        ax.plot(time, omega3, '--', label="imf $\in$ [1.0, 20.0]")
        ax.plot(time, omega3, '-.', label="imf $\in$ [0.1, 20.0]")
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("pop3_bound_iron")
        fig.savefig(filename)

    if plot_arg in ["all", "6"]:
        #plot spectroscopic data with different agb/M yield tables
        filename = data_filename_lambdafunc("v2_1_n30")
        fig = pl.figure("v2.1.1"); 
        fig.suptitle("Transitionmass between AGB-stars and Massive stars")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        omega_desc = ["7.0","8.0","9.0","10.0"]
        ax.plot(time, omega1, '--', label="$M_{trans.}=%sM_\odot$"%omega_desc[0])
        ax.plot(time, omega2, '-.', label="$M_{trans.}=%sM_\odot$"%omega_desc[1])
        ax.plot(time, omega3, '--', label="$M_{trans.}=%sM_\odot$"%omega_desc[2])
        ax.plot(time, omega4, '-.', label="$M_{trans.}=%sM_\odot$"%omega_desc[3])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("transmass")
        fig.savefig(filename)


def v2_sn1a_useless():
    """ Plot the useless data from sn1a-files """
    print "plotting the SN1a tables"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "sn1a_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_sn1a_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_time = eris_data().sfgas["time"]
    eris_oxy = eris_data().sfgas["[O/H]"]
    eris_iron = eris_data().sfgas["[Fe/H]"]
    eris_time /= timescale #scale with timescale

    #plot spectroscopic data with change in transitionmass #[Fe/H]
    filename = data_filename_lambdafunc("v3_spectro_1_n30")
    """ explanatory-file
    first array: sn1a_i99_CDD1.txt Iwamoto et al. (1999) CDD1
    second array: sn1a_i99_CDD2.txt Iwamoto et al. (1999) CDD2
    third array: sn1a_i99_W7.txt Iwamoto et al. (1999) W7
    fourth array: sn1a_ivo12_mix_z.txt Seitenzahl et al. (2012) table 2 &C-12      &3.04E-03  &3.10e-03  &3.15e-03  &3.16e-03
    fifth array: sn1a_ivo12_stable_z.txt Seitenzahl et al. (2012) table 2 &C-12      &3.04E-03  &3.10e-03  &3.15e-03  &3.16e-03
    sixth array: sn1a_ivo13_mix_z.txt Seitenzahl et al. (2012) table 2 &C-12      &3.04E-03  &3.10e-03  &3.15e-03  &3.16e-03
    seventh array: sn1a_ivo13_stable_z.txt Seitenzahl et al. (2012) table 2 &C-12      &3.04E-03  &3.10e-03  &3.15e-03  &3.16e-03
    eigth array: sn1a_t03.txt Tielemann et al. (2003)
    ninth array: sn1a_t86.txt Tielemann et al. (1986) table 5
    """
    omega_desc = ["Iwamoto et al. (1999) CDD1", "Iwamoto et al. (1999) CDD2", "Iwamoto et al. (1999) W7",
                   "Seitenzahl et al. (2012) table 2", "Seitenzahl et al. (2012) table 2", "Seitenzahl et al. (2012) table 2",
                   "Seitenzahl et al. (2012) table 2", "Tielemann et al. (2003)", "Tielemann et al. (1986) table 5"]
    fig = pl.figure("v2.2.1"); 
    fig.suptitle("Type 1a Supernova yield tables")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
    time, omega1, omega2, omega3, omega4, \
        omega5, omega6, omega7, omega8, omega9 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, ':', label=omega_desc[2])
    ax.plot(time, omega4, '--', label=omega_desc[3])
    #ax.plot(time, omega5, '-.', label=omega_desc[4])
    #ax.plot(time, omega6, ':', label=omega_desc[5])
    #ax.plot(time, omega7, '--', label=omega_desc[6])
    ax.plot(time, omega8, '-.', label=omega_desc[7])
    ax.plot(time, omega9, ':', label=omega_desc[8])
    ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("sn1a_yt")
    fig.savefig(filename)

def v2_sn1a(plot_arg="all"):
    """ Plot the relevant and useful data from pop3-files """
    print "plotting sn1a"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "sn1a_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_sn1a_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr
    numbers_string = r"$N_{SN1a}/M_{\odot}$"
    dtd_string = r"$DTD_{SN1a}$"

    #get eris-data for [O/H] and [Fe/H]
    eris_time = eris_data().sfgas["time"]
    eris_oxy = eris_data().sfgas["[O/H]"]
    eris_iron = eris_data().sfgas["[Fe/H]"]
    eris_time /= timescale #scale with timescale


    if plot_arg in ["all", "1"]:
        #plot [O/H] and [Fe/H] for sn1a-numbers
        print "plotting sn1a numbers"
        #[O/H]
        filename = data_filename_lambdafunc("v1_spectro_0_n30")
        """ explanatory file
        first array: 'Eris' bestfit w/nb1a_per_m=1.0e-05 
        second array: 'Eris' bestfit w/nb1a_per_m=8.0e-04 
        third array: 'Eris' bestfit w/nb1a_per_m=1.0e-03 
        fourth array: 'Eris' bestfit w/nb1a_per_m=1.5e-03 
        fifth array: 'Eris' bestfit w/nb1a_per_m=2.0e-03 
        sixth array: 'Eris' bestfit w/nb1a_per_m=3.0e-03 
        seventh array: 'Eris' bestfit w/nb1a_per_m=1.0e-01 
        eigth array: 'Eris' bestfit w/nb1a_per_m=1.0e+00 
        """
        omega_desc = ["1.0e-05","8.0e-04","1.0e-03","1.5e-03","2.0e-03","3.0e-03","1.0e-01","1.0e+00"]
        fig = pl.figure("v2.3.1"); 
        fig.suptitle("Number of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        time, omega1, omega2, omega3, omega4, \
            omega5, omega6, omega7, omega8 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=numbers_string+"=%s"%omega_desc[0])
        ax.plot(time, omega2, '-.', label=numbers_string+"=%s"%omega_desc[1])
        ax.plot(time, omega3, ':', label=numbers_string+"=%s"%omega_desc[2])
        ax.plot(time, omega4, '--', label=numbers_string+"=%s"%omega_desc[3])
        ax.plot(time, omega5, '-.', label=numbers_string+"=%s"%omega_desc[4])
        ax.plot(time, omega6, ':', label=numbers_string+"=%s"%omega_desc[5])
        ax.plot(time, omega7, '--', label=numbers_string+"=%s"%omega_desc[6])
        ax.plot(time, omega8, '-.', label=numbers_string+"=%s"%omega_desc[7])
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_num1_oxy")
        fig.savefig(filename)

        #[Fe/H]
        filename = data_filename_lambdafunc("v1_spectro_1_n30")
        fig = pl.figure("v2.3.2"); 
        fig.suptitle("Number of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3, omega4, \
            omega5, omega6, omega7, omega8 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=numbers_string+"=%s"%omega_desc[0])
        ax.plot(time, omega2, '-.', label=numbers_string+"=%s"%omega_desc[1])
        ax.plot(time, omega3, ':', label=numbers_string+"=%s"%omega_desc[2])
        ax.plot(time, omega4, '--', label=numbers_string+"=%s"%omega_desc[3])
        ax.plot(time, omega5, '-.', label=numbers_string+"=%s"%omega_desc[4])
        ax.plot(time, omega6, ':', label=numbers_string+"=%s"%omega_desc[5])
        ax.plot(time, omega7, '--', label=numbers_string+"=%s"%omega_desc[6])
        ax.plot(time, omega8, '-.', label=numbers_string+"=%s"%omega_desc[7])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_num1_iron")
        fig.savefig(filename)

    if plot_arg in ["all", "2"]:
        #plot [O/H] and [Fe/H] for power-law dtd
        print "plotting power-law delay-time distribution"
        """ explanatory file
        first array: 'Eris' bestfit w/sn1a power=-5.0 
        second array: 'Eris' bestfit w/sn1a power=-3.5 
        third array: 'Eris' bestfit w/sn1a power=-1.0 
        fourth array: 'Eris' bestfit w/sn1a power=-0.1 
        """
        omega_desc = ["-5.0","-3.5","-1.0","-0.1"]
        
        #[O/H]
        filename = data_filename_lambdafunc("v2_powerlaw_spectro_0_n30")
        fig = pl.figure("v2.3.3"); 
        fig.suptitle("Delay-time distribution of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        ax.set_title("Power law distribution")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=dtd_string+r"=$t^{%s}$"%omega_desc[0])
        ax.plot(time, omega2, '-.', label=dtd_string+r"=$t^{%s}$"%omega_desc[1])
        ax.plot(time, omega3, '--', label=dtd_string+r"=$t^{%s}$"%omega_desc[2])
        ax.plot(time, omega4, '-.', label=dtd_string+r"=$t^{%s}$"%omega_desc[3])
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_dtd1_oxy")
        fig.savefig(filename)

        #[Fe/H]
        filename = data_filename_lambdafunc("v2_powerlaw_spectro_1_n30")
        fig = pl.figure("v2.3.4"); 
        fig.suptitle("Delay-time distribution of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_title("Power law distribution")
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=dtd_string+r"=$t^{%s}$"%omega_desc[0])
        ax.plot(time, omega2, '-.', label=dtd_string+r"=$t^{%s}$"%omega_desc[1])
        ax.plot(time, omega3, '--', label=dtd_string+r"=$t^{%s}$"%omega_desc[2])
        ax.plot(time, omega4, '-.', label=dtd_string+r"=$t^{%s}$"%omega_desc[3])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_dtd1_iron")
        fig.savefig(filename)

    if plot_arg in ["all", "3"]:
        print "plotting gaussian delay-time distribution"
        """ explanatory file
        first array: 'Eris' bestfit w/sn1a gauss=[1.0e+10,1.0e+08] 
        second array: 'Eris' bestfit w/sn1a gauss=[1.0e+10,1.0e+10] 
        third array: 'Eris' bestfit w/sn1a gauss=[1.0e+08,5.0e+07] 
        fourth array: 'Eris' bestfit w/sn1a gauss=[1.0e+08,1.0e+10]
        """
        omega_desc = ["[1.0e+10,1.0e+08]", "[1.0e+10,1.0e+10]", "[1.0e+08,5.0e+07]", "[1.0e+08,1.0e+10]"]
        
        #[O/H]
        filename = data_filename_lambdafunc("v2_gauss_spectro_0_n30")
        fig = pl.figure("v2.3.5"); 
        fig.suptitle("Delay-time distribution of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        ax.set_title("Gaussian distribution")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=dtd_string+r"=G(%s)"%omega_desc[0])
        ax.plot(time, omega2, '-.', label=dtd_string+r"=G(%s)"%omega_desc[1])
        ax.plot(time, omega3, '--', label=dtd_string+r"=G(%s)"%omega_desc[2])
        ax.plot(time, omega4, '-.', label=dtd_string+r"=G(%s)"%omega_desc[3])
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_dtd2_oxy")
        fig.savefig(filename)

        #[Fe/H]
        filename = data_filename_lambdafunc("v2_gauss_spectro_1_n30")
        fig = pl.figure("v2.3.6"); 
        fig.suptitle("Delay-time distribution of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        ax.set_title("Gaussian distribution")
        time, omega1, omega2, omega3, omega4 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=dtd_string+r"=G(%s)"%omega_desc[0])
        ax.plot(time, omega2, '-.', label=dtd_string+r"=G(%s)"%omega_desc[1])
        ax.plot(time, omega3, '--', label=dtd_string+r"=G(%s)"%omega_desc[2])
        ax.plot(time, omega4, '-.', label=dtd_string+r"=G(%s)"%omega_desc[3])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_dtd2_iron")
        fig.savefig(filename)

    if plot_arg in ["all", "4"]:
        print "plotting exponential delay-time distribution"
        """ explanatory file
        first array: 'Eris' bestfit w/sn1a exp=1.0e+06[yr] 
        second array: 'Eris' bestfit w/sn1a exp=5.0e+06[yr] 
        third array: 'Eris' bestfit w/sn1a exp=5.1e+06[yr] 
        fourth array: 'Eris' bestfit w/sn1a exp=5.2e+06[yr] 
        fifth array: 'Eris' bestfit w/sn1a exp=5.3e+06[yr] 
        sixth array: 'Eris' bestfit w/sn1a exp=5.4e+06[yr] 
        seventh array: 'Eris' bestfit w/sn1a exp=5.5e+06[yr] 
        eigth array: 'Eris' bestfit w/sn1a exp=6.0e+06[yr] 
        ninth array: 'Eris' bestfit w/sn1a exp=1.0e+08[yr] 
        """
        e_folding_time_yrs = [1.0e+06,5.0e+06,5.1e+06,5.2e+06,5.3e+06,5.4e+06,5.5e+06,6.0e+06,1.0e+08]
        e_folding_time_Myrs = [e_folding_time / 1e+6 for e_folding_time in e_folding_time_yrs]
        
        #[O/H]
        filename = data_filename_lambdafunc("v2_exp_spectro_0_n30")
        fig = pl.figure("v2.3.7"); 
        fig.suptitle("Delay-time distribution of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        ax.set_title("Exponential distribution")
        time, omega1, omega2, omega3, omega4, \
            omega5, omega6, omega7, omega8, omega9 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[0])
        ax.plot(time, omega2, '-.', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[1])
        ax.plot(time, omega3, ':', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[2])
        ax.plot(time, omega4, '--', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[3])
        ax.plot(time, omega5, '-.', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[4])
        ax.plot(time, omega6, ':', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[5])
        ax.plot(time, omega7, '--', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[6])
        ax.plot(time, omega8, '-.', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[7])
        ax.plot(time, omega9, ':', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[8])
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_dtd3_oxy")
        fig.savefig(filename)

        #[Fe/H]
        filename = data_filename_lambdafunc("v2_exp_spectro_1_n30")
        fig = pl.figure("v2.3.8"); 
        fig.suptitle("Delay-time distribution of Type 1a Supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        ax.set_title("Exponential distribution")
        time, omega1, omega2, omega3, omega4, \
            omega5, omega6, omega7, omega8, omega9 = np.load(filename)
        time /= timescale
        ax.plot(time, omega1, '--', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[0])
        ax.plot(time, omega2, '-.', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[1])
        ax.plot(time, omega3, ':', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[2])
        ax.plot(time, omega4, '--', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[3])
        ax.plot(time, omega5, '-.', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[4])
        ax.plot(time, omega6, ':', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[5])
        ax.plot(time, omega7, '--', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[6])
        ax.plot(time, omega8, '-.', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[7])
        ax.plot(time, omega9, ':', label=dtd_string+r"=$e^{-t/%1.1f[Myr]}$"%e_folding_time_Myrs[8])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-5,2))
        filename = plot_filename_lambdafunc("sn1a_dtd3_iron")
        fig.savefig(filename)

    if plot_arg in ["all", "5"]:
        #plot [O/H] and [Fe/H] for sn1a-numbers
        """ explanatory file
        first array: 'Eris' bestfit w/nb1a_per_m=8.0e-04 
        second array: 'Eris' bestfit w/nb1a_per_m=9.0e-04 
        third array: 'Eris' bestfit w/nb1a_per_m=1.0e-03 
        fourth array: 'Eris' bestfit w/nb1a_per_m=2.0e-03 
        fifth array: 'Eris' bestfit w/nb1a_per_m=3.0e-03
        """
        print "plotting sn1a numbers"
        omega_desc = [8.0e-04, 9.0e-4, 1.0e-3, 2.0e-3, 3.0e-3]
        #[O/H]
        filename = data_filename_lambdafunc("v4_spectro_0_n30")
        fig = pl.figure("v2.3.9"); 
        fig.suptitle("Fitting of Fiducial Omega to type 1a supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[O/H]")
        time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
        time /= timescale
        #ax.plot(time, omega1, '--', label=numbers_string+"=%1.1e"%omega_desc[0])
        #ax.plot(time, omega2, '-.', label=numbers_string+"=%1.1e"%omega_desc[1])
        ax.plot(time, omega3, '--', label="Fiducial Omega") #numbers_string+"=%1.1e"%omega_desc[2])
        #ax.plot(time, omega4, '--', label=numbers_string+"=%1.1e"%omega_desc[3])
        #ax.plot(time, omega5, '-.', label=numbers_string+"=%1.1e"%omega_desc[4])
        ax.plot(eris_time, eris_oxy, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-2,1))
        filename = plot_filename_lambdafunc("sn1a_num2_oxy")
        print filename
        fig.savefig(filename)

        #[Fe/H]
        filename = data_filename_lambdafunc("v4_spectro_1_n30")
        fig = pl.figure("v2.3.10"); 
        fig.suptitle("Fitting of Fiducial Omega to type 1a supernovae")
        ax = fig.gca(); ax.grid(True); ax.hold(True)
        ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Fe/H]")
        time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
        time /= timescale
        #ax.plot(time, omega1, '--', label=numbers_string+"=%1.1e"%omega_desc[0])
        #ax.plot(time, omega2, '-.', label=numbers_string+"=%1.1e"%omega_desc[1])
        ax.plot(time, omega3, '--', label="Fiducial Omega") #numbers_string+"=%1.1e"%omega_desc[2])
        #ax.plot(time, omega4, '--', label=numbers_string+"=%1.1e"%omega_desc[3])
        #ax.plot(time, omega5, '-.', label=numbers_string+"=%1.1e"%omega_desc[4])
        ax.plot(eris_time, eris_iron, 'k-', label="'Eris'")
        ax.legend(loc='best')
        ax.set_ylim((-2,1))
        filename = plot_filename_lambdafunc("sn1a_num2_iron")
        print filename
        fig.savefig(filename)

if plot_all or star_param or False:
    if False:
        v2_star_useless()
    if False:
        v2_sn1a_useless()
    if True:
        v2_sn1a("5")

############################
### plots from version 3 ###
############################
def v3_dtd():
    #plot [Eu/H] for delay-time distribution
    print "plotting the nsm dtd's"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "nsm_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_nsm_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_time = eris_data().sfgas["time"]
    eris_euro = eris_data().sfgas["[Eu/H]"]
    eris_time /= timescale #scale with timescale

    #plot spectroscopic data with dtd-variations #[Fe/H]
    filename = data_filename_lambdafunc("v1_2_n30")
    """ explanatory-file
    first array: 'Eris' bestfit w/nsm_dtd_pow=[5.0e+07,1.4e+10,-3.0] 
    second array: 'Eris' bestfit w/nsm_dtd_pow=[5.0e+07,1.4e+10,-2.0] 
    third array: 'Eris' bestfit w/nsm_dtd_pow=[1.0e+08,1.4e+10,-2.0] 
    fourth array: 'Eris' bestfit w/nsm_dtd_pow=[2.0e+08,1.4e+10,-1.0] 
    fifth array: 'Eris' bestfit w/t_nsm_coal=1.0e+07 
    sixth array: 'Eris' bestfit w/t_nsm_coal=1.0e+08 
    seventh array: 'Eris' bestfit w/t_nsm_coal=1.0e+09 
    """
    omega_desc = ["nsm_dtd_pow=[5.0e+07,1.4e+10,-3.0]","nsm_dtd_pow=[5.0e+07,1.4e+10,-2.0]",
                  "nsm_dtd_pow=[1.0e+08,1.4e+10,-2.0]","nsm_dtd_pow=[2.0e+08,1.4e+10,-1.0]",
                  "t_nsm_coal=1.0e+07","t_nsm_coal=1.0e+08","t_nsm_coal=1.0e+09"]
    fig = pl.figure("v3.1.1"); 
    fig.suptitle("Delay-time distribution of Neutron Star Mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Eu/H]")
    time, omega1, omega2, omega3, omega4, \
        omega5, omega6, omega7 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, 'b--', label=omega_desc[0])
    ax.plot(time, omega2, 'g--', label=omega_desc[1])
    ax.plot(time, omega3, 'r--', label=omega_desc[2])
    ax.plot(time, omega4, 'c--', label=omega_desc[3])
    ax.plot(time, omega5, 'b:', label=omega_desc[4])
    ax.plot(time, omega6, 'g:', label=omega_desc[5])
    ax.plot(time, omega7, 'r:', label=omega_desc[6])
    ax.plot(eris_time, eris_euro, 'k-', label="'Eris'")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("dtd")
    fig.savefig(filename)

    return None

def v3_ejmass():
    #plot [Eu/H] for ejecta mass
    print "plotting the nsm ejecta mass"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "nsm_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_nsm_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_time = eris_data().sfgas["time"]
    eris_euro = eris_data().sfgas["[Eu/H]"]
    eris_time /= timescale #scale with timescale

    #plot spectroscopic data with dtd-variations #[Fe/H]
    filename = data_filename_lambdafunc("v2_ejmass_2_n30")
    """ explanatory-file
    first array: 'Eris' bestfit w/ej_mass=1.0e-03 
    second array: 'Eris' bestfit w/ej_mass=1.0e-01 
    third array: 'Eris' bestfit w/ej_mass=2.0e-01 
    fourth array: 'Eris' bestfit w/ej_mass=3.0e-01 
    fifth array: 'Eris' bestfit w/ej_mass=1.0e+00 
    """
    loa_ejectamass = ["1.0e-03","1.0e-01","2.0e-01","3.0e-01","1.0e+00"]
    omega_desc = loa_ejectamass
    
    fig = pl.figure("v3.2.1"); 
    fig.suptitle("Ejecta mass from Neutron Star Mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Eu/H]")
    time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, ':', label=omega_desc[2])
    ax.plot(time, omega4, '--', label=omega_desc[3])
    ax.plot(time, omega5, '-.', label=omega_desc[4])
    ax.plot(eris_time, eris_euro, 'k-', label="'Eris'")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("ejmass")
    fig.savefig(filename)

    return None

def v3_mergerfraction():
    #plot [Eu/H] and nsm rates for merger fraction
    print "plotting the nsm merger fraction"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "nsm_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_nsm_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_rate = eris_data().nsm["nsm_rate"]
    eris_time_rate = eris_data().nsm["time_rate"]
    eris_time_rate /= timescale #scale with timescale
    eris_euro = eris_data().sfgas["[Eu/H]"]
    eris_time_euro = eris_data().sfgas["time"]
    eris_time_euro /= timescale #scale with timescale
    """ explanatory-file
    first array: 'Eris' bestfit w/f_merger=7.0e-04 
    second array: 'Eris' bestfit w/f_merger=9.0e-04 
    third array: 'Eris' bestfit w/f_merger=1.0e-03 
    fourth array: 'Eris' bestfit w/f_merger=7.0e-03 
    fifth array: 'Eris' bestfit w/f_merger=1.0e-02 
    sixth array: 'Eris' bestfit w/f_merger=1.0e-01 
    """
    loa_frac = ["7.0e-04","9.0e-04","1.0e-03","7.0e-03","1.0e-02","1.0e-01"]
    omega_desc = loa_frac

    #plot nsm-rates data with mergerfractions
    filename = data_filename_lambdafunc("v2_mergerfraction_rates_2_n300")
    
    fig = pl.figure("v3.3.1"); 
    fig.suptitle("Merger fraction of Neutron Star Mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("nsm rate")
    time, omega1, omega2, omega3, omega4, omega5, omega6 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, ':', label=omega_desc[2])
    #ax.plot(time, omega4, '--', label=omega_desc[3])
    #ax.plot(time, omega5, '-.', label=omega_desc[4])
    #ax.plot(time, omega6, ':', label=omega_desc[5])
    ax.plot(eris_time_rate, eris_rate, 'k-', label="'Eris'")
    ax.legend(loc='best')
    #ax.ticklabel_format(style="sci")
    ax.set_ylim((-1e-6,1e-5))
    filename = plot_filename_lambdafunc("mergerfraction_rates")
    fig.savefig(filename)

    #plot spectroscopic data with mergerfractions
    filename = data_filename_lambdafunc("v2_mergerfraction_spectro_2_n300")
    
    fig = pl.figure("v3.3.2"); 
    fig.suptitle("Merger fraction of Neutron Star Mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Eu/H]")
    time, omega1, omega2, omega3, omega4, omega5, omega6 = np.load(filename)
    time /= timescale
    #ax.plot(time, omega1, '--', label=omega_desc[0])
    #ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, ':', label=omega_desc[2])
    ax.plot(time, omega4, '--', label=omega_desc[3])
    ax.plot(time, omega5, '-.', label=omega_desc[4])
    ax.plot(time, omega6, ':', label=omega_desc[5])
    ax.plot(eris_time_euro, eris_euro, 'k-', label="'Eris'")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("mergerfraction_spectro")
    fig.savefig(filename)

    return None

def v3_nbnsm():
    #plot [Eu/H] and nsm rates for number of nsm per stellar mass formed
    print "plotting the number nsm's per mass"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "nsm_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_nsm_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_rate = eris_data().nsm["nsm_rate"]
    eris_time_rate = eris_data().nsm["time_rate"]
    eris_time_rate /= timescale #scale with timescale
    eris_euro = eris_data().sfgas["[Eu/H]"]
    eris_time_euro = eris_data().sfgas["time"]
    eris_time_euro /= timescale #scale with timescale
    """ explanatory-file
    first array: 'Eris' bestfit w/(#nsm/m)=2.0e-06 
    second array: 'Eris' bestfit w/(#nsm/m)=1.0e-05 
    third array: 'Eris' bestfit w/(#nsm/m)=2.0e-05 
    fourth array: 'Eris' bestfit w/(#nsm/m)=3.0e-05 
    fifth array: 'Eris' bestfit w/(#nsm/m)=1.0e-04
    """
    loa_frac = ["2.0e-06","1.0e-05","2.0e-05","3.0e-05","1.0e-04"]
    omega_desc = loa_frac

    #plot nsm-rates data with nb_nsm_per_mass
    filename = data_filename_lambdafunc("v2_nbnsm_rates_2_n300")    
    fig = pl.figure("v3.4.1"); 
    fig.suptitle("Number of Neutron Star Mergers per stellar mass formed")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("nsm rate")
    time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, ':', label=omega_desc[2])
    #ax.plot(time, omega4, '--', label=omega_desc[3])
    #ax.plot(time, omega5, '-.', label=omega_desc[4])
    ax.plot(eris_time_rate, eris_rate, 'k-', label="'Eris'")
    ax.legend(loc='best')
    #ax.ticklabel_format(style="sci")
    ax.set_ylim((-1e-6,1e-5))
    filename = plot_filename_lambdafunc("nbnsm_rates")
    fig.savefig(filename)
    
    #plot spectroscopic data with nbnsm
    filename = data_filename_lambdafunc("v2_nbnsm_spectro_2_n300")
    
    fig = pl.figure("v3.4.2"); 
    fig.suptitle("Number of Neutron Star Mergers per stellar mass formed")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Eu/H]")
    time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, ':', label=omega_desc[2])
    ax.plot(time, omega4, '--', label=omega_desc[3])
    ax.plot(time, omega5, '-.', label=omega_desc[4])
    ax.plot(eris_time_euro, eris_euro, 'k-', label="'Eris'")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("nbnsm_spectro")
    fig.savefig(filename)

    return None

def v3_combo():
    #plot [Eu/H] and nsm rates for combination of ejecta mass and merger fraction
    print "plotting nsm KN/Spectro combo (needs better descirption)"
    print "Warning! Check the entries in explanatory file, might be mixed up"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "nsm_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_nsm_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_rate = eris_data().nsm["nsm_rate"]
    eris_time_rate = eris_data().nsm["time_rate"]
    eris_time_rate /= timescale #scale with timescale
    eris_euro = eris_data().sfgas["[Eu/H]"]
    eris_time_euro = eris_data().sfgas["time"]
    eris_time_euro /= timescale #scale with timescale
    """ explanatory-file
    first array: 'Eris' bestfit M_ej=6.0e-02 f_m=8.0e-04 
    second array: 'Eris' bestfit M_ej=8.0e-02 f_m=8.0e-04 
    third array: 'Eris' bestfit M_ej=9.0e-02 f_m=8.0e-04 
    fourth array: 'Eris' bestfit M_ej=2.0e-01 f_m=8.0e-04 
    fifth array: 'Eris' bestfit M_ej=3.0e-01 f_m=8.0e-04 
    """
    merger_fraction = "8e-4"
    loa_ejmass = ["6.0e-02", "8.0e-02", "9.0e-02", "2.0e-01", "3.0e-01"]
    omega_desc = [r"$M_{ej}=$%s"%ejmass for ejmass in loa_ejmass]

    #plot nsm-rates data with nb_nsm_per_mass
    filename = data_filename_lambdafunc("v3_rates_2_n300")    
    fig = pl.figure("v3.5.1"); 
    fig.suptitle("Fitting of Fiducial Omega to neutron star mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("nsm rate")
    time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, '--', label=omega_desc[2])
    ax.plot(time, omega4, '-.', label=omega_desc[3])
    ax.plot(time, omega5, '--', label=omega_desc[4])
    ax.plot(eris_time_rate, eris_rate, 'k-', label="'Eris'")
    ax.legend(loc='best')
    #ax.ticklabel_format(style="sci")
    ax.set_ylim((-1e-6,1e-5))
    filename = plot_filename_lambdafunc("combo_rates")
    print filename
    fig.savefig(filename)
    
    #plot spectroscopic data with combo
    filename = data_filename_lambdafunc("v3_spectro_2_n300")
    
    fig = pl.figure("v3.5.2"); 
    fig.suptitle("Fitting of Fiducial Omega to neutron star mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Eu/H]")
    time, omega1, omega2, omega3, omega4, omega5 = np.load(filename)
    time /= timescale
    ax.plot(time, omega1, '--', label=omega_desc[0])
    ax.plot(time, omega2, '-.', label=omega_desc[1])
    ax.plot(time, omega3, '--', label=omega_desc[2])
    ax.plot(time, omega4, '-.', label=omega_desc[3])
    ax.plot(time, omega5, '--', label=omega_desc[4])
    ax.plot(eris_time_euro, eris_euro, 'k-', label="'Eris'")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("combo_spectro")
    print filename
    fig.savefig(filename)

    return None

def v3_final():
    #plot [Eu/H] and nsm rates for final nsm-bestfit results
    print "plotting final nsm"
    data_filename_lambdafunc = lambda file_str: data_dir + \
                               "nsm_parameters_%s.npy"%file_str
    plot_filename_lambdafunc = lambda file_str: plot_dir + \
                               "set_nsm_plot_%s.png"%file_str
    timescale = 1e+9 #scale time-axes to Gyr

    #get eris-data for [O/H] and [Fe/H]
    eris_rate = eris_data().nsm["nsm_rate"]
    eris_time_rate = eris_data().nsm["time_rate"]
    eris_time_rate /= timescale #scale with timescale
    eris_euro = eris_data().sfgas["[Eu/H]"]
    eris_time_euro = eris_data().sfgas["time"]
    eris_time_euro /= timescale #scale with timescale

    #plot nsm-rates data with nb_nsm_per_mass
    filename = data_filename_lambdafunc("v4_rates_2_n300")    
    fig = pl.figure("v3.6.1"); 
    fig.suptitle("Fitting of Fiducial Omega to neutron star mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("nsm rate")
    time, omega = np.load(filename)
    time /= timescale
    ax.plot(time, omega, '--', label="Fiducial Omega")
    ax.plot(eris_time_rate, eris_rate, 'k-', label="Eris")
    ax.legend(loc='best')
    #ax.set_ylim((-1e-6,1e-5))
    filename = plot_filename_lambdafunc("final_rates")
    print filename
    fig.savefig(filename)
    
    #plot spectroscopic data with combo
    filename = data_filename_lambdafunc("v4_spectro_2_n300")
    
    fig = pl.figure("v3.6.2"); 
    fig.suptitle("Fitting of Fiducial Omega to neutron star mergers")
    ax = fig.gca(); ax.grid(True); ax.hold(True)
    ax.set_xlabel("time [Gyr]"), ax.set_ylabel("[Eu/H]")
    time, omega = np.load(filename)
    time /= timescale
    ax.plot(time, omega, '--', label="Fiducial Omega")
    ax.plot(eris_time_euro, eris_euro, 'k-', label="Eris")
    ax.legend(loc='best')
    ax.set_ylim((-5,2))
    filename = plot_filename_lambdafunc("final_spectro")
    print filename
    fig.savefig(filename)

    return None

if plot_all or nsm_param or False:
    if False:
        v3_dtd()
    if False:
        v3_ejmass()
    if False:
        v3_mergerfraction()
    if False:
        v3_nbnsm()
    if False:
        v3_combo()
    if True:
        v3_final()

##############################
### plot timestep analysis ###
##############################
if plot_all or timestep or False:
    None

##################################
### plots from current bestfit ###
##################################
"""
spectro_n300_param0
spectro_n300_param1
spectro_n300_param2"""
def cbf_masses(plot_arg="all"):
    if plot_arg in ["all", "1"]:
        filename_in = data_dir + "masses_n300_param0"
        filename_out = plot_dir + ""
    if plot_arg in ["all", "2"]:
        filename_in = data_dir + "masses_n300_param1"
        filename_out = plot_dir + ""
    if plot_arg in ["all", "3"]:
        filename_in = data_dir + "masses_n300_param2"
        filename_out = plot_dir + ""

    return None

def cbf_spectro(plot_arg="all"):
    if plot_arg in ["all", "1"]:
        filename_in = data_dir + "spectro_n300_param0"
        filename_out = plot_dir + ""
    if plot_arg in ["all", "2"]:
        filename_in = data_dir + "spectro_n300_param1"
        filename_out = plot_dir + ""
    if plot_arg in ["all", "3"]:
        filename_in = data_dir + "spectro_n300_param2"
        filename_out = plot_dir + ""
        
    return None

def cbf_rates(plot_arg="all"):
    if plot_arg in ["all", "1"]:
        filename_in = data_dir + "rates_n300_param0"
        filename_out = plot_dir + ""
    if plot_arg in ["all", "2"]:
        filename_in = data_dir + "rates_n300_param1"
        filename_out = plot_dir + ""
    if plot_arg in ["all", "3"]:
        filename_in = data_dir + "rates_n300_param2"
        filename_out = plot_dir + ""

    return None

if plot_all or cbf or False:
    if True:
        cbf_masses()
    if True:
        cbf_spectro()
    if True:
        cbf_rates()

pl.show()
