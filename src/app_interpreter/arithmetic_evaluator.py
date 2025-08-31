from collections import deque
from typing import Any

class ArithmeticEvaluator:
    """Stack based Postfix arithmetic evaluator.
    """
    def __init__(self) -> None:
        self._instruction_pointer = 0

    def evaluate(self, arithmetic_expression: str, variables: dict[str, Any]):
        """Evaluates a arithmetic expression.
           Only supports integers.

        Args:
            arithmetic_expression (str): Arithmetic expression to evaluate.
        """
        tokens = arithmetic_expression.split()
        stack = deque()

        for t in tokens:
            if t.isdigit():
                stack.append(int(t))
            elif t in variables:
                stack.append(variables[t])
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                if t == "+": stack.append(lhs + rhs)
                elif t == "*": stack.append(lhs * rhs)
                elif t == "/": stack.append(lhs / rhs)
                elif t == "-": stack.append(lhs - rhs)
                elif t == ">=":
                    # 1 pushed onto stack for true
                    # 0 pushed onto stack for false
                    if lhs >= rhs: stack.append(1)
                    else: stack.append(0)
                else:
                    raise NotImplementedError(
                        f"Provided operator {t} is not supported.")

        return stack.pop()
