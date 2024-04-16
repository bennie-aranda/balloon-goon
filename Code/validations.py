"""
Tue - Feb 20, 2024
@author: Bennie Aranda

 Email Standards:
    1. For RegEx do not use WhiteSpace because RegEx utilizes WhiteSpace 
    differently
    2. Some groupings for UID will be upper/lower case characters, numbers, 
    periods and underscores
    3. REQUIREMENT is the '@' sign to establish that the input will be an EMAIL
    4. No limit on characters for Domain addrress and or TLD address
    
    Explanation of the following regEx code:
    ^ == used to look through entire input
    [] == indicate a selection set
    \w = looking for a word character
    [\w] == looking for a word character in the selection set
    +\.? == any number followed by a period 'if you find it cool and if 
    you don't then cool'

"""

def validatePhone( phone: str ) -> bool:
    response = False 
    # initialize the response variable to False
    
    if len( phone ) == 10:
        # check if the phone number has 10 digits
        if phone.isdigit( ):
            # check if the phone number consists of digits only
            response = True
            # set the response variable to True if phone number is valid
        # end inner select
    # end outer select
    
    return response
# return the validation result
# end validatePhone

def validateEmail( email: str ) -> bool:    # function to validate an email address
    import re                               # import Python's NATIVE RegEx Library

    validation = "^((\w+\.?\w+)|(\w+))@([A-Za-z0-9-]{2,})\.([A-Za-z]{2,4})$"           
                                        # ^^ the piece of regEx we test ^^

    regEx = re.compile( validation )    # COMPILE the regex CODE

    matcher = regEx.match( email )      # Build a MATCHER object

    response = False                    # Init response to False
    if matcher != None:                 # NOT without match
        response = True                 # set response to True if email is valid
        # end selection
        
        return response                 # return the validation result
# end validateEmail