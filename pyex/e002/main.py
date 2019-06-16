#!/usr/bin/env python3


"""
002 Simple Recursion

Demonstrates how the stack is used in recursion. Run the program in a
debugger (as described below). Step through the program and watch how
the stack grows and shrinks when functions are called and returns. You
may also want to inspect the different variables values in each stack
frame. Also, try changing the initial recurse call and watch how that
affects the number of frames on the stack.

Running the program in the debugger:
    $ pudb3 pyex/e002/main.py
"""


def recurse(number):
    """
    Recursively counts down to 0.
    """
    if number == 0:
        return number
    else:
        return recurse(number - 1)


def main():
    """
    Runs the program.
    """
    result = recurse(7)

    print(f"The result is {result}!")


if __name__ == '__main__':
    main()
