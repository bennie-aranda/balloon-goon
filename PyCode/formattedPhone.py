"""
Tue - Feb 6, 2024
@author: Bennie Aranda
"""

def formatPhone( number ) -> str: 
    # this arrow makes it so that it will only return a STRING

    if number == None:
        # phone number NOT entered
        formattedPhone = "Missing Phone Number"

    else:
        if number == 0:
            # phone number INCORRECTLY entered
            formattedPhone = "Invalid Phone Number"

        else:
            if isinstance( number, int ): 
                phoneStr = str( number )

                if len( phoneStr ) == 10:
                    # Example: 3615631821

                    formattedPhone = '(' + phoneStr[ 0:3 ] 
                    # start from index 0 and end with index 3
                    formattedPhone = formattedPhone + ') '
                    formattedPhone = formattedPhone + phoneStr[ 3:6 ]
                    # start index 3 and end with index 6
                    formattedPhone = formattedPhone + '-'
                    formattedPhone = formattedPhone + phoneStr[ 6: ]
                    # start index 6 and completely stop after the final index

                    # Example Output: (361) 563-1821

                else:
                    formattedPhone = "Phone number wrong length."

            else:
                formattedPhone = "Phone number contain invalid characters"
        return formattedPhone

# end of function
"""
    TESTING the function that we created for formatting a phone number.
    We will send a GROUP of "candidate" phone numbers to the function, one
    at a time, and collect the results of each test.
"""

# CREATE a GROUP of TEST CASES
testCases = [ 2104584208,
              2104586300,
              0,
              None,
              21045842089,
              210458420,
              '210458420A'
             ]

# Now, we will use our TESTCASES, sending each one to the function to be 
# tested
candidate = 0

for each in testCases:
    candidate += 1
    print( "Running Test Case #%d and using value: %s" %
          ( candidate,
           each ) )
    print( "\t\t^", formatPhone( each ), "^" )
    print() 
# end iteration




