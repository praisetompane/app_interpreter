from collections import deque
from typing import Any


class ArithmeticLogicUnit:
    """Stack based Postfix arithmetic logic evaluator."""

    def evaluate(self, expression: str, general_purpose_registers: dict[str, Any]) -> Any:
        """Evaluates an arithmetic or logic expression.

        Constraints:
           Only supports integers.

        Args:
            expression (str): Arithmetic or Logic expression to evaluate.
        """
        tokens = expression.split()
        operands_stack = deque()

        for t in tokens:
            if t.isdigit():
                operands_stack.append(int(t))
            elif t in general_purpose_registers:
                operands_stack.append(general_purpose_registers[t])
            else:
                rhs = operands_stack.pop()
                lhs = operands_stack.pop()
                if t == "+":
                    operands_stack.append(lhs + rhs)
                elif t == "*":
                    operands_stack.append(lhs * rhs)
                elif t == "/":
                    operands_stack.append(lhs / rhs)
                elif t == "-":
                    operands_stack.append(lhs - rhs)
                elif t == ">=":
                    # 1 pushed onto stack for true
                    # 0 pushed onto stack for false
                    if lhs >= rhs:
                        operands_stack.append(1)
                    else:
                        operands_stack.append(0)
                else:
                    raise NotImplementedError(
                        f"Provided operator {t} is not supported."
                    )

        return operands_stack.pop()
