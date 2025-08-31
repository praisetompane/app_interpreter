from collections import deque
import argparse

class Evaluator:
    def __init__(self) -> None:
        self.variables = {}
        self._instruction_pointer = 0

    def evaluate_program(self, program_text):
        def extract_statement(text):
            return text.split(maxsplit=1)[0]

        instructions = [line for line in program_text.split(
            "\n") if line.strip() != ""]

        while self._instruction_pointer < len(instructions):
            instruction_register = instructions[self._instruction_pointer]
            statement = extract_statement(instruction_register)
            match statement:
                case "while":
                    _, expression = instruction_register.split(maxsplit=1)
                    if self.evaluate_arithmetic(expression):
                        # move to the body of while loop
                        self._instruction_pointer += 1
                    else:
                        # skip the body of the loop
                        while instructions[self._instruction_pointer] != "end":
                            self._instruction_pointer += 1
                        # move the instruction pointer to the next instruction after the loop keyword|statement
                        self._instruction_pointer += 1
                case "end":
                        # circle back to the while loop statement|keyword
                        # until its expressions evaluates to false and we move the instruction pointer past the while loop's end
                        while extract_statement(instructions[self._instruction_pointer]) != "while":
                            self._instruction_pointer -= 1
                case _: # assume non while instructions are assignments or literal expressions
                    (variable, equal_symbol, expression) = instruction_register.split(maxsplit=2)
                    if equal_symbol == "=":
                        self.variables[variable] = self.evaluate_arithmetic(expression)
                    else:
                        # store literals as an identity of key and value, where key = value
                        result = self.evaluate_arithmetic(instruction_register)
                        self.variables[result] = result
                    self._instruction_pointer += 1

        return self.variables

    def evaluate_arithmetic(self, arithmetic_expression):
        """Postfix notation arithmetic evaluation

        Args:
            arithmetic_expression (str): Arithmetic expression ton evaluate.
        """
        tokens = arithmetic_expression.split()
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
    parser = argparse.ArgumentParser("python src/app_interpreter/interpreter.py ./tests/resources/factorial.txt")
    parser.add_argument("program_file")

    args = parser.parse_args()
    program_text = open(args.program_file).read()

    interpreter = Evaluator()
    print(interpreter.evaluate_program(program_text))
