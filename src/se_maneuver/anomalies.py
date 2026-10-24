#Anomaly? More like a-gnome-aly!
#Look idk man I was struggling with this one.

import numpy as np
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
        E: eccentric anomaly (radians)
    '''
    M = np.deg2rad(M)

    f = lambda E : E - e * np.sin(E) - M
    fprime = lambda E : 1 - e * np.cos(E)
    fp2 = lambda E : e * np.sin(E)

    return scipy.optimize.newton(f, 0, fprime, fprime2 = fp2)

#Function to determine true anomaly
def true_anomaly(M, e):
    '''Calculates the true anomaly via the eccentric anomaly.

    Args:
        M: mean anomaly (degrees)
        e: eccentricity
    
    Returns:
        nu: true anomaly (radians)
    '''
    beta = e / (1 + np.sqrt(1 - e**2))
    E = eccentric_anomaly(M, e)
    nu = E + 2*(np.arctan((beta*np.sin(E))/(1-beta*np.cos(E))))

    return nu