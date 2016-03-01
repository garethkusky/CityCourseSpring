#Check password
#Some Web sites impose certain rules for passwords. Write a function that checks whether a string is a valid
#password. Suppose the password rules are as follows:
#■ A password must have at least eight characters.
#■ A password must consist of only letters and digits.
#■ A password must contain at least two digits.
#Write a program that prompts the user to enter a password and displays valid password if the rules are
#followed or invalid password otherwise.

def main():
    password=input("please enter your password: ")
    # initialise pwCheck as True
    pwCheck=True

    # check length is at least 8 chars
    if len(password) >= 8:
        #check password is alphanumeric
            if password.isalnum():
                # check password contains at least 2 digits
                nbDigits=0
                for i in range(0,len(password)):
                    letter=password[i:i+1]
                    if letter.isdigit():
                        nbDigits+=1

                if nbDigits < 2:
                    pwCheck=False
            else:
                pwCheck=False
    else:
        pwCheck=False

    if pwCheck:
        print("valid password")
    else:
        print ("Invalid Password")

main()