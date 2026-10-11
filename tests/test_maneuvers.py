from se_maneuver.kepler import period
from se_maneuver.maneuvers import *
import pytest
import scipy.constants as const

earth_mass = 5.9722e24
solar_mass = 1.9884e30

''' Hohmann transfer '''

#Test LEO to GEO
def test_hohmann_gto():
    gto = hohmann(earth_mass,6678,42164,9.81)
    assert round(gto.dv1, -2) == pytest.approx(2400, rel=1e-3)
    assert round(gto.dv2, -2) == pytest.approx(1500, rel=1e-3)
    assert round(gto.dv_total, -2) == pytest.approx(3900, rel=1e-2)
    assert gto.time == pytest.approx(19080, rel=1e-2)

#Test same orbit transfer
def test_hohmann_same():
    same = hohmann(earth_mass,7000,7000)
    assert same.dv_total == 0
    assert same.time == period(earth_mass,7000)/2

#Test reversibility
def test_hoh_rev():
    rev1 = hohmann(earth_mass,7000,50000)
    rev2 = hohmann(earth_mass,50000,7000)
    assert rev2.dv_total == 0-rev1.dv_total
    assert rev2.time == rev1.time

#Test bigger transfer = more dv
def test_hoh_bigger():
    trans1 = hohmann(earth_mass,7000,10000)
    trans2 = hohmann(earth_mass,7000,25000)
    assert trans1.dv_total < trans2.dv_total