#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1, program that proves the phrase is a palindrome
"""


import argparse


def palindrome(phrase):
    """
    change the pharase to lower case and then reverse it
    """
    phrase = phrase.casefold()
    rev_phrase = (phrase)[::-1]

    if list(phrase) == list(rev_phrase):
        return (" is palindrome")
    else:
        return ("is not palindrome")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("str", help=" Enter a string:")
    args = parser.parse_args()
    result = palindrome(args.str)
    print("the phrase " + str(args.str) + str(result))

if __name__ == '__main__':
    main()
