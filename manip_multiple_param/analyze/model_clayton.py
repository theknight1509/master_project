"""
This script is for modelling the chemical evolution model of Clayton (1964)
to the data from Omega (after fitting to Eris). 
The model relies on two parameters, the point is to find uncertainty distributions
of the parameters after fitting to data, with uncertainty.

Use scipy.optimize.curve_fit (https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.optimize.curve_fit.html)
"""
import sys, os
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

### Fix details for plots ###
from matplotlib import rcParams
# for key in rcParams.keys():
#     print key
# print rcParams[u"legend.fontsize"] 
# sys.exit()
rcParams[u"legend.fontsize"] = "small"
rcParams[u"lines.linewidth"] = 2.0
rcParams[u"font.size"] = 14

def cosmochronology_luck(time, a, b):
    lambda_re187 = a
    beta_rncp = b

    exp_lambda_re187 = np.exp(-lambda_re187*time)
    exp_beta_rncp = np.exp(-beta_rncp*time)

    os_187_c = (lambda_re187/beta_rncp)*(1-exp_beta_rncp) - (1-exp_lambda_re187)
    re_187 = exp_beta_rncp - exp_lambda_re187
    
    return os_187_c/re_187

def cosmochronology_luck_sudden(time, a):
    beta_rncp = 1e-6 #1/yr (Luck et al. 1980)
    return cosmochronology_luck(time=time, a=a, b=beta_rncp)

def cosmochronology_luck_uniform(time, a):
    beta_rncp = 1e-12 #1/yr (Luck et al. 1980)
    return cosmochronology_luck(time=time, a=a, b=beta_rncp)

def cosmochronology_clayton_sudden(time, a):
    lambda_re187 = a
    exp_lambda_re187 = np.exp(lambda_re187*time)
    return exp_lambda_re187 - 1

def cosmochronology_clayton_uniform(time, a):
    lambda_re187 = a
    exp_lambda_re187 = np.exp(-lambda_re187*time)
    sub_term1 = (lambda_re187*time)/(1-exp_lambda_re187)
    return sub_term1 - 1

def cosmochronology_shizuma(time, a, b):
    lambda_eff_re187 = a
    lambda_rncp = b

    exp_lambda_eff_re187 = np.exp(-lambda_eff_re187*time)
    exp_lambda_rncp = np.exp(-lambda_rncp*time)

    re_187 = exp_lambda_eff_re187 - exp_lambda_rncp
    os_187 = (1-exp_lambda_eff_re187) - (1-exp_lambda_rncp)*(lambda_eff_re187/lambda_rncp)

    return os_187/re_187

def get_data(filename):
    pandas_data_frame = pd.read_csv(filename)
    time = pandas_data_frame["time"]
    mean = pandas_data_frame["mean"]
    uncertainty_up = pandas_data_frame["mean+sigma"] - mean
    uncertainty_down = pandas_data_frame["mean-sigma"] - mean
    return time, mean, uncertainty_up, uncertainty_down

def plot_timeevol(toa_time_mean_sigma_arrays, ax, color='b', bool_std=True, plot_string=""):
    time = toa_time_mean_sigma_arrays[0]
    mean = toa_time_mean_sigma_arrays[1]
    pos_sigma = toa_time_mean_sigma_arrays[2]
    neg_sigma = toa_time_mean_sigma_arrays[3]
    
    #scale time to Gyr
    time /= 1.0e+9

    frac_string = "f_{187}"
    ax.set_xlabel("time [Gyr]")
    ax.grid(True)
    ax.set_ylabel(r"$%s=^{187}Os/^{187}Re$"%(frac_string))
    ax.set_title(r"Isotope fraction in Galactic time")
    ax.axvline(9.5, color='k')
    
    #plot mean, sigmas, extremas and shaded region
    ax.plot(time, mean, color, 
            label=r"$\langle %s \rangle$ %s"%(frac_string, plot_string))
    if bool_std:
        ax.fill_between(time, pos_sigma, neg_sigma, color=color[0], alpha=0.3) #Use first char of fmt-string as color
                        #label=r"$\langle %s \rangle \pm \sigma$ %s"%(frac_string, plot_string))
    ax.legend(loc="upper left")

    return

def add_meteor_data(ax, fsos=True, now=False):
    #fraction of os-187/Re-187 at the time of formation of the solar system (with absolute uncertainty)
    f_187_fsos = [0.136, 0.0323]
    #same for current time
    f_187_now = [0.226, 57.9e-3]
    if fsos:
        ax.axhspan(f_187_fsos[0]+f_187_fsos[1], f_187_fsos[0]-f_187_fsos[1],
                   alpha=0.5, label="$f_{187}(t_{f,sos})$", color="g")
    if now:
        ax.axhspan(f_187_now[0]+f_187_now[1], f_187_now[0]-f_187_now[1],
                   alpha=0.5, label="$f_{187}(t_{now})$", color="g")
    return

