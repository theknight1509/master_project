#!/bin/bash
#bash-script for moving relevant data-files to thesis-folder

master_dir="/home/oyvind/github_uio/Master/"
thesis_dir=${master_dir}"latex/thesis/results/data_fitting/"

#Directories and files
v0_dir=${master_dir}"bestfit_param_omega/find_bestfit_param_v0/data/"
v0_array_test=("test_transfer_v0")
v0_array=("highres_eris_parameters_gas_mass"
          "highres_eris_parameters_m_locked"
          "highres_eris_parameters_rates0"
          "highres_eris_parameters_rates1"
          "highres_eris_parameters_rates2"
          "highres_eris_parameters_spectro0"
          "highres_eris_parameters_spectro1"
          "highres_eris_parameters_spectro2")

v1_dir=${master_dir}"bestfit_param_omega/find_bestfit_param_v1/data/"
v1_array=("mass_parameters_v1_1_n1100"
          "mass_parameters_v1_2_n1100"
          "mass_parameters_v2_mass_1_n300"
          "mass_parameters_v2_mass_2_n300"
          "mass_parameters_v2_spectro_0_n300"
          "mass_parameters_v2_spectro_1_n300"
          "mass_parameters_v3_masses_1_n300"
          "mass_parameters_v3_masses_2_n300"
          "mass_parameters_v3_rates_0_n300"
          "mass_parameters_v3_spectro_0_n300"
          "mass_parameters_v3_spectro_1_n300")

v2_dir=${master_dir}"bestfit_param_omega/find_bestfit_param_v2/data/"
v2_array=("sn1a_parameters_v1_spectro_0_n30"
          "sn1a_parameters_v1_spectro_1_n30"
          "sn1a_parameters_v1_rates_1_n30"
          "sn1a_parameters_v2_exp_spectro_0_n30"
          "sn1a_parameters_v2_exp_spectro_1_n30"
          "sn1a_parameters_v2_exp_rates_1_n30"
          "sn1a_parameters_v2_gauss_spectro_0_n30"
          "sn1a_parameters_v2_gauss_spectro_1_n30"
          "sn1a_parameters_v2_gauss_rates_1_n30"
          "sn1a_parameters_v2_powerlaw_spectro_0_n30"
          "sn1a_parameters_v2_powerlaw_spectro_1_n30"
          "sn1a_parameters_v2_powerlaw_rates_1_n30"
          "sn1a_parameters_v3_spectro_1_n30"
          "sn1a_parameters_v4_spectro_0_n30"
          "sn1a_parameters_v4_spectro_1_n30"
          "sn1a_parameters_v4_rates_1_n30"
          "star_parameters_v1_0_n30"
          "star_parameters_v1_1_n30"
          "star_parameters_v2_0_n30"
          "star_parameters_v2_1_n30"
          "star_parameters_v3_0_n300"
          "star_parameters_v3_1_n300"
          "star_parameters_v4_0_n300"
          "star_parameters_v4_1_n300")

v3_dir=${master_dir}"bestfit_param_omega/find_bestfit_param_v3/data/"
v3_array=("nsm_parameters_v1_2_n300"
          "nsm_parameters_v2_ejmass_2_n30"
          "nsm_parameters_v2_mergerfraction_rates_2_n300"
          "nsm_parameters_v2_mergerfraction_spectro_2_n300"
          "nsm_parameters_v2_nbnsm_rates_2_n300"
          "nsm_parameters_v2_nbnsm_spectro_2_n300"
          "nsm_parameters_v3_rates_2_n300"
          "nsm_parameters_v3_spectro_2_n300"
          "nsm_parameters_v4_rates_2_n300"
          "nsm_parameters_v4_spectro_2_n300")

cur_bft_dir=${master_dir}"bestfit_param_omega/current_bestfit_plots/"
cur_bft_array=("spectro_n300_param0"
               "spectro_n300_param1"
               "spectro_n300_param2"
               "rates_n300_param0"
               "rates_n300_param1"
               "rates_n300_param2"
               "masses_n300_param0"
               "masses_n300_param1"
               "masses_n300_param2")

#count length of each array
v0_test_length=${#v0_array_test[@]}
v0_length=${#v0_array[@]}
v1_length=${#v1_array[@]}
v2_length=${#v2_array[@]}
v3_length=${#v3_array[@]}
cur_bft_length=${#cur_bft_array[@]}

echo "Do you want to update ALL datafiles? y/n"
read response

if [ $response == 'y' ]
then
    for (( i=0; i<${v0_length}; i++ ));
    do
        expl_file=${v0_array[i]}"_explanatory.txt"
        data_file=${v0_array[i]}".npy"
        echo "Copying '${expl_file}' and '${data_file}'"
        echo "  from folder '${v0_dir}'"
        echo "  into folder '${thesis_dir}'"
        cp ${v0_dir}${data_file} ${thesis_dir}${data_file}
        cp ${v0_dir}${expl_file} ${thesis_dir}${expl_file}
    done
    for (( i=0; i<${v1_length}; i++ ));
    do
        expl_file=${v1_array[i]}"_explanatory.txt"
        data_file=${v1_array[i]}".npy"
        echo "Copying '${expl_file}' and '${data_file}'"
        echo "  from folder '${v1_dir}'"
        echo "  into folder '${thesis_dir}'"
        cp ${v1_dir}${data_file} ${thesis_dir}${data_file}
        cp ${v1_dir}${expl_file} ${thesis_dir}${expl_file}
    done
    for (( i=0; i<${v2_length}; i++ ));
    do
        expl_file=${v2_array[i]}"_explanatory.txt"
        data_file=${v2_array[i]}".npy"
        echo "Copying '${expl_file}' and '${data_file}'"
        echo "  from folder '${v2_dir}'"
        echo "  into folder '${thesis_dir}'"
        cp ${v2_dir}${data_file} ${thesis_dir}${data_file}
        cp ${v2_dir}${expl_file} ${thesis_dir}${expl_file}
    done
    for (( i=0; i<${v3_length}; i++ ));
    do
        expl_file=${v3_array[i]}"_explanatory.txt"
        data_file=${v3_array[i]}".npy"
        echo "Copying '${expl_file}' and '${data_file}'"
        echo "  from folder '${v3_dir}'"
        echo "  into folder '${thesis_dir}'"
        cp ${v3_dir}${data_file} ${thesis_dir}${data_file}
        cp ${v3_dir}${expl_file} ${thesis_dir}${expl_file}
    done
    for (( i=0; i<${cur_bft_length}; i++ ));
    do
        expl_file=${cur_bft_array[i]}"_explanatory.txt"
        data_file=${cur_bft_array[i]}".npy"
        echo "Copying '${expl_file}' and '${data_file}'"
        echo "  from folder '${v3_dir}'"
        echo "  into folder '${thesis_dir}'"
        cp ${cur_bft_dir}${data_file} ${thesis_dir}${data_file}
        cp ${cur_bft_dir}${expl_file} ${thesis_dir}${expl_file}
    done
    ls ${thesis_dir}
elif [ $response == 'n' ]
then echo "Exiting"
elif [ $response == "test" ]
then
    for (( i=0; i<${v0_test_length}; i++ ));
    do
        echo "Copying '${v0_array_test[i]}'"
        echo "  from folder '${v0_dir}'"
        echo "  into folder '${thesis_dir}'"
        cp ${v0_dir}${v0_array_test[i]} ${thesis_dir}${v0_array_test[i]}
    done
fi


#copy all data-files from list into result-folder
