---
title: '`ah`: A Python Package for creating Aligned Hierarchies'
tags:
  - Python
  - Music Information Retrieval
  - Structure representations

authors:
  - name: Adrian M. Price-Whelan^[Custom footnotes for e.g. denoting who the corresspoinding author is can be included like this.]
    orcid: 0000-0003-0872-7098
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Author Without ORCID
    affiliation: 2
  - name: Author with no affiliation
    affiliation: 3
affiliations:
 - name: Name, Position (if relevant), Affiliation
   index: 1
 - name: Institution Name
   index: 2
 - name: Independent Researcher
   index: 3
date: DD Month YYYY
bibliography: joss.bib

---

# Abstract

AH is a python package that contributes to the efforts in the MIR community towards increased accessibility and reproducibility. This package is based on Katherine M. Kinnaird?s thesis {Aligned Hierarchies for Sequential Data} and the accompanying MATLAB code. In Kinnaird's work, over 70 Matlab scripts build the Aligned Hierarchies. Improving upon Kinnaird's work, our package provides further accessibility and opportunity for reproducibility. Now written in python, ah creates aligned-hierarchies of music based data streams through finding and encoding repeated structures. The package is organized into four modules - utilities, search, transform and assemble - that work in tandem to extract and output the aligned hierarchies of music data. The package includes five vignettes that provide full detailed explanation of how each function works with examples and images. An overarching vignette is also provided with an example input of a Mazurka score that walks the user through the process and logic of the package. In addition to the framing and documentation of the package, ah includes unit tests for all functions and are organized by the modules. 


# 1. Introduction 

In this paper, we introduce a python package, ah, which provides instructions to build aligned hierarchies from a given input. The input is a sequential stream of data and through the approach in to the dimension reduction problem, our package creates representations, called aligned hierarchies. These representations are created by finding all repeated structures within the sequential stream of data. In the overarching vignette, called AH_example, which walks the user through the process and logic of the algorithm with examples and images, the sequential stream of data input is of a Mazurka score. This vignette highlights the structure of the algorithm, detailing when and from where functions are called. For clarity and deeper comprehension of how the aligned hierarchies are built, we distinguished the functions by their main purposes in the algorithm. Some are considered utilities functions since they are repeatedly used throughout the function by different modules. Others are responsible for searching for and recording structures or managing the transformation of inputs for use in larger functions. Finally, there are functions that assemble every extracted information from the input digital score to create the essential structure of the aligned hierarchies....

- include a general introduction to MIR? 
- include motivation for the paper and package 
- include the packages we repy on, numpy etc.
- why we chose to convert to python insetad of keeping MATLAB
- related work: librosa, 
- follows in the trend of MIR software 

Talk about librosa  
- package inspiration 
- inspired by the structure?
- wanted something similar of use 
- visualizations to help understanding, similar to librosa 

# Statement of Need 
- look at a few JOSS papers 
    - these papers explain the problem at hand and what scientists do right now to overcome that problem
    - at the end state that this package is a solution to this problem 
    - intended users?
    

# Module Organization
- This package is made up of 4 modules, as well as an example module, which runs a full example. 
- The utilities module includes functions that are repeatedly used throughout to allow larger functions in the modules to function
- The search module has functions that find the various repeated structures and generate information about them, such as their width and annotations
- The functions in the transform module change their inputs to be of use in the larger functions of assemble.py. The transformations mainly include removing overlapping repeats of the same width and annotation.
- The assemble module assembles the aligned hierarchies with functions that first create the essential structure components and then piece them together to create the final product. 
[@Kinnaird:2014] 

[@MuellerZ19_FMP_ISMIR]

[@brian_mcfee-proc-scipy-2015]

[@amen]

[@Raffel14mir_eval:a]

[@Bittner19mirdata]



# References


