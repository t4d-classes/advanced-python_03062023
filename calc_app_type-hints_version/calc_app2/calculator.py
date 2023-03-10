""" calculator module """

from collections.abc import Callable

from calc_app.history import History

math_ops: dict[str, Callable[[float, float], float]] = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}

class Calculator:
    """ command class"""

    def __init__(self, history: History):
        self.history = history

    def perform_math(self, command_name: str, operand: float) -> None:
        """ command perform math """
        self.history.append_entry(command_name, operand)

    def get_history(self) -> list[str]:
        """ command print history """
        return [ f"Entry: {entry}" for entry in self.history.history ]

    def remove_history_entry(self, entry_id: int) -> None:
        """ command remove history entry """
        self.history.remove_entry(entry_id)

    def clear(self) -> None:
        """ command clear """
        self.history.clear_entries()

    def get_result(self) -> float:
        """ calculate the current result from the history """
        result: float = 0
        for entry in self.history.history:
            math_op = math_ops[entry.command]
            result = math_op(result, entry.operand)
        return result
