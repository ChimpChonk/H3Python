#!/usr/bin/env python3

def reverse_dictionary(d):
    inv_dict = {}
    for key in d:
        for item in d[key]:
            if item not in inv_dict:
                inv_dict[item] = [key]
            else:
                inv_dict[item].append(key)
    return inv_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
