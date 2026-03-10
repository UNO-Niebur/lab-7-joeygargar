#NumberTests.py

def isThreeOrFive(n):
    return n % 3 == 0 or n % 5 == 0


def isPrime(p):
    if p < 2:
        return False

    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False

    return True


def isEven(n):
    return n % 2 == 0


def addNum(numList, num):
    if num not in numList:
        numList.append(num)


def fibonacciSequence(value):
    nums = [1, 2]

    while True:
        n = nums[-1] + nums[-2]
        if n >= value:
            break
        addNum(nums, n)

    return nums


def main():
    knownPrimes = [2, 3, 5, 7, 11, 13, 17]
    knownNonPrimes = [0, 1, 4, 6, 8, 9, 10, 12]

    print("Testing isPrime...")
    for num in knownPrimes:
        print(num, isPrime(num))

    for num in knownNonPrimes:
        print(num, isPrime(num))

    num = int(input("Enter a number: "))

    if isPrime(num):
        print("%d is a prime number" % num)
    else:
        print("%d is not a prime number" % num)

    if isEven(num):
        print("%d is an even number" % num)
    else:
        print("%d is not an even number" % num)



if __name__ == '__main__':
    main()
