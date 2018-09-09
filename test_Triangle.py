# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import pytest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(3,3,4),'Isosceles','3,3,4 should be isosceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(2,3,9),'NotATriangle','2,3,9 is not a triangle')

    def testInvalidInputInt(self): 
   	    self.assertEqual(classifyTriangle(2.5,3,9),'InvalidInput','2.5 is not an integer')

    def testInvalidInputZero(self): 
        self.assertEqual(classifyTriangle(0,3,5),'InvalidInput','0 is invalid')

    def testInvalidInput200(self): 
        self.assertEqual(classifyTriangle(201,3,2),'InvalidInput','201 exceeds maximum input')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

