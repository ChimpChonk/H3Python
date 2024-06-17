#!/usr/bin/env python3


def main():
    for i  in range(1, 11):
        s = square(i)
        t = triple(i)
        if s > t:
            break
        else:
            print(f"triple({i})=={t} square({i})=={s}", )

def triple(x):
    return x*3

def square(x):
    return x**2

if __name__ == "__main__":
    main()


