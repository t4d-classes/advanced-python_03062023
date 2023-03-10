from calc_app.user_input import get_command
from calc_app.history_list import HistoryList
from calc_app.calculator import Calculator
from calc_app.history_file_storage import HistoryFileStorage

def app():

    history_storage = HistoryFileStorage()
    history_list = HistoryList(history_storage)
    calculator = Calculator(history_list)

    while True:

        command = get_command()

        if calculator.is_math_op(command):
            calculator.command_calc(command)
        elif command == "remove":
            calculator.command_remove_history_entry()
        elif command == "clear":
            calculator.command_clear_history()
        elif command == "load":
            calculator.command_load_history()
        elif command == "save":
            calculator.command_save_history()
        elif command == "history":
            calculator.command_show_history()
        elif command == "exit":
            break
        else:
            calculator.command_invalid()

if __name__ == "__main__":
    app()


