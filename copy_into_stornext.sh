#!/bin/bash
#copy files from current working directory into 'stornext'
stornext_folder="/mn/stornext/d7/oyvinbsv/Master/"
echo "stornext folder: " $stornext_folder
loa_files=("bestfit_param_omega/__init__.py" "bestfit_param_omega/bestfit_file.py" "bestfit_param_omega/current_bestfit.py" "bestfit_param_omega/time_sfr_Shen_2015.txt" "manip_yields_experiment/experiment.py" "manip_yields_experiment/paralell_yield_experiment.py" "manip_yields_experiment/make_fudge_factor_table.py" "manip_yields_experiment/analyze_stddev.py")
loa_dirs=("bestfit_param_omega" "manip_yields_experiment")
dir_file="directory_master.py"

echo "Are you currently in home-folder on /hume? y/n"
echo "(usage: y for yes, n for no, f for yes, but new folders are required)"
read response
if [ $response = "y" ]; then
    echo "Okay, continuing!"
elif [ $response = "f" ]; then
    #Loop over all directories and copy them into 'stornext'
    for folder in "${loa_dirs[@]}"
    do
	echo "new folder" ${stornext_folder}$folder
	mkdir ${stornext_folder}${folder}
    done
elif [ $response = "n" ]; then
    echo "Well fine then, get on it!"
    exit
else
    echo "Unintelligble response, fuck off!"
    exit
fi

#Loop over all files and copy them into 'stornext'
for file in "${loa_files[@]}"
do
    cp ${file} ${stornext_folder}${file}
done

#copy 'directory_master.py' into /stornext/ and reinitialize if necessary
echo "Would you like to copy 'directory_master.py'?"
read response
if [ $response = "y" ]; then
    cp ${dir_file} ${stornext_folder}${dir_file}
    echo "Swapping to 'stornext'"
    cd ${stornext_folder}
    echo "Reinitializing 'directory_master.py'"
    python directory_master.py #re-initialize 'directory_master'
    bash #start a new BourneAgainSHell to get the python paths
fi
