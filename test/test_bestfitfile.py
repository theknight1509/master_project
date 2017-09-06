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
import os
os.environ['SYGMADIR'] = folder.nupycee[:-1]
#import 'Omega', visualize, and other relevant packages
import NuPyCEE.omega as om
import visualize as vs
#import numpy as np
#import matplotlib.pyplot as pl

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
m_DM_0 = 1.0e12 #final dark matter mass
stellar_mass_0 = 5.0e10

##################################
### Outflow must match sn-rate ###
##################################
mass_loading = 1.0 #ratio between outflow and sfr

###################################
### Inflow must match Matteucci ###
###################################
inflow_matteucci = (0.3,1.5) #[M_sol/(Gyr pc^2)]

################################
### compile sets of 'Omega's ###
""" Vary parameters and find the best fit """
################################
#test current parameters
inst = om.omega(dt=1.0e+5,
                imf_type=imf_type,
                sfh_file=sfh_file_relpath,
                m_DM_0=m_DM_0, stellar_mass_0=stellar_mass_0,
                mgal=mgal,
                in_out_control=True, inflow_rate=10.0,
                mass_loading=mass_loading)

#vary supernovae-rates
omegas_vary_snr = []

#vary kilonova-rates
omegas_vary_nsm = []

