"""
Tue - Feb 27, 2024
@author: Bennie Aranda
"""

def main( ):
    again = True
    
    while again:
        candidate = input( "Input a candidate value: " )
        print( "Results: ",
                checkValidation( candidate ) )
        if input ( "Another test? Y or N ").lower( ) != "y":
            again = False
        # end selection
    # end loop
# end function

    
    
