'''
Created on 28.08.2014

@author: proSingularity
'''

from copy import copy as copy
from cmath import phase as phase

class ConvexHull(object):
    '''
    Operates on complex numbers as if they where 2 dim real-valued vectors, i.e. points in the plane.
    '''

    def __init__(self, points):
        '''
        Constructor
        @param points: a set or a list of points, in form of complex numbers, in the plain.
        '''
        self.__points = copy(list(points))
        
    def get_points(self):
        return self.__points
    
    def set_points(self, points):
        
        self.__points = copy(list(points))
        
    def find_min_y_index(self, points):
        y_list = [c.imag for c in points]
        return y_list.index(min(y_list))
    
    def normalize(self, origin, points):
        ''' sets @param origin as new coordinate origin and translates the other points accordingly '''
        return [c - origin for c in points]
    
    def sort_by_phase(self, points):
        ''' @return: points ordered by their angle w.r.t. to the origin. '''
        return sorted(points, key=phase)
    
    def sort_by_real(self, points):
        return sorted(points, key=self.__get_real )
    
    def ccw(self, a, b, c): 
        return (b.real-a.real) * (c.imag - a.imag) - (b.imag - a.imag) * (c.real - a.real)
        
    def is_ccw(self, a, b, c):
        return (True if self.ccw(a, b, c) >= 0 else False )
    
    def __get_real(self, complex):
        return complex.real
    
    def graham_scan(self):
        ''' 
        Perform the Graham scan Algorithm with the point of set, that is given to this ConvexHull instance.
        @return: A set containing the points on the convex hull.
        '''
        points = self.sort_by_real(self.get_points())
        n = len(points)
        
        min_index = self.find_min_y_index(points)
        origin = points[min_index]
        points[0], points[min_index] = points[min_index], points[0]
        
        points = self.normalize(origin, points)
        points[1:] = self.sort_by_phase(points[1:])
        res = points[:] #copies points
        M = 2
        
        for i in range(3,n):
            while not self.is_ccw(res[M-1],res[M], points[i]):
                del res[M]
                M -= 1
                
            M += 1
        return set(self.normalize(-origin, res))
