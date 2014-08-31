'''
Created on 25.08.2014

@author: proSingularity
'''
import unittest
from copy import copy
from comp_convex_hull.ConvexHull import ConvexHull as ConvexHull
from comp_convex_hull.ConvexHullView import ConvexHullView
from util.point_generator import point_generator_uniform


class ConvexHullTests(unittest.TestCase):

    def get_list_one_point(self):
        return [1 + 2j]

    def get_list_five_points(self):
        return [10 + 5j, 0j, -199 + 32j, -10 + 0j, 123 + 1j]

    def get_list_five_points_ordered(self):
        list_ordered = [0j, -10 + 0j, 123 + 1j, 10 + 5j, -199 + 32j]
        return list_ordered

    def test___init__(self):
        points = self.get_list_one_point()
        hull = ConvexHull(points)
        self.assertEqual(hull.get_points(), self.get_list_one_point())
            
    def test_copy(self):
        points = self.get_list_one_point()
        self.assertIsNot(points, copy(points))
        
    def test_find_min_y_index_ordered(self):
        points = self.get_list_five_points_ordered()
        hull = ConvexHull(points)
        self.assertEqual(hull.find_min_y_index(points), 0)
        
    def test_sort_by_phase_ordered(self):
        points = [1 + 0j, 1 + 1j, 1 + 2j, 0 + 1j, -1 + 1j, -1 + 0j]
        hull = ConvexHull(points)
        self.assertEqual(hull.sort_by_phase(points), points)
        
    def test_sort_by_phase_disordered(self):
        disordered_points = [-1 + 1j, -1 + 0j, 1 + 1j, 1 + 0j, 1 + 2j, 0 + 1j]
        hull = ConvexHull(disordered_points)
        solution = [1 + 0j, 1 + 1j, 1 + 2j, 0 + 1j, -1 + 1j, -1 + 0j]
        self.assertEqual(hull.sort_by_phase(disordered_points), solution)
        
    def test_normalize(self):
        hull = ConvexHull([2 + 2j, 1 + 1j])
        normalized_points = hull.normalize(1 + 1j, hull.get_points())
        self.assertEqual(normalized_points, [1 + 1j, 0j])
        normalized_points = hull.normalize(0j, hull.get_points())
        self.assertEqual(normalized_points, [2 + 2j, 1 + 1j])
        
    def test_sort_by_real(self):
        points = [1 + 0j, 0j]
        hull = ConvexHull(points)
        self.assertEqual(hull.sort_by_real(points), [0j, 1 + 0j])
        
    def test_graham_scan_nothing_to_do(self):
        points = [0j, 2 + 0j, 2 + 2j, 2j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set(points))
    
    def test_graham_scan_easy_sorted_normed(self):
        points = [0j, 2 + 0j, 1 + 0.5j, 2 + 2j, 2j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set([0j, 2 + 0j, 2 + 2j, 2j]))
        
    def test_graham_scan_easy_sorted_normed2(self):
        points = [0j, 2 + 0j, 1 + 0.5j, 1 + 0.8j, 2 + 2j, 2j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set([0j, 2 + 0j, 2 + 2j, 2j]))
        
    def test_graham_scan_easy_normed(self):
        points = [0j, 2 + 2j, 2 + 0j, 1 + 0.5j, 1 + 0.8j, 2j ]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set([0j, 2 + 0j, 2 + 2j, 2j]))
        
    def test_graham_scan_easy_normed2(self):
        points = [ 2 + 2j, 2 + 0j, 1 + 0.5j, 1 + 0.8j, 2j, 0j ]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set([0j, 2 + 0j, 2 + 2j, 2j]))
        
    def test_graham_scan_easy_normed3(self):
        points = [ 2 + 2j, -2 + 0j, 1 + 0.5j, 1 + 0.8j, 2j, 0j ]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set([-2 + 0j, 0j, 1 + 0.5j, 2 + 2j, 2j]))
        
    def test_graham_scan_easy(self):
        points = [ 2 + 2j, -2 + 0j, 1 + 0.5j, 1 + 0.8j, 2j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set([-2 + 0j, 1 + 0.5j, 2 + 2j, 2j]))
        
    def test_graham_scan_one_point(self):
        hull = ConvexHull([1 + 1j])
        self.assertEqual(hull.graham_scan(), set([1 + 1j]))
           
    def test_graham_scan_two_points(self):
        hull = ConvexHull([1 + 1j, 2 + 0.5j])
        self.assertEqual(hull.graham_scan(), set([2 + 0.5j, 1 + 1j]))
    
    def test_graham_scan_two_lin_dependant_points_sorted(self):
        points = [0j, 1 + 1j, 2 + 2j, 2j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), set(points))
        
    def test_graham_scan_two_lin_dependant_points(self):
        hull = ConvexHull([0j, 2 + 2j, 1 + 1j, 2j])
        self.assertEqual(hull.graham_scan(), set([0j, 1 + 1j, 2 + 2j, 2j]))
        
    def test_graham_scan_many_uninteresting_points(self):
        solution = [0 + -2j, 2 + 0j, 2j, -2 + 0j]
        l = point_generator_uniform(10000, 1) + solution
        hull = ConvexHull(l)
        solutionset = set(solution)
        self.assertEqual(hull.graham_scan(), solutionset)
        
    def test_graham_scan_same_points1(self):
        points = [1j, 1j, 1j, 2j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), {1j, 2j})
        
    def test_graham_scan_same_points2(self):
        points = [1j, 1j, 1j]
        hull = ConvexHull(points)
        self.assertEqual(hull.graham_scan(), {1j})
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
