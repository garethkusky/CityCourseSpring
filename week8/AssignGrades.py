__author__ = 'acpb968'

def main():
    grades=[int(y) for y in input("Please input a list of grades").split()]


    for x in range(0,len(grades)):
        best=checkBest(grades)
        grade=checkGrade(grades[x], best)
        print ("Student",str(x),"score is", str(grades[x]), "and grade is", grade)

def checkGrade(score=0, best=0):
    if score>= best - 10:
        grade="A"
    elif score>= best - 20:
        grade="B"
    elif score>= best - 30:
        grade="C"
    elif score>= best - 40:
        grade="D"
    else:
        grade="F"

    return grade

def checkBest(scores):
    best=0
    for x in range(0,len(scores)-1):
        if scores[x]> best:
            best=scores[x]

    return best

main()