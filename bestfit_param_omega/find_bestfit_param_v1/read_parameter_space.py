"""
Purpose:
Open parameter_space.txt
-> read the desired variable
-> return list of values and name_of_image

This piece of code is designed to be be 
executed/imported in the same directory it exists;
'find_bestfit_param_v1/'
"""
plot_dir = "variable_plots/"

def read_param(variable):
    """ """
    filename = "parameter_space.txt"
    
    #get all lines from data-file
    with open(filename) as infile:
        loa_lines = infile.readlines()

    #loop through lines to get correct line(except variable)
    for line in loa_lines:
        if line.split()[0] == variable:
            correct_line = line.split()[1:] #remove variable
            break

    try:
        #find image_name and list of values
        image_name = correct_line.pop(-1)
        loa_value_str = correct_line #list of all values as strings
        loa_value_flt = [float(val) for val in loa_value_str] #floats
        return loa_value_flt, image_name
    except:
        print "Error in finding parameter"
        return False

if __name__ == '__main__':
    print "test of read_parameter_space.read_param()"
    for var in ["mgal"]:
        outstring = "variable: %s"%var
        loa_val, img_str = read_param(var)
        outstring += '\t' + "image_name: %s"%img_str
        outstring += '\t' + "values: %s"%loa_val
        print outstring
