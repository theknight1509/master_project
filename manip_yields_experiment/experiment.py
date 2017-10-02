"""
Description:
-Make a class that inherits everything from omega or sygma
-change the functions that uses sygma to get yields
-add a funky factor to the yields of a single isotope
"""
#get folder-handling-script
from directory_master import FolderMap
folder = FolderMap

#set environment for chem_evol
import os
os.environ["SYGMADIR"] = folder.nupycee
from omega import omega #NuPyCEE one-zone chemical evolution code

class experiment(omega):
    def __init__(self, input_isotope='Re-187', input_factor=1.0):
        self.experiment_isotope = input_isotope
        self.experiment_factor = input_factor

        #initialize omega
        print "TODO!!!"


    ##############################################
    #              Set Yield Tables              #
    ##############################################
    def __set_yield_tables(self, isotope=self.experiment_isotope,
                           factor=self.experiment_factor): 
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

        ### End of function as written in 'chem_evol.py' ###
        #change ytables(multiply yields of 'isotope' with 'factor'

if __name__ == '__main__':
    """ Make simple test """
    None
