import scipy.constants as const
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Orbit:
    '''Orbital parameters

    Units:
    All distances in km
    All angles in degrees (decimal)
    Mass in kg
    Times in seconds
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