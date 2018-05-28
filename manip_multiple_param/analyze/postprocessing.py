#!/usr/bin/python2.7
"""
Class and function for extracting data from 
sea of data-files in experiment-folders.
"""
import sys
import os
import numpy as np
import configparser as cp
import pandas as pd
from directory_master import Foldermap

class Extract(object):
    def __init__(self, dir_name):
        self.dir_string_func = lambda dir_name: dir_name if (dir_name[-1]=="/") else dir_name + "/"
        self.data_index_filename = self.dir_string_func(dir_name) + "data_indeces.txt"

        self.get_dir = dir_name
        self.save_dir = dir_name

        self.check_filename_level = 0 #base level, all good

    def __call__(self, nsm=False):
        if nsm:
            self.setup_extract_nsm()
        else:
            self.setup_extract_reos()
        return

    def set_save_dir(self, save_dir):
        self.save_dir = save_dir
        return

    def check_filename(self, filename=False):
        if self.check_filename_level == 0:
            return True
        elif self.check_filename_level == 1:
            if not filename:
                raise UserWarning("No 'filename' given!")
            else:
                pid = get_pid_from_filename(filename=filename)
                if not pid:
                    raise UserWarning("Invalid pid in filename: %s"%(filename))
                directory = "/".join(filename.split("/")[:-1])
                y_hat_re187 = get_yhat(directory=directory, pid=pid, iso="Re-187")
                y_hat_os187 = get_yhat(directory=directory, pid=pid, iso="Os-187")
                if (y_hat_re187 > 0.0) and (y_hat_re187 > 0.0):
                    return True
                else:
                    return False
        else:
            raise UserWarning("'self.checkout_filename_level' %d not accounted for!'"%(self.check_filename_level))

    def get_data_index(self, string):
        """ Go through data-index-file, find index matching 'string'
        return index or raise error """
        found_index = False
        return_index = 0
        
        with open(self.data_index_filename, 'r') as data_index_file:
            loa_content_rows = data_index_file.readlines()

        #loop over all rows in file
        for content_row in loa_content_rows:
            #split row into index and array-name
            current_row = content_row.split()
            current_index = int(current_row[0])
            current_array_name = current_row[1]
            if (current_array_name == string):
                return_index = current_index
                found_index = True
                break

        if not found_index:
            raise Exception("No array-name '%s' found in data-index-file"%(string))
        else:
            return return_index
        
    def get_numpy_filenames(self, trait="pid", untrait="decayed"):
        """ Loop over all filenames, compile list with filenames that have:
        '.npy' and trait in the filename."""
        loa_filenames = os.listdir(self.get_dir)
        loa_numpy_filenames = [self.dir_string_func(self.get_dir) + filename
                               for filename in loa_filenames
                               if ('.npy' in filename) 
                               and (trait in filename)
                               and (untrait not in filename)]
        return loa_numpy_filenames

    def handle_all_data(self, extract_func, extract_filename, decayed_data=False):
        """ Loop over all numpy arrays and extract array according to 
        function in keyword-arguments.
        'extract_func' - must take numpy matrix and return single array
        """
        loa_extracted_arrays = []
        if decayed_data:
            loa_chosen_datafiles = self.get_numpy_filenames(trait="decayed",
                                                            untrait="extract")
        else:
            loa_chosen_datafiles = self.get_numpy_filenames(untrait="decayed")
        
        for data_filename in loa_chosen_datafiles:
            if self.check_filename(filename=data_filename):
                pass
            else:
                continue
            data = np.load(data_filename) #get data from a single data-file
            extracted_arr = extract_func(data) #extract according to input function
            loa_extracted_arrays.append(extracted_arr) #store extracted array
        extracted_data = np.stack(loa_extracted_arrays) #stack into matrix of extracted arrays
        extracted_filename = self.dir_string_func(self.save_dir) + "extract_" + extract_filename + ".npy"
        np.save(extracted_filename, extracted_data) #save extracted data
        print "Saving extracted data to %s"%(extracted_filename)
        return

    def extract_single_array(self, data, index_array):
        return data[index_array,:]
    
    def extract_ratio_array(self, data, index_numer, index_denom):
        numerator = data[index_numer,:]
        denominator = data[index_denom,:]
        return_array = np.nan_to_num(numerator/denominator)
        return return_array

    def get_time_array(self):
        #Get time-array from the first numpy-filename
        index_time = self.get_data_index(string="time")
        loa_numpy_filenames = self.get_numpy_filenames()
        numpy_filename = loa_numpy_filenames[0] #choose the first filename

        data = np.load(numpy_filename)
        time_array = data[index_time,:]

        return time_array

    def setup_extract_reos(self):
        """ Extract all data for ISM-data of Re-187, Os-187 and Os-187/Re-187."""
        re187 = "Re-187"
        os187 = "Os-187"
        loa_keys = [re187, os187]
        doa_array_string = {key: "ism_iso_%s"%key for key in loa_keys}
        doa_array_index = {key: self.get_data_index(doa_array_string[key]) for key in loa_keys}
        doa_filename = {key: "ism_%s"%key for key in loa_keys}

        #extract single-isotope ism-array from loa_keys
        for key in loa_keys:
            extract_func = lambda data: self.extract_single_array(data=data, index_array=doa_array_index[key])
            self.handle_all_data(extract_func=extract_func,
                                 extract_filename=doa_filename[key])
            self.handle_all_data(extract_func=extract_func,
                                 extract_filename=doa_filename[key]+"_decayed",
                                 decayed_data=True)

        #extract os-187/re187 ism-array
        extract_func = lambda data: self.extract_ratio_array(data=data,
                                                             index_numer=doa_array_index[os187],
                                                             index_denom=doa_array_index[re187])
        self.handle_all_data(extract_func=extract_func,
                             extract_filename="ism_%sdiv%s"%(os187,re187))
        self.handle_all_data(extract_func=extract_func,
                             extract_filename="ism_%sdiv%s"%(os187,re187)+"_decayed",
                             decayed_data=True)
        return

    def setup_extract_nsm(self):
        loa_keys = ["num_sn1a", "num_sn2", "num_nsm", "num_bhnsm"]
        loa_indeces = [self.get_data_index(key) for key in loa_keys]
        
        #extract single array with keys for all keys for all data
        for i,key in enumerate(loa_keys):
            extract_func = lambda data: self.extract_single_array(data=data, index_array=loa_indeces[i])
            self.handle_all_data(extract_func=extract_func,
                                 extract_filename=key)

        return

    def setup_extract_reos_donotconciderzeroyields(self):
        """ Extract all data for ISM-data of Re-187, Os-187 and Os-187/Re-187.
        Do not concider any file where Y_Re187 or Y_Os187 is zero"""
        re187 = "Re-187"
        os187 = "Os-187"
        loa_keys = [re187, os187]
        doa_array_string = {key: "ism_iso_%s"%key for key in loa_keys}
        doa_array_index = {key: self.get_data_index(doa_array_string[key]) for key in loa_keys}
        doa_filename = {key: "ism_%s"%key for key in loa_keys}

        #extract single-isotope ism-array from loa_keys
        for key in loa_keys:
            extract_func = lambda data: self.extract_single_array(data=data, index_array=doa_array_index[key])
            self.handle_all_data(extract_func=extract_func,
                                 extract_filename=doa_filename[key])
            self.handle_all_data(extract_func=extract_func,
                                 extract_filename=doa_filename[key]+"_decayed",
                                 decayed_data=True)

        #extract os-187/re187 ism-array
        extract_func = lambda data: self.extract_ratio_array(data=data,
                                                             index_numer=doa_array_index[os187],
                                                             index_denom=doa_array_index[re187])
        self.handle_all_data(extract_func=extract_func,
                             extract_filename="ism_%sdiv%s"%(os187,re187))
        self.handle_all_data(extract_func=extract_func,
                             extract_filename="ism_%sdiv%s"%(os187,re187)+"_decayed",
                             decayed_data=True)
        return

