# Assignment 7


## Task 1

"able was i ere i saw elba" is a well-known [palindrome](https://en.wikipedia.org/wiki/Palindrome).  Write a generalized program that **proves** this phrase is a palindrome.  Because the program is generalized, it should also prove that *any other palindromes* are actually palindromes **and** it should prove when phrases or words **are not** palindromes.  Be sure to write your program such that this is the case.  And, be sure that your argument takes any palindrome on the command line as input (i.e., use the argparse module). Write the program to include a `main()` function and the `ifmain` statement.  The `main()` function should call the function or functions that you create to test for "palindrome-ness".

## Task 2

Here is a recursive program that is mean to print each base of a given input sequence to the screen, one base per line.

```python
#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""


def sequence_eater(sequence, position):
    print(sequence[position])
    position -= 1
    sequence_eater(sequence, position)


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()

```

Alas, it is somewhat broken.  Try to fix the program (while maintaining its function **and** its recursive nature) in the fewest number of changes possible.  Save your fixed version of the code as something like `task2.py` in `answers/<your-github-name>` (i.e., as usual).

----

**Have a fun and safe Mardi Gras!**

![mardi gras](images/mardi-gras-indians.jpg)
