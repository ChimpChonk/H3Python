#!/usr/bin/env python3

def merge(L1, L2):
    merge = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merge.append(L1[i])
            i += 1
        else:
            merge.append(L2[j])
            j += 1
    return merge

def main():
    L1 = sorted([1, 3, 5, 7])
    L2 = sorted([2, 4, 6, 8])
    
    result = merge(L1, L2)
    print("Merged list:", result)

if __name__ == "__main__":
    main()
