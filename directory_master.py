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

#set global parameters
path_of_folder = "" #create variable that eventually will be filled by current dir
path_of_nupycee = "" #create variable that eventually will be filled by nupyee-dir

selfname = sys.argv[0]# "directory.py" #sys.argv[0]?? #name of this script
current_dir = os.getcwd() #the full path of the current dir
home_dir = os.path.expanduser("~") #full path of home dir

class Foldermap:
    def __init__(self):
        self.main_folder = path_of_folder #global string
        self.nupycee = path_of_nupycee #global_string

        self.write_latex_folders()
        self.write_bestfit_folders()
        self.write_sfh_file()
        
    def __call__(self):
        self.call_bool = True
        return self.main_folder
    
    def write_latex_folders(self):
        self.latex_bool = True
        self.latex = self.main_folder + "latex/"

    def write_bestfit_folders(self):
        self.bestfit_bool = True
        self.bestfit = self.main_folder \
                       + "bestfit_param_omega/"
    def write_sfh_file(self):
        self.eris_sfh_file = self.bestfit \
                             + "time_sfr_Shen_2015.txt"

    def activate_environ(self):
        #add full path to os.environ (minus the last backslash)
        os.environ['SYGMADIR'] = self.nupycee[:-1]

        #add NuPyCEE-dir to pythonpath
        sys.path.append(self.nupycee[:-1])

    def hume_folder(self):
        full_path = "/uio/hume/student-u27/oyvinbsv/github_uio/Master/"
        return full_path
    
    def stornext_folder(self):
        full_path = "/mn/stornext/d7/oyvinbsv/"
        return full_path

def calibrate():
    """
    Write path of current dir to local variable.
    Look for NuPyCEE-path...
    if found; write path to local variable
    if not found; print error message, with instructions on how to get NuPyCEE
    """
    #function for turning var-name and path-string to string
    storage_string = lambda path_string, var_string: \
                     "%s = '%s/'"%(var_string, path_string)

    insert_string = "" #string to inserted into self-file

    #write current dir to local_var
    insert_string += storage_string(current_dir, "path_of_folder")
    
    #write NuPyCEE dir to local var
    nupycee_name = "NuPyCEE"
    nupycee_folder = find_folder(nupycee_name)
    if nupycee_folder: #nupycee-dir was found
        insert_string += '\n'
        insert_string += storage_string(nupycee_folder, "path_of_nupycee") #insert nupycee-folder
    else: #nupycee-dir was not found
        print "'%s'-directory was not found in HOME-dir or any sub-folder"%nupycee_name
        print "directory can be download with the command;"
        print "git clone https://github.com/NuGrid/NuPyCEE.git"

    #Perform insertion into self-file
    insert_into_self(insert_string) #write insert-string to self-file

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

def find_folder(folder_name):
    """
    USE WITH DISCRESSION!
    Try all home-directories, walk thrugh all directories,
    return full path of folder with folder_name
    """
    full_path = ""
    for root, dirs, files in os.walk(home_dir):
        print "searching for '%s': "%folder_name, root
        current_path = root.split('/') #path of current dir in os.walk
        if folder_name == current_path[-1]: #found full path of folder_name
            full_path = root
            break
    if full_path: #var is not empty and path was found
        return full_path
    else:
        print "'%s' was not found"%folder_name
        return False

def add_path2pythonpath():
    #Write the path of the current folder to pythonpath in the bashrc-script.
    #NOTE! only do so if the string doesn't exist already!    
    pythonpath_string = "export PYTHONPATH=$PYTHONPATH:"+current_dir+"\n"
    bashrc_path = home_dir + "/.bashrc"

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
path_of_nupycee = '/home/oyvind/github_uio/NuPyCEE/'
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
