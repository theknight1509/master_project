"""
Make a function to load the hypatia tsv-file
"""

def load_hypatia(filename="hypatia-10012018.tsv"):
    with open(filename, 'r') as infile:
        header = infile.readline().split()
        fe_index = header.index("Fe")
        eu_index = header.index("Eu")
        eu2_index = header.index("EuII")

        #lists of matching coordinates; Fe-Eu, Fe-Eu2
        fe_list = []; fe2_list = []
        eu_list = []; eu2_list = []

        #loop over all lines
        for line in infile.readlines():
            row = line.split()
            #make sure there is data
            if not len(row) > eu_index:
                continue
            #add Fe-Eu point
            fe_list.append( float(row[fe_index]) )
            eu_list.append( float(row[eu_index]) )
            #add Fe-EuII point if it exists
            if len(row) > eu2_index:
                fe2_list.append( float(row[fe_index]) )
                eu2_list.append( float(row[eu_index]) )

        return fe_list, eu_list, fe2_list, eu2_list

if __name__ == '__main__':
    #test function
    list1, list2, list3, list4 = load_hypatia()
    print "This is a test of 'load_hypatia()'"
    print "length of first list: ", len(list1)
    print "length of second list: ", len(list2)
    print "length of third list: ", len(list3)
    print "length of fourth list: ", len(list4)