class Reduce(Extract):
    def __init__(self, dir_name):
        Extract.__init__(self, dir_name=dir_name)

    def __call__(self, nsm=False):
        if nsm:
            self.setup_reduce_nsm()
        else:
            self.setup_reduce_reos()
        return
    
    def get_extracted_filenames(self):
        #Get all numpy-filenames with "extract" in filenames and not decayed
        return self.get_numpy_filenames(trait="extract", untrait="There is no way this filename does exist")

    # def get_extracted_filenames(self):
    #     #Get all numpy-filenames with "extract" in filenames and not decayed
    #     return self.get_numpy_filenames(trait="extract", untrait="decayed")
    # def get_extracted_decayed_filenames(self):
    #     #Get all numpy-filenames with "decayed" in filenames
    #     return self.get_numpy_filenames(trait="decayed", untrait="There is no way this filename does exist")
    
    def get_timeevol(self, filename):
        #Get filename of "extracted data" return dictionary of arrays
        axis = 0
        time_array = self.get_time_array()
        data = np.load(filename)
        mean = np.mean(data, axis=axis)
        sigma = np.std(data, axis=axis)
        maximum = np.amax(data, axis=axis)
        minimum = np.amin(data, axis=axis)
        
        doa_arrays = {}
        doa_arrays["time"] = time_array
        doa_arrays["mean"] = mean
        doa_arrays["mean+sigma"] = mean + sigma
        doa_arrays["mean-sigma"] = mean - sigma
        doa_arrays["maximum"] = maximum
        doa_arrays["minimum"] = minimum
        
        return doa_arrays

    def get_hist(self, filename, loa_timepoints):
        """ Find closest indeces of time_array closest to timepoint,
        find the appropriate array in numpy_matrix,
        return array of values. """
        time_array = self.get_time_array()
        data = np.load(filename)
        doa_arrays = {}
        
        for timepoint in loa_timepoints:
            #find exact values
            if timepoint in time_array: 
                numpy_array = data[:,timepoint==time_array] #get values
                numpy_array = numpy_array.reshape(len(numpy_array)) #flatten to 1D
            #interpolate
            elif (timepoint>time_array[0]) and (timepoint<time_array[-1]): 
                broken_time_array = np.abs(time_array-timepoint)
                sorted_indeces = np.argsort(broken_time_array) #sorted indeces from timepoint
                interp_indeces = [sorted_indeces[0], sorted_indeces[1]] #indeces of time-array closest to timepoint
                lower_interp_index = min(interp_indeces)
                upper_interp_index = max(interp_indeces)
                
                lower_interp_time = time_array[lower_interp_index] #values of time-array closest to timepoint
                upper_interp_time = time_array[upper_interp_index]
                fraction_interp_time = (timepoint-lower_interp_time)/(upper_interp_time-lower_interp_time) #relative timejump between time-array and timepoint
                
                lower_interp_numpy_array = data[:,lower_interp_index] #values of numpy_matrix closest to timepoint
                upper_interp_numpy_array = data[:,upper_interp_index]
                delta_interp_numpy_array = (upper_interp_numpy_array-lower_interp_numpy_array)*fraction_interp_time #jump in numpy_matrix to timepoint
                
                numpy_array = lower_interp_numpy_array + delta_interp_numpy_array #interpolated array
                
            else:
                print "Extrapolation not considered! Fuck off!"
                print "timepoint", timepoint, time_array[0], time_array[-1]
                
            doa_arrays["t=%1.2fGyr"%(float(timepoint)/1.0e+9)] = numpy_array
    
        return doa_arrays

    def save_pandas(self, save_filename, dictionary):
        """ Save dictionary as panda-dataframe in csv"""
        save_filename = self.dir_string_func(self.save_dir) + "reduce_" + save_filename + ".csv"
        import pandas as pd
        pandaframe = pd.DataFrame(dictionary)
        pandaframe.to_csv(save_filename)
        print "Saving reduced PandasDataFrame to %s"%(save_filename)

        return
    
    def save_numpy(self, save_filename, dictionary):
        """ Save arrays from dictionary into numpy-matrix, store keys in txt-file"""
        save_filename = self.dir_string_func(self.save_dir) + "reduce_" + save_filename
        loa_arrays = []
        loa_index_key = []
        for i,key in enumerate(dictionary.keys()):
            loa_index_keys.append("%d %s"%(i, key))
            loa_arrays.append(dictionary[key])

        np.save(save_filename + ".npy",np.stack(loa_arrays))
        with open(save_filename + "_content.txt", 'w') as outfile:
            outfile.write("index array\n")
            outfile.write('\n'.join(loa_index_keys))

        return

    def setup_reduce_reos(self, loa_timepoints=[9.5e+9, 14e+9]):
        """ Get histograms and timevolutions for all the extracted datafiles. """
        loa_extracted_filenames = self.get_extracted_filenames()
        loa_extracted_filenames = [filename for filename in loa_extracted_filenames
                                   if "num" not in filename.split("/")[-1]]
        if len(loa_extracted_filenames) == 0:
            print "L320 Warning: no extracted filenames found"
        for extracted_filename in loa_extracted_filenames:
            #get relevant filename-section
            save_filename = extracted_filename.split("/")[-1]
            save_filename = save_filename[len("extract_"):]
            save_filename = save_filename[:-len(".npy")]
            
            timeevol_dict = self.get_timeevol(extracted_filename)
            self.save_pandas(save_filename + "_timeevol", timeevol_dict)
            hist_dict = self.get_hist(filename=extracted_filename, 
                                      loa_timepoints=loa_timepoints)
            self.save_pandas(save_filename + "_hist", hist_dict)
        return

    def setup_reduce_nsm(self):
        loa_extracted_filenames = self.get_extracted_filenames()
        loa_extracted_filenames = [filename for filename in loa_extracted_filenames
                                   if "num" in filename]
        for extracted_filename in loa_extracted_filenames:
            #get relevant filename-section
            save_filename = extracted_filename.split("/")[-1]
            save_filename = save_filename[len("extract_"):]
            save_filename = save_filename[:-len(".npy")]
            
            timeevol_dict = self.get_timeevol(extracted_filename)
            self.save_pandas(save_filename, timeevol_dict)
        return


