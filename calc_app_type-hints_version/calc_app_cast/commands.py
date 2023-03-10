""" commands module """

from typing import Any

from calc_app.user_input import input_operand, input_entry_id
from calc_app.user_output import output_result
from calc_app.history import get_next_id, calc_result

def command_perform_math(
    history: list[dict[str, Any]],
    command_name: str) -> list[dict[str, Any]]:
    """ command perform math """

    operand = input_operand()
    history.append({
        "id": get_next_id(history),
        "command": command_name,
        "operand": operand
    })
    output_result(calc_result(history))
    return history

def command_print_history(history: list[dict[str, Any]]) -> None:
    """ command print history """

    for entry in history:
        print(entry)

def command_remove_history_entry(
    history: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """ command remove history entry """

    entry_id = input_entry_id()
    for entry in history:
        if entry["id"] == entry_id:
            history.remove(entry)
    return history

def command_clear() -> list[dict[str, Any]]:
    """ command clear """

    output_result(0)
    return []

def command_show_result(history: list[dict[str, Any]]) -> None:
    """ command show result """

    output_result(calc_result(history))
