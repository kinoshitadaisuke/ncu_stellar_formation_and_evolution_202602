#!/usr/bin/env python3

#
# Time-stamp: <2026/05/28 16:10:06 (UT+08:00) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 12C (carbon-12)
massexcess_12C, err_massexcess_12C = nuclyr.mass.massExcess (6, 12)

# printing mass excess of 12C (carbon-12)
print (f'mass excess of 12C =', \
       f'{massexcess_12C:6.3f} +/- {err_massexcess_12C:6.3f} [MeV]')
