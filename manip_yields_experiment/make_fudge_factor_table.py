"""
Generate a *number* of gaussian fudge-factor 
values around 1.0 with a *sigma* standard-deviation.
Also index the randomly generated numbers.
"""
import random as rd

### Function for writing data ###
def write_single_line(filename, index_value_tuple=()):
    if not index_value_tuple: #empty tuple
        #open file for the first time
        with open(filename, 'w') as outfile:
            #write first indexing line of datafile
            outstring = "#index value \n"
            outfile.write(outstring)
    else:
        #open file and append new line of data
        with open(filename, 'a') as outfile:
            #write tuple to datafile
            outstring = "%d %1.10e \n"%index_value_tuple
            outfile.write(outstring)

### Function for writing a new table ###
def write_new_table(filename, num_factors, sigma):
    #Reset file by writing first line
    write_single_line(filename)

    #loop over all indexes, pull random number
    for i in range(num_factors):
        random_value = rd.gauss(1.0, sigma)
        write_single_line(filename, (i, random_value))

### Function for reading appropriate value ###
def read_fudge_factor(filename, req_index=0):
    """
    Open a datafile with indeces and fudgefactors, 
    return the value corresponding to *req_index*.
    """
    filename = "fudge_factor_table.dat" #name of table
    req_value = False #value of requested index
    with open(filename, 'r') as infile:
        for line in infile.readlines():
            try:
                read_index, read_val = line.split()
            except: #possible errors include wrong format of line
                continue
            if read_index == str(req_index):
                req_value = float(read_val)
                break
    return req_value

""" Do not yet know how to implement cmd-line arguments
### Take cmd-line arguments ###

### Set global parameters ###
datafilename = "fudge_factor_table.dat"
n = 10 #ten randomly generated values
sigma = 0.1 #ten percent standard deviation
"""
