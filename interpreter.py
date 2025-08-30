import sys
from collections import deque

def evaluate_expression(expression):
    """Postfix notation arithmetic evaluation

    Args:
        program_string (str): _description_
    """
    tokens = expression.split()
    stack = deque()

    for t in tokens:
        if t.isdigit():
            stack.append(int(t))
        elif t == "+":
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(lhs + rhs)

        elif t == "*": pass
        elif t =="/": pass
        elif t == "-": pass
        else:
            raise NotImplementedError(f"Unsupported operation {t} provided")

    return stack.pop()

if __name__ == "__main__":
    program_file = open(sys.argv[1])
    print(evaluate_expression(program_file.read()))