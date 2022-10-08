#!/usr/bin/env python3.10
'''rotate 13 cypher'''

import sys

rot13_dict_lower = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
}

rot13_dict_upper = {
    'A': 'N',
    'B': 'O',
    'C': 'P',
    'D': 'Q',
    'E': 'R',
    'F': 'S',
    'G': 'T',
    'H': 'U',
    'I': 'V',
    'J': 'W',
    'K': 'X',
    'L': 'Y',
    'M': 'Z',
    'N': 'A',
    'O': 'B',
    'P': 'C',
    'Q': 'D',
    'R': 'E',
    'S': 'F',
    'T': 'G',
    'U': 'H',
    'V': 'I',
    'W': 'J',
    'X': 'K',
    'Y': 'L',
    'Z': 'M',
}

def rot13(letter):
    '''return letter moved by 13 characters or input string, if letter not in dict'''
    result = ''

    if letter in  rot13_dict_lower:
        result = rot13_dict_lower[letter]
    elif letter in rot13_dict_upper:
        result = rot13_dict_upper[letter]
    else:
        result = letter

    return result

def main(input_string):
    '''main function'''
    result_string = ''
    for letter in input_string:
        new_letter = rot13(letter)
        result_string = result_string+new_letter

    print(result_string)

if __name__ == "__main__":
    main(sys.argv[1])
