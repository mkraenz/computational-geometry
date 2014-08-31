'''
Created on 31.08.2014

@author: proSingularity
'''

import matplotlib.pyplot as plt
from comp_convex_hull.ConvexHull import ConvexHull

class ConvexHullView(object):
    '''
    classdocs
    '''


    def __init__(self, points):
        hull = ConvexHull(set(points))
        hullpoints = hull.graham_scan_as_list()
        hullpoints.append(hullpoints[0])
        self.draw_lines(hullpoints)
        self.draw_points(points)
        plt.show()
    def __to_coord_lists(self, points):
        ''' 
        Converts the (complex) points to a list with only x-values and a corresponding list with the y-values.
        @return: (x_coord_list, y_coord_list)
        '''
        x_list = []
        y_list = []
        for p in points:
            x_list.append(p.real)
            y_list.append(p.imag)
        return (x_list, y_list)
    
    def draw_lines(self, points):
        (x, y) = self.__to_coord_lists(points)
        plt.plot(x,y, '-') # draw lines between points
        plt.ylabel("y")
        plt.xlabel("x")
        
    def draw_points(self, points):
        (x,y) = self.__to_coord_lists(points)
        plt.plot(x,y, 'or') # draw points
        