#Kepler? I hardly know her!

import numpy
import scipy.constants as const

def circ_speed(m,r):
    '''Determines speed of circular orbit.

    Args:
        m: mass of body being orbited (kg)
        r: orbital radius (m)
    
    Returns:
        speed: speed of the circular orbit (km/s)
    '''
    mu = const.G*m
    speed = numpy.sqrt(mu/r)
    return speed