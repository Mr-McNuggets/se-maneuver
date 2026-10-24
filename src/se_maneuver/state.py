#Insert pun here

from se_maneuver.anomalies import *
from se_maneuver.orbit import Orbit
import numpy as np

#Calculate state vectors from orbital elements and mean anomaly
def elem2state(orbit, M):
    #Calculate vectors in the perifocal plane (plane of orbit with x axis towards periapsis, centered on focus)
    #True anomaly from mean anomaly
    M = np.rad2deg(M)
    nu = true_anomaly(M, orbit.e)

    #Convert orbital elements to radians
    argp = np.deg2rad(orbit.argp)
    long_asc = np.deg2rad(orbit.long_asc)
    i = np.deg2rad(orbit.i)
    

    #Magnitude of position vector
    r = (orbit.a * (1-orbit.e**2))/(1 + orbit.e*np.cos(nu))

    #Perifocal position vector
    pos_pf = np.array([
        [r*np.cos(nu)],
        [r*np.sin(nu)],
        [0]
        ])
    
    #Perifocal velocity vector
    const = np.sqrt(orbit.mu/(orbit.a * (1-orbit.e**2)))
    vel_pf = np.array([
        [const*(-np.sin(nu))],
        [const*(orbit.e + np.cos(nu))],
        [0]
        ])
    
    #Define the rotation matrix (big and scary but not actually that bad)
    sin_long_asc = np.sin(orbit.long_asc)
    cos_long_asc = np.cos(orbit.long_asc)
    sin_argp = np.sin(orbit.argp)
    cos_argp = np.cos(orbit.argp)
    sin_i = np.sin(orbit.i)
    cos_i = np.cos(orbit.i)
    rot_matrix = np.array([
        [cos_long_asc*cos_argp - sin_long_asc*cos_i*sin_argp, -cos_long_asc*sin_argp - sin_long_asc*cos_i*cos_argp, sin_long_asc*sin_i],
        [sin_long_asc*cos_argp + cos_long_asc*cos_i*sin_argp, -sin_long_asc*sin_argp + cos_long_asc*cos_i*cos_argp, -cos_long_asc*sin_i],
        [sin_i*sin_argp, sin_i*cos_argp, cos_i]
        ])
    
    #Multiply the state vectors in the perifocal plane by the rotation matrix to get the true state vectors
    pos = np.matmul(rot_matrix, pos_pf)
    vel = np.matmul(rot_matrix, vel_pf)
    state = [pos, vel]
    return state

iss_orbit = Orbit(e=0.0006885, a=6797.7, argp=302.9098, long_asc=21.6229, i=51.6335, m=5.972e24)
iss_state = elem2state(iss_orbit, 57.1228)
print(iss_state)