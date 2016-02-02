#Exercise 2: Financial application, calculate tips
#Write a program that reads the subtotal and the gratuity rate and computes the gratuity and
#total. For example, if the user enters 10 for the subtotal and 15% for the gratuity rate, the
#program displays 1.5 as the gratuity and 11.5 as the total
subTotal, gratuityRate=eval(input("Please enter the subtotal and gratuity rate percent: "))
gratuity=(subTotal / 100)*gratuityRate 
total=subTotal + gratuity
print("Subtotal: " + str(subTotal))
print("Gratuity at " + str(gratuityRate) + "% is " + str(int(gratuity*100)/100) )
print("Total is: " + str(int(total*100)/100)) 