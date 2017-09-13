"""
Use this file to probe different parameters of 'Omega' 
in order to fit with 'Eris'
"""

################################################
### Import modules and set global parameters ###
################################################
#Get module for handling folders correctly
import directory_master as dir_m
folder = dir_m.Foldermap() #instance with all the correct folders
#Set environment option for the 'Omega' simulation
import os, sys
os.environ['SYGMADIR'] = folder.nupycee[:-1]
#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs
#import numpy as np
#import matplotlib.pyplot as pl

###############################
### Set cmd-line parameters ###
###############################
num_cmdline = len(sys.argv)
self_name = sys.argv[0]
n = 20 #number of timesteps
if num_cmdline >= 2:
    n = int(sys.argv[1])


###############################
### Insert data from 'Eris' ###
###############################
#relative path to sfh-file from 'NuPyCEE'-directory
sfh_file_dir = "../reproduce_shen/"
sfh_file_relpath = sfh_file_dir+"time_sfr_Shen_2015.txt"
#sfh_file_relpath = sfh_file_dir+"timegal5e8_sfr_Shen_2015.txt"
imf_type = "kroupa93" #IMF from 'Eris'
#supernova rate
#kilonova rate

################################
### Final mass must match MW ###
################################
#https://academic.oup.com/mnras/article-lookup/doi/10.1093/mnras/stw2759
MW_mass = (48.6e+9, 60.0e+9) #[M_sol]
#'Omega' parameters and articles within
mgal = 1.6e11 #initial mass of gas
m_tot = 200e+9 #total mass of MW at present
m_DM_0 = 1.0e12 #final dark matter mass
stellar_mass_0 = 6.0e10 #https://arxiv.org/abs/1407.1078
f_merger = 0.008

##################################
### Outflow must match sn-rate ###
##################################
mass_loading = 0.8 #ratio between outflow and sfr

###################################
### Inflow must match Matteucci ###
###################################
inflow_matteucci = (0.3,1.5) #[M_sol/(Gyr pc^2)]
inflow = 10.0 #[M_sol/yr]

