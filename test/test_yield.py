"""
Description: Test various ways of making an 'Experiment'-class that will fuck with the yields of a specific isotope.
TODO:
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
import sys
import numpy as np

###############################################
### Get boolean test-switches from cmd-line ###
###############################################

print "Using boolean cmd-line args: *all* *test1* *test2* etc."
try:
    test_all = bool(int(sys.argv[1]))
except:
    test_all = True
try:
    test_array_bool = [bool(int(arg)) for arg in sys.argv[2:]]
except:
    test_array_bool = []
    
num_tests = 2
while len(test_array_bool) < num_tests:
    test_array_bool.append(False)
num_steps = 150

###########################################
### Tests various ways of inserting SFR ###
###########################################

#relative path to sfh-file from 'NuPyCEE'-directory
sfh_file_dir = "../reproduce_shen/"
sfh_file_relpath1 = sfh_file_dir+"time_sfr_Shen_2015.txt"
sfh_file_relpath2 = sfh_file_dir+"timegal5e8_sfr_Shen_2015.txt"

if test_all or test_array_bool[0]: #for simple testing of omega
    yield_omega = om.omega(special_timesteps=5)

class experiment(om.omega):
    def __init__(self):
        self.constant_isotope = 1.0
        self.name_isotope = "Re-187"

    ##############################################
    #              Add yields Mdot               #
    """ 
    This function is copied from class 'chem_evol'.
    Manipulating it will override the loaded function
    in the 'Omega' class(which inherits this function
    from the 'chem_evol' class.
    THE ONLY MODIFICATION IS A CONSTANT ADDED TO THE YIELDS
    AT A SPECIFIC ISOTOPE!!!
    """
    ##############################################
    def __add_yields_mdot(self, minm1, maxm1, yields, yields_extra, i, j, w,\
            number_stars, mstars, tt, lifetimemax, p_number, func_total_ejecta,\
            mass_sampled, scale_cor):

        '''
        This function adds the yields of the stars formed during timestep i
        in a future upcoming timestep j.  The stars here are only a fraction
        of the whole stellar population that just formed.

        Arguments
        =========

          minm1 : Minimum stellar mass having ejecta in this timestep j.
          maxm1 : Minimum stellar mass having ejecta in this timestep j.
          yields : Stellar yields for the considered mass bin.
          yields_extra : Stellar yields from extra source.
          i : Index of the current timestep.
          j : Index of the future timestep where ejecta is added.
          w : Index of the stellar model providing the yields.
          number_stars : Number of stars having ejecta in timestep j.
          mstars : Initial mass of stellar models available in the input yields.
          tt : Time between timestep j and timestep i.
          lifetimemax : Maximum lifetime .
          p_number : IMF (number) coefficient in the mass interval.
          mass_sampled : Stars sampled in the IMF by an external program
          scale_cor : Envelope correction for the IMF

        '''
        index_isotope = self.history.isotopes.\
                        index(self.string_isotope)
        yields[index_isotope] = self.constant_isotope*\
                                yields[index_isotope]
        
        # Scale the total yields (see func_total_eject)
	if (self.total_ejecta_interp == True):
		m_tot_ejecta=(func_total_ejecta(minm1)+func_total_ejecta(maxm1)) / 2.0
        	scalefactor = m_tot_ejecta / sum(yields)
		
	else:
		scalefactor = 1

        # Output information
        if self.iolevel > 1:
            print 'Scalefactor:', scalefactor

        # Calculate the scaling factor if mass_sampled is provided
        if len(mass_sampled) > 0:
            number_stars, yield_factor = self.__get_yield_factor(minm1, \
                maxm1, mass_sampled, func_total_ejecta, mstars[w])

        # If the IMF is full ...
        else:

            # If the is a correction to apply to the scale factor ...
            if len(scale_cor) > 0:
                scalefactor_factor = self.__get_scale_cor(minm1,\
                    maxm1, scale_cor)
                scalefactor = scalefactor * scalefactor_factor

            # Calculate the factor that multiplies the yields
            yield_factor = scalefactor * number_stars

        # For every isotope ...
        for k in range(len(self.ymgal[i])):

            # Add the total ejecta
            if k >= 76 and mstars[w] > self.transitionmass:
                self.mdot[j][k] = self.mdot[j][k] + \
                    self.f_arfo * yields[k] * scalefactor * number_stars
            else:
                self.mdot[j][k] = self.mdot[j][k] + \
                    yields[k] * scalefactor * number_stars

            # For massive stars ...
            if mstars[w] > self.transitionmass:

		#if self.history.isotopes[k]=='N-14':
			#print 'N14: ',mstars[w],yields[k],scalefactor,number_stars			
                # In the case of an extra source in massive stars ...
                #if self.extra_source_on:
                #    self.mdot_massive[j][k] = self.mdot_massive[j][k] + \
                #        yields_extra[k] * self.f_extra_source * yield_factor
                #    self.mdot[j][k] = self.mdot[j][k] + \
                #        yields_extra[k] * self.f_extra_source * yield_factor
                    


                # Add the contribution of massive stars
                if k >= 76:
                    self.mdot_massive[j][k] = self.mdot_massive[j][k] + \
                        self.f_arfo * yields[k] * yield_factor
                else:
                    self.mdot_massive[j][k] = self.mdot_massive[j][k] + \
                        yields[k] * yield_factor

            # Add contribution of AGB stars
            else:
                self.mdot_agb[j][k] = self.mdot_agb[j][k] + \
                    yields[k] * yield_factor

            #here extra source contributions are added
            if self.extra_source_on:

		       #print self.Z_gridpoint,self.extra_source_exclude_Z   		    
		    for ee in range(len(yields_extra)):
		       if not self.Z_gridpoint in self.extra_source_exclude_Z[ee]:
			if ((minm1 >= self.extra_source_mass_range[ee][0]) and (maxm1 <= self.extra_source_mass_range[ee][1])):	
			
		          self.mdot[j][k] = self.mdot[j][k] + \
                          yields_extra[ee][k] * self.f_extra_source[ee] * yield_factor

		          if mstars[w] > self.transitionmass:
                            self.mdot_massive[j][k] = self.mdot_massive[j][k] + \
                            yields_extra[ee][k] * self.f_extra_source[ee] * yield_factor
                          else:
                            self.mdot_agb[j][k] = self.mdot_agb[j][k] + \
		            yields_extra[ee][k] * self.f_extra_source[ee] * yield_factor
		       #else:
		          #if k==0:
		          #   print self.zmetal,'Z_gridpoint',self.Z_gridpoint,self.extra_source_mass_range[ee]

        #print 'general : ',self.zmetal,'Z_gridpoint',self.Z_gridpoint
        # Count the number of core-collapse SNe
        if mstars[w] > self.transitionmass:
            self.sn2_numbers[j] += number_stars
            if self.out_follows_E_rate:
                self.ssp_nb_cc_sne[j-i-1] += number_stars
#                self.ssp_nb_cc_sne[j-i+1] += number_stars
        if ((minm1 >= 3) and (maxm1 <= 8)) or ((minm1 < 3) and (maxm1 > 8)):
            self.wd_sn1a_range1[j] += number_stars
        elif minm1 < 3 and maxm1 > 3:
            self.wd_sn1a_range1[j] += p_number * (self._imf(3, maxm1, 1))
        elif minm1 < 8 and maxm1 > 8:	
            self.wd_sn1a_range1[j] += p_number * (self._imf(minm1, 8, 1,))

        # Sum the total number of stars born in the current timestep i (not j)
        self.number_stars_born[i] += number_stars

	#Add other stellar input, only for Z>0 because of different input grid.
	if self.Z_gridpoint>0. and self.stellar_param_on:
		q=0
		qq=0
		mass_scale_f=0.
		for p in range(len(self.stellar_param_attrs)):
			attr=self.stellar_param_attrs[p]
			#Handle SNIa energy in __sn1a_contribution
			if attr == 'SNIa energy':
				continue
			idx=list(self.stellar_param_evol_masses).index(mstars[w])
			#to process yield table parameter (1 val for 1 star)
			if attr in self.stellar_param_attrs_y:
				# rate of quantity
				self.stellar_param[p][j] = self.stellar_param[p][j] + self.stellar_param_y[idx][qq]*number_stars/(self.history.timesteps[j]*self.const.syr) 
				qq=qq+1
			else:
				#Apply quantities for stars in time interval i/j, apply their contribution over their whole lifetime (table)
				#I need m_tot_ejecta , current time tt at index j, lifetime of star stellar_param_evol_lifetimes[idx]
				'''
				#if 'Ekindot_wind' in self.stellar_param_attrs and 'Mdot_wind' in self.stellar_param_attrs:
				if True:
					if 'Mdot_wind' == attr:	 
						#scale to total ejecta: total ejecta summed from each time bin / total ejecta from fit
						mass_scale_f=sum(np.array(self.stellar_param_evol[idx][j-1][q]) * np.array(self.history.timesteps)) / m_tot_ejecta
						self.stellar_param[p][:]= self.stellar_param[p][:] + number_stars* mass_scale_f * np.array(self.stellar_param_evol[idx][j-1][q])
					#if 'Ekindot_wind' == attr:
					#	self.stellar_param[p][:]= self.stellar_param[p][:] + number_stars* mass_scale_f * np.array(self.stellar_param_evol[idx][j-1][q])
						
				else:
				'''
				self.stellar_param[p][:]= self.stellar_param[p][:] + number_stars * np.array(self.stellar_param_evol[idx][j-1][q])
				q=q+1

        # Exit loop if no more ejecta to be distributed 
        if tt >= lifetimemax:
            break_bol = True
        else:
            break_bol = False

        # Return whether the parent function needs to break or not
        return break_bol
    #############################
    ### END __add_yields_mdot ###
    #############################
