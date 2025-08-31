from app_interpreter.arithmetic_evaluator import ArithmeticEvaluator

class Interpreter:
    def __init__(self) -> None:
        self.variables = {}
        self._instruction_pointer = 0
        self._arithmetic_expression_evaluator = ArithmeticEvaluator()

    def evaluate(self, program_text):
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
                    if self._arithmetic_expression_evaluator.evaluate(expression, self.variables):
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
                case _: # assume all other instructions are assignments or literal expressions
                    (variable, equal_symbol, expression) = instruction_register.split(maxsplit=2)
                    if equal_symbol == "=":
                        self.variables[variable] = self._arithmetic_expression_evaluator.evaluate(expression, self.variables)
                    else:
                        # store literals as an identity of key and value, where key = value
                        result = self._arithmetic_expression_evaluator.evaluate(instruction_register, self.variables)
                        self.variables[result] = result
                    self._instruction_pointer += 1

        return self.variables

