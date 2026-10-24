#Anomaly? More like a-gnome-aly!
#Look idk man I was struggling with this one.

import numpy
import scipy
import scipy.optimize

#Mean anomaly is given

#Function to determine eccentric anomaly (Kepler's equation)
def eccentric_anomaly(M, e):
    '''Calculates eccentric anomaly from eccentric anomaly using Kepler's equation and the Newton-Raphson method.

    Args:
        M: mean anomaly (degrees)
        e: eccentricity
    
    Returns:
        E: eccentric anomaly (degrees)
    '''
    M = numpy.deg2rad(M)

    f = lambda E : E - e * numpy.sin(E) - M
    fprime = lambda E : 1 - e * numpy.cos(E)
    fp2 = lambda E : e * numpy.sin(E)

    return numpy.rad2deg(scipy.optimize.newton(f, 0, fprime, fprime2 = fp2))

#Function to determine true anomaly
def true_anomaly(M, e):
    '''Calculates the true anomaly via the eccentric anomaly.

    Args:
        M: mean anomaly (degrees)
        e: eccentricity
    
    Returns:
        nu: true anomaly (degrees)
    '''
    beta = e / (1 + numpy.sqrt(1 - e**2))
    E = numpy.deg2rad(eccentric_anomaly(M, e))
    nu = E + 2*(numpy.arctan((beta*numpy.sin(E))/(1-beta*numpy.cos(E))))

    return numpy.rad2deg(nu)