#! /usr/bin/python
import sys

def gcd(num1,num2):
    while num1 > 0:
        if num1 < num2:
            num1,num2 = num2,num1
        num1 = num1 % num2
    return num2

def main(args):
    print(gcd(int(args[0]),int(args[1])))

if __name__ == '__main__':
    main(sys.argv[1:])
