#Kepler? I hardly know her!

import numpy
import scipy.constants as const

def circ_speed(m,r):
    '''Determines speed of circular orbit.

    Args:
        m: mass of body being orbited (kg)
        r: orbital radius (km)
    
    Returns:
        v: speed of the circular orbit (km/s)
    '''
    mu = (const.G/1e9)*m
    v = numpy.sqrt(mu/r)
    return v

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

def escape(m,d): #Yes yes I know it's technically a speed and not a velocity shut up
    '''Determines the escape velocity from a body at a certain distance from the center

    Args:
        m: mass of body (kg)
        d: distance from center of body (km)
    
    Returns:
        esc_v: the escape velocity from a body of the given mass at the given distance (km/s)
    '''
    mu = (const.G/1e9)*m
    esc_v = numpy.sqrt((2*mu)/d)
    return esc_v

def vis_viva(m,a,r):
    '''The vis-viva equation. Not much more to it really.

    Args:
        m: mass of central body (kg)
        a: semimajor axis of spacecraft orbit (km)
        r: radial distance of spacecraft from central body (km)
    
    Returns:
        v: speed of spacecraft (km/s)
    '''
    mu = (const.G/1e9)*m
    v = numpy.sqrt(mu*((2/r)-(1/a)))
    return v