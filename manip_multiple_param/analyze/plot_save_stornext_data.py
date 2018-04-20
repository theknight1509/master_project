"""
Go through /stornext/-directories and plot various data-sets
with mean + regions and such.
Decide which data is to be stored in /results/
"""
from directory_master import Foldermap

#Get relevant directory-names for uio-systems
folder_instance = Foldermap()
dir_stornext = folder_instance.stornext_folder()
dir_hume = folder_instance.hume_folder()
