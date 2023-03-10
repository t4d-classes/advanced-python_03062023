""" calc app main """

from typing import Any
from calc_app.user_input import input_command
from calc_app.user_output import output_unknown_command
from calc_app import commands as cmds
from calc_app.history import math_ops


def app() -> None:
    """ calc app main function """

    history: list[dict[str,Any]] = []

    command = input_command()

    while command:
        if command in math_ops:
            history = cmds.command_perform_math(history, command)
        elif command == "clear":
            history = cmds.command_clear()
        elif command == "history":
            cmds.command_print_history(history)
        elif command == "remove":
            history = cmds.command_remove_history_entry(history)
        elif command == "result":
            cmds.command_show_result(history)
        else:
            output_unknown_command()

        command = input_command()

# enables this module to be imported or executed
if __name__ == '__main__':
    app()
