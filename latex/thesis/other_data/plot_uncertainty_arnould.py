"""
Plot gaussian distributions of the upper and lower relative standard deviation around 1.0
"""
from make_latex_table import get_sigma_from_table
import numpy as np
import matplotlib.pyplot as pl

def plot_gaussians(fig_object, loa_means, loa_sigmas, loa_labels, x_array):
    ax = fig_object.gca()
    ax.grid(True)
    gauss = lambda x, x0, sigma: np.exp(-((x-x0)/sigma)**2)
    for mean, sigma, label in zip(loa_means, loa_sigmas, loa_labels):
        y_array = gauss(x_array, mean, sigma)
        ax.plot(x_array, y_array, label=label)
    return fig_object

if __name__ == '__main__':
    #get all sigma values
    doa_sigmas = get_sigma_from_table("arnould_table_modified.dat")
    x_array = np.linspace(0,2,1001)
    #repeat for each isotope
    for isotope_tuple in doa_sigmas["tuple-list"]:
        iso, sigma_lower, sigma_upper = isotope_tuple
        sigma_lower = abs(sigma_lower)
        sigma_mean = 0.5*(sigma_lower + sigma_upper)
        loa_sigmas = [sigma_lower, sigma_mean, sigma_upper]
        loa_labels = [r"$\sigma_{lower}$", r"$\bar{\sigma}$", r"$\sigma_{upper}$"]
        loa_means = [1.0 for i in range(len(loa_sigmas))]
        fig_object = plot_gaussians(fig_object=pl.figure(), loa_means=loa_means,
                                    loa_sigmas=loa_sigmas, loa_labels=loa_labels,
                                    x_array=x_array)
        fig_object.suptitle(iso.capitalize())
        fig_object.legend(numpoints=1,bbox_to_anchor=(0.9,0.9), loc='upper right')
        fig_object.savefig("arnould_plots/isotope_gaussian_%s.png"%iso)
        fig_object.show()
        #print(iso)
