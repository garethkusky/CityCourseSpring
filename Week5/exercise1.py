__author__ = 'acpb968'
#Write a module that contains the following two functions:
#Convertsfromfeettometers
#deffootToMeter(foot):
#Convertsfrommeterstofeet
#defmeterToFoot(meter):
#The formulas for the conversion are:
#foot = meter / 0.305
#meter = 0.305 * foot
#Write a test program that invokes these functions to display the following tables:
#Feet Meters|MetersFeet
#1.0 0.305 |20.0 66.574
#2.0 0.610 |26.0 81.967
#...
#9.0 2.745 |60.0 196.721
#10.0 3.050 |66.0 213.115

def footToMeter(foot):
    meter = 0.305 * foot
    return meter

def meterToFoot(meter):
    foot = meter / 0.305
    return foot

def main ():
    print (format('Feet','<6s'),format("Meter",'<6s'), " | ", format("Meter",'<6s'), format("Feet",'<6s'))
    print ("---------------|------------------")
    #set starting feet
    #set starting meter
    curfeet=1.0
    curmeter=20.0
    for i in range (0,10):
        print (format(str(curfeet),'<6s'),format(str(footToMeter(curfeet)),'<6s')," | ",
               format(str(curmeter),'<6s'),format(str(meterToFoot(curmeter)),'<6s'))
        curfeet +=1
        curmeter +=6

main();