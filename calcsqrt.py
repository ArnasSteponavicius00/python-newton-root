#! /usr/bin/env python3

# Arnas Steponavicius
# Calculate the square root of a number.

def sqrt(x):
    """
    Calculate the square root of argument x
    """
    # Check x is positive
    if x < 0:
        print("Error: Negative value given")
        return -1
    else:
        print("Calculating..")
    
    # Initial guess for the square root
    z = x / 2.0
    
    # Continously improve guess
    # Adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.0000001:
        z = z - ((z*z) - x) / (2 * z)
    
    return z

myval = float(input("Enter Value: "))

print("Square root of ",myval," is ", sqrt(myval))
