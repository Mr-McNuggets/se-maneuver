from se_maneuver.kepler import circ_speed

#Test 400 km Earth orbit, should be 7.67 km/s
test1 = circ_speed(5.9722e24,6771000)
print(test1)

#Test orbit of moon around Earth, should be ~1.02 km/s
test2 = circ_speed(5.9722e24,385000000)
print(test2)