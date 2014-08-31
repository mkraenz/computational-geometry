'''
Created on 31.08.2014

@author: proSingularity
'''
from util.point_generator import point_generator
from comp_convex_hull.ConvexHullView import ConvexHullView

points = point_generator(100, 2000)
ConvexHullView(points)