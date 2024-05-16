"""
Tue - Feb 27, 2024
@author: Bennie Aranda
"""

import re

testCases = [ "terri.davis",
              "terri_davis",
              "terriDavis666",
              "79someoneElse",
              "x",
              "t3rri_d@vis",        # special characters were able to pass through
              "t3rri!d4vis"]        # will fix this on thursday

testThis = "^(\w+\.?\w+)|(\w+)@[A-Za-z0-9-]{2,}\.[A-Za-z]{2,4}$"           
            # the piece of regEx we test

# Other Regex Examples:
 #1. [\w+\.?\w+]
 #2. ^(\w+\.?\w+)\(\w+)@[A-Za-z0-9-]{2,}\.[A-Za-z]{2,4}$
 # ^ this character is a sequence modifier: Start w/ char 0
 #  ^ begin a grouping
 #    ^ word class

regEx = re.compile( testThis )      # COMPILE the regex CODE

for each in testCases:
    matcher = regEx.match( each )   # Build a MATCHER object
    # and then tie regEx to what we want to test
    
    response = False
    if matcher != None:             # NOT without match
        response = True
    # end selection
    
    print ( "Candidate: %s returns %s," %
           ( each, response ) )
# end for loop