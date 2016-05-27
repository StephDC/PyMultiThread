#! /usr/bin/python3

import os
import sys
import time
import PyMultiThread

def sqrt(inputNum):
    return int(inputNum ** 0.5)

# Returns a random int with length of x bytes.
def randNum(length=1):
    return int.from_bytes(os.urandom(length),'big')

# Returns True if Num2 is a factor of Num1
def divTest(nums):
    return not bool(nums[0] % nums[1])

# Returns True if inputNum is a Prime
def primeTest(inputNum):
    result = bool(inputNum & 1)
    if result:
    # 2nd Level Multiprocessing Starts Here
    # Set up pendingPool - numPool
        numPool = list(range((sqrt(inputNum)-1)>>1))
        for i in range(len(numPool)):
            numPool[i] = [inputNum,3 + (numPool[i] << 1)]
        numPool.reverse()
    # And processWrapper - pWrap
        mpResult = PyMultiThread.bpHolder()
        pWrap = PyMultiThread.processWrapper(divTest,PyMultiThread.resultGetter(mpResult),lambda x: x)
    # Now we can rotate our pool
        PyMultiThread.rotatePool(pWrap,numPool)
        if not mpResult:
            result = False
    return result

# Returns a random prime number with length of x bytes.
def randomPrime(length=1):
    result = randNum(length) | 1
    # 1st Level Multiprocessing Starts Here
    while not primeTest(result):
        result = randNum(length)
    return result

def main(args):
    for i in range(int(args[0])):
        print(randomPrime(int(args[1])))

if __name__ == '__main__':
    main(sys.argv[1:])