class Decay(Extract):
    """ Class for adding cosmoradiogenic decay to data """
    def __init__(self, dir_name):
        Extract.__init__(self, dir_name=dir_name)

    def __call__(self):
        self.re187_cosmoradiogenic_decay()
        return

    def apply_decay(self, time_array, parent_array, daughter_array, halflife):
        """ Apply decay from parent to daughter with 
        the corresponding time-array and nuclear halflife.
        Halflife in same units as time_array. """

        decay_constant = np.log(2)/halflife

        for i in range(len(time_array)-1):
            #calculate time
            dt = time_array[i+1] - time_array[i]
            #calculate decay
            dN = - decay_constant * parent_array[i] * dt
            #apply decay to parent forall indeces greater then i
            parent_array[i+1:] += dN
            #same for daughter, but negative decay
            daughter_array[i+1:] -= dN

        return parent_array, daughter_array

    def re187_cosmoradiogenic_decay(self):
        """ For all datafiles, apply radioactive decay from Re-187 to Os-187. """
        halflife_re187 = 43.3e+9 #yr
        index_time = self.get_data_index("time")
        index_re187 = self.get_data_index("ism_iso_Re-187")
        index_os187 = self.get_data_index("ism_iso_Os-187")

        for datafilename in self.get_numpy_filenames():
            #load data as numpy 2D array
            data = np.load(datafilename)
            #get arrays from data
            time_array = data[index_time,:]
            re187_array = data[index_re187,:]
            os187_array = data[index_os187,:]
            new_re187_array, new_os187_array = self.apply_decay(time_array=time_array, parent_array=re187_array, daughter_array=os187_array, halflife=halflife_re187)
            data[index_re187,:] = new_re187_array
            data[index_os187,:] = new_os187_array
            
            new_datafilename = datafilename[:-len(".npy")] + "_decayed.npy"
            np.save(new_datafilename, data)
            print "Saving decayed data to %s"%(new_datafilename)

        return



