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
print( orig_frame.head() )

colList = [ 'Semester', 'Course', 'Section', 'Seats' ]

seatsView = orig_frame.loc[ : , colList]

print( "Our new object is of type: ", type( seatsView ) )
print( "The shape of the object is", seatsView.shape )
#===========================================================================
print( "\n\n" )
print( "Calculating Basic Descriptive Stats on seatsView" )
print( "Stats Function        Value" )

print( "Mean                %.4f" % 
        seatsView[ "Seats" ] .mean( ) )
print( "Median              %.4f" % 
        seatsView[ "Seats" ] .median( ) )
print( "Mode                %.4f" % 
        seatsView[ "Seats" ] .mode( ) )
print( "Min                 %.4f" % 
        seatsView[ "Seats" ] .min( ) )
print( "Max                 %.4f" % 
        seatsView[ "Seats" ] .max( ) )
print( "Standard Deviation  %.4f" % 
        seatsView[ "Seats" ] .std( ) )
print( "Variance            %.4f" % 
        seatsView[ "Seats" ] .var( ) )

#==========================================================================

# GROUP DATA based on one column for comparison
byCourse = orig_frame.groupby( 'Course' )

print( "\n\nMean Available Seats by Course" )

#print( byCourse[ 'Seats' ].mean() )

with pd.option_context( 'display.max_rows', None ):
    print( byCourse[ 'Seats' ].mean( ) )
# end LOGICAL SCOPE // "with"

#==========================================================================

courseAggs = byCourse.agg( { 'Seats'    : [ 'mean', 'median' ],
                             'Enrolled' : [ 'mean', 'median' ] } )

with pd.option_context( 'display.max_rows', None ):
    print( courseAggs )
# end LOGICAL SCOPE // "with"