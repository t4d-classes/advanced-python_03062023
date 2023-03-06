from calc_app.user_entry import get_command, get_operand, get_history_entry_id
from calc_app.history import (
    command_add_history_entry, command_clear_history,
    command_remove_history_entry, command_show_history,
    get_next_id
)
from calc_app.calc_result import calc_result, calc_commands

def run():

    # application state
    history = []

    while True:

        command = get_command()

        if command in calc_commands:
            operand = get_operand()
            command_add_history_entry(
                history, get_next_id(history), command, operand)
            print(calc_result(history))   
        elif command == "remove":
            history_entry_id = get_history_entry_id()
            command_remove_history_entry(history, history_entry_id)
        elif command == "clear":
            command_clear_history(history)
        elif command == "history":
            command_show_history(history)
        elif command == "exit":
            break
        else:
            print("Invalid Command, Try Again")
            continue

print(f"calc.py name {__name__}")

if __name__ == "__main__":
    run()

