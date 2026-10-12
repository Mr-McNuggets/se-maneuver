#Maneuver? I hardly know her!
#Ok ok I won't use that one again :3

from se_maneuver.kepler import *
import numpy

''' Hohmann transfer '''

class Hoh_Param:
    def __init__(self,m: float,r1: float,r2: float,thrust: float=0) -> None:
        if thrust < 0:
            raise Exception("Negative thrust values are not allowed.")
        if r1 < 0 or r2 < 0:
            raise Exception("Negative orbital radius values are not allowed.")
        if m < 0:
            raise Exception("Negative mass values are not allowed.")

        #Transfer orbit semimajor axis
        a_trans = (r1+r2)/2

        #Speeds throughout transfer
        v_start = circ_speed(m,r1)
        v_trans_start = vis_viva(m,a_trans,r1)
        v_trans_end = vis_viva(m,a_trans,r2)
        v_final = circ_speed(m,r2)

        self.dv1 = (v_trans_start-v_start)*1000
        self.dv2 = (v_final-v_trans_end)*1000
        self.dv_total = abs(self.dv1+self.dv2)
        self.time = period(m,a_trans)/2

        #Optional burn time
        if thrust!=0: #Only return burn time if thrust given
            self.burn_time1 = self.dv1/thrust
            self.burn_time2 = self.dv2/thrust
        else:
            self.burn_time1 = "No thrust value given"
            self.burn_time2 = "No thrust value given"

def hohmann(m: float,r1: float,r2: float,thrust: float=0) -> Hoh_Param:
    '''Calculates the parameters of a Hohmann transfer between two circular orbits.

    Args:
        m: mass of central body (kg)
        r1: radius of starting orbit (km)
        r2: radius of target orbit (km)
        thrust: acceleration/thrust of spacecraft (m/s^2), OPTIONAL
    
    Returns:
        dv1: delta-v of first burn of Hohmann transfer (starting --> transfer orbit) (m/s)
        dv2: delta-v of second burn of Hohmann transfer (transfer --> final orbit) (m/s)
        dv_total: Total delta-v of the transfer (m/s)
        time: transfer time (s)
        burn_time1: time required for first burn of transfer (returned if thrust arg given) (s)
        burn_time2: time required for second burn of transfer (returned if thrust arg given) (s)

    Negative dv means retrograde burn
    '''
    return Hoh_Param(m,r1,r2,thrust)

''' Bi-elliptic transfer '''

class BEllip_Param:
    def __init__(self,m: float,r1: float,r2: float,r_b: float,thrust: float=0) -> None:
        if thrust < 0:
            raise Exception("Negative thrust values are not allowed.")
        if m < 0:
            raise Exception("Negative mass values are not allowed.")
        if r1 < 0 or r2 < 0 or r_b < 0:
            raise Exception("Negative radii are not allowed.")
        if r_b < r1 or r_b < r2:
            raise Exception("r_b must be larger than both r1 and r2.")
