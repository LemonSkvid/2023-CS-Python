from operator import add, mul, sub, truediv
from typing import List, Optional, Union

ops = {"+": add, "-": sub, "*": mul, "/": truediv}

def _split_if_string(string_or_list: Union[List[str], str]) -> List[str]:
    return string_or_list.split() if isinstance(string_or_list, str) else string_or_list

def prefix_evaluate(prefix_equation: Union[List[str], str]) -> Optional[int]:
    if not prefix_equation:
        return None
    prefix_equation = _split_if_string(prefix_equation)
    value_stack = []
    while prefix_equation:
        el = prefix_equation.pop()
        if el not in ops:
            value_stack.append(int(el))
        else:
            r_val = value_stack.pop()
            l_val = value_stack.pop()
            operation = ops[el]
            value_stack.append(operation(r_val, l_val))

    return value_stack[0]

def to_prefix(equation: str) -> List[str]:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    operators = set("+*-/")
    output = []
    stack = []

    for token in reversed(equation.split()):
        if token.isdigit():
            output.append(token)
        elif token in operators:
            while stack and stack[-1] != ")" and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token == ")":
            stack.append(token)
        elif token == "(":
            while stack and stack[-1] != ")":
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())
    return list(reversed(output))


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
