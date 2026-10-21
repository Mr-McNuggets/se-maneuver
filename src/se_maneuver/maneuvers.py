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
        self.dv_total = abs(self.dv1)+abs(self.dv2)
        self.time = period(m,a_trans)/2

        #Optional burn time
        if thrust!=0: #Only return burn time if thrust given
            self.burn_time1 = abs(self.dv1)/thrust
            self.burn_time2 = abs(self.dv2)/thrust
        else:
            self.burn_time1 = "No thrust value given"
            self.burn_time2 = "No thrust value given"

def hohmann(m: float,r1: float,r2: float,thrust: float=0) -> Hoh_Param:
    '''Calculates the parameters of a Hohmann transfer between two circular orbits.

    Args:
        m: mass of central body (kg)
        r1: radius of starting orbit (km)
        r2: radius of target orbit (km)
        thrust: acceleration/thrust of spacecraft, optional (m/s^2)
    
    Returns:
        dv1: delta-v of first burn of Hohmann transfer (starting --> transfer orbit) (m/s)
        dv2: delta-v of second burn of Hohmann transfer (transfer --> final orbit) (m/s)
        dv_total: Total delta-v of the transfer, always positive (m/s)
        time: transfer time (s)
        burn_time1: time required for first burn of transfer, returned if thrust arg given (s)
        burn_time2: time required for second burn of transfer, returned if thrust arg given (s)

    Negative dv means retrograde burn, except dv_total
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
        
        #Transfer SMAs
        a_trans1 = (r1+r_b)/2
        a_trans2 = (r2+r_b)/2

        v_init = circ_speed(m,r1)
        v_trans1_peri = vis_viva(m,a_trans1,r1)
        self.dv1 = (v_trans1_peri-v_init)*1000

        v_trans1_apo = vis_viva(m,a_trans1,r_b)
        v_trans2_apo = vis_viva(m,a_trans2,r_b)
        self.dv2 = (v_trans2_apo-v_trans1_apo)*1000

        v_trans2_peri = vis_viva(m,a_trans2,r2)
        v_final = circ_speed(m,r2)
        self.dv3 = (v_final-v_trans2_peri)*1000

        self.dv_total = abs(self.dv1)+abs(self.dv2)+abs(self.dv3)

        self.time = (period(m,a_trans1)/2)+(period(m,a_trans2)/2)

        if thrust != 0:
            self.burn_time1 = abs(self.dv1)/thrust
            self.burn_time2 = abs(self.dv2)/thrust
            self.burn_time3 = abs(self.dv3)/thrust
        else:
            self.burn_time1 = "No thrust value given."
            self.burn_time2 = "No thrust value given."
            self.burn_time3 = "No thrust value given."

def bi_ellip(m: float,r1: float,r2: float,r_b: float,thrust: float=0) -> BEllip_Param:
    '''Calculates the parameters of a bi-elliptic transfer between two circular orbits
    Args:
        m: mass of body (kg)
        r1: radius of starting orbit (km)
        r2: radius of target orbit (km)
        r_b: apoapsis of transfer orbit (must be greater than both r1 and r2) (km)
        thrust: spacecraft thrust/acceleration (optional) (m/s^2)
    
    Returns:
        dv1: delta-v of the first burn of the transfer (m/s)
        dv2: delta-v of the second burn of the transfer (m/s)
        dv3: delta-v of the third and final burn of the transfer (m/s)
        dv_total: total delta-v of the transfer (always positive) (m/s)
        time: time spent in transfer (s)
        burn_time1: time required for the first burn of the transfer, returned if thrust value given (s)
        burn_time2: time required for the second burn of the transfer, returned if thrust value given (s)
        burn_time3: time required for the third and final burn of the transfer, returned if thrust value given (s)

        Negative dv means retrograde burn, except dv_total
    '''
    return BEllip_Param(m,r1,r2,r_b,thrust)