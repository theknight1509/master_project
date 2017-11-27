"""
Calculate the mean, median, 1 sigma, 2 sigma, and default array of a specific array from a data-folder.
"""
#import statements and global varaibles
import os, sys
import numpy as np
from directory_master import Foldermap
folder = Foldermap()
default_filename_postamble = "default.npy" #Final string of default-datafile-name
index_filename = "data_indeces.txt"

loa_contents = os.listdir('.')
loa_folders = []
for content in loa_contents: #loop over all strings in cwd
    if not ('.' in content): #string is not a filename, but folder
        loa_folders.append(content)

#find folder name
print "Current available folders: ", dict(enumerate(loa_folders))
response = raw_input("What folder would you like to choose? (full path or index)")
try:
    #is response the index of folder-list?
    response = int(response)
    input_index = response
    input_datafolder = loa_folders[response]
except ValueError: 
    #the response cannot be integer, full path is given
    input_datafolder = response
    input_index = loa_folders.index(input_datafolder)
    #check that folder exist in list
    if not (input_datafolder in loa_folders):
        print "Folder: %s not available"%(input_datafolder)
        sys.exit("Exiting!")
except IndexError:
    #index is out of range of folder-list
    print "Index: %d is not available"%response
    sys.exit("Exiting!")

#choose array
array_name = "ism_iso_Re-187"
print "Using the %s arrays for analysis"%array_name

#find index of array from file in folder
array_index = False
with open(input_datafolder + '/' + index_filename, 'r') as index_file:
    for line in index_file.readlines():
        if line.split()[1] == array_name:
            array_index = line.split()[0]
            break
if not array_index: #index was not found
    print "Index of %s was not found"%array_name
    sys.exit("Exiting!")

#find default filename from known postamble
loa_filenames = os.listdir(input_datafolder)
for filename in loa_filenames:
    if (filename[-len(default_filename_postamble):] == default_filename_postamble):
        #Found default-file (fudgefactor=1) get generic data-file name and default-file name
        default_filename = filename #full name of datafile with fudgefactor=1
        data_filename = filename[:-len(default_filename_postamble)] #generic data-path
        break

#get shape and array from default experiment
data_matrix_default = np.load(input_datafolder + '/' + default_filename)
default_shape = data_matrix_default.shape
num_arrays = default_shape[0]
num_timepoints = default_shape[1]
default_array = np.copy(data_matrix_default[array_index,:])
#get number of experiments from README
readmestring = "Number of experiments:"
readmefilename = input_datafolder + "/README.md"
with open(readmefilename, 'r') as readmefile:
    for line in readmefile.readlines():
        if line[:len(readmestring)] == readmestring:
            num_experiments = int(line[len(readmestring):])

#Make empty array to fill with all values
data_matrix_arrays = np.zeros((num_experiments,num_timepoints)) #collection of arrays wanted

#Go through all data files
for i in range(num_experiments):
    data_matrix = np.load(input_datafolder + '/' + data_filename + str(i) + '.npy') #collection of all arrays from calculation
    data_matrix_arrays[i,:] = data_matrix[array_index,:] #store wanted array from one simulation

#get median, mean, and sigma from data_matrix
data_mean = np.mean(data_matrix_arrays, axis=0)
data_median = np.median(data_matrix_arrays, axis=0)
data_sigma = np.std(data_matrix_arrays, axis=0)
data_2sigma = 2*data_sigma

#make matrix of all processed arrays
relevant_arrays = [default_array, data_mean, data_median, data_sigma, data_2sigma]
all_relevant_arrays = np.zeros((len(relevant_arrays), num_timepoints))
for i in range(len(relevant_arrays)):
    all_relevant_arrays[i,:] = relevant_arrays[i]

#save numpy matrix in folder with same filename as data-files and new suffix
filename_stddev = input_datafolder + "/" + data_filename + "_stddev.npy"
np.save(filename_stddev, all_relevant_arrays)
if raw_input("Would you like to store results in /hume/? y/n") == "y":
    result_folder = folder.hume_folder() + "results/"
    filename_stddev = result_folder + data_filename + "_stddev%d.npy"%input_index
    np.save(filename_stddev, all_relevant_arrays)

#add comment regarding analysis in README
with open(input_datafolder + '/README.md', 'a') as readmefile:
    readmefile.write('\n')
    readmefile.write("Analyzed " + input_datafolder + '\n')
    readmefile.write("file consists of one %s array with the following arrays:"%(all_relevant_arrays.shape,) + '\n')
    readmefile.write("* Default array (No fudge factor) for " + array_name + '\n')
    readmefile.write("* Mean value for " + array_name + '\n')
    readmefile.write("* Median value for " + array_name + '\n')
    readmefile.write("* one sigma value for " + array_name + '\n')
    readmefile.write("* two sigma value for " + array_name + '\n')
