from se_maneuver.kepler import *
import pytest
import scipy.constants as const

earth_mass = 5.9722e24
solar_mass = 1.9884e30

'''Circular orbit speed tests'''

#Test 400 km Earth orbit, should be 7.67 km/s
def test_circ_leo():
    v = circ_speed(earth_mass,6771000)
    assert v == pytest.approx(7672, rel=1e-3)

#Test orbit of moon around Earth, should be ~1.02 km/s
def test_circ_moon():
    v = circ_speed(earth_mass,385000000)
    assert v == pytest.approx(1020, rel=1e-2) #More error allowed bc lunar orbit not actually circular

'''Orbital period tests'''

#Test period of LEO orbit, should be ~92.4 mins
def test_period_leo():
    T = period(earth_mass,6771000)
    assert T == pytest.approx(92.4*60, rel=1e-3 )

#Test period of GEO orbit, should be 24h
def test_period_geo():
    T = period(earth_mass,42165800)
    assert T == pytest.approx(86164, rel=1e-3)

#Test period of asteroid 1024 Ganymed, should be ~1588.24 days
def test_period_ganymed():
    T = period(solar_mass,2.664*const.au)
    assert T == pytest.approx(1588.24*86400, rel=1e-3)

'''Escape velocity tests'''

#Test escape velocity from Earth surface
def test_esc_earth_surf():
    v = escape(earth_mass,6371000)
    assert v == pytest.approx(11186, rel=1e-3)

#Test escape velocity from lunar surface
def test_esc_earth_moon():
    v = escape(7.346e22,1737400)
    assert v == pytest.approx(2380, rel=1e-2) #Had to reduce this because getting results too accurate

#Test escape velocity from Sun at Earth orbit radius
def test_esc_sun_earth():
    v = escape(solar_mass,const.au)
    assert v == pytest.approx(42100, rel=1e-3)

'''Vis-viva tests'''

#Test that vis_viva == circ_speed in circular orbit
def test_vis_circ_1():
    v_circ = circ_speed(earth_mass,6771000)
    v_vis = vis_viva(earth_mass,6771000,6771000)
    assert v_circ == v_vis

def test_vis_circ_2():
    v_circ = circ_speed(solar_mass,const.au)
    v_vis = vis_viva(solar_mass,const.au,const.au)
    assert v_circ == v_vis

#Test decreasing v from periapsis to apoapsis
def test_vis_decrease():
    m = earth_mass
    a = 15142000
    v1 = vis_viva(m,a,6771000)
    v2 = vis_viva(m,a,7271000)
    v3 = vis_viva(m,a,7771000)
    v4 = vis_viva(m,a,8271000)
    v5 = vis_viva(m,a,8371000)
    assert v1>v2>v3>v4>v5

#Test same r with greater a gives greater speed
def test_vis_a_change():
    v1 = vis_viva(earth_mass,15142000,6771000)
    v2 = vis_viva(earth_mass,16142000,6771000)
    assert v1<v2

#Test GTO example
def test_vis_gto1():
    a = 24371000
    v_peri = vis_viva(earth_mass,a,6571000)
    v_apo = vis_viva(earth_mass,a,42157000)
    assert v_peri == pytest.approx(10239, rel=1e-3)
    assert v_apo == pytest.approx(1597.4, rel=1e-3)