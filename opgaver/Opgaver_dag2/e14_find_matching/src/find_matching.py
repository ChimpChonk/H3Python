#!/usr/bin/env python3

def find_matching(L, pattern):
    index = []
    for i, x in enumerate(L):
        if x.find(pattern) != -1:
            index.append(i)
    return index

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
