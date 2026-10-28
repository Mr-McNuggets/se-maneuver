from se_maneuver.kepler import period
from se_maneuver.maneuvers import *
import pytest
import scipy.constants as const
import numpy

earth_mass = 5.9722e24
solar_mass = 1.9884e30

''' Hohmann transfer '''

#Test LEO to GEO
def test_hohmann_gto():
    gto = hohmann(earth_mass,6678000,42164000,9.81)
    assert round(gto.dv1, -5) == pytest.approx(2400000, rel=1e-3)
    assert round(gto.dv2, -5) == pytest.approx(1500000, rel=1e-3)
    assert round(gto.dv_total, -5) == pytest.approx(3900000, rel=1e-2)
    assert gto.time == pytest.approx(19080, rel=1e-2)

#Test same orbit transfer
def test_hohmann_same():
    same: Hoh_Param = hohmann(m=earth_mass,r1=7000000,r2=7000000)
    assert same.dv_total == 0
    assert same.time == period(m=earth_mass,a=7000000)/2

#Test reversibility
def test_hoh_rev():
    rev1: Hoh_Param = hohmann(m=earth_mass,r1=7000000,r2=50000000)
    rev2: Hoh_Param = hohmann(m=earth_mass,r1=50000000,r2=7000000)
    assert rev2.dv_total == rev1.dv_total
    assert rev2.time == rev1.time

#Test bigger transfer = more dv
def test_hoh_bigger():
    trans1: Hoh_Param = hohmann(m=earth_mass,r1=7000000,r2=10000000)
    trans2: Hoh_Param = hohmann(m=earth_mass,r1=7000000,r2=25000000)
    assert trans1.dv_total < trans2.dv_total

''' Bi-elliptic transfer '''

#Test r_b = r2 same as Hohmann
def test_biellip_same():
    trans_hoh = hohmann(earth_mass,7000000,15000000)
    trans_biellip = bi_ellip(earth_mass,7000000,15000000,15000000)
    assert trans_hoh.dv_total == trans_hoh.dv_total

#Test a --> b == b --> a
def test_biellip_reverse():
    trans1 = bi_ellip(earth_mass,7000000,15000000,50000000)
    trans2 = bi_ellip(earth_mass,15000000,7000000,50000000)
    assert trans1.dv_total == trans2.dv_total

#Test more dv than Hohmann with low ratio
def test_more_than_hoh():
    good_hoh = hohmann(earth_mass,7000000,15000000)
    bad_biellip = bi_ellip(earth_mass,7000000,15000,75000000)
    assert good_hoh.dv_total < bad_biellip.dv_total

#Test less dv than Hohmann with high ratio
def test_less_than_hoh():
    bad_hoh = hohmann(earth_mass,7000000,140000000)
    good_biellip = bi_ellip(earth_mass,7000000,140000000,250000000)
    assert bad_hoh.dv_total > good_biellip.dv_total

#Test dv_total converges as r_b increases, dv2 decreases
def test_converge():
    r_b = 100000000
    total_dv_list = []
    dv2_list = []
    for i in range(5):
        biellip_converge = bi_ellip(earth_mass,7000000,50000000,r_b)
        total_dv_list.append(biellip_converge.dv_total)
        dv2_list.append(biellip_converge.dv2)
        r_b *= 10
    diffs = numpy.abs(numpy.diff(total_dv_list))
    assert dv2_list[0] > dv2_list[1] > dv2_list[2] > dv2_list[3] > dv2_list[4]
    assert diffs[0] > diffs[1] > diffs[2] > diffs[3]