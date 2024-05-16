# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:43:06 2024

@author: maris
"""

import pandas as pd

orig_frame = pd.read_csv( 'Data Sets/ISCS_Scheds_5YR.csv' )

'''
let's take a look at our "frame"...
'''
print( "The object orig_frame is a %s" % type( orig_frame ) )
print( "The object orig_frame contains %d elements" % len( orig_frame) )

print( "The DataFrame orig_frame has the SHAPE",
      orig_frame.shape )
rows, columns = orig_frame.shape


columnNames = orig_frame.columns
print( "Coungt of columns in orig_frame:",
      len( columnNames ) )
print( columnNames )

#===========================================================================

print( "\n\n" )
print( orig_frame.loc[ 17 ] )

















