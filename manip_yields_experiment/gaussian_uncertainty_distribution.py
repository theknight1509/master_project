"""
The purpose of this script is to run MonteCarlo simulations on 'experiment.py'
"""
#import vital libraries
import sys, os
#set global parameters

def start_experiment(folder_name, readme_text=""):
    """
    Function return True if succesful and False when something fails.
    """
    #Make sure script is called directly, from same folder
    if '/' in sys.argv[0]:
        print "The experiment has to be called directly"
        print "from the same directory"
        return False
    #Make folder for experiment if it does not exist
    if os.path.exists(folder_name): #folder already exist
        print "The suggested foldername already exist."
        return False
    os.mkdir(folder_name)
    #Initilize with a readme-file
    readme_path = folder_name + "/README.md"
    with open(readme_path, 'w') as readme:
        readme.write(folder_name + '\n')
        readme.write('='*len(folder_name) + '\n')
        readme.write('\n')
        if readme_text:
            readme.write(readme_text + '\n')
            readme.write('\n')
    if not os.path.exists(readme_path): #no readme-file
        print "README.md was not created"
        return False
    #Everything went alright so far
    return True

def gaussian_variate_experiment():
    
