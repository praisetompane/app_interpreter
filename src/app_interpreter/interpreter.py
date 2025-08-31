import sys
from collections import deque


class Evaluator:
    def __init__(self) -> None:
        self.variables = {}

    def evaluate_program(self, program_text):
        lines = [line for line in program_text.split(
            "\n") if line.strip() != ""]
        instruction_pointer = 0
        while instruction_pointer < len(lines):
            instruction_register = lines[instruction_pointer]
            statement = instruction_register.split(maxsplit=1)[0]
            match statement:
                case "while": pass
                case "end": pass
                case _:
                    (variable, equal_symbol, expression) = instruction_register.split(maxsplit=2)
                    if equal_symbol == "=":
                        self.variables[variable] = self.evaluate_arithmetic(expression)
                    else:
                        # store literals as identity key and value
                        result = self.evaluate_arithmetic(instruction_register)
                        self.variables[result] = result
            instruction_pointer += 1

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
                if t == "+": stack.append(lhs + rhs)
                elif t == "*": stack.append(lhs * rhs)
                elif t == "/": pass
                elif t == "-": stack.append(lhs - rhs)
                elif t == ">=":
                    # 1 pushed onto stack for true
                    # 0 pushed onto stack for false
                    if lhs >= rhs: stack.append(1)
                    else: stack.append(0)
                else:
                    raise NotImplementedError(
                        f"Unsupported operation {t} provided")

        return stack[0]


if __name__ == "__main__":
    # program_file = open(sys.argv[1])
    program_text = open("tests/app_interpreter/addition.txt").read()
    interpreter = Evaluator()
    interpreter.evaluate_program(program_text)
