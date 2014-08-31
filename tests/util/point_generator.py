'''
Created on 31.08.2014

@author: proSingularity
'''
from random import uniform
from random import normalvariate

def point_generator_uniform(number, radius):
    ''' generates a list of number many randomized points in the plane with norm <= radius '''
    return [complex(uniform(-radius, radius), uniform(-radius, radius)) for i in range(number)]


def point_generator_normalvariate(number, radius):
    ''' generates a list of number many randomized points in the plane with norm <= radius '''
    return [complex(normalvariate(-radius, radius), normalvariate(-radius, radius)) for i in range(number)]
