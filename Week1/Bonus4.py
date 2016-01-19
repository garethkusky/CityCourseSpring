__author__ = 'acpb968'
# this program estimates the population growth for the next 5 years
# based on 1 birth every 40 seconds, 1 death every minute and 1 new
# imigrant every 1 min 40 seconds
currentPop=64596800
#calculate number of seconds in a year
secInYear=((60*60)*24)*365
#calculate number of minutes in a year
minInYear=(60*24)*365
# number of births per year
birthInYear=secInYear / 40
# number of deaths per year
deathInYear=minInYear
# number of imigrants per year
imiInYear=secInYear / 100
# population change per year
yearChange=(birthInYear - deathInYear) + imiInYear
# estimated population each year. based on previous year + population change
Year1=currentPop + yearChange
print ("Pulation at end of Year1= " + str(Year1))
Year2=Year1 + yearChange
print ("Pulation at end of Year2= " + str(Year2))
Year3=Year2 + yearChange
print ("Pulation at end of Year3= " + str(Year3))
Year4=Year3 + yearChange
print ("Pulation at end of Year4= " + str(Year4))
Year5=Year4 + yearChange
print ("Pulation at end of Year5= " + str(Year5))
