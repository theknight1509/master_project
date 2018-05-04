"""
Purpose:
Make a class/object that inherits the properties og 'child_omega',
which inherits 'Omega'. 
The new class will modify an existing function in order to 
modify the yield of a single isotope in all yield tables available.

Description:
"""

from child_omega import child_omega

class grandchild_omega(child_omega):
    def __init__(self, namespace, loa_manip_isotopes,
                 loa_manip_yields):
        #Make list of isotopes and factors to apply to yields
        self.loa_manip_isotopes = loa_manip_isotopes
        self.loa_manip_yields = loa_manip_yields

        #call __init__ and run model.
        child_omega.__init__(self,bestfit_namespace=namespace)
        return

    ##############################################
    #              Set Yield Tables              #
    ##############################################
    def _chem_evol__set_yield_tables(self): 
	'''
        This function sets the variables associated with the yield tables
        and the stellar lifetimes used to calculate the evolution of stars.
	'''
        import read_yields as ry
        import os
        import sys
        global_path = os.environ['SYGMADIR'] + '/'
        
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
        This step requires 
        'self.experiment_isotope' and 'self.experiment_factor'!
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
                    #loop over all isotopes to manipulate
                    for manip_isotope, manip_factor in zip(self.loa_manip_isotopes,self.loa_manip_yields):
                        #get current yield 
                        try:
                            present_yield = table_object.get(M=M, Z=Z, quantity="Yields",
                                                             specie=manip_isotope)
                        except IndexError: #this means that isotope doesn't exist for this table
                            continue
                        #modify yield by some factor
                        new_yield = present_yield*manip_factor 
                        #"insert" new yield back into table
                        table_object.set(M=M, Z=Z, specie=manip_isotope, value=new_yield)
                        #print "Fixed new yield(%s): from %1.4e to %1.4e"%(table_name,present_yield, new_yield)
                        
        # SN1a, NS-NS merger, BH-NS merger
        #loop over different objects
        for table_object, table_name in zip(
                [self.ytables_1a, self.ytables_nsmerger, self.ytables_bhnsmerger],
                ["sn1a", "nsm", "bhnsm"]):
            #get list of available metalicities
            loa_metallicities = table_object.metallicities
            #loop over metallicities
            for i_Z, Z in enumerate(loa_metallicities):
                #loop over all isotopes to manipulate
                for manip_isotope, manip_factor in zip(self.loa_manip_isotopes,self.loa_manip_yields):
                    # get index of isotope
                    index_iso = self.history.isotopes.index(manip_isotope)
                    #get current yield
                    try:
                        present_yield = table_object.yields[i_Z][index_iso]
                    except IndexError: #this means that isotope doesn't exist for this table
                        continue
                    #modify yield by some factor
                    new_yield = present_yield*manip_factor
                    #"insert" new yield back into table
                    table_object.yields[i_Z][index_iso] = new_yield
                    #print "Fixed new yield(%s): from %1.4e to %1.4e"%(table_name,present_yield, new_yield)
        return
