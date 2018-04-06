"""
This script holds the class for writing readme-files for a
MonteCarlo-experiment subdirectory.
"""
import sys
import os

class readme(object):
    """
    """
    def __init__(self, filename):
        self.filename = filename

        #check if filename exists

        #create dictionary with data-tuples for sections of readme
        self.content_dict = {}

        #fill content-dict with empty parameters from fill-functions
        self.add_header()
        self.add_param_info()
        self.add_mc_info()
        self.add_processor_info()

    def add_header(self, date=False,
                   exp_filenames=False, opt_desc=False):
        key = "header" #key for this section
        input_list = [date, exp_filenames, opt_desc]
        if key in self.content_dict.keys(): #data-tuple exists
            old_data_list = list(self.content_dict[key])
            #if input data is True, add input data, else use old
            new_data_list = [input_data if input_data else old_data
                             for old_data, input_data
                             in zip(old_data_list, input_list)]
            self.content_dict[key] = tuple(new_data_list)
        else: #fill dict with empty values
            self.content_dict[key] = tuple(input_list)
        return

    def write_header(self, data_tuple):
        #Data-tuple has date, experiment-filename, optional desc.
        date, exp_filename, opt_desc = data_tuple
        if not date:
            date = "unknown date"
        if not exp_filename:
            exp_filename = "unknown filename"

        header_string = "This is the readme-file for a MonteCarlo experiment of 'Omega' performed on %s."%(date) + '\n'
        header_string += "The datafiles are two-dimensional numpy-matrices named %s."%(exp_filename) + '\n'

        if opt_desc:
            header_string += "%s"%(opt_desc) + '\n'

        return header_string + '\n'

    def add_param_info(self, filename=False, parameter_tuples=False,
                       opt_namespace_info=False):
        key = "param_info"
        input_list = [filename,parameter_tuples,opt_namespace_info]
        if key in self.content_dict.keys(): #data-tuple exists
            old_data_tuple = self.content_dict[key]
            #if input data is True, add input data, else use old
            new_data_list = [input_data if input_data else old_data
                             for old_data, input_data
                             in zip(old_data_tuple, input_list)]
            self.content_dict[key] = tuple(new_data_list)
        else: #fill dict with empty values
            self.content_dict[key] = tuple(input_list)
        return

    def write_param(self, data_tuple):
        #Data-tuple has ...
        param_filename, loa_param_tuples, opt_namespace_string \
            = data_tuple
        if not param_filename:
            param_filename = "N/A"
        if not loa_param_tuples:
            loa_param_tuples = []

        param_string = "The values for parameters (fudge factors applied to parameters) can be found in [parameter-table](%s)"%param_filename + '\n'
        param_string += "The parameter-values (fudge factors) are drawn from the following gaussian distriutions: \n"
        for param_tuple in loa_param_tuples:
            param_string += "%s: mean %1.4f, stddev %1.4f"%param_tuple + '\n'
        if opt_namespace_string:
            param_string += "Regarding the parameters used for the simulation:\n"
            param_string += "%s"%opt_namespace_string + '\n'

        return param_string

    def add_mc_info(self, num_processes=False,
                    num_processors=False, tot_time=False):
        key = "mc_info"
        input_list = [num_processes, num_processors, tot_time]
        if key in self.content_dict.keys(): #data-tuple exists
            old_data_tuple = self.content_dict[key]
            #if input data is True, add input data, else use old
            new_data_list = [input_data if input_data else old_data
                             for old_data, input_data
                             in zip(old_data_tuple, input_list)]
            self.content_dict[key] = tuple(new_data_list)
        else: #fill dict with empty values
            self.content_dict[key] = tuple(input_list)
        return

    def write_mc(self, data_tuple):
        #Data-tuple has ...
        num_processes, num_processors, tot_time = data_tuple

        if not num_processes:
            num_processes = "N/A"
        if not num_processors:
            num_processors = "N/A"
        if not tot_time:
            tot_time = "N/A"

        mc_string = "Total number of processes to spawn: %s \n"%num_processes
        mc_string += "Total number of processors available: %s \n"%num_processors
        mc_string += "Total time used to calculate all models: %s \n"%tot_time
        return mc_string

    def add_processor_info(self, index=False, status=False,
                           time=False):
        key = "processor_info"
        input_list = [index, status, time]
        if key in self.content_dict.keys(): #data-tuple exists
            loa_processor_info = content_dict[key]
            #if input data is True, add input data, else use old
            new_data_list = [input_data if input_data else old_data
                             for old_data, input_data
                             in zip(old_data_list, input_list)]
            self.content_dict[key] = tuple(new_data_list)
            self.update_processor_data_to_file() #write latest data to file!
        else: #fill dict with empty list
            self.content_dict[key] = []
        return

    def write_single_process_data(self, data_tuple):
        index, status, time = data_tuple
        if not index:
            index = "unknown"
        if not status:
            status = "unknown"
        if not time:
            time = "unknown"
        data_tuple = index, status, time
        process_string = "Process-id: %s, status: %s, calculation time: %s \n"%data_tuple
        return process_string

    def write_new_file(self):
        """ Transform data from content-dict. into 
        readable string, and to new file 'self.filename'.
        Warning, this deletes the old content."""
        readme_string = ""
        loa_sections = self.content_dict.keys()

        #make known keys
        header_key = "header"
        parameter_key = "param_info"
        mc_key = "mc_info"
        processor_info_key = "processor_info"

        #Write section from header-key
        readme_string += self.write_header(self.content_dict[header_key])
        #remove key from list of sections
        loa_sections.remove(header_key)

        #Write section from parameter-key
        readme_string += self.write_param(self.content_dict[parameter_key])
        #remove key from list of sections
        loa_sections.remove(parameter_key)

        #Write section from mc-key
        readme_string += self.write_mc(self.content_dict[mc_key])
        #remove key from list of sections
        loa_sections.remove(mc_key)

        #loop over all sections remaining, not processor-info
        for key in [sec for sec in loa_sections
                    if sec != processor_info_key]:
            #Write section from key
            readme_string += str(self.content_dict[key]) + "\n"
            #remove key from list of sections
            loa_sections.remove(key)

        #Write section from processor_info
        loa_processor_info = self.content_dict[processor_info_key]
        loa_indeces = [tup[0] for tup in loa_processor_info]
        #sort list of tuples based on list of indeces
        loa_processor_info = [processor_info for index,processor_info in sorted(zip(loa_indeces,loa_processor_info))]
        for processor_info in loa_processor_info:
            readme_string += self.write_single_process_data(processor_info)
        #remove key from list of sections
        loa_sections.remove(processor_info_key)

        #Write all of string to file
        with open(self.filename, 'w') as readmefile:
            readmefile.write(readme_string)
        return readme_string

    def update_processor_data_to_file(self):
        """Write last processor-data-tuple appended to file"""
        processor_info_key = "processor_info"
        loa_processor_data_tuples = self.content_data[processor_info_key] #list of all current processor-data
        latest_data_tuple = loa_processor_data_tuples[-1] #tuple with latest data-tuple
        processor_string = self.write_single_process_data(latest_data_tuple) #string with data of latest process-data
        #append data string from latest process to end of file
        with open(self.filename, 'a') as outfile:
            outfile.write(process_string)
        return 

if __name__ == '__main__':
    ### Tests for readme-class ###
    print "Testing %s"%(sys.argv[0])
    obj = readme("test")

    #check empty dictionary
    print "content dictionary of empty class-object:"
    print obj.content_dict

    #check add_header function twice
    print "Header-data: ", obj.content_dict["header"]
    obj.add_header(date="today")
    print "Header-data w/date: ", obj.content_dict["header"]
    obj.add_header(opt_desc="test")
    print "Header-data w/description: ", obj.content_dict["header"]
    obj.add_header(date="tomorrow")
    print "Header-data w/new date: ", obj.content_dict["header"]

    #check string written to file
    print "output to file:"
    print obj.write_new_file()

    del obj