if __name__ == '__main__':
    #find app. directory
    from directory_master import Foldermap
    directory = Foldermap().results + "MCExperiment_revised_2_delmax/"
    #find app. data
    loa_filenames = os.listdir(directory)
    for filename in loa_filenames:
        if ("reduce" in filename) and ("div" in filename) \
        and ("timeevol" in filename) and ("decay" in filename):
            app_filename = filename
    time, mean, uncertainty_up, uncertainty_down = get_data(directory+app_filename)
    
    #plot data
    fig = pl.figure()
    ax = fig.gca()
    bool_std = True
    add_meteor_data(ax=ax)
    plot_timeevol((time, mean, mean+uncertainty_up, mean-uncertainty_down), ax, color='k-', bool_std=bool_std, plot_string="data")
    
    #Clayton Sudden Synthesis
    T_half = 47e+9
    eps_T_half = 10.0/47.0
    decay_rate_re187 = np.log(2)/(T_half) #1/yr (Clayton 1964)
    p_array = np.array([decay_rate_re187])
    p_error = np.array([eps_T_half])*p_array
    clayton_model = cosmochronology_clayton_sudden(time, *p_array)
    clayton_model_pluss = cosmochronology_clayton_sudden(time, *(p_array+p_error))
    clayton_model_minus = cosmochronology_clayton_sudden(time, *(p_array-p_error))
    plot_timeevol((time, clayton_model, clayton_model_pluss, clayton_model_minus),
                  ax, color='b-', bool_std=bool_std, plot_string="Clayton sudden")
    print "Clayton sudden synthesis parameters to model: (lambda_eff) = %s +/- %s"%(p_array, p_error)
    
    #Clayton Uniform Synthesis
    clayton_model = cosmochronology_clayton_uniform(time, *p_array)#decay_rate_eff, rncp_frequency)
    clayton_model_pluss = cosmochronology_clayton_uniform(time, *(p_array+p_error))
    clayton_model_minus = cosmochronology_clayton_uniform(time, *(p_array-p_error))
    plot_timeevol((time, clayton_model, clayton_model_pluss, clayton_model_minus),
                  ax, color='b--', bool_std=bool_std, plot_string="Clayton uniform")
    print "Clayton uniform synthesis parameters to model: (lambda_re187) = %s +/- %s"%(p_array, p_error)
    
    #Luck sudden synthesis
    decay_rate_re187 = 1.62e-11 #1/yr (Luck et al. 1980)
    p_array = np.array([decay_rate_re187])
    p_error = np.array([0.03e-11]) #(Luck et al. 1980)
    luck_model = cosmochronology_luck_sudden(time, *p_array)
    luck_model_pluss = cosmochronology_luck_sudden(time, *(p_array+p_error))
    luck_model_minus = cosmochronology_luck_sudden(time, *(p_array-p_error))
    plot_timeevol((time, luck_model, luck_model_pluss, luck_model_minus),
                  ax, color='m-', bool_std=bool_std, plot_string="Luck sudden")
    print "Luck Sudden Synthesis parameters to model: (lambda_re187) = %s +/- %s"%(p_array, p_error)

    #Luck uniform synthesis
    luck_model = cosmochronology_luck_uniform(time, *p_array)
    luck_model_pluss = cosmochronology_luck_uniform(time, *(p_array+p_error))
    luck_model_minus = cosmochronology_luck_uniform(time, *(p_array-p_error))
    plot_timeevol((time, luck_model, luck_model_pluss, luck_model_minus),
                  ax, color='m--', bool_std=bool_std, plot_string="Luck uniform")
    print "Luck Uniform Synthesis parameters to model: (lambda_re187) = %s +/- %s"%(p_array, p_error)
    
    ### Shizuma ###
    #Shizuma
    rncp_frequency = 1e-9 #1/yr (Shizuma et al. 2005)
    eps_rncp_frequency = 1 #1/yr (Shizuma et al. 2005)
    halflife = 41.6e+9 # yr (shizuma et al. 2005)
    eps_halflife = 1.3/41.2 #(galeazzi 2001)
    decay_rate_re_187 = np.log(2)/halflife #1/yr (Shizuma et al. 2005)
    decay_rate_eff = 1.2*decay_rate_re_187 #(Shizuma et al. 2005)
    p_array = np.array([decay_rate_eff, rncp_frequency])
    p_error = np.array([eps_halflife, eps_rncp_frequency])*p_array 
    shizuma_model = cosmochronology_shizuma(time, *p_array)
    shizuma_model_pluss = cosmochronology_shizuma(time, *(p_array+p_error))
    shizuma_model_minus = cosmochronology_shizuma(time, *(p_array-p_error))
    plot_timeevol((time, shizuma_model, shizuma_model_pluss, shizuma_model_minus),
                  ax, color='r-', bool_std=bool_std, plot_string="Shizuma")
    print "Shizuma parameters to model: (lambda_eff, lambda_rncp) = %s +/- %s"%(p_array, p_error)
    
    ### MODEL FITTING ###
    print "fitting model"
    #find app. starting point in parameter-space FROM SHIZUMA
    #caluclate model with scipy
    resolution = 1e-2
    bool_mask1 = mean>=resolution
    resolution = 1e-4
    bool_mask2 = np.abs(uncertainty_up) > resolution
    bool_mask3 = np.abs(uncertainty_up) > resolution
    bool_mask = bool_mask1&bool_mask2&bool_mask3
    popt_upper, pcov_upper = curve_fit(f=cosmochronology_shizuma, xdata=time[bool_mask],
                                       ydata=mean[bool_mask],
                                       p0=p_array, 
                                       #bounds=(p_array*1e-1, p_array*1e+1),
                                       sigma=uncertainty_up[bool_mask],
                                       absolute_sigma=True)
    perr_upper = np.sqrt(np.diag(pcov_upper))
    popt_lower, pcov_lower = curve_fit(f=cosmochronology_shizuma, xdata=time[bool_mask],
                                       ydata=mean[bool_mask],
                                       p0=p_array, 
                                       #bounds=(p_array*1e-1, p_array*1e+1),
                                       #sigma=mean[start_index:]-uncertainty_down[start_index:],
                                       sigma=uncertainty_down[bool_mask],
                                       absolute_sigma=True)
    perr_lower = np.sqrt(np.diag(pcov_lower))
            
    popt = 0.5*(popt_upper + popt_lower)
    print "SciPy-fitting to data: (lambda_eff, lambda_rncp) = %s +/- %s/%s"%(popt, perr_upper, perr_lower)

    #plot model
    scipy_fitted_model = cosmochronology_shizuma(time, *popt)
    scipy_fitted_model_pluss = cosmochronology_shizuma(time, *(popt+perr_upper))
    scipy_fitted_model_minus = cosmochronology_shizuma(time, *(popt-perr_lower))
    
    plot_timeevol((time, scipy_fitted_model, scipy_fitted_model_pluss, scipy_fitted_model_minus),
                  ax, color='r--', bool_std=bool_std, plot_string="SciPy-fit")

    fig.savefig(directory+"model_fitting.png")

    #plot clayton only
    fig = pl.figure()
    ax = fig.gca()
    bool_std = True
    add_meteor_data(ax=ax)
    
    #Clayton Sudden Synthesis
    T_half = 47e+9
    eps_T_half = 10.0/47.0
    decay_rate_re187 = np.log(2)/(T_half) #1/yr (Clayton 1964)
    p_array = np.array([decay_rate_re187])
    p_error = np.array([eps_T_half])*p_array
    clayton_model = cosmochronology_clayton_sudden(time, *p_array)
    clayton_model_pluss = cosmochronology_clayton_sudden(time, *(p_array+p_error))
    clayton_model_minus = cosmochronology_clayton_sudden(time, *(p_array-p_error))
    plot_timeevol((time, clayton_model, clayton_model_pluss, clayton_model_minus),
                  ax, color='b-', bool_std=bool_std, plot_string="Clayton sudden")
    print "Clayton sudden synthesis parameters to model: (lambda_eff) = %s +/- %s"%(p_array, p_error)
    
    #Clayton Uniform Synthesis
    clayton_model = cosmochronology_clayton_uniform(time, *p_array)#decay_rate_eff, rncp_frequency)
    clayton_model_pluss = cosmochronology_clayton_uniform(time, *(p_array+p_error))
    clayton_model_minus = cosmochronology_clayton_uniform(time, *(p_array-p_error))
    plot_timeevol((time, clayton_model, clayton_model_pluss, clayton_model_minus),
                  ax, color='b--', bool_std=bool_std, plot_string="Clayton uniform")
    print "Clayton uniform synthesis parameters to model: (lambda_re187) = %s +/- %s"%(p_array, p_error)

    fig.savefig(directory+"model_fitting2.png")
    pl.show()
