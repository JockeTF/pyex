#!/usr/bin/env python3


"""
001 Scoping

This program is deliberately confusing in order to demonstrate how
functions interact with variables, and how scoping within a function
works. Try to answer the questions before running the program, then try
running the program and answering the questions again! You may also want
to try running the program in a debugger in order to step through it.

Try to answer the following questions:
    - What is the first number?
    - What is the second number?
    - Why is this the case?

Running the program:
    $ python3 pyex/e001/main.py

Running the program in the debugger:
    $ pudb3 pyex/e001/main.py
"""


a = 1
b = 1
c = 1


def calculate(a):
    """
    Calculates a sum of values.
    """
    b = a + 2
    d = b + c

    return d


def main():
    """
    Runs the program.
    """
    c = calculate(3)
    print(f"The first number is {c}!")

    d = calculate(3)
    print(f"The second number is {d}!")


a = 4
b = 4
c = 4


if __name__ == '__main__':
    main()


a = 5
b = 5
c = 5
