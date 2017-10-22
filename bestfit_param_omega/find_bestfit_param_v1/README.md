Find bestfit parameters for 'Omega'
===========================================

Version One - Single parameters
-----------------------------------

This folder is varying a single parameter at a time.

mgal - The initial mass of the galaxy [M\_sol]
inflow\_rate - The constant inflow of mass [M\_sol/yr]
outflow\_rate - The constant outflow of mass [M\_sol/yr]
sfh\_array\_norm - The total amount of stellar mass formed [M\_sol]
imf\_bdys - Mass boundaries of IMF [M\_sol]
f\_arfo - Fraction applied to yields of massive stars []
TODO!!! nsm\_table
nsmerger\_bdys - Mass boundaries of NSM-events [M\_sol]
nb\_nsm\_per\_m - Number of NSM per stellar mass formed []
f\_binary - Fraction of binary systems in the galaxy
f\_merger - Fraction of binary systems that merge
m\_ej\_nsm - Mass of ejecta from NSM
t\_nsm\_coal - Time after which all compact binary systems merge [yr]
t\_merger\_max - 
pop3\_table - which table of population III ejecta to use
imf\_bdys\_pop3 - Mass boundaries of population III IMF
imf\_yields\_range\_pop3 - Mass boundaries of population III ejecta

Methodology
------------
The different parameters are listed in [parameter-space](parameter_space.txt), alongside all the different parameters to be tested ended by the name of the image-file generated.
There is a single plotting-script for each parameter, and a script that call each one of them when an 'update' is in order.
The images are stored in the [image-folder](variable_plots), but the results are also summarized in [the results](Results.md).

Personal notes
----------------
Sfr-normalization should be set by the default Eris-parameters, since it uses the last value of the 'm_growth' array in the 'sfr'-dictionary.

Value = 38914300000.0
