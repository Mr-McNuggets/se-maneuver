import scipy.constants as const
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Orbit:
    '''Orbital parameters

    Args:
        r_peri: radius of periapsis (km)
        r_apo: radius of apoapsis (km)
        e: eccentricity
        a: semimajor axis
        argp: argument of periapsis (decimal degrees)
        long_asc: longitude of the ascending node (decimal degrees)
        i: inclination (decimal degrees)
        m: mass of body (kg)

    Extra parameters:
        mu: standard gravitational parameter (m^3*s^-2)
        T: period of orbit (s)
    '''
    r_peri = float
    r_apo = float
    e = float
    a = float
    argp = float
    long_asc = float
    i = float
    m = float

    @property
    def mu(self) -> float:
        return self.m * const.G
    
    def T(self) -> float:
        return (2*numpy.pi)*numpy.sqrt(self.a**3/self.mu)