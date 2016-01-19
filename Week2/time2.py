__author__ = 'acpb968'
import time
currentTime=time.time() # get current time
timeInSec=int(currentTime)
currentSecs=timeInSec % 60
totalMinutes=timeInSec // 60
currentMinute=totalMinutes % 60
totalHours=totalMinutes // 60
currentHour=totalHours % 24
print ("time is: ", currentHour,":",currentMinute,":",currentSecs)