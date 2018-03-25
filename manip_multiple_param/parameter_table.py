"""
Purpose:
Functions for writing and reading tables of randomly generated parameter-values.

Data-file format:
header - #index parameter-1 ... parameter-n 
datarow - index-number value-1 ... value-2
"""

### Generating and writing data to file ###
def make_table(filename, loa_parameter_tuples, N):
    """
    kwd_args:
    filename - name of table to write data to.
    loa_parameter_tuples - list with parameter-tuples
    N - number of rows to write

    shape of parameter-tuples - (param-name, mean-val, stddev-val)
    """
    import random as rn #random number generator
    #Make variables with indeces of parameter-tuples
    index_param = 0; index_mean = 1; index_stddev = 2
    #data string format function
    data_string = lambda val: "%1.4e "%val
    #make dict with (empty) lists of all randomly generated values
    doa_loa_generated_values = {tup[index_param]:[] for tup in loa_parameter_tuples}
    
    #Write new file
    with open(filename, 'w') as outfile:
        #write header from 'loa_parameters'
        header = "#index " + " ".join([tup[index_param] for tup in loa_parameter_tuples])
        outfile.write(header + "\n")
        #loop over all rows, index 1->'N'
        for row_index in range(1,N+1):
            #make data-string to write to row
            row_string = "%d "%row_index
            #loop over all parameter-tuples
            for parameter, mean, stddev in loa_parameter_tuples:
                #generate a random number from gaussian dist.
                random_val = rn.gauss(mean, stddev)
                #save random number to data-string and data-dict
                row_string += data_string(random_val)
                doa_loa_generated_values[parameter].append(random_val)
            #write data-string to file
            outfile.write(row_string + "\n")
    
    return doa_loa_generated_values

### Reading data from file ###
def read_table(filename, index):
    """ Open file, retrieve parameter-names from row zero, 
    and values from row index. """

    #get all data as string
    with open(filename, 'r') as infile:
        loa_content = infile.read()
    #split content by new-line chars and remove empty strings
    loa_content = list(filter(None, loa_content.split('\n')))

    #get row zero and index as strings
    row_0 = loa_content[0]
    row_i = loa_content[index]
    
    #check index of row-i
    first_elem = int(row_i.split(' ')[0]) 
    if (first_elem != index):
        print "Error! Indeces of data-file do not match"
        print "Index drawn: %d Index stored: %d"%(index, first_elem)
        return False

    #turn rows into appropriate lists
    row_0 = row_0.split()[1:] #split by WS and remove first elem
    row_i = row_i.split()[1:] #split by WS and remove first elem
    row_i = [float(elem) for elem in row_i] #turn to float

    loa_parameter_tuples = zip(row_0, row_i)
    return loa_parameter_tuples

if __name__ == '__main__':
    import sys
    print "Test of '%s'\n"%sys.argv[0]
    print "Return from 'make_table'"
    print make_table("test_table", [("test1",0,1.0),
                                    ("test2",0,1.0)], 5)
    print "Return from 'read_table' index 3"
    print read_table("test_table", 3)
