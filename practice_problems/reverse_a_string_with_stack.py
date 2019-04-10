"""
Reverse a string using a stack.

Input: string
Output: string

EX: "chelsea" --> "aeslehc"
"""

from data_structures.stack import Stack


def stack_reverse_string(input):
    stk = Stack()
    for elem in input:
        stk.push(elem)
    res = ""
    while stk.size() > 0:
        elem = stk.pop()
        res += elem
    return res
