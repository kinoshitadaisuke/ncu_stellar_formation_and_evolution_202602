#!/usr/bin/env python3

#
# Time-stamp: <2026/05/28 16:09:05 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# standard acceleration of gravity
g = scipy.constants.physical_constants['standard acceleration of gravity']

# value of g
g_value = g[0]

# unit of g
g_unit = g[1]

# error of g
g_error = g[2]

# printing result
print (f'standard acceleration of gravity:')
print (f' g = {g_value} +/- {g_error} [{g_unit}]')
