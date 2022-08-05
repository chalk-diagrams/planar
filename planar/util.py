#############################################################################
#
# Copyright (c) 2010 by Casey Duncan and contributors
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD License
# A copy of the license should accompany this distribution.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#
#############################################################################

import math

# Define assert_unorderable() depending on the language 
# implicit ordering rules. This keeps things consistent
# across major Python versions
def assert_unorderable(a, b):
    """Assert that a and b are unorderable"""
    return NotImplemented

def cached_property(func):
    """Special property decorator that caches the computed 
    property value in the object's instance dict the first 
    time it is accessed.
    """

    def getter(self, name=func.__name__):
        try:
            return self.__dict__[name]
        except KeyError:
            self.__dict__[name] = value = func(self)
            return value
    
    getter.__name__ = func.__name__
    return property(getter, doc=func.__name__)

def cos_sin_deg(deg):
    """Return the cosine and sin for the given angle
    in degrees, with special-case handling of multiples
    of 90 for perfect right angles
    """
    deg = deg % 360.0
    if deg == 90.0:
        return 0.0, 1.0
    elif deg == 180.0:
        return -1.0, 0
    elif deg == 270.0:
        return 0, -1.0
    rad = math.radians(deg)
    return math.cos(rad), math.sin(rad)


# vim: ai ts=4 sts=4 et sw=4 tw=78

