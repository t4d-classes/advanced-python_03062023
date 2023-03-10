""" history module """

from collections.abc import Callable
from typing import Any, cast

math_ops = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}


def calc_result(history: list[dict[str, Any]]) -> float:
    """ calculate the current result from the history """
    result: float = 0
    for entry in history:
        math_op = cast(
            Callable[[float, float], float], math_ops[entry["command"]])
        result = math_op(result, cast(float, entry["operand"]))
    return result


def get_next_id(history: list[dict[str, Any]]) -> int:
    """ get next id """
    if len(history) == 0:
        return 1
    ids = [ cast(int, entry["id"]) for entry in history]
    return max(ids) + 1
