# Program Tips
# Description: 
#   a program that take the total sales of servers and takes 6 percent and splits it
# between workers. with bartenders getting 45 percent of the 6 percent and support staff splitting the rest.
#then it writes out the tip sheet in a spreadsheet file or .csv
# Author: Alex Castaneda
# Date: 5/1/23
# Revised: 
#   5/7/23

# import library modules here
import csv,  tip_functions , datetime

# Define global constants (name in ALL_CAPS)


def main():

    num_bartenders = int()
    total_bartender_hours = 0
    bartender_hours = []
    num_support_staff = int()
    total_support_hours = 0
    support_hours = []
    bartender_tips_by_hours = int()
    support_tips_by_hours = int()
    
    # Declare Variable types (EVERY variable used in this main program)


    tip_functions.calculate_tips()
    print('a spreadsheet is downloaded in folder/directory this program is saved in')



# End Program

# Function firstFunction()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def firstFunction ():

    # Declare Local Variable types (NOT parameters)

    print ( "firstFunction" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function firstFunction()

if ( __name__ == "__main__" ):
    main()
# if running standalone


#****************************************************************
#   blank layout for adding more functions                      *
#****************************************************************

# Function stub()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def stub ():

    # Declare Local Variable types (NOT parameters)

    print ( "stub" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function stub()




