import sys
from collections import deque


class Evaluator:
    def __init__(self) -> None:
        self.variables = {}

    def evaluate_program(self, program_text):
        lines = [line for line in program_text.split(
            "\n") if line.strip() != ""]
        for line in lines:
            (variable, equal_symbol, expression) = line.split(maxsplit=2)
            if equal_symbol == "=":
                self.variables[variable] = self.evaluate_arithmetic(expression)
            else:
                result = self.evaluate_arithmetic(line)
                self.variables[result] = result

    def evaluate_arithmetic(self, expression):
        """Postfix notation arithmetic evaluation

        Args:
            program_string (str): _description_
        """
        tokens = expression.split()
        stack = deque()

        for t in tokens:
            if t.isdigit():
                stack.append(int(t))
            elif t in self.variables:
                stack.append(self.variables[t])
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                if t == "+":stack.append(lhs + rhs)
                elif t == "*": stack.append(lhs * rhs)
                elif t == "/": pass
                elif t == "-": stack.append(lhs - rhs)
                else:
                    raise NotImplementedError(
                        f"Unsupported operation {t} provided")

        return stack[0]


if __name__ == "__main__":
    # program_file = open(sys.argv[1])
    program_text = open("tests/app_interpreter/addition.txt").read()
    interpreter = Evaluator()
    interpreter.evaluate_program(program_text)
