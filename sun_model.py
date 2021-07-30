from astropy.coordinates import get_sun
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.time import Time
import numpy as np


def julian_to_calendar(jd):
    '''
    converts julian date into calendar date of format 'iso'. 'iso' is a string format mentioning the year, month, day, hour, minute, second, and microsecond.

    param jd: julian date 
    type jd: float

    returns: calendar date
    '''
    t = Time(jd, format='jd', scale='utc')
    t.format = 'iso'
    return (t)

#print(calendar_to_julian('2014-03-17T23:25:30'))


def sun_vec_earth_sun(t):
    '''
    calculates sun_vector at time t

    param t: time in iso format
    type t: string

    returns: sun_vector
    '''
    sun = get_sun(t)
    c = SkyCoord(sun)
    return (c)


def sun_vec(t):
    calender_date = julian_to_calendar(t)
    s_v_earth_sun = sun_vec_earth_sun(calender_date)
    current_positition = orbit_propagator(t).r

    sun_vec = s_v_earth_sun - current_positition

    return (sun_vec)






time = julian_to_calendar(2457163.5)
print(time)

sun_vec = sun_model(time).cartesian*u.km
sun_vec_km = sun_vec * 1.496 * 10**8

print(sun_vec_km)


