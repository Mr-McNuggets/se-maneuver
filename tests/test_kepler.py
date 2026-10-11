from se_maneuver.kepler import *
import pytest
import scipy.constants as const

earth_mass = 5.9722e24
solar_mass = 1.9884e30

#Test 400 km Earth orbit, should be 7.67 km/s
def test_circ_leo():
    v = circ_speed(earth_mass,6771)
    assert v == pytest.approx(7.672, rel=1e-3)

#Test orbit of moon around Earth, should be ~1.02 km/s
def test_circ_moon():
    v = circ_speed(earth_mass,385000)
    assert v == pytest.approx(1.02, rel=1e-2) #More error allowed bc lunar orbit not actually circular

#Test period of LEO orbit, should be ~92.4 mins
def test_period_leo():
    T = period(earth_mass,6771)
    assert T == pytest.approx(92.4*60, rel=1e-3 )

#Test period of GEO orbit, should be 24h
def test_period_geo():
    T = period(earth_mass,42165.8)
    assert T == pytest.approx(86164, rel=1e-3)

#Test period of asteroid 1024 Ganymed, should be ~1588.24 days
def test_period_ganymed():
    T = period(solar_mass,2.664*(const.au/1000))
    assert T == pytest.approx(1588.24*86400,rel=1e-3)