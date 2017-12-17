"""
Description:
-Make a class that inherits everything from omega or sygma
-change the functions that uses sygma to get yields
-add a funky factor to the yields of a single isotope
"""
######################################
### Various imports and structures ###
######################################
#get folder-handling-script
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ() #set environment for omega before importing
#NuPyCEE one-zone chemical evolution code
from omega import *
#use pandas for data-storage
import pandas as pd
<<<<<<< HEAD


#import the current bestfit parameters if not already done
#global parameter is not defined...
print "experiment"
print ('bestfit_imported' in globals().keys())
if not ('bestfit_imported' in globals().keys()):
    bestfit_imported = False #define global parameter
    #no bestfit-file has been imported yet...
if not bestfit_imported:
    from bestfit_param_omega.bestfit_file import *
    bestfit_imported = True
    print "Reimporting!"

#import namespace of the default bestfit-parameters
import bestfit_param_omega.bestfit_file as default_bestfit_namespace

#####################################################
### Class inheriting omega for experimental usage ###
#####################################################
class experiment(omega):
    def __init__(self, input_isotope='Re-187', input_factor=1.0,
                 input_timesteps=30, dt=0,
                 bestfit_namespace=default_bestfit_namespace):
        self.experiment_isotope = input_isotope
        self.experiment_factor = input_factor
        
        ### initialize omega ###
        bestfit_namespace.bestfit_special_timesteps = input_timesteps
        if dt > 0: #deactive special timestepping
            bestfit_namespace.bestfit_special_timesteps = 0
            bestfit_namespace.bestfit_dt = dt
        bestfit_namespace.bestfit_external_control = False
        omega.__init__(self, galaxy=bestfit_namespace.bestfit_galaxy, in_out_control=bestfit_namespace.bestfit_in_out_control, SF_law=bestfit_namespace.bestfit_SF_law, DM_evolution=bestfit_namespace.bestfit_DM_evolution, Z_trans=bestfit_namespace.bestfit_Z_trans, f_dyn=bestfit_namespace.bestfit_f_dyn, sfe=bestfit_namespace.bestfit_sfe, outflow_rate=bestfit_namespace.bestfit_outflow_rate, inflow_rate=bestfit_namespace.bestfit_inflow_rate, rand_sfh=bestfit_namespace.bestfit_rand_sfh, cte_sfr=bestfit_namespace.bestfit_cte_sfr, m_DM_0=bestfit_namespace.bestfit_m_DM_0, mass_loading=bestfit_namespace.bestfit_mass_loading, t_star=bestfit_namespace.bestfit_t_star, sfh_file=bestfit_namespace.bestfit_sfh_file, in_out_ratio=bestfit_namespace.bestfit_in_out_ratio, stellar_mass_0=bestfit_namespace.bestfit_stellar_mass_0, z_dependent=bestfit_namespace.bestfit_z_dependent, exp_ml=bestfit_namespace.bestfit_exp_ml, nsmerger_bdys=bestfit_namespace.bestfit_nsmerger_bdys, imf_type=bestfit_namespace.bestfit_imf_type, alphaimf=bestfit_namespace.bestfit_alphaimf, imf_bdys=bestfit_namespace.bestfit_imf_bdys, sn1a_rate=bestfit_namespace.bestfit_sn1a_rate, iniZ=bestfit_namespace.bestfit_iniZ, dt=bestfit_namespace.bestfit_dt, special_timesteps=bestfit_namespace.bestfit_special_timesteps, tend=bestfit_namespace.bestfit_tend, mgal=bestfit_namespace.bestfit_mgal, transitionmass=bestfit_namespace.bestfit_transitionmass, iolevel=bestfit_namespace.bestfit_iolevel, ini_alpha=bestfit_namespace.bestfit_ini_alpha, nb_nsm_per_m=bestfit_namespace.bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_namespace.bestfit_t_nsm_coal, table=bestfit_namespace.bestfit_table, hardsetZ=bestfit_namespace.bestfit_hardsetZ, sn1a_on=bestfit_namespace.bestfit_sn1a_on, nsm_dtd_power=bestfit_namespace.bestfit_nsm_dtd_power, sn1a_table=bestfit_namespace.bestfit_sn1a_table, ns_merger_on=bestfit_namespace.bestfit_ns_merger_on, f_binary=bestfit_namespace.bestfit_f_binary, f_merger=bestfit_namespace.bestfit_f_merger, t_merger_max=bestfit_namespace.bestfit_t_merger_max, m_ej_nsm=bestfit_namespace.bestfit_m_ej_nsm, nsmerger_table=bestfit_namespace.bestfit_nsmerger_table, bhns_merger_on=bestfit_namespace.bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_namespace.bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_namespace.bestfit_bhnsmerger_table, iniabu_table=bestfit_namespace.bestfit_iniabu_table, extra_source_on=bestfit_namespace.bestfit_extra_source_on, extra_source_table=bestfit_namespace.bestfit_extra_source_table, f_extra_source=bestfit_namespace.bestfit_f_extra_source, pre_calculate_SSPs=bestfit_namespace.bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_namespace.bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_namespace.bestfit_extra_source_exclude_Z, pop3_table=bestfit_namespace.bestfit_pop3_table, imf_bdys_pop3=bestfit_namespace.bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_namespace.bestfit_imf_yields_range_pop3, starbursts=bestfit_namespace.bestfit_starbursts, beta_pow=bestfit_namespace.bestfit_beta_pow, gauss_dtd=bestfit_namespace.bestfit_gauss_dtd, exp_dtd=bestfit_namespace.bestfit_exp_dtd, nb_1a_per_m=bestfit_namespace.bestfit_nb_1a_per_m, f_arfo=bestfit_namespace.bestfit_f_arfo, t_merge=bestfit_namespace.bestfit_t_merge, imf_yields_range=bestfit_namespace.bestfit_imf_yields_range, exclude_masses=bestfit_namespace.bestfit_exclude_masses, netyields_on=bestfit_namespace.bestfit_netyields_on, wiersmamod=bestfit_namespace.bestfit_wiersmamod, skip_zero=bestfit_namespace.bestfit_skip_zero, redshift_f=bestfit_namespace.bestfit_redshift_f, print_off=bestfit_namespace.bestfit_print_off, long_range_ref=bestfit_namespace.bestfit_long_range_ref, f_s_enhance=bestfit_namespace.bestfit_f_s_enhance, m_gas_f=bestfit_namespace.bestfit_m_gas_f, cl_SF_law=bestfit_namespace.bestfit_cl_SF_law, external_control=bestfit_namespace.bestfit_external_control, calc_SSP_ej=bestfit_namespace.bestfit_calc_SSP_ej, tau_ferrini=bestfit_namespace.bestfit_tau_ferrini, input_yields=bestfit_namespace.bestfit_input_yields, popIII_on=bestfit_namespace.bestfit_popIII_on, t_sf_z_dep=bestfit_namespace.bestfit_t_sf_z_dep, m_crit_on=bestfit_namespace.bestfit_m_crit_on, norm_crit_m=bestfit_namespace.bestfit_norm_crit_m, mass_frac_SSP=bestfit_namespace.bestfit_mass_frac_SSP, sfh_array_norm=bestfit_namespace.bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_namespace.bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_namespace.bestfit_out_follows_E_rate, r_gas_star=bestfit_namespace.bestfit_r_gas_star, cte_m_gas=bestfit_namespace.bestfit_cte_m_gas, t_dtd_poly_split=bestfit_namespace.bestfit_t_dtd_poly_split, stellar_param_on=bestfit_namespace.bestfit_stellar_param_on, delayed_extra_log=bestfit_namespace.bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_namespace.bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_namespace.bestfit_dt_in_SSPs, DM_array=bestfit_namespace.bestfit_DM_array, nsmerger_dtd_array=bestfit_namespace.bestfit_nsmerger_dtd_array, sfh_array=bestfit_namespace.bestfit_sfh_array, ism_ini=bestfit_namespace.bestfit_ism_ini, mdot_ini=bestfit_namespace.bestfit_mdot_ini, mdot_ini_t=bestfit_namespace.bestfit_mdot_ini_t, ytables_in=bestfit_namespace.bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_namespace.bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_namespace.bestfit_isotopes_in, ytables_pop3_in=bestfit_namespace.bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_namespace.bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_namespace.bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_namespace.bestfit_ytables_nsmerger_in, SSPs_in=bestfit_namespace.bestfit_SSPs_in, dt_in=bestfit_namespace.bestfit_dt_in, dt_split_info=bestfit_namespace.bestfit_dt_split_info, ej_massive=bestfit_namespace.bestfit_ej_massive, ej_agb=bestfit_namespace.bestfit_ej_agb, ej_sn1a=bestfit_namespace.bestfit_ej_sn1a, ej_massive_coef=bestfit_namespace.bestfit_ej_massive_coef, ej_agb_coef=bestfit_namespace.bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_namespace.bestfit_ej_sn1a_coef, dt_ssp=bestfit_namespace.bestfit_dt_ssp, yield_interp=bestfit_namespace.bestfit_yield_interp, mass_sampled=bestfit_namespace.bestfit_mass_sampled, scale_cor=bestfit_namespace.bestfit_scale_cor, poly_fit_dtd_5th=bestfit_namespace.bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_namespace.bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_namespace.bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_namespace.bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_namespace.bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_namespace.bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_namespace.bestfit_delayed_extra_yields_norm)
        
    ##############################################
    #              Set Yield Tables              #
    ##############################################
    def _chem_evol__set_yield_tables(self): 
	'''
        This function sets the variables associated with the yield tables
        and the stellar lifetimes used to calculate the evolution of stars.
	'''
        # Set if the yields are the default ones or not
        if not int(self.iniZ) == int(-1):
            default_yields = True
            self.default_yields = True
        else:
            default_yields = False
            self.default_yields = False

        # Read stellar yields
        if self.table[0] == '/':
            ytables = ry.read_nugrid_yields(self.table,excludemass=self.exclude_masses)
	else:	
	    ytables = ry.read_nugrid_yields(global_path + self.table,excludemass=self.exclude_masses)
        self.ytables = ytables

        # Interpolate stellar lifetimes
        self.zm_lifetime_grid_nugrid = self._chem_evol__interpolate_lifetimes_grid(ytables)

        # Get the isotopes considered by NuGrid
        mtest=float(ytables.table_mz[0].split(',')[0].split('=')[1])
        ztest=float(ytables.table_mz[0].split(',')[1].split('=')[1][:-1])
        isotopes = ytables.get(mtest,ztest,'Isotopes')
        
        self.history.isotopes = isotopes
        self.nb_isotopes = len(self.history.isotopes)

        # Read PopIII stars yields - Heger et al. (2010)
        self.ytables_pop3 = ry.read_nugrid_yields( \
            global_path+self.pop3_table,isotopes,excludemass=self.exclude_masses)

        # Interpolate PopIII stellar lifetimes
        self.zm_lifetime_grid_pop3 = \
            self._chem_evol__interpolate_lifetimes_pop3(self.ytables_pop3)

        # Read SN Ia yields
        sys.stdout.flush()
        self.ytables_1a = ry.read_yield_sn1a_tables( \
            global_path + self.sn1a_table, isotopes)

        # Read NS merger yields
        self.ytables_nsmerger = ry.read_yield_sn1a_tables( \
            global_path + self.nsmerger_table, isotopes)

        # Read BHNS merger yields
        self.ytables_bhnsmerger = ry.read_yield_sn1a_tables( \
            global_path + self.bhnsmerger_table, isotopes)

        # Read delayed extra yields
        if self.nb_delayed_extra > 0:
          self.ytables_delayed_extra = []
          for i_syt in range(0,self.nb_delayed_extra):
            self.ytables_delayed_extra.append(ry.read_yield_sn1a_tables( \
            global_path + self.delayed_extra_yields[i_syt], isotopes))

        # Should be modified to include extra source for the yields
        #self.extra_source_on = False
        #self.ytables_extra = 0
        if self.extra_source_on == True:
	    #go over all extra sources
	    self.ytables_extra =[]
	    for ee in range(len(self.extra_source_table)):  
               #if absolute path don't apply global_path
               if self.extra_source_table[ee][0] == '/':
                   self.ytables_extra.append( ry.read_yield_sn1a_tables( \
			self.extra_source_table[ee], isotopes))
               else:
                   self.ytables_extra.append( ry.read_yield_sn1a_tables( \
                        global_path + self.extra_source_table[ee], isotopes))

	#Read stellar parameter. stellar_param
	if self.stellar_param_on:
		table_param=ry.read_nugrid_parameter(global_path + self.stellar_param_table)
		self.table_param=table_param
        # Output information
        if self.iolevel >= 1:
            print 'Warning - Use isotopes with care.'
            print isotopes

        ####################################################
        ### End of function as written in 'chem_evol.py' ###
        """ 
        Change ytables(multiply yields of 'isotope' with 'factor') 
        """
        ####################################################
        #print self.experiment_isotope, self.experiment_factor
        #print "It's'a'mi! The new __set_yield_tables()!"

        #AGB + massive stars, and pop3 stars
        #loop over the different objects
        for table_object, table_name in zip([self.ytables, self.ytables_pop3],
                                            ["agb/massive", "pop3"]):
            #get list of available metalicities
            loa_metallicities = table_object.metallicities
            for Z in loa_metallicities:
                #get list of masses for each metallicity
                loa_masses = table_object.get(Z=Z, quantity="masses")
                for M in loa_masses:
                    #get current yield
                    try:
                        present_yield = table_object.get(M=M, Z=Z, quantity="Yields",
                                                         specie=self.experiment_isotope)
                    except IndexError: #this means that isotope doesn't exist for this table
                        continue
                    #modify yield by some factor
                    new_yield = present_yield*self.experiment_factor
                    #"insert" new yield back into table
                    table_object.set(M=M, Z=Z, specie=self.experiment_isotope, value=new_yield)
                    #print "Fixed new yield(%s): from %1.4e to %1.4e"%(table_name,
                    #                                                  present_yield, new_yield)
                        
        # SN1a, NS-NS merger, BH-NS merger
        # get index of isotope
        index_iso = self.history.isotopes.index(self.experiment_isotope)
        #loop over different objects
        for table_object, table_name in zip(
                [self.ytables_1a, self.ytables_nsmerger, self.ytables_bhnsmerger],
                ["sn1a", "nsm", "bhnsm"]):
            #get list of available metalicities
            loa_metallicities = table_object.metallicities
            #loop over metallicities
            for i_Z, Z in enumerate(loa_metallicities):
                #get current yield
                try:
                    present_yield = table_object.yields[i_Z][index_iso]
                except IndexError: #this means that isotope doesn't exist for this table
                    continue
                #modify yield by some factor
                new_yield = present_yield*self.experiment_factor
                #"insert" new yield back into table
                table_object.yields[i_Z][index_iso] = new_yield
                #print "Fixed new yield(%s): from %1.4e to %1.4e"%(table_name,
                #                                                  present_yield, new_yield)

    def save2file_old(self, filename):
        """ 
        Put all necesary arrays in a dictionary.
        Save dictionary to csv using Pandas.
        Necesary data:
        -isotope(str)
        -yieldfactor(float)
        -time(array)
        -ism(array) - (total, agb, massive, sn1a, nsm, bhnsm) - (H,O,Mg,C,Fe,Eu,Re,Os - isotopes)
        -yield(array) - (total, agb, massive, sn1a, nsm, bhnsm) - (H,O,Mg,C,Fe,Eu,Re,Os - isotopes)
        -mass(array) - (gas, stellar_locked, ism, out-/inflow)
        -numbers(array) - (sn1a, sn2, nsm, bhnsm)
        """
        """
        #add varying isotope and factor to filename
        if '.' not in filename: #no extension given
            filename += "_%s_%1.10f.csv"%(self.experiment_isotope, self.experiment_factor)
        else: #extension in filename
            extension = filename.split('.')[-1]
            filename = filename.split('.')[0]
            filename += "_%s_%1.10f"%(self.experiment_isotope, self.experiment_factor)
            filename += '.' + extension
        print "New filename: ", filename
        """
        #make list of elements, isotopes, yield-sources
        save_elements = ['H','C','O','Mg','Fe','Eu','W','Re','Os','Ir']
        save_isotopes = ['H-1', 'H-2','C-12','C-13','O-16','O-17','O-18','Mg-24','Mg-25','Mg-26','Fe-54','Fe-56','Fe-57','Fe-58','Eu-151', 'Eu-153','W-180','W-182','W-183','W-184','W-186','Re-185','Re-187','Os-184','Os-186','Os-187','Os-188','Os-189','Os-190','Os-192','Ir-191','Ir-193']
        save_sources = ['total', 'agb', 'massive', 'sn1a', 'nsm', 'bhnsm']
        loa_ism_arrays = [self.history.ism_iso_yield, self.history.ism_iso_yield_agb,
                          self.history.ism_iso_yield_massive, self.history.ism_iso_yield_1a,
                          self.history.ism_iso_yield_nsm, self.history.ism_iso_yield_bhnsm]
        loa_yields_arrays = [self.mdot, self.mdot_agb, self.mdot_massive,
                             self.mdot_1a, self.mdot_nsm, self.mdot_bhnsm]
        save_numbers = ['sn1a', 'sn2', 'nsm', 'bhnsm']
        loa_number_arrays = [self.history.sn1a_numbers, self.history.sn2_numbers,
                             self.history.nsm_numbers, self.history.bhnsm_numbers]
        
        #make dictionary of arrays
        save_dictionary = {}
        
        save_dictionary["time"] = self.history.age
        save_dictionary["sfr"] = self.history.sfr_abs
        save_dictionary["gas_mass"] = self.history.gas_mass
        #save_dictionary["m_tot_ISM_t"] = self.history.m_tot_ISM_t
        save_dictionary["m_outflow_t"] = self.history.m_outflow_t
        save_dictionary["m_inflow_t"] = self.history.m_inflow_t
        save_dictionary["m_locked"] = self.history.m_locked
        save_dictionary["m_locked_agb"] = self.history.m_locked_agb
        save_dictionary["m_locked_massive"] = self.history.m_locked_massive
        
        #NOTE! add extra zero to beginning to make all arrays equal in length
        save_dictionary["m_outflow_t"] = np.insert(save_dictionary["m_outflow_t"], 0,0)
        save_dictionary["m_inflow_t"] = np.insert(save_dictionary["m_inflow_t"], 0,0)
        save_dictionary["m_locked"] = np.insert(save_dictionary["m_locked"], 0,0)
        save_dictionary["m_locked_agb"] = np.insert(save_dictionary["m_locked_agb"], 0,0)
        save_dictionary["m_locked_massive"] = np.insert(save_dictionary["m_locked_massive"], 0,0)
        
        for number, array in zip(save_numbers, loa_number_arrays):
            key = "number_" + number
            save_dictionary[key] = array
        for source, array in zip(save_sources, loa_ism_arrays):
            for iso in save_isotopes:
                key = "ism_" + source + "_" + iso
                np_array = np.array(array)
                save_dictionary[key] = np_array[:,self.history.isotopes.index(iso)]
        for source, array in zip(save_sources, loa_yields_arrays):
            for iso in save_isotopes:
                key = "yield_" + source + "_" + iso
                np_array = np.array(array)
                save_dictionary[key] = np_array[:,self.history.isotopes.index(iso)]
                #NOTE! add extra zero to beginning to make all arrays equal in length
                save_dictionary[key] = np.insert(save_dictionary[key], 0,0)

        panda_object = pd.DataFrame(data=save_dictionary)
        panda_object.to_csv(filename, compression=None)

    def save2file(self, filename, write_index_file=False):
        """
        Description of _second_ save-function:
        Store 288 time-sized arrays as a 2D matrix
        Get all relevant arrays(as a function of time), store in a (n*m)-matrix.
        Store matrix in binary with numpys save-function.

        NOTE! #add0 means add extra zero to beginning of array for equal length arrays
        """
        n = len(self.history.age) #number of time-points in GCE
        m = 288 #number of arrays to store
        dim = (m,n) #dimension of matrix
        store_arr = np.zeros(dim) #2D array to store all 1D arrays
        index_arr = 0 #index of array in 2D array
        loa_arr_names = [] #list of names of all arrays
        filename = filename.split('.')[0] #remove format-suffix from filename

        store_arr[index_arr,:] = self.history.age
        loa_arr_names.append("time"); index_arr += 1
        store_arr[index_arr,:] = self.history.sfr_abs 
        loa_arr_names.append("sfr"); index_arr += 1 
        store_arr[index_arr,:] = self.history.gas_mass
        loa_arr_names.append("gas_mass"); index_arr += 1
        store_arr[index_arr,:] = np.array([0] + list(self.history.m_outflow_t)) #add0
        loa_arr_names.append("m_outflow"); index_arr += 1
        store_arr[index_arr,:] = np.array([0] + list(self.m_inflow_t)) #add0
        loa_arr_names.append("m_inflow"); index_arr += 1
        store_arr[index_arr,:] = np.array([0] + list(self.history.m_locked)) #add0
        loa_arr_names.append("m_locked"); index_arr += 1
        store_arr[index_arr,:] = np.array([0] + list(self.history.m_locked_agb)) #add0
        loa_arr_names.append("m_locked_agb"); index_arr += 1
        store_arr[index_arr,:] = np.array([0] + list(self.history.m_locked_massive)) #add0
        loa_arr_names.append("m_locked_massive"); index_arr += 1

        #make list of elements, isotopes, yield-sources
        save_elements = ['H','C','O','Mg','Fe','Eu','W','Re','Os','Ir']
        save_isotopes = ['H-1', 'H-2','C-12','C-13','O-16','O-17','O-18','Mg-24','Mg-25','Mg-26','Fe-54','Fe-56','Fe-57','Fe-58','Eu-151', 'Eu-153','W-180','W-182','W-183','W-184','W-186','Re-185','Re-187','Os-184','Os-186','Os-187','Os-188','Os-189','Os-190','Os-192','Ir-191','Ir-193']
        save_isotopes = ['Eu-151', 'Eu-153','W-180','W-182','W-183','W-184','W-186','Re-185','Re-187','Os-184','Os-186','Os-187','Os-188','Os-189','Os-190','Os-192','Ir-191','Ir-193']

        save_elements_indeces = [self.history.elements.index(elem) for elem in save_elements]
        save_isotopes_indeces = [self.history.isotopes.index(iso) for iso in save_isotopes]

        #elemental abundances
        for elem_index, elem_name in zip(save_elements_indeces, save_elements):
            #print np.array(self.history.ism_elem_yield).shape, elem_index
            store_arr[index_arr,:] = np.array(self.history.ism_elem_yield)[:,elem_index]
            loa_arr_names.append("ism_elem_%s"%elem_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_elem_yield_agb)[:,elem_index]
            loa_arr_names.append("ism_elem_%s_agb"%elem_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_elem_yield_massive)[:,elem_index]
            loa_arr_names.append("ism_elem_%s_massive"%elem_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_elem_yield_1a)[:,elem_index]
            loa_arr_names.append("ism_elem_%s_1a"%elem_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_elem_yield_nsm)[:,elem_index] 
            loa_arr_names.append("ism_elem_%s_nsm"%elem_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_elem_yield_bhnsm)[:,elem_index]
            loa_arr_names.append("ism_elem_%s_bhnsm"%elem_name); index_arr += 1
            
        #isotopic abundances
        for iso_index, iso_name in zip(save_isotopes_indeces, save_isotopes):
            store_arr[index_arr,:] = np.array(self.history.ism_iso_yield)[:,iso_index]
            loa_arr_names.append("ism_iso_%s"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_iso_yield_agb)[:,iso_index]
            loa_arr_names.append("ism_iso_%s_agb"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_iso_yield_massive)[:,iso_index] 
            loa_arr_names.append("ism_iso_%s_massive"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_iso_yield_1a)[:,iso_index]
            loa_arr_names.append("ism_iso_%s_1a"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_iso_yield_nsm)[:,iso_index]
            loa_arr_names.append("ism_iso_%s_nsm"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.array(self.history.ism_iso_yield_bhnsm)[:,iso_index]
            loa_arr_names.append("ism_iso_%s_bhnsm"%iso_name); index_arr += 1

        #yields
        for iso_index, iso_name in zip(save_isotopes_indeces, save_isotopes):
            store_arr[index_arr,:] = np.insert(np.array(self.mdot)[:,iso_index],0,0) #add0
            loa_arr_names.append("yield_%s"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.insert(np.array(self.mdot_agb)[:,iso_index],0,0) #add0
            loa_arr_names.append("yield_%s_agb"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.insert(np.array(self.mdot_massive)[:,iso_index],0,0) #add0
            loa_arr_names.append("yield_%s_massive"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.insert(np.array(self.mdot_1a)[:,iso_index],0,0) #add0
            loa_arr_names.append("yield_%s_1a"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.insert(np.array(self.mdot_nsm)[:,iso_index],0,0) #add0
            loa_arr_names.append("yield_%s_nsm"%iso_name); index_arr += 1
            store_arr[index_arr,:] = np.insert(np.array(self.mdot_bhnsm)[:,iso_index],0,0) #add0
            loa_arr_names.append("yield_%s_bhnsm"%iso_name); index_arr += 1
            
        #numbers
        store_arr[index_arr,:] = np.array(self.history.sn1a_numbers)
        loa_arr_names.append("num_sn1a"); index_arr += 1
        store_arr[index_arr,:] = np.array(self.history.sn2_numbers)
        loa_arr_names.append("num_sn2"); index_arr += 1
        store_arr[index_arr,:] = np.array(self.history.nsm_numbers)
        loa_arr_names.append("num_nsm"); index_arr += 1
        store_arr[index_arr,:] = np.array(self.history.bhnsm_numbers)
        loa_arr_names.append("num_bhnsm"); index_arr += 1

        np.save(filename+".npy", store_arr)
        print "Data written to filename: %s"%(filename+".npy")

        if write_index_file:
            #Write a file with the name of arrays and their index in the 2D-matrix
            #find folder of filename
            filefolder_list =  filename.split('/')[:-1]
            filefolder = ''
            for folder in filefolder_list:
                filefolder += folder + '/'
            index_filename = filefolder + "data_indeces.txt"
            with open(index_filename, 'w') as outfile:
                for i, arr_name in enumerate(loa_arr_names):
                    outfile.write("%d %s \n"%(i,arr_name))
            print "Indeces of arrays written to file: %s"%index_filename

if __name__ == '__main__':
    """ #Make simple test 
    Three instances of Experiment the Re-187 
    is varied with factors 0.5, 1.0, 2.0. 
    Plot the resulting yields(SUM) for all omegas 
    with only CCSN/NSNSM as source
    """
    #get kwdargs from cmd-line
    #TODO; apply when necessary!
    
    #make instances for a single isotope and three scalefactors
    isotope = "Eu-151"
    loa_scalefactors = [0.5,1.0,2.0]
    loa_scalefactor_texts = ["%s $f_{yields}$=%1.1f"%(isotope,scalefactor)
                             for scalefactor in loa_scalefactors ]
    loa_experiments = [experiment(isotope, scalefactor)
                       for scalefactor in loa_scalefactors]

    #plot with visualize
    import visualize as vs
    plot_inst = vs.visualize(loa_experiments, loa_scalefactor_texts,
                             yields=True)
    plot_inst.add_yields(source=["agb", "massive", "nsm"],
                         nuclide=isotope, time="sum")
    plot_inst.finalize(show=True)
