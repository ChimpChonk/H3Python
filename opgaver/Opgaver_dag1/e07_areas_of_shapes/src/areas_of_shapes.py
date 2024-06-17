#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while(True):
        user_input = input("Choose a share (triangle, rectangle, circle): ")
        if(user_input == "triangle"):
            a = int(input("Give base of the triangle: "))
            b = int(input("Give height of the triangle: "))
            print(f"The area is: {triangle(a,b)}")

        elif(user_input == "rectangle"):
            a = int(input("Give width of the rectangle: "))
            b = int(input("Give height of the rectangle: "))
            print(f"The area is: {rectangle(a,b)}")

        elif(user_input == "circle"):
            r = int(input("Give radius of the circle: "))
            print(f"The area is: {circle(r)}")

        elif(user_input.strip() == ""):
            break
        else:
            print("Unkown shape!")

def triangle(a,b):
    return (a*b)/2

def rectangle(a,b):
    return a*b

def circle(r):
    return math.pi*r**2

if __name__ == "__main__":
    main()
