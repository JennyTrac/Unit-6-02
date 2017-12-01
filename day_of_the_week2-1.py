# created by jenny trac
# created on dec 1 2017
# program uses an enumerator to determine the user's favourite day of the week

from enum import Enum

# enumerated type for days of the week
Days_of_the_week = Enum('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')

# input
chosen_day = str.upper(raw_input("What day of the week is your favourite?  "))

# process
if chosen_day in Days_of_the_week:
    for counter in range(0,7):
        check_day = Days_of_the_week[counter]
        # output
        if str(check_day) == str(chosen_day):
            print(str(check_day) + ": " + str(counter + 1))
else:
    print("That is not a valid day of the week.")
