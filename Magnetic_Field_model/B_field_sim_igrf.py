import igrf
import pymap3d as fc
import numpy as np

def magnetic_field_eci(time,latitude,longitude,altitude):
    magnetic_field_ned = igrf.igrf(time,latitude,longitude,altitude)
    magnetic_field_eci = fc.ecef2eci(fc.ned2ecef(magnetic_field_ned))
    print(magnetic_field_eci)

    return magnetic_field_eci

alt = np.array([6300])
ig = igrf.igrf(1900.0, 175, -150, alt)



#magnetic_field_eci(2015.0,60,60,600)
#print(ig)


