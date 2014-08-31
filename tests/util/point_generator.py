'''
Created on 31.08.2014

@author: proSingularity
'''
from random import uniform

def point_generator(number, radius):
    ''' generates a list of number many randomized points in the plane with norm <= radius '''
    return [complex(uniform(-radius, radius), uniform(-radius, radius)) for i in range(number)]
