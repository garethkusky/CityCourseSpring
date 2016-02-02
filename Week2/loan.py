__author__ = 'acpb968'
# promt user to enter interest rate, loan amount and duration. output monthly payments
interestRate=eval(input("please enter annual interest rate: "))
monthlyInterest=interestRate / 1200
loanAmount=eval(input("please enter loan amount: "))
term=eval(input("Please enter number of years for loan repayment: "))
monthlyPayment=loanAmount * monthlyInterest / (1 - 1/(1 + monthlyInterest)**(term*12))
totalPayment=monthlyPayment * term * 12
print ("monthly payment is " + str(int(monthlyPayment *100)/100))
print("Total payment is " + str(int(totalPayment *100)/100))
