__author__ = 'acpb968'
# In the course, the program PrimeNumberFunction.py provides the isPrime(number) function for
# testing whether a number is prime. Use this function to find the number of prime numbers less
# than 10,000.
from Week5.session5 import PrimeNumberFunction
def allPrimes(maxPrime):
    countPerLine = 20
    count = 0
    totalPrimes=0
    for i in range(maxPrime):
        if PrimeNumberFunction.isPrime(i):
            totalPrimes +=1
            if count == countPerLine: # only print 20 numbers per line
                print()
                print(str(i),end= ' ')
                count = 1
            else:
                print(str(i),end= ' ')
                count += 1

    print ("\nTotal number of primes found is ", str(totalPrimes))

def main():
    print("Output all PrimeNumbers below 10000")
    allPrimes(10000)

main()