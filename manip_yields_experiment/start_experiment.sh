#!/usr/bin/env bash

index=0

n=500
sigma=0.5
folder="MC_run${index}_sigma${sigma}_${n}"
name="Omega_experiment_run${index}_sigma${sigma}"
readme="This_is_run#${index}_of_MC-variant_Omega_experiment"

filename="paralell_yield_experiment.py"
sigma_string=" -s ${sigma}"
folder_string=" -f $folder $name $readme"
arguments="${sigma_string} ${folder_string}"

#screen -dm -S experiment${index} python ${filename} ${arguments}
#screen python ${filename} ${arguments}
#echo screen -dm -S experiment${index} python ${filename} ${arguments}

python ${filename} ${arguments}
