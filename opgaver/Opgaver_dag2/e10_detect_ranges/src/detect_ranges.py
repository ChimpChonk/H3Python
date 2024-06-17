#!/usr/bin/env python3

def detect_ranges(L):

    #sort the list
    #track the numbers in the list that is in range
    #
    sort = sorted(L)
    result = []
    current = sort[0]
    end = current

    for i in sort[1:]:
        if i == end + 1:
            end = i
        else:
            if current == end:
                result.append(current)
            else:
                result.append((current, end + 1))
            current = i
            end = i
    if current == end:
        result.append(current)
    else:
        result.append((current, end + 1))
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
