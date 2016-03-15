from string import ascii_lowercase
from collections import Counter


def main():
    filename = input("Enter a filename: ").strip()
    with open(filename) as f:
        print\
            (Counter(letter for line in f
                      for letter in line.lower()
                      if letter in ascii_lowercase))

main()