#!/usr/bin/env python3

#
# Time-stamp: <2026/05/28 16:09:54 (UT+08:00) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 4He (helium-4)
massexcess_4He, err_massexcess_4He = nuclyr.mass.massExcess (2, 4)

# printing mass excess of 4He (helium-4)
print (f'mass excess of 4He =', \
       f'{massexcess_4He:6.3f} +/- {err_massexcess_4He:6.3f} [MeV]')
