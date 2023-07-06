#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10):
        print((i+2) - 1)
        print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    new_list = []
    for i in int_list:
        new_list.append(abs(i**2))
    return new_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0 and i != 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i != 0:
            print("Fizz")
        elif i % 5 == 0 and i != 0:
            print("Buzz")
        else: 
            print(i)
    pass
