""" main module """

import asyncio

from calc_app.user_input import get_command
from calc_app.history_file_storage import HistoryFileStorage
from calc_app.history_list import HistoryList
from calc_app.calculator import Calculator


async def app():
    """app function"""

    calculator = Calculator(HistoryList(HistoryFileStorage()))

    while True:

        command = get_command()

        if calculator.is_math_op(command):
            calculator.command_calc(command)
        elif command == "remove":
            calculator.command_remove_history_entry()
        elif command == "clear":
            calculator.command_clear_history()
        elif command == "load":
            await calculator.command_load_history()
        elif command == "save":
            await calculator.command_save_history()
        elif command == "history":
            calculator.command_show_history()
        elif command == "exit":
            break
        else:
            calculator.command_invalid()


def main():
    """main function"""
    asyncio.run(app())


if __name__ == "__main__":
    main()