def get_pid_from_filename(filename):
    if "pid" not in filename:
        return False
    #get string that follows 'pid'
    pid_string = filename.split("pid")[-1]
    #cut off string following first '_' or '.' or '/'
    pid_string = pid_string.split("_")[0]
    pid_string = pid_string.split(".")[0]
    pid_string = pid_string.split("/")[0]
    return int(pid_string)

def get_yhat(directory, pid, iso):
    #look for "parameter_files.dat" in directory
    param_filename = "parameter_files.dat"
    if directory[-1] != "/": directory = directory + "/"
    full_path = directory + param_filename
    #get contents of file
    with open(full_path, 'r') as infile:
        loa_contents = infile.readlines()
    #find index of 'iso' in header
    header = loa_contents.pop(0)
    header = header.split()
    if iso not in header:
        raise UserWarning("isotope, %s, cannot be found in parameter-header %s"%(iso, header))
    else:
        iso_index = header.index(iso)
    #find row of 'pid'
    found_pid = False
    for row in loa_contents:
        current_row = row.split()
        if int(current_row[0]) == pid:
            yhat = float(current_row[iso_index])
            found_pid = True
    if found_pid:
        return yhat
    else:
        raise UserWarning("pid %d could not be found in parameter_file %s"%(pid, full_path))


