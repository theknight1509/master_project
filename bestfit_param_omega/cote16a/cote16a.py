"""
"""
sigma_val2rel = lambda x0, s_val: s_val/x0
sigma_rel2val = lambda x0, s_rel: s_rel*x0

#lower mass limit of mass function
M_lower = 8.00e-2 #[M_sol]
M_lower_sigma_val = 0.62e-2 #[M_sol]
M_lower_sigma_rel = sigma_val2rel(M_lower, M_lower_sigma_val)
M_lower_tuple = (M_lower, M_lower_sigma_val, M_lower_sigma_val)

#upper mass limit of mass function
M_upper = 138.0 #[M_sol]
M_upper_sigma_val = 36.0 #[M_sol]
M_upper_sigma_rel = sigma_val2rel(M_upper, M_upper_sigma_val)
M_upper_tuple = (M_upper, M_upper_sigma_val, M_upper_sigma_val)

#slope of mass function
imf_slope = 2.29 #[]
imf_slope_sigma_val = 0.20 #[]
imf_slope_sigma_rel = sigma_val2rel(imf_slope, imf_slope_sigma_val)
imf_slope_tuple = (imf_slope, imf_slope_sigma_val, imf_slope_sigma_val)

#slope of Delay-time distribution of SN1a
DTD1a_slope = 1.07 #[]
DTD1a_slope_sigma_val = 0.15 #[]
DTD1a_slope_sigma_rel = sigma_val2rel(DTD1a_slope, DTD1a_slope_sigma_val)
DTD1a_slope_tuple = (DTD1a_slope, DTD1a_slope_sigma_val, DTD1a_slope_sigma_val)

#number of SN1a
Num1a = 1.01e-3 #[1/M_sol]
Num1a_sigma_val = 0.62e-3 #[1/M_sol]
Num1a_sigma_rel = sigma_val2rel(Num1a, Num1a_sigma_val)
Num1a_slope_tuple = (Num1a_slope, Num1a_slope_sigma_val, Num1a_slope_sigma_val)

#current mass of stars, used to calibrate SFH
M_star_f = 5.84e10 #[M_sol]
M_star_f_sigma_val = 1.17e10 #[M_sol]
M_star_f_sigma_rel = sigma_val2rel(M_star_f, M_star_f_sigma_val)
M_star_f_tuple = (M_star_f_slope, M_star_f_sigma_val, M_star_f_sigma_val)

#current mass of galactic gas
M_gas_f = 9.2e9 #[M_sol]
M_gas_f_sigma_val = 5.3e9 #[M_sol]
M_gas_f_sigma_rel = sigma_val2rel(M_gas_f, M_gas_f_sigma_val)
M_gas_f_tuple = (M_gas_f_slope, M_gas_f_sigma_val, M_gas_f_sigma_val)

if __name__ == '__main__':
    from directory_master import Foldermap
    folder = Foldermap()
    fodler.activate_environ()
    from omega import omega
    from visualize import visualize
    
    #for each parameter... plot 'Eris', empty 'Omega' and parameter +/- sigma
    loa_param_tuples = [M_lower_tuple, M_upper_tuple, imf_slope_tuple,
                        DTD1a_slope_tuple, Num1a_slope_tuple,
                        M_star_f_slope_tuple, M_gas_f_tuple]
    loa_param_names = ["Mlower", "Mupper", "imfslope",
                        "DTD1aSlope", "Num1aSlope",
                        "Mstar", "Mgas"]
    #Use 'visualize' to plot spectro-scopic data from 'Omega'
    loa_omega = [omega()] + [omega(
    plot_obj = visualize(loa_omega, loa_omega_names, num_yaxes=3)
