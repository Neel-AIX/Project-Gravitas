import numpy as np
import matplotlib as mpl

'''constants'''

G = 0.0000000000667
m1 = float(input("Enter the mass for the first body (the larger mass) (in kg): "))
m2 = float(input("Enter the mass of the second body (the smaller mass) (in kg): "))
r = float(input("Enter the initial distance between the two bodies (in m): "))

def Force_of_grav(mass1, mass2, radius, G):
    F_g = (mass1 * mass2 * G)/(radius * radius)

    return F_g

def orbital_velocity(mass1, radius, G):
    v = np.sqrt((G*mass1)/radius)

    return v

def orbital_period(velocity, radius):
    T = (2 * np.pi * radius)/velocity

    return T


def accel(mass1, radius, G):
    a = (mass1 * G)/(radius * radius)

    return a


v = orbital_velocity(m1, r, G)
print("Force of gravity is: ", Force_of_grav(m1, m2, r, G), 'N')
print("Orbital velocity is: ", orbital_velocity(m1, r, G), "m/s")
print("Orbital period is: ", orbital_period(v, r), 's')
print("Acceleration due to gravity is: ", accel(m1, r, G), "m/s^2")
