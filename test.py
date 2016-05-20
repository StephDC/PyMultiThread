#! /usr/bin/python3

import os
import sys
import time

def sqrt(inputNum):
    return int(inputNum ** 0.5)

# Returns a random int with length of x bytes.
def randNum(length=1):
    return int.from_bytes(os.urandom(length),'big')

# Returns True if Num2 is a factor of Num1
def divTest(num1,num2):
    return bool(num1 % num2)

# Returns True if inputNum is a Prime
def primeTest(inputNum):
    result = bool(inputNum & 1)
    lastTime = time.time()
    if result:
    # 2nd Level Multiprocessing Starts Here
        for i in range((sqrt(inputNum)-1)>>1):
            lastTime = time.time()
            if not divTest(inputNum,(i<<1)+3):
                result = False
                break
            if time.time()-lastTime > 0.01:
                print(inputNum," % ",(i<<1)+3," takes ",time.time()-lastTime,'s')
    return result

# Returns a random prime number with length of x bytes.
def randomPrime(length=1):
    result = randNum(length)
    # 1st Level Multiprocessing Starts Here
    while not primeTest(result):
        result = randNum(length)
    return result

def main(args):
    for i in range(int(args[0])):
        print(randomPrime(int(args[1])))

if __name__ == '__main__':
    main(sys.argv[1:])

