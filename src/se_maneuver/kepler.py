#Kepler? I hardly know her!

import numpy
import scipy
import scipy.constants as const

#Function to determine speed of circular orbit given mass (kg), radius (m)
def circ_speed(m,r):
    mu = const.G*m
    speed = numpy.sqrt(mu/r)
    return speed