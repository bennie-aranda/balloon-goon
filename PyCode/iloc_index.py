#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:58:40 2024

@author: benniearanda
"""

import pandas as pd 

orig_frame = pd.read_csv( 'Data Sets/temperatureData.csv', index_col = 0)

print( orig_frame.loc[ '11/5/2021' ] )

print ( orig_frame.iloc[ 4 ] )