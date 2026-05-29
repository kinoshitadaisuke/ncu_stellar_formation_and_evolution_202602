#!/usr/bin/env python3

#
# Time-stamp: <2026/05/28 16:09:47 (UT+08:00) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 1H (proton)
massexcess_1H, err_massexcess_1H = nuclyr.mass.massExcess (1, 1)

# printing mass excess of 1H (proton)
print (f'mass excess of 1H  =', \
       f'{massexcess_1H:6.3f} +/- {err_massexcess_1H:6.3f} [MeV]')
