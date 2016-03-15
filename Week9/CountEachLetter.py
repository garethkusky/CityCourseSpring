def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r") # Open the file

    counts = 26 * [0] # Create and initialize counts
    for line in infile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)
    
    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            # ord(c) : returns an integer representing the Unicode code point of the character. This is the inverse of chr() for 8-bit strings
            # chr(i): returns a string of one character whose ASCII code is the integer i.
            letter = chr(ord('a') + i) # enables to iterate over the letters
            print(letter + " appears " + str(counts[i])
              + (" time" if counts[i] == 1 else " times"))

    infile.close() # Close file
  
# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

main() # Call the main function
