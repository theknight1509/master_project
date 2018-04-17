#!/usr/bin/python3
from tabulate import tabulate

def get_content(filename):
    nested_content_list = []
    with open(filename, 'r') as infile:
        for line in infile.readlines():
            nested_content_list.append(line.split())
    return nested_content_list

def write_table(filename, nested_content_list,
                printer=False, tablefmt='latex_raw'):
    latex_table = tabulate(nested_content_list, headers='firstrow',
                           tablefmt=tablefmt)
    with open(filename, 'w') as outfile:
        outfile.write(latex_table)
    if printer:
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
            sigma_low = "%1.4f"%(sigma(min_val, mean_val))
            sigma_up = "%1.4f"%(sigma(max_val, mean_val))
            additional_column_elements = [sigma_low, sigma_up]
        nested_content_list[i] = row + additional_column_elements
    return nested_content_list

def get_sigma_from_table(filename):
    #get index 0, -1, -2 for all rows except header
    
    loa_keys = ["iso", "s_lower", "s_upper"]
    loa_indeces = [0,-2,-1]
    doa_indeces = {key:index for key, index in zip(loa_keys, loa_indeces)}
    doa_lists = {key:[] for key in loa_keys}

    #sort into dictionary
    nested_content_list = get_content(filename)
    for row in nested_content_list[1:]:
        for key in loa_keys:
            table_element = row[doa_indeces[key]]
            try: table_element = float(table_element)
            except: pass
            doa_lists[key].append(table_element)

    #make loa_tuple option
    tuple_key = "tuple-list"
    doa_lists[tuple_key] = []
    for iso, s_lower, s_upper in zip(doa_lists[loa_keys[0]], doa_lists[loa_keys[1]], doa_lists[loa_keys[2]]):
        doa_lists[tuple_key].append((iso, s_lower, s_upper))

    return doa_lists

def main_arnould_table():
    filename = "arnould_table"
    loa_content = get_content(filename + ".dat")
    filename += "_modified"
    loa_content = add_relsigma_to_table(loa_content) 
    write_table("../texfiles/" + filename + '.tex', loa_content, printer=True)
    write_table(filename + '.dat', loa_content, printer=True, tablefmt="plain")
    return

if __name__ == '__main__':
    main_arnould_table()
    #print(get_sigma_from_table("arnould_table_modified.dat"))
