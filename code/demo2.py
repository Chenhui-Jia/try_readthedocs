# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:24:32 2021

@author: Administrator

utilities.py 

This script when imported as a module allows search.py, transform.py and 
assemble.py in the ah package to run smoothly. 

This file contains the following functions:
    
    * create_sdm - Creates a self-dissimilarity matrix; this matrix is found 
    by creating audio shingles from feature vectors, and finding cosine 
    distance between shingles. 
    
    
    * find_initial_repeats - Finds all diagonals present in thresh_mat, 
    removing each diagonal as it is found.
"""


def my_function(a, b):
    """函数功能说明

     >>> my_function(2, 3)
     6
     >>> my_function('a', 3)
     'aaa'

    """
    return a * b