"""
Purpose:
Test different values for constant timestep size.
Use two different omega-models; The original with default params,
and the new model with eris bestfit parameters.
Write the result to file: 'test_const_dt.dat'
"""
### Import modules ###
import sys
#import "new-omega" model
from bestfit_param_omega import current_bestfit as cbf
from bestfit_param_omega.omega_new import omega_new
#import "old-omega" model
from omega import omega

def test_timestep(timestepsize):
    """
    For a given length of timestep; test both default omega (old),
    and new omega. 
    Return the result as strings:
    HOW DOES STRINGS APPEAR??
    """
    #allocate resulting strings
    result_old = ""
    result_new = ""
    
    #calculate result for 'old' omega
    try:
        O_obj = omega(dt=timestepsize, special_timesteps=0)
        n_steps = len(O_obj.history.age)
        time_string = O_obj._gettime()
    except IndexError: #same old error, cannot create timestep-list
        result_old += "IndexError"
    except: #Some other error
        result_old += "Unknown Error"
    else: #Did not fail
        result_old += "Success! %d timesteps %s"%(n_steps, time_string)

    #calculate result for 'new' omega
    try:
        cbf.bestfit_special_timesteps = 0
        cbf.bestfit_dt = timestepsize
        O_obj = omega_new(cbf)
        n_steps = len(O_obj.history.age)
        time_string = O_obj._gettime()
    except IndexError: #same old error, cannot create timestep-list
        result_new += "IndexError"
    except: #Some other error
        result_new += "Unknown Error"
    else: #Did not fail
        result_new += "Success! %d timesteps %s"%(n_steps, time_string)

    return result_old, result_new

def save_table_datafile(loa_data_strings, filename):
    with open(filename+".dat", 'w') as outfile:
        for line in loa_data_strings:
            outfile.write(line + '\n')
    return

def save_table_markdown(loa_data_strings, filename):
    sep = "|" #markdown table separator
    #fetch header from first element in list
    header = loa_data_strings.pop(0)
    n_comma = header.count(",")
    header = sep + sep.join(header.split(",")) + sep
    #make row (horizontal line) that separates header from table
    horiz = "---".join([sep]*(n_comma+2))
    with open(filename+".md", 'w') as outfile:
        outfile.write(header + '\n')
        outfile.write(horiz + '\n')
        for line in loa_data_strings:
            #replace strings with markdown-separator
            modified_line = sep + sep.join(line.split(",")) + sep
            outfile.write(modified_line + '\n')
    return

def save_table_latex(loa_data_string, filename):
    latex_col_sep = r" & "
    latex_row_sep = r" \\"
    hline = r"\hline"
    #fetch header from first element in list
    header = loa_data_strings.pop(0)
    n_comma = header.count(",")
    header = hline + '\n' + \
             r"$" + \
             (r"$"+latex_col_sep+r"$").join(header.split(",")) + \
             r"$" + latex_row_sep
    #make row (horizontal line) that separates header from table
    horiz = r"\hline"
    with open(filename+".tex", 'w') as outfile:
        outfile.write(header + '\n')
        outfile.write(horiz + '\n')
        for line in loa_data_strings:
            modified_line = latex_col_sep.join(line.split(",")) \
                            + latex_row_sep
            outfile.write(modified_line + '\n')
    return


if __name__ == '__main__':
    #Add computer string to filenames
    comp_string = raw_input("Which computer are you on?")
    #remove whitespace, add underscore
    comp_string = "_" + "".join(comp_string.split(" "))

    #Find minimum exponent
    min_exponent = int(input("What is the minimum exponent?"))
    
    #make steplengths between 10^5 and 10^10 years
    loa_constdt_values = []
    for exponent in range(min_exponent, 10)[::-1]:
        step = int(10**exponent)
        start = step
        stop = int(10**(exponent+1))
        loa_constdt_values += range(start,stop, step)

    #loop over constant timesteps
    loa_data_strings = ["dt, default-omega result, bestfit-omega result"]
    for i,constdt in enumerate(loa_constdt_values):
        print "Number %d, timesteplength %1.0e yr"%(i,constdt)
        result_old, result_new = test_timestep(constdt)
        data_tuple = (constdt, result_old, result_new)
        data_string = "%1.0e, %s, %s"%data_tuple
        loa_data_strings.append(data_string)

    #save data into table-files
    filename = sys.argv[0].split(".")[0] #use self-filename
    filename = filename + comp_string
    save_table_datafile(list(loa_data_strings), filename)
    save_table_markdown(list(loa_data_strings), filename)
    save_table_latex(list(loa_data_strings), filename)
