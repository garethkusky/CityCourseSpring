# Exercise 1: Financial application: payroll
# Write a program that reads the following information and prints a payroll statement:
# Employees name (e.g., James)
# Number of hours worked in a week (e.g., 10) Hourly pay rate (e.g., 9.75)
# Tax withholding rate (e.g., 20%) other tax withholding rate (e.g., 9%)

empName=input("Enter Employees Name: ")
hoursWorked=eval(input("Enter Number of hours worked in week: "))
payRate=eval(input("Enter hourly pay rate: "))
taxRate=eval(input("Enter tax witholding Rate: "))
otherTaxRate=eval(input("Enter other tax witholding Rate"))

# Work out gross pay
grossPay=hoursWorked * payRate

#tax deduction calcualtions
taxRatePercent=format(taxRate,'<10.2%')
taxToPay=grossPay * taxRate
otherTaxRatePerc=format(otherTaxRate,'<10.2%')
otherTaxToPay=(grossPay - taxToPay) * otherTaxRate
totalDeductions=taxToPay+otherTaxToPay

#Final Salary
netPay = grossPay - totalDeductions

#Print Statements
print ("Employee Name: " + str(empName))
print ("Hours Worked: " +  str(hoursWorked))
print ("Pay Rate: " + str(payRate) )
print ("Gross Pay: " +  str(grossPay))
print ("Deductions: \nTax Withholding ( " + str(taxRatePercent) + "): " +  str(taxToPay))
print ("Other Tax Withholding ( " + str(otherTaxRatePerc) +"): " +  str(otherTaxToPay))
print ("Total Deduction: " +  str(totalDeductions))
print ("Net Pay: " + str(netPay) )