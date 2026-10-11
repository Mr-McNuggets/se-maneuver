#Kepler? I hardly know her!

import numpy
import scipy.constants as const

def circ_speed(m,r):
    '''Determines speed of circular orbit.

    Args:
        m: mass of body being orbited (kg)
        r: orbital radius (km)
    
    Returns:
        speed: speed of the circular orbit (km/s)
    '''
    mu = (const.G/1e9)*m
    speed = numpy.sqrt(mu/r)
    return speed

def period(m,a):
    '''Determines the period of an orbit.
    Args:
        m: mass of body being orbited (kg)
        a: semimajor axis of orbit (km)
    
    Returns:
        T: period of orbit (s)
    '''
    mu = (const.G/1e9)*m
    T = (2*numpy.pi)*numpy.sqrt(a**3/mu)
    return T