#!/usr/bin/env python3.10
'''rotate 13 cypher'''

import sys

def main(input_string):
    '''main function'''
    result_string = ''
    for letter in input_string:
        result_string = result_string+letter

    print(result_string)

if __name__ == "__main__":
    main(sys.argv[1])
