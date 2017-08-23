""" directory.py
How to use:
Run this program from the terminal, 
to calibrate the directory-location and add the pythonpath to '.bashrc'-file

Description:

class Foldermap - Contains all the relevant folders to be used in this module
calibrate() - Checks current location and adds the cwd inside the script
add_path2pythonpath() - Adds cwd to '.bashrc'-file
insert_into_self() - Adds a piece of string, between two other strings to itself.
"""
import sys
import os

path_of_folder = "" #create variable that eventually will be filled
selfname = sys.argv[0]# "directory.py" #sys.argv[0]?? #name of this script

class Foldermap:
    def __init__(self):
        self.main_folder = path_of_folder #global string

        self.write_summerproject_folders()
        self.write_latex_folders()
        
    def __call__(self):
        return self.main_folder
    
    def write_latex_folders(self):
        self.latex = self.main_folder + "latex/"
        
    def write_summerproject_folders(self):
        self.summerproject = self.main_folder + "../Summer_project/"

        self.nupycee = self.summer_project + "NuPyCEE/"
        
        self.eris_folder = self.summerproject + "reproduce_shen/"
        self.eris_sfgas = self.eris_folder \
                          + "Eris_hostSFgas_aveZ.dat"
        self.eris_sfr = self.eris_folder \
                        + "L90Mpc8000_hithres.00400.sfr_time.grp01"
        self.eris_nsm = self.eris_folder \
                        + "NSmergers_per_timestep_delay100Myr_idx1p0_yield0p05.dat"
        
    def test(self):
        """ Write a meaningful set of tests for 'Foldermap' here."""
        None
        
def insert_into_self(text, start_marker="### START PYTHONMARKER ###",
                     end_marker="### END PYTHONMARKER ###"):
    """
    Description: Open 'directory.py' and insert 'text' between
    the lines 'start_marker' and 'end_marker'. 
    Forcibly add '\n'-characters after every line of
    'start_marker', 'text', and 'end_marker'.
    Please don't kill me!
    """
    
    #read all content from selfname(global str) into string
    with open(selfname, 'r') as selffile:
        content = ""
        reached_start_marker = False
        reached_end_marker = False
        """
        Define three regions in self-file ('directory.py')
        (reached_start_marker == False) and (reached_end_marker == False):
        --- the current line is before the start_marker
        --- check if current line is start_marker
        --- insert current line into content
        (reached_start_marker == True) and (reached_end_marker == False):
        --- the current line is between the markers
        --- check if current line is end_marker
        (reached_start_marker == True) and (reached_end_marker == True):
        --- the current line is after the end_marker
        --- add the current line to content
        """
        for current_line in selffile.readlines(): #loop over all lines
            if (not reached_start_marker) and (not reached_end_marker):
                if current_line[0:len(start_marker)] == start_marker:
                    #found the start_marker! woohoo!
                    #print "found the start_marker! woohoo!"
                    reached_start_marker = True
                    #write marker and all desired text to content
                    content += current_line
                    content += text + '\n'
                else:
                    #read current_line to content
                    content += current_line
            elif (reached_start_marker) and (not reached_end_marker):
                if current_line[0:len(end_marker)] == end_marker:
                    #found the end_marker! woohoo!
                    #print "found the end_marker! woohoo!"
                    reached_end_marker = True
                    #write the marker to content
                    content += current_line
                else:
                    #skip this line, go to next
                    continue
            elif (reached_start_marker) and (reached_end_marker):
                content += current_line

    #Write new content to a new file with the same name
    with open(selfname, 'w+') as selffile:
        selffile.write(content)
        
def calibrate(test=False):
    """
    Use os.getcwd() to find path of folder.
    Write path to local variable.
    """
    local_dir = os.getcwd()
    storage_string = lambda path_string: "path_of_folder = '%s/'"%path_string
    insert_into_self(storage_string(local_dir))
    if test:
        return path_of_folder

def add_path2pythonpath():
    #Write the path of the current folder to pythonpath in the bashrc-script.
    #NOTE! only do so if the string doesn't exist already!

    pythonpath_string = "export PYTHONPATH=$PYTHONPATH:"+os.getcwd()+"\n"
    bashrc_path = "/home/oyvind/.bashrc"

    #look if string already exists in .bashrc
    with open(bashrc_path, "r") as bashfile_read:
        for line in bashfile_read.readlines():
            if line == pythonpath_string: #the pythonpath_line exists
                print "Pythonpath for cwd already exist in .bashrc"
                return False
    #since path does not exist, append string to end of .bashrc
    with open(bashrc_path, "a") as bashfile_app:
        bashfile_app.write(pythonpath_string)
        return True
    
### START PYTHONMARKER ###
path_of_folder = '/home/oyvind/github_uio/Master/'
### END PYTHONMARKER ###

if __name__ == '__main__':
    #if 'directory.py' is called from the correct folder...
    if selfname in os.listdir(os.getcwd()):
        #calibrate the path_of_folder variable
        calibrate()
        add_path2pythonpath()
    #otherwise; reason and quit
    else:
        print "Program must be called directly! No relative paths"
        sys.exit("Exiting!")

    if len(sys.argv) >= 2:
        if sys.argv[1] == "test":
            #test 'insert into self()' and 'calibrate()'
            insert_into_self("#THIS IS SKYNET")
            print calibrate(test=True)

    print "Current path saved to file: ", path_of_folder
