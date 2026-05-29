#!/usr/bin/env python3

#
# Time-stamp: <2026/05/28 16:07:40 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# x values
output_x = numpy.linspace (0.0, 50.0, 50001)

# analytical solution
ana_x = output_x
ana_y = y_0 * numpy.exp (-k * ana_x)

# printing result
print (f'analytical solution:')
print (f'x: {ana_x}')
print (f'y: {ana_y}')
