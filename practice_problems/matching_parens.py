"""
Input: string of parenthesis
Output: Boolean: if they are "valid"/properly matching, or not.

EX:

"(())" --> True
")()" --> False
"()()" --> True
"""

from data_structures.stack import Stack

paren_map = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def matching_parens(input):
    stk = Stack()

    for elem in input:
        if elem in paren_map.keys():
            stk.push(elem)
        else:
            if stk.size() == 0:
                return False
            match = stk.pop()
            if not paren_map[match] == elem:
                return False
    return True
