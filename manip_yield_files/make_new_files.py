def make_new_file(input_filename, output_filename,
                  isotope_name, fraction):
    """
    Open file with name 'input_filename', multiply 'isotope_name'
    with 'fraction' and store in file with name 'output_filename'.
    """
    with open(input_filename, 'r') as infile:
        loa_lines = []
        num_isos_found = 0
        while True: #loop endlessly
            line = infile.readline() #read next line in file
            words = line.split()
            if not line: #line is empty -> file is empty
                break #stop looping NOW!
            elif words[0][1:] == isotope_name:
                #manipulate second_word
                second_word = words[1]
                preamble_second_word = second_word[0]
                second_word = float(second_word[1:])
                second_word *= fraction
                second_word = preamble_second_word + str(second_word)
                #store second word as line again
                line = words[0] + ' ' + second_word + '\n'
                num_isos_found += 1
            else:
                None
            loa_lines.append(line)
        print "%d number of correct matches for %s in file: %s"%(num_isos_found, isotope_name, input_filename)
        
    with open(output_filename, 'w') as outfile:
        for line in loa_lines:
            outfile.write(line)

if __name__ == '__main__':
    #test funciton 'make_new_file' on local copy of r-process table
    iso = "Eu-151"
    scale_factor = (1.2, "p20percent")
    filename = "r_process_rosswog_2014_copy.txt"
    correction =  filename.split('.')
    correction.insert(1,'_'+str(iso)+scale_factor[1]+'.')
    new_filename = ''.join(correction)
    
    make_new_file(filename, new_filename, iso, scale_factor[0])
