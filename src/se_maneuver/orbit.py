import scipy.constants as const
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Orbit:
    '''Orbital parameters

    Args:
        e: eccentricity
        a: semimajor axis (m)
        argp: argument of periapsis (decimal degrees)
        long_asc: longitude of the ascending node (decimal degrees)
        i: inclination (decimal degrees)
        m: mass of body (kg)

    Extra parameters:
        mu: standard gravitational parameter (m^3*s^-2)
        T: period of orbit (s)
    '''
    e: float
    a: float
    argp: float
    long_asc: float
    i: float
    m: float

    @property
    def mu(self) -> float:
        return self.m * (const.G)
    
    @property
    def T(self) -> float:
        return (2*np.pi)*np.sqrt(self.a**3/self.mu)