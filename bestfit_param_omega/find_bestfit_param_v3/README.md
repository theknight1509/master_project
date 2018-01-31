Best fit of 'Omega' parameters - v3
===========================================

Fix the neutron star merger parameters to fit [Eu/H] from 'Eris'

Parameters
-----------

- delay-time of neturon star mergers - either as polynomial distribution or maximum collapse time
- mass ejected per event
- fraction of merging binaries
- number of neutron star mergers per solar mass formed

Results
--------
- Set delay time distribution inspired by Shen et. al. (2015), but also include models where all neutron star binaries merge after a given amount of time
  - There is not much difference (in spectroscopic data) between a steep power-law distribution and a global coallesence time (all nsm occurs after a given amount of time)
  - In order to keep the model slightly more "realitic", a dtd similar to Shen et. al. (2015) will be used, but with a much shorter minimum time.
  - NSM DTD: `\int_{t_min}^{t_Hubble=14Gyr}t^{-2}dt}` with `t_min`=50Myr
![dtd](data/nsm_parameters_v1_n30.png)

- Change the mass ejected from each BNSM in order to get the appropriate amount of Eu
  - ejecta mass ~ 0.3 in order to reproduce [Eu/H] by itself
![ejecta](data/nsm_parameters_v2_ejmass_n30.png)
- Change the fraction of binary neutron stars that do merge, in order to find the appropriate rate of KN
  - the merger fraction should be ~ 9e-4 in order to reproduce the KN rates
  - the merger fraction should be ~ 1e-2 in order to reproduce [Eu/H]
![merger fraction](data/nsm_parameters_v2_mergerfraction_rates_n300.png)
![merger fraction](data/nsm_parameters_v2_mergerfraction_spectro_n300.png)
- Get KN-rate from star-formation rate (set number of NSMs per solar mass formed)
  - NSMs per mass should be ~ 2e-6 in order to reproduce the KN rates
  - NSMs per mass should be ~ (2-3)e-5 in order to reproduce [Eu/H]
![nsm per mass](data/nsm_parameters_v2_nbnsm_rates_n300.png)
![nsm per mass](data/nsm_parameters_v2_nbnsm_spectro_n300.png)
- Use appropriate merger-fraction to find appropriate ejecta mass
  - merger fraction ~ 8e-4 to reproduce rates
  - ejecta mass ~ 0.3 to reproduce [Eu/H]
![merger fraction and ejecta mass](data/nsm_parameters_v3_rates_n300.png)
![merger fraction and ejecta mass](data/nsm_parameters_v3_spectro_n300.png)
- End result with bestfit parameters
  - NSM DTD: `\int_{t_min}^{t_Hubble=14Gyr}t^{-2}dt}` with `t_min`=50Myr
  - merger fraction ~ 8e-4 to reproduce rates
  - ejecta mass ~ 0.3 to reproduce [Eu/H]
![final](data/nsm_parameters_v4_rates_n300.png)
![final](data/nsm_parameters_v4_spectro_n300.png)

Comments to self
------------------
Datafiles for thesis
 - [dtd/t\_nsm\_coal - [Eu/H]](data/nsm_parameters_v1_2_n30_explanatory.txt)
 - [ejecta mass - [Eu/H]](data/nsm_parameters_v2_ejmass_2_n30_explanatory.txt)
 - [merger fraction - KN rate](data/nsm_parameters_v2_mergerfraction_rates_2_n300_explanatory.txt)
 - [merger fraction - [Eu/H]](data/nsm_parameters_v2_mergerfraction_spectro_2_n300_explanatory.txt)
 - [nsm per mass - KN rate](data/nsm_parameters_v2_nbnsm_rates_2_n300_explanatory.txt)
 - [nsm per mass - [Eu/H]](data/nsm_parameters_v2_nbnsm_spectro_2_n300_explanatory.txt)
 - [merger fraction and ejecta mass - KN rate](data/nsm_parameters_v3_rates_2_n300_explanatory.txt)
 - [merger fraction and ejecta mass - [Eu/H]](data/nsm_parameters_v3_spectro_2_n300_explanatory.txt)
 - [Final - KN rate](data/nsm_parameters_v4_rates_2_n30_explanatory.txt)
 - [Final - [Eu/H]](data/nsm_parameters_v4_spectro_2_n30_explanatory.txt)

[Go back](../README.md)
