"""
Description:
-Make a class that inherits everything from omega or sygma
-change the functions that uses sygma to get yields
-add a funky factor to the yields of a single isotope
"""
#get folder-handling-script
from directory_master import Foldermap
folder = Foldermap()
folder.activate_environ() #set environment for omega before importing
from NuPyCEE.omega import omega #NuPyCEE one-zone chemical evolution code
from bestfit_param_omega.bestfit_file import * #import the current bestfit parameters

class experiment(omega):
    def __init__(self, input_isotope='Re-187', input_factor=1.0):
        self.experiment_isotope = input_isotope
        self.experiment_factor = input_factor

    def __call__(self):
                ### initialize omega ###
        bestfit_special_timesteps = 30
        bestfit_external_control = False
        #super(experiment, self).
        #super(omega, self).
        omega.__init__(self, galaxy=bestfit_galaxy, in_out_control=bestfit_in_out_control, SF_law=bestfit_SF_law, DM_evolution=bestfit_DM_evolution, Z_trans=bestfit_Z_trans, f_dyn=bestfit_f_dyn, sfe=bestfit_sfe, outflow_rate=bestfit_outflow_rate, inflow_rate=bestfit_inflow_rate, rand_sfh=bestfit_rand_sfh, cte_sfr=bestfit_cte_sfr, m_DM_0=bestfit_m_DM_0, mass_loading=bestfit_mass_loading, t_star=bestfit_t_star, sfh_file=bestfit_sfh_file, in_out_ratio=bestfit_in_out_ratio, stellar_mass_0=bestfit_stellar_mass_0, z_dependent=bestfit_z_dependent, exp_ml=bestfit_exp_ml, nsmerger_bdys=bestfit_nsmerger_bdys, imf_type=bestfit_imf_type, alphaimf=bestfit_alphaimf, imf_bdys=bestfit_imf_bdys, sn1a_rate=bestfit_sn1a_rate, iniZ=bestfit_iniZ, dt=bestfit_dt, special_timesteps=bestfit_special_timesteps, tend=bestfit_tend, mgal=bestfit_mgal, transitionmass=bestfit_transitionmass, iolevel=bestfit_iolevel, ini_alpha=bestfit_ini_alpha, nb_nsm_per_m=bestfit_nb_nsm_per_m, t_nsm_coal=bestfit_t_nsm_coal, table=bestfit_table, hardsetZ=bestfit_hardsetZ, sn1a_on=bestfit_sn1a_on, nsm_dtd_power=bestfit_nsm_dtd_power, sn1a_table=bestfit_sn1a_table, ns_merger_on=bestfit_ns_merger_on, f_binary=bestfit_f_binary, f_merger=bestfit_f_merger, t_merger_max=bestfit_t_merger_max, m_ej_nsm=bestfit_m_ej_nsm, nsmerger_table=bestfit_nsmerger_table, bhns_merger_on=bestfit_bhns_merger_on, m_ej_bhnsm=bestfit_m_ej_bhnsm, bhnsmerger_table=bestfit_bhnsmerger_table, iniabu_table=bestfit_iniabu_table, extra_source_on=bestfit_extra_source_on, extra_source_table=bestfit_extra_source_table, f_extra_source=bestfit_f_extra_source, pre_calculate_SSPs=bestfit_pre_calculate_SSPs, extra_source_mass_range=bestfit_extra_source_mass_range, extra_source_exclude_Z=bestfit_extra_source_exclude_Z, pop3_table=bestfit_pop3_table, imf_bdys_pop3=bestfit_imf_bdys_pop3, imf_yields_range_pop3=bestfit_imf_yields_range_pop3, starbursts=bestfit_starbursts, beta_pow=bestfit_beta_pow, gauss_dtd=bestfit_gauss_dtd, exp_dtd=bestfit_exp_dtd, nb_1a_per_m=bestfit_nb_1a_per_m, f_arfo=bestfit_f_arfo, t_merge=bestfit_t_merge, imf_yields_range=bestfit_imf_yields_range, exclude_masses=bestfit_exclude_masses, netyields_on=bestfit_netyields_on, wiersmamod=bestfit_wiersmamod, skip_zero=bestfit_skip_zero, redshift_f=bestfit_redshift_f, print_off=bestfit_print_off, long_range_ref=bestfit_long_range_ref, f_s_enhance=bestfit_f_s_enhance, m_gas_f=bestfit_m_gas_f, cl_SF_law=bestfit_cl_SF_law, external_control=bestfit_external_control, calc_SSP_ej=bestfit_calc_SSP_ej, tau_ferrini=bestfit_tau_ferrini, input_yields=bestfit_input_yields, popIII_on=bestfit_popIII_on, t_sf_z_dep=bestfit_t_sf_z_dep, m_crit_on=bestfit_m_crit_on, norm_crit_m=bestfit_norm_crit_m, mass_frac_SSP=bestfit_mass_frac_SSP, sfh_array_norm=bestfit_sfh_array_norm, imf_rnd_sampling=bestfit_imf_rnd_sampling, out_follows_E_rate=bestfit_out_follows_E_rate, r_gas_star=bestfit_r_gas_star, cte_m_gas=bestfit_cte_m_gas, t_dtd_poly_split=bestfit_t_dtd_poly_split, stellar_param_on=bestfit_stellar_param_on, delayed_extra_log=bestfit_delayed_extra_log, bhnsmerger_dtd_array=bestfit_bhnsmerger_dtd_array, dt_in_SSPs=bestfit_dt_in_SSPs, DM_array=bestfit_DM_array, nsmerger_dtd_array=bestfit_nsmerger_dtd_array, sfh_array=bestfit_sfh_array, ism_ini=bestfit_ism_ini, mdot_ini=bestfit_mdot_ini, mdot_ini_t=bestfit_mdot_ini_t, ytables_in=bestfit_ytables_in, zm_lifetime_grid_nugrid_in=bestfit_zm_lifetime_grid_nugrid_in, isotopes_in=bestfit_isotopes_in, ytables_pop3_in=bestfit_ytables_pop3_in, zm_lifetime_grid_pop3_in=bestfit_zm_lifetime_grid_pop3_in, ytables_1a_in=bestfit_ytables_1a_in, ytables_nsmerger_in=bestfit_ytables_nsmerger_in, SSPs_in=bestfit_SSPs_in, dt_in=bestfit_dt_in, dt_split_info=bestfit_dt_split_info, ej_massive=bestfit_ej_massive, ej_agb=bestfit_ej_agb, ej_sn1a=bestfit_ej_sn1a, ej_massive_coef=bestfit_ej_massive_coef, ej_agb_coef=bestfit_ej_agb_coef, ej_sn1a_coef=bestfit_ej_sn1a_coef, dt_ssp=bestfit_dt_ssp, yield_interp=bestfit_yield_interp, mass_sampled=bestfit_mass_sampled, scale_cor=bestfit_scale_cor, poly_fit_dtd_5th=bestfit_poly_fit_dtd_5th, poly_fit_range=bestfit_poly_fit_range, m_tot_ISM_t_in=bestfit_m_tot_ISM_t_in, delayed_extra_dtd=bestfit_delayed_extra_dtd, delayed_extra_dtd_norm=bestfit_delayed_extra_dtd_norm, delayed_extra_yields=bestfit_delayed_extra_yields, delayed_extra_yields_norm=bestfit_delayed_extra_yields_norm)

        #Run omega-simulation
        #self.__run_simulation(self.mass_sampled, self.scale_cor)
        #for i in range(1, self.nb_timesteps+1):
        #    self.run_step(i, self.sfr_input[i-1])
        
    ##############################################
    #              Set Yield Tables              #
    ##############################################
    def __set_yield_tables(self): 
	'''
        This function sets the variables associated with the yield tables
        and the stellar lifetimes used to calculate the evolution of stars.
	'''
        print "It's'a'mi! The new __set_yield_tables()!"

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
        self.zm_lifetime_grid_nugrid = self.__interpolate_lifetimes_grid(ytables)

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
            self.__interpolate_lifetimes_pop3(self.ytables_pop3)

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

        #AGB + massive stars, and pop3 stars
        #loop over the different objects
        for table_object in [self.ytables, self.ytables_pop3]:
            #get list of available masses and metalicities
            loa_metallicities = table_object.metallicities
            loa_masses = table_object.get(quantity="masses")
            #loop over M-Z-pairs
            for M in loa_masses:
                for Z in loa_metallicities:
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

        # SN1a, NS-NS merger, BH-NS merger
        # get index of isotope
        index_iso = self.history.isotopes.index(self.experiment_isotope)
        #loop over different objects
        for table_object in [self.ytables_1a, self.ytables_nsmerger, self.ytables_bhnsmerger]:
            #get list of available metalicities
            loa_metallicities = table_object.metallicities
            #loop over metallicities
            for i_Z, Z in enumerate(loa_metallicites):
                #get current yield
                try:
                    present_yield = table_object.yields[i_Z][index_iso]
                except IndexError: #this means that isotope doesn't exist for this table
                    continue
                #modify yield by some factor
                new_yield = present_yield*self.experiment_factor
                #"insert" new yield back into table
                table_object.yields[i_Z][index_iso] = new_yield

if __name__ == '__main__':
    """ #Make simple test 
    Three instances of Experiment the Re-187 
    is varied with factors 0.5, 1.0, 2.0. 
    Plot the resulting yields(SUM) for all omegas 
    with only CCSN/NSNSM as source
    """

    isotope = "Re-187"
    loa_scalefactors = [0.5,1.0,2.0]
    loa_scalefactor_texts = ["%s $f_{yields}$=%1.1f"%(isotope,scalefactor)
                             for scalefactor in loa_scalefactors ]
    #loa_experiments = [experiment(isotope, scalefactor)
    #                   for scalefactor in loa_scalefactors]
    loa_experiments = []
    for scalefactor in loa_scalefactors:
        exp = experiment(isotope, scalefactor) #make instance
        exp() #run simulation
        loa_experiments.append(exp) #add instance to loa_experiments

    #plot with visualize
    import visualize as vs
    plot_inst = vs.visualize(loa_experiments, loa_scalefactor_texts,
                             yields=True)
    plot_inst.add_yields(source=["agb", "massive", "nsm"],
                         nuclide=isotope, time="sum")
    plot_inst.finalize(show=True)
