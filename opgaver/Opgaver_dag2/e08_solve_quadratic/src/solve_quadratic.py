#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    dis = b * b -4 * a * c
    square = math.sqrt(dis)
    return (-b + square) / (2 * a), (-b - square) / (2 * a)



def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1, 2, 1))

if __name__ == "__main__":
    main()
