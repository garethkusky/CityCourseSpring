#Reverse a string
#Write a function that reverses a string. The header of the function is:
#defreverse(s):
#Write a test program that prompts the user to enter a string, invokes the reverse
#function, and displays the reversed string

def reverseString (inString):
    reverse=''
    for i in range(0,len(inString)):
        letter=inString[i:i+1]
        reverse=letter+reverse

    return reverse

def main():
    inString=input("Please enter a string to be reversed:")
    print(inString, "reversed is", reverseString(inString))

main()