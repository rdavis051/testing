'''
Purpose:
        This module was created to count all of the Sundays that occur
        between two use specified dates where the 1st of the month is 
        a Sunday.
'''

import sys
from datetime import date

__version__ = "1.0"
__author__  = "Robert Davis Jr"
__date__    = "8/31/12"

# list of date objects
datelist = []

# exit status for out of sequence
date
SEQERR = 1

usage = """
Directions
    In order to properly run this program, you will have to insert two dates
    when prompted. The first date will have to proceed the second date and 
    the dates must be entered in the proper date format as shown below.

    Date Format Example: YYYY-MM-DD

---------------------------------------------------------------------------
"""

def sundayCount(startdate, enddate):
    '''
    This is the date processing portion of the code.
    It builds the date list with the proper date values.
    '''
    day = startdate.day
    month = startdate.month
    year = startdate.year

    # If startdate is in the month of December - increments date if needed
    if (day != 1):
        day = 1
        month += 1
        if (month > 12):
            month = 1
            year += 1
    date_to_check = date(year, month, day)

    # Builds list of Sundays
    while (date_to_check <= enddate):
        if (date_to_check.weekday() == 6):
            datelist.append(date_to_check)
        # Increments date to next year if date is in December
        month += 1
        if (month > 12):
            month = 1
            year += 1
        date_to_check = date(year, month, day)

# Begin execution of main
if __name__ == '__main__':
    '''
    This function grabs the input from the user to determine
    the range the user would like to have checked.
    '''

    print(usage)
    try:
        firstdate = input("Please enter first date: ")
        firstdate = str(firstdate)
        firstdate = firstdate.split("-")
        secondate = input("Please enter second date: ")
        secondate = str(secondate)
        secondate = secondate.split("-")
        start_date = date(int(firstdate[0]), int(firstdate[1]), int(firstdate[2]))
        end_date = date(int(secondate[0]), int(secondate[1]), int(secondate[2]))

        # catches start date that preceds end date in time
        if (start_date > end_date):
            print("**First date must precede Second date in time**")
            print("--PROCESSSING HALTED - please try again--")
            sys.exit(SEQERR)

        # process dates
        sundayCount(start_date, end_date)
        print("Sum of months that meet this criteria: " + str(len(datelist)))
        print("List of months:")
        # prints out all objects in list
        for date in datelist:
            print(date)
    except ValueError as e:
        print("ValueError: Input data must be of Date Format: YYYY-MM-DD: ")
    except NameError as e:
        print("NameError: Input data must be of Date Format: YYYY-MM-DD: ")

# end of program
