"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Only numbers greaater than 0")
    else:
        list = []
        primeCount = 0
        loopCount = 1
        while primeCount < number_of_primes:
            loopCount += 1
            for y in range(2, loopCount):
                if loopCount % y == 0:
                    break
            else:
                list.append(loopCount)
                primeCount += 1
        return list
