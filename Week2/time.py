__author__ = 'acpb968'
timeInSec=eval(input("please enter the time in seconds:"))

totalMinutes=timeInSec // 60
totalHours=totalMinutes // 60
currentMinute=totalMinutes % 60
currentHour=totalHours % 24
#remainSecs=timeInSec - (totalMinutes*60) -(totalHours*60*60)
currentSecs=timeInSec % 60
print ("time is: ", currentHour,":",currentMinute,":",currentSecs)