################################
### compile sets of 'Omega's ###
""" Vary parameters and find the best fit """
################################
if False: #test current parameters to make sure plotting works
    inst = om.omega(special_timesteps=n,
                    #dt=1.0e+3,
                    imf_type=imf_type,
                    sfh_file=sfh_file_relpath,
                    mgal=mgal,
                    m_DM_0=m_DM_0, stellar_mass_0=stellar_mass_0,
                    sn1a_on=False,
                    in_out_control=True,
                    inflow_rate=10.0, mass_loading=mass_loading,
                    ns_merger_on=True, f_merger=f_merger)
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(inst, "simple_test",
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic plotting test in bestfitfile", save="test_spectro")
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(inst, "simple_test",
                                 num_yaxes=5) 
    Harry_Plotter.add_time_rate('sn', index_yaxis=0,
                                rate_type='one')
    Harry_Plotter.add_time_rate('sn', index_yaxis=1,
                                rate_type='two')
    Harry_Plotter.add_time_rate('kn', index_yaxis=2,
                                rate_type='one')
    Harry_Plotter.add_time_rate('kn', index_yaxis=3,
                                rate_type='two')
    Harry_Plotter.add_time_rate('sf', index_yaxis=4)
    Harry_Plotter.finalize(show=True, title="rate plotting test in bestfitfile", save="test_rate")

if False: #test sfr input and vary stellar mass at present
    loa_fac = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]#, 10.0]
    loa_sm0 = [fac*stellar_mass_0 for fac in loa_fac]
    loa_omega_names = [str(fac) for fac in loa_fac]
    loa_omegas = [om.omega(special_timesteps=n,
                           imf_type=imf_type,
                           sfh_file=sfh_file_relpath,
                           m_DM_0=m_DM_0,
                           stellar_mass_0=sm0,
                           sn1a_on=False)
                  for sm0 in loa_sm0]
    #use visualize to compare 'Omega' and 'Eris'
    #compare rates for supernova and star formation
    Harry_Plotter = vs.visualize(loa_omegas,
                                 loa_omega_names,
                                 num_yaxes=2)
    Harry_Plotter.add_time_rate('sn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=1,rate_type='one')
    Harry_Plotter.finalize(show=True,
                           save="testSM0_rates_n%d.png"%n,
                           title="Vary final stellar mass")
    """ Conclusion: 0.5 omega value is optimal """
if False:
    #vary inflow and outflow
    loa_inflow = [2.0, 5.0, 10.0]
    loa_massloading = [0.0, 0.0, 0.0]
    loa_omega_names = ["in:%1.1f out:%1.1f"%(inflow, ml) for inflow, ml
                       in zip(loa_inflow, loa_massloading)]
    loa_omegas_vary_nsm = [om.omega(special_timesteps=n,
                                    imf_type=imf_type,
                                    sfh_file=sfh_file_relpath,
                                    stellar_mass_0=-1.0,
                                    #DM_evolution=True,
                                    #m_DM_0=False,
                                    sn1a_on=False,
                                    in_out_control=True,
                                    inflow_rate=inflow,
                                    mass_loading=ml)
                           for inflow, ml
                           in zip(loa_inflow, loa_massloading)]
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(loa_omegas_vary_nsm,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic data while varying gasflow",
                           save="varyFLOW_spectro_n%d"%n)
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(loa_omegas_vary_nsm,
                                 loa_omega_names,
                                 num_yaxes=2) 
    Harry_Plotter.add_time_rate('sn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=1)
    Harry_Plotter.finalize(show=True, save="varyFLOW_rate_n%d"%n,
                           title="Rates while varying gas flow")
    """ 
    Conclusions:
    inflow_rate at 10 solar masses per year and a 
    outflow rate of 0.3*SFR are decent values
    """
    
if False:
    #vary kilonova-rates
    loa_fac = [0.001, 0.01,0.02, 0.03]#, 0.1]#, 1.0]
    loa_fmerger = [fac*f_merger for fac in loa_fac]
    loa_omega_names = ["f_merger %1.3e*Omega"%fac
                       for fac in loa_fac]
    loa_omegas_vary_nsm = [om.omega(special_timesteps=n,
                                    imf_type=imf_type,
                                    sfh_file=sfh_file_relpath,
                                    sn1a_on=False,
                                    in_out_control=True,
                                    inflow_rate=10.0,
                                    mass_loading=0.3,
                                    ns_merger_on=True,
                                    f_merger=f_merger)
                       for f_merger in loa_fmerger]
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(loa_omegas_vary_nsm,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic data while varying NSM", save="varyNSM_spectro_n%d"%n)
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(loa_omegas_vary_nsm,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_rate('kn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sn',index_yaxis=1,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=2)
    Harry_Plotter.finalize(show=True, save="varyNSM_rate_n%d"%n,
                           title="Rates while varying NSM")
    """
    Conclusion: 2% of default omega value is appropriate
    """

if False: #vary kilonova-ejecta
    loa_ejecta = [2.5e-2, 5.0e-2, 1.0e-1]
    loa_omega_names = ["NSM ejecta %1.2e M_sol"%ejecta
                       for ejecta in loa_ejecta]
    loa_omegas_vary_nsm = [om.omega(special_timesteps=n,
                                    imf_type=imf_type,
                                    sfh_file=sfh_file_relpath,
                                    sn1a_on=False,
                                    in_out_control=True,
                                    inflow_rate=5.0,
                                    mass_loading=0.03,
                                    ns_merger_on=True,
                                    f_merger=0.008*0.02,
                                    m_ej_nsm=ejecta)
                           for ejecta in loa_ejecta]
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(loa_omegas_vary_nsm,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic data while varying NSM ejecta", save="varyNSMejecta_spectro_n%d"%n)
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(loa_omegas_vary_nsm,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_rate('kn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sn',index_yaxis=1,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=2)
    Harry_Plotter.finalize(show=True, save="varyNSMejecta_rate_n%d"%n,
                           title="Rates while varying NSM ejecta")
    """
    Conclusions:
    Maximize m_ej_nsm, lower inflow and outflow
    """

if True: # Vary mgal
    loa_fac = [0.1,0.5,1.0,2.0,10.0]
    loa_omega_names = ["$m_{gal}$=%1.1f*Omega"%fac
                       for fac in loa_fac]
    loa_omegas_vary_mgal = [om.omega(special_timesteps=n,
                                    imf_type=imf_type,
                                    sfh_file=sfh_file_relpath,
                                    sn1a_on=False,
                                    mgal=mgal*fac,
                                    m_gas_f=m_tot,
                                    stellar_mass_0=stellar_mass_0)
                                    #in_out_control=True,
                                    #inflow_rate=5.0,
                                    #mass_loading=0.03,
                                    #ns_merger_on=True,
                                    #f_merger=0.008*0.02,
                                    #m_ej_nsm=ejecta)
                                    for fac in loa_fac]
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(loa_omegas_vary_mgal,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic data while varying M_gal w/present SM and totM", save="varyMGAL_spectro_n%d"%n)
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(loa_omegas_vary_mgal,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_rate('kn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sn',index_yaxis=1,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=2)
    Harry_Plotter.finalize(#show=True,
                           title="Rates while varying M_gal w/present Sm and totM", save="varyMGAL_rate_n%d"%n)
    """
    Conclusions:
    Less initial gas increases spectroscopic values in beginning
    factor of 0.5 is preferred, but the sfr is scaled up to adjust.
    """
    
if True: # m_total
    loa_fac = [0.1,0.5,1.0,2.0,10.0]
    loa_omega_names = ["$m_{tot}$=%1.1f*Omega"%fac
                       for fac in loa_fac]
    loa_omegas = [om.omega(special_timesteps=n,
                                    imf_type=imf_type,
                                    sfh_file=sfh_file_relpath,
                                    sn1a_on=False,
                                    mgal=mgal,
                                    m_gas_f=m_tot*fac,
                                    stellar_mass_0=stellar_mass_0)
                                    #in_out_control=True,
                                    #inflow_rate=5.0,
                                    #mass_loading=0.03,
                                    #ns_merger_on=True,
                                    #f_merger=0.008*0.02,
                                    #m_ej_nsm=ejecta)
                                    for fac in loa_fac]
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(loa_omegas,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic data while varying tot M present", save="varyMTOT_spectro_n%d"%n)
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(loa_omegas_vary_mgal,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_rate('kn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sn',index_yaxis=1,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=2)
    Harry_Plotter.finalize(#show=True,
                           title="Rates while varying tot M present", save="varyMTOT_rate_n%d"%n)
    """
    Conclusions:
    """

if True: # Vary stellar mass 0
    loa_fac = [0.1,0.5,1.0,2.0,10.0]
    loa_omega_names = ["$m_{*}$=%1.1f*Omega"%fac
                       for fac in loa_fac]
    loa_omegas = [om.omega(special_timesteps=n,
                                    imf_type=imf_type,
                                    sfh_file=sfh_file_relpath,
                                    sn1a_on=False,
                                    #mgal=mgal*fac)
                                    m_gas_f=m_tot,
                                    stellar_mass_0=stellar_mass_0*fac)
                                    #in_out_control=True,
                                    #inflow_rate=5.0,
                                    #mass_loading=0.03,
                                    #ns_merger_on=True,
                                    #f_merger=0.008*0.02,
                                    #m_ej_nsm=ejecta)
                                    for fac in loa_fac]
    #use visualize to compare 'Omega' and 'Eris'
    #compare spectroscopic data
    Harry_Plotter = vs.visualize(loa_omegas,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_relabu('[O/H]', index_yaxis=0)
    Harry_Plotter.add_time_relabu('[Fe/H]', index_yaxis=1)
    Harry_Plotter.add_time_relabu('[Eu/H]', index_yaxis=2)
    Harry_Plotter.zoom([[-4,1],[-4,1],[-4,1]])
    Harry_Plotter.finalize(title="Spectroscopic data while varying SM present", save="varyMSTELLAR_spectro_n%d"%n)
    #compare SN/KN-rates
    Harry_Plotter = vs.visualize(loa_omegas,
                                 loa_omega_names,
                                 num_yaxes=3) 
    Harry_Plotter.add_time_rate('kn',index_yaxis=0,rate_type='one')
    Harry_Plotter.add_time_rate('sn',index_yaxis=1,rate_type='one')
    Harry_Plotter.add_time_rate('sf',index_yaxis=2)
    Harry_Plotter.finalize(show=True,
                           title="Rates while varying SM present", save="varyMSTELLAR_rate_n%d"%n)
    """
    Conclusions:
    """
