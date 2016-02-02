#Exercise1
#Write a program that converts pounds into kilograms. The program prompts the user to enter a
#value in pounds, converts it to kilograms, and displays the result. One pound is 0.454
#kilograms
pounds=eval(input("Please enter weight in pounds: "))
kilos=pounds * 0.454
print(str(pounds) + " is " + str(int(kilos*100)/100) + " kilograms" )
 