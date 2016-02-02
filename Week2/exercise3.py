#Exercise 3: Financial application, investment amount
#Write a program that prompts the user to enter final account value, annual interest
#rate in percent, and the number of years, and displays the initial deposit amount
amount, interestRate, years = eval(input("Please enter the final balance, Annual interest rate percentage and num of years:"))
months=years*12
monthlyInterestRate=interestRate / 1200
initalDeposit=amount/(1+monthlyInterestRate)**months
print("Initial Deposit amount: " + str(initalDeposit))