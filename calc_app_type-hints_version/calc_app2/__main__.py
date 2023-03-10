""" calc app main """

from calc_app.user_input import input_command, input_operand, input_entry_id
from calc_app.user_output import (
    output_result, output_list, output_unknown_command
)
from calc_app.calculator import math_ops, Calculator
from calc_app.history import History


def app() -> None:
    """ calc app main function """

    history = History()
    calculator = Calculator(history)

    command = input_command()

    while command:
        if command in math_ops:
            operand = input_operand()
            calculator.perform_math(command, operand)
            output_result(calculator.get_result())
        elif command == "clear":
            calculator.clear()
            output_result(calculator.get_result())
        elif command == "history":
            output_list(calculator.get_history())
        elif command == "remove":
            entry_id = input_entry_id()
            calculator.remove_history_entry(entry_id)
        elif command == "result":
            output_result(calculator.get_result())
        else:
            output_unknown_command()

        command = input_command()

# enables this module to be imported or executed
if __name__ == '__main__':
    app()
