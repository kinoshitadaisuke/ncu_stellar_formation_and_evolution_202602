#!/usr/bin/env python3

#
# Time-stamp: <2026/05/28 16:10:12 (UT+08:00) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 4He (helium-4)
massexcess_4He, err_massexcess_4He = nuclyr.mass.massExcess (2, 4)

# mass excess of 12C (carbon-12)
massexcess_12C, err_massexcess_12C = nuclyr.mass.massExcess (6, 12)

# energy produced by triple-alpha process
energy_3alpha = massexcess_4He * 3 - massexcess_12C

# printing result of calculation
print (f'mass excess of 4He =', \
       f'{massexcess_4He:6.3f} +/- {err_massexcess_4He:6.3f} [MeV]')
print (f'mass excess of 12C =', \
       f'{massexcess_12C:6.3f} +/- {err_massexcess_12C:6.3f} [MeV]')
print (f'energy produced by triple-alpha process:')
print (f'  E = {massexcess_4He:6.3f} x 4 - {massexcess_12C:6.3f} [MeV]')
print (f'    = {massexcess_4He * 4:6.3f} - {massexcess_12C:6.3f} [MeV]')
print (f'    = {energy_3alpha:6.3f} [MeV]')
