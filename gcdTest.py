#! /usr/bin/python

import gcd
import time

magNum = 2305567963945518424753102147331756070
def main():
    for i in range(100000,10000000):
        startTime = time.time()
        gcd.gcd(i,magNum)
        stopTime = time.time()
        if stopTime-startTime > 0.01:
            print(i,' takes ',stopTime-startTime,'s')

if __name__ == '__main__':
    main()
