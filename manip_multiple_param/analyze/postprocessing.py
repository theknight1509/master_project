#!/usr/bin/python2.7
"""
Class and function for extracting data from 
sea of data-files in experiment-folders.
"""
import os
import numpy as np

class Extract(object):
    def __init__(self, dir_name):
        self.dir_string_func = lambda dir_name: dir_name if (dir_name[-1]=="/") else dir_name + "/"
        self.data_index_filename = self.dir_string_func(dir_name) + "data_indeces.txt"

        self.get_dir = dir_name
        self.save_dir = dir_name

    def __call__(self):
        self.setup_extract_reos()
        return

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
        
    def get_numpy_filenames(self, trait="pid"):
        """ Loop over all filenames, compile list with filenames that have:
        '.npy' and trait in the filename."""
        loa_filenames = os.listdir(self.get_dir)
        loa_numpy_filenames = [self.dir_string_func(self.get_dir) + filename
                               for filename in loa_filenames
                               if ('.npy' in filename) and (trait in filename)]
        return loa_numpy_filenames

    def handle_all_data(self, extract_func, extract_filename):
        """ Loop over all numpy arrays and extract array according to 
        function in keyword-arguments.
        'extract_func' - must take numpy matrix and return single array
        """
        loa_extracted_arrays = []
        for data_filename in self.get_numpy_filenames(): #loop over numpy-files
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
        """ Extract all data for ISM-data of Re-187, Os-187 and Re-187/Os-187."""
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
        #extract re187/os-187 ism-array
        extract_func = lambda data: self.extract_ratio_array(data=data,
                                                        index_numer=doa_array_index[re187],
                                                        index_denom=doa_array_index[re187])
        self.handle_all_data(extract_func=extract_func,
                             extract_filename="ism_%sdiv%s"%(re187,os187))
        return


class Reduce(Extract):
    def __init__(self, dir_name):
        Extract.__init__(self, dir_name=dir_name)

    def __call__(self):
        self.setup_reduce_reos()
        return
    
    def get_extracted_filenames(self):
        #Get all numpy-filenames with "extract" in filenames
        return self.get_numpy_filenames(trait="extract")
    
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

if __name__ == '__main__':
    import configparser as cp
    config_filename = "../config_beehive_revised.ini"
    config = cp.ConfigParser()
    config.read(config_filename)
    subdir_name = config["montecarlo parameters"]["directory_name"]
    print "Mucking around in directory: %s"%(subdir_name)
    
    extract_instance = Extract(dir_name=subdir_name) #make instance of extract-class
    extract_instance() #do the stuff for Re-Os
    print "Succesfully extracted!"

    reduce_instance = Reduce(dir_name=subdir_name) #make instance of reduce-class
    reduce_instance() #do the stuff for Re-Os
    print "Succesfully reduced!"