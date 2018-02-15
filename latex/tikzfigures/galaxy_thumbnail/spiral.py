#!/bin/python3
## filename spiral.py
"""
Use PILLOW to draw a spiral
"""
import numpy as np
from PIL import Image, ImageDraw

def center(point, screen_size):
    """
    Takes a point and converts it to the appropriate coordinate system.
    Note that PIL uses upper left as 0, we want the center.
    Args:
        point (real, real): A point in space.
        screen_size (int): Size of an N x N screen.
    Returns:
        (real, real): Translated point for Pillow coordinate system.
    """
    point_x, point_y = point
    mid_screen = screen_size//2
    new_point_x = point_x + mid_screen
    new_point_y = point_y + mid_screen
    return new_point_x, new_point_y

"""
Make functions for mathematical spirals by feeding an array of theta-values.
"""
def archimedian_spiral(theta, a=1.0, b=1.0):
    r = a + b*theta
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y
def logarithmic_spiral(theta, a=1.0, b=1.0):
    r = a*np.exp(b*theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y
def hyperbolic_spiral(theta, a=1.0):
    r = a/theta
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

if __name__ == '__main__':
    None
