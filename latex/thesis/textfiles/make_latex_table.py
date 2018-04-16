#!/usr/bin/python3
from tabulate import tabulate

def get_content(filename):
    nested_content_list = []
    with open(filename, 'r') as infile:
        for line in infile.readlines():
            nested_content_list.append(line.split())
    return nested_content_list

def write_table(filename, nested_content_list):
    latex_table = tabulate(nested_content_list, headers='firstrow', tablefmt='latex_raw')
    with open(filename, 'w') as outfile:
        outfile.write(latex_table)
    print("Writing table to file: %s"%(filename))
    print(latex_table)
    return

def add_relsigma_to_table(nested_content_list):
    """ Assume that table is column of index, mean value, min value, max value.
    Calculate standard deviation (min/max - mean)/mean for min and max."""
    new_columns = ["$\sigma_{lower}$", "$\sigma_{upper}$"]
    sigma = lambda dev, mean: (float(dev)-float(mean))/(float(mean))
    
    #loop over all rows
    for i, row in enumerate(nested_content_list):
        if i == 0: #header
            additional_column_elements = new_columns
        else: #value row
            index, mean_val, min_val, max_val = tuple(row)
            sigma_low = str(sigma(min_val, mean_val))
            sigma_up = str(sigma(max_val, mean_val))
            additional_column_elements = [sigma_low, sigma_up]
        nested_content_list[i] = row + additional_column_elements
    return nested_content_list

def main_arnould_table():
    filename = "arnould_table"
    loa_content = get_content(filename + ".dat")
    loa_content = add_relsigma_to_table(loa_content) 
    write_table("../texfiles/" + filename + '.tex', loa_content)
    return 

if __name__ == '__main__':
    main_arnould_table()
