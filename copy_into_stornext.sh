#!/bin/bash
#copy files from current working directory into 'stornext'
stornext_folder="/mn/stornext/d7/oyvinbsv/Master/"
loa_files=( "directory_master.py" "bestfit_param_omega/__init__.py" "bestfit_param_omega/bestfit_file.py" "bestfit_param_omega/current_bestfit.py" "bestfit_param_omega/time_sfr_Shen_2015.txt" "manip_yields_experiment/experiment.py" "manip_yields_experiment/paralell_yield_experiment.py")

echo "Are you currently in home-folder on /hume? y/n"
read response
if [ $response = "y" ]; then
    continue
elif [ $response = "n" ]; then
    echo "Well fine then, get on it!"
    exit
else
    echo "Unintelligble response, fuck off!"
    exit
fi

#Loop over all files and copy them into 'stornext'
for file in "$loa_files[@]"
do
    cp ${file} ${stornext_folder}${file}
done

#change directory, and reinitialize directory_master
cd stornext_folder
python directory_master.py

#change directory back?
