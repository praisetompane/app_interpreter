from app_interpreter.arithmetic_logic_unit import ArithmeticLogicUnit


class ControlUnit:
    def __init__(self, arithmetic_logic_unit: ArithmeticLogicUnit) -> None:
        self._general_purpose_registers = {}
        self._instruction_pointer = 0
        self._ALU = arithmetic_logic_unit

    def _extract_statement(self, text): return text.split(maxsplit=1)[0]

    def execute(self, program_text):

        instructions = [line for line in program_text.split(
            "\n") if line.strip() != ""]

        while self._instruction_pointer < len(instructions):
            instruction_register = instructions[self._instruction_pointer]
            statement = self._extract_statement(instruction_register)
            match statement:
                case "while":
                    _, expression = instruction_register.split(maxsplit=1)
                    if self._ALU.evaluate(expression, self._general_purpose_registers):
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
                    while (
                        self._extract_statement(
                            instructions[self._instruction_pointer]) != "while"
                    ):
                        self._instruction_pointer -= 1
                case "if": pass
                case _:
                    # assume all other instructions are assignments or literal expressions
                    variable, equal_symbol, expression = instruction_register.split(
                        maxsplit=2)

                    if equal_symbol == "=":
                        self._general_purpose_registers[variable] = (
                            self._ALU.evaluate(
                                expression, self._general_purpose_registers
                            )
                        )
                    else:
                        # store literals as an identity of key and value, where key = value
                        result = self._ALU.evaluate(
                            instruction_register, self._general_purpose_registers
                        )

                        self._general_purpose_registers[result] = result

                    self._instruction_pointer += 1

        return self._general_purpose_registers
