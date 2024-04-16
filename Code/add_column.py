#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:08:18 2024

@author: benniearanda
"""

import pandas as pd

orig_frame = pd.read_csv( 'Data Sets/ISCS_Scheds_5YR.csv' )

"""
    We will ADD a COLUMN to the DataFrame to gold "Utilization".
    This is the RATION of 'Enrolled' to 'Seats', carried as a 
    float/double value.
"""

orig_frame[ 'Utilization' ] = orig_frame[ 'Enrolled' ] / orig_frame[ 'Seats' ]

"""
    Take a 'slice' of the Frame with Semester, Course, Section, Utilization
"""

colList = [ 'Semester', 'Course', 'Section', 'Utilization' ]
util_slice = orig_frame.loc[ : , colList ]


"""
    We can use a "MASK" to "hide" rows we do not want to condier in our
    calculations/analysis.
"""

mask = ( orig_frame[ 'Status' ] != 'CANCELED' )

filter_frame = orig_frame[ mask ]


clean_data = filter_frame.loc[ : , [ 'Semester', 'Course', 'Section', 'CRN',
                                     'Enrolled', 'Utilization', 'Fees', 
                                     'Instructor' ] ]

# We want to KEEP this "cleaned up" version of our data....
analysis_data = pd.DataFrame( clean_data )


# REALLY for KEEPS
analysis_data.to_pickle( 'pickleSched.pkl')








                               
                                
                                