def complete_postprocessing(config_filename=False, directory_path=False,
                            decay=True, extraction=True, reduction=True, delete=False):
    """
    Choose Experiment-folder from config-file.
    Apply beta-decay to all data-files, SAVE AS '*_decayed.npy'!!
    Extract Re-Os-data from data-files and decayed-data-files, SAVE AS 'extract_..._.npy'
    Reduce extracted data to reasonable pandas-csv-files, save in experiment-folder and results-folder!

    delete-option: execute extraction, with suboption "do not consider files were Y_Re-187 or Y_Os-187 = 0"
    """

    if config_filename:
        config = cp.ConfigParser()
        config.read(config_filename)
        dir_data = config["montecarlo parameters"]["directory_name"]
    elif directory_path:
        dir_data = directory_path
    else:
        raise TypeError("Wrong use of keyword arguments!"+
                        "'config_filename' or 'directory_path' must be given!")
    print "Mucking around in directory: %s"%(dir_data)

    if decay:
        print "Applying decay"
        decay_instance = Decay(dir_name=dir_data) #make instance of decay-class
        decay_instance() #do the stuff for Re-Os

    if extraction:
        print "Applying extraction"
        extract_instance = Extract(dir_name=dir_data) #make instance of extract-class
        extract_instance.check_filename_level = 1 #check Y_hat(Re-187) and Y_hat(Os-187) from pid-in filename
        extract_instance() #do the stuff for Re-Os
        extract_instance(nsm=True)
        
    if reduction:
        print "Applying reduction"
        reduce_instance = Reduce(dir_name=dir_data) #make instance of reduce-class
        reduce_instance() #do the stuff for Re-Os
        reduce_instance(nsm=True)

        results_folder = Foldermap().hume_folder() + "latex/thesis/results/" + dir_data.split("/")[-1]
        print "Results-folder: %s"%(results_folder)
        try:
            os.mkdir(results_folder)
        except OSError: #folder already exists
            pass
        reduce_instance.set_save_dir(results_folder)
        reduce_instance()
        reduce_instance(nsm=True)

    return

if __name__ == '__main__':
    decay=False
    extraction=False
    reduction=True
    
    # config_filename = "../config_beehive_revised.ini"
    # complete_postprocessing(config_filename=config_filename,
    #                         decay=decay, extraction=extraction, reduction=reduction)
    # config_filename = "../config_beehive_revised_nsmtest.ini"
    # complete_postprocessing(config_filename=config_filename,
    #                         decay=decay, extraction=extraction, reduction=reduction)
    # config_filename = "../config_beehive_revised_delete.ini"
    # complete_postprocessing(config_filename=config_filename,
    #                         decay=decay, extraction=extraction, reduction=reduction,
    #                         delete=True)
    # config_filename = "../config_beehive_revised_imfslope.ini"
    # complete_postprocessing(config_filename=config_filename,
    #                         decay=decay, extraction=extraction, reduction=reduction,
    #                         delete=True)
    config_filename = "../config_beehive_revised_numnsm.ini"
    complete_postprocessing(config_filename=config_filename,
                            decay=decay, extraction=extraction, reduction=reduction,
                            delete=True)
