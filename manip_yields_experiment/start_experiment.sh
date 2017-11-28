#!/usr/bin/env bash

#experiment-index
index=0

#parameters
n=500
sigma=0.5
folder="MC_run${index}_sigma${sigma}_${n}"
name="Omega_experiment_run${index}_sigma${sigma}"
readme="This_is_run#${index}_of_MC-variant_Omega_experiment"

#python-call parameters
filename="paralell_yield_experiment.py"
sigma_string=" -s ${sigma}"
folder_string=" -f $folder $name $readme"
arguments="${sigma_string} ${folder_string}"

#screen call parameters
screen_string="omega_experiment${index}"
screen_shell_cmd="sh -c 'python ${filename} ${arguments}'"

screen -dmS ${screen_string} ${screen_shell_cmd}
