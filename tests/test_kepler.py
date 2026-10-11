from se_maneuver.kepler import circ_speed
import pytest

#Test 400 km Earth orbit, should be 7.67 km/s
def test_circ_leo():
    v = circ_speed(5.9722e24,6771000)
    assert v == pytest.approx(7672, rel=1e-3)

#Test orbit of moon around Earth, should be ~1.02 km/s
def test_circ_moon():
    v = circ_speed(5.9722e24,385000000)
    assert v == pytest.approx(1020, rel=1e-2) #More error allowed bc lunar orbit not actually circular