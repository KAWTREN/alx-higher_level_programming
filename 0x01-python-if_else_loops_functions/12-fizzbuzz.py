#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        j = i % 3
        k = i % 5
        if j == 0 and k == 0:
            print("FizzBuzz", end=" ")
        elif k == 0:
            print("Buzz", end=" ")
        elif j == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
