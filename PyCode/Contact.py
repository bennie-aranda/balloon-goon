"""
  This code DESCRIBES an object of class Contact, its 
  attributes & its operations.

  Attributes:
      Last name,
      first name,
      phone number,
      email address
"""
# Must use "self" when def in a class
class Contact:
  
  # "*args" means some data will follow
  def __init__( self, *args ):
    
    # if all instance vars present
    if len( args ) == 4:
      # do something
      self.first = args[ 0 ] # first name attribute
      self.last = args[ 1 ] # last name attribute
      
      # checking whether the phone number is an int, otherwise set a default value
      if isinstance( args[ 2 ], int ):
        self.phone = args[ 2 ] # Phone number attribute
        
      else:
        self.phone = 2105550000 # Default phone number
        # end selection
        self.email = args[ 3 ] # Email address attribute
        # end of FULL CONSTRUCTOR code
    
    else:
      # NULL CONSTRUCTOR
      # Create a NULL/EMPTY object
      self.first = '' # Init first name attribute
      self.last = '' # Init last name attribute
      self.phone = 0 # Init phone name attribute
      self.email = '' # Init email name attribute
  # end of selection

# end of constructor ===========================================================

  """
    NAME:
        formattedPhone

    PARAMETERS:
        None
        Instance variable phone is retreived from object.

    RETURNS:
        A formatted string containinge EITHER the formatted phone number
        OR an error message

    PROCESS:
        Check for presence of an argument value
        Check for argument type (should be an int)
        Cast argument to string
        Check for argument length (==10)
        If all tests are passed:
            format and return the phone number
        Else
            return error message
  """

  def formatPhone( self ) -> str:
    number = self.phone
    # this arrow = only return a STRING

    if number == None:
      # phone number NOT entered
      formattedPhone = "Missing Phone Number"

    else:
      if isinstance( number, int ):
        phoneStr = str( number ) # convert phone number to a string
        if len( phoneStr ) == 10: #check the phone number length
          
          # the following puts phone number into the format wanted '(222) 222-222'
          
          formattedPhone = '(' + phoneStr[ 0:3 ]
          # start from index 0 and end with index 3
          formattedPhone = formattedPhone + ') '
          formattedPhone = formattedPhone + phoneStr[ 3:6 ]
          # start index 3 and end with index 6
          formattedPhone = formattedPhone + '-'
          formattedPhone = formattedPhone + phoneStr[ 6: ]
          # start index 6 and completely stop after the final index
        else:
          """
          This error message could be thrown when:
          number = 0
          len ( number ) <> 10
          """
          formattedPhone = "Phone number wrong length."

      else:
        formattedPhone = "Phone number includes invalid characters."
      # end outer selection

    return formattedPhone

  # end function

  def produceContactCard( self ) -> str:
    """
    This function returns a string that is a product of the contact card.
    """
    card = ''

    card = card + self.last + ", " + self.first + "\n" # add last and first name
    card = card + self.formatPhone( ) + "\n" # add formated phone number to contact card
    card = card + self.email + "\n" # add email address to contact card

    return card

  def __str__( self ) -> str:
    return self.produceContactCard( )

  # end toString function
