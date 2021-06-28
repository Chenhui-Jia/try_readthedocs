# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:21:22 2021

@author: Administrator
"""

import numpy as np
from scipy import signal
import scipy.sparse as sps
import scipy.spatial.distance as spd

def add(self,a,b):
        """两个数字相加，并返回结果"""
        return a+b

def google_style(arg1, arg2):
        """函数功能.

        函数功能说明.

        Args:
            arg1 (int): arg1的参数说明
            arg2 (str): arg2的参数说明

        Returns:
            bool: 返回值说明

        """
        return True

def numpy_style(arg1, arg2):
        """函数功能.

        函数功能说明.

        Parameters
        ----------
        arg1 : int
            arg1的参数说明
        arg2 : str
            arg2的参数说明

        Returns
        -------
        bool
            返回值说明

        """
        return True

def create_sdm(fv_mat, num_fv_per_shingle):
        """intro
        Creates self-dissimilarity matrix; this matrix is found by creating audio 
        shingles from feature vectors, and finding the cosine distance between 
        shingles.
    
        Args
        ----
        fv_mat: np.array
            matrix of feature vectors where each column is a timestep and each row
            includes feature information i.e. an array of 144 columns/beats and 12
            rows corresponding to chroma values
        
        num_fv_per_shingle: int
            number of feature vectors per audio shingle
    
        Returns
        -------
        self_dissim_mat: np.array 
            self dissimilarity matrix with paired cosine distances between 
            shingles
        
        """
    
        [num_rows, num_columns] = fv_mat.shape
    
        if num_fv_per_shingle == 1:
            mat_as = fv_mat
        else:
            mat_as = np.zeros(((num_rows * num_fv_per_shingle),
                               (num_columns - num_fv_per_shingle + 1)))
            for i in range(1, num_fv_per_shingle + 1):
                # Use feature vectors to create an audio shingle
                # for each time step and represent these shingles
                # as vectors by stacking the relevant feature
                # vectors on top of each other
                mat_as[((i - 1)*num_rows + 1) - 1:(i*num_rows), : ] = fv_mat[:, 
                                   i - 1:(num_columns- num_fv_per_shingle + i)]
    
        # Build the pairwise-cosine distance matrix between audio shingles
        sdm_row = spd.pdist(mat_as.T, 'cosine')
        
        # Build self dissimilarity matrix by changing the condensed 
        # pairwise-cosine distance matrix to a redundant matrix
        self_dissim_mat = spd.squareform(sdm_row)
        
        return self_dissim_mat


