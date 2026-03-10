#Problem2.py
#Project Euler problem 2

from NumberTests import isEven
from NumberTests import fibonacciSequence


def main():
    nums = fibonacciSequence(4000000)
    total = 0

    for fib in nums:
        if isEven(fib):
            total += fib

    print(total)   

if __name__ == '__main__':
  main()
