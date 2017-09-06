"""
This script is for plotting various isotopes of Eu, Re, and Os.
"""
################################################
### Import modules and set global parameters ###
################################################
#Get module for handling folders correctly
import sys
import directory_master as dir_m
folder = dir_m.Foldermap() #instance with all the correct folders
#Set environment option for the 'Omega' simulation
import os
os.environ['SYGMADIR'] = folder.nupycee[:-1]
#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs

def test_simple(n):
    """
    Just plot a simple standard MW-galaxy to make sure the 
    plotting syntax is up-to-date
    """
    inst = om.omega(galaxy="milky_way", special_timesteps=n,
                           ns_merger_on=True, bhns_merger_on=True)
    plotter = vs.visualize(inst, "test_omega",
                           num_yaxes=3, age=0)

    Eu_isos = ["Eu-151", "Eu-153"]
    Re_isos = ["Re-187", "Re-185"]
    Os_isos = ["Os-184", "Os-186", "Os-187",
               "Os-188", "Os-189", "Os-190", "Os-192"]

    for i, iso_list in enumerate([Eu_isos, Re_isos, Os_isos]):
        for iso in iso_list:
            plotter.add_time_relabu_singleomega(iso, index_yaxis=i, ylabel="log abundance")
            
    plotter.finalize(save="test_rncp_isos_n%d.png"%n,
                     show=True,
                     title="R-process isotopes of 'Omega'")
    return None

def re_eu_ratios(n):
    """
    Plot various isotope and element ratios of Re and Eu.
    Make three subplots:
    - Re/Eu
    - Re-isos/Eu-151
    - Re-isos/Eu-153
    """
    Eu_isos = ["Eu-151", "Eu-153"]
    Re_isos = ["Re-187", "Re-185"]
    fractions = ["Re/Eu"] \
                + [re+'/'+Eu_isos[0] for re in Re_isos] \
                + [re+'/'+Eu_isos[1] for re in Re_isos]
    spectro_notation = ['['+frac+']' for frac in fractions]
    
    #make instance of 'Omega'
    inst = om.omega(galaxy="milky_way", special_timesteps=n,
                           ns_merger_on=True, bhns_merger_on=True)
    plotter = vs.visualize(inst, "test_omega",
                           num_yaxes=3, age=0,
                           loa_spectro_abu=spectro_notation)
    
    for frac, index in zip(fractions, [0,1,1,2,2]):
        plotter.add_time_relabu_singleomega(frac,
                                            index_yaxis=index)
    limit = [-3,0]
    plotter.zoom([False, limit, limit])
    plotter.finalize(save="test_rnscp_fraction_n%d"%n,
                     title="Re/Eu - fractions",
                     show=True)
    return None
    
if __name__ == '__main__':
    try:
        resolution = float(sys.argv[1])
    except:
        resolution = 2
        
    #test_simple(n=resolution)
    re_eu_ratios(n=resolution)
