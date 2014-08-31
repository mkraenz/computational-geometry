'''
Created on 31.08.2014

@author: proSingularity
'''
from util.point_generator import point_generator_uniform, point_generator_normalvariate
from comp_convex_hull.ConvexHullView import ConvexHullView

points = point_generator_uniform(100, 2000)
ConvexHullView(points)

points2 = point_generator_normalvariate(10000, 2000)
ConvexHullView(points2)