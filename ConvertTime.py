# ConvertTime.py
# Alexander Croteau

# methods 
# hours to seconds
def hoursToSeconds(hours):
    hours = (hours * 60) * 60
    return hours

# minutes to seconds
def minutesToSeconds(minutes):
    minutes = minutes * 60
    return minutes

# values
hours = 0
minutes = 0
convertedHours = 0
convertedMinutes = 0
finalSeconds = 0

# input
print("This program is intended to convert hours and minutes into seconds")
print("Please enter the amount of hours and minutes")
hours = int(input())
minutes = int(input())

# call functions
convertedHours = hoursToSeconds(hours)
convertedMinutes = minutesToSeconds(minutes)
finalSeconds = convertedHours + convertedMinutes

# output
print("The hours and minutes have been converted and the final output is", finalSeconds)
