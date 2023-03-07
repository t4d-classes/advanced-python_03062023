from calc_app.user_entry import get_command
from calc_app.history import HistoryList
from calc_app.calculator import Calculator


def app():

    # application state
    history = HistoryList()
    calculator = Calculator(history)


    while True:

        command = get_command()

        if calculator.is_calc_command(command):
            calculator.command_calc(command)   
        elif command == "remove":
            calculator.command_remove_history_entry()   
        elif command == "clear":
            calculator.command_clear_history()   
        elif command == "history":
            calculator.command_show_history()   
        elif command == "exit":
            break
        else:
            calculator.command_invalid()
            continue


if __name__ == "__main__":
    app()

