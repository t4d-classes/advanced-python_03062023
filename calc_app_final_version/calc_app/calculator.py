""" calculator module """

from calc_app.user_input import get_operand, get_history_entry_id
from calc_app.user_output import (
    output_result,
    output_list,
    output_invalid_command,
)

math_ops = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
    "exponent": lambda a, b: a**b,
}


class Calculator:
    """calculator class"""

    def __init__(self, history_list):
        self.history_list = history_list

    def command_calc(self, op_name):
        """command calc"""
        operand = get_operand()
        self.history_list.append_history_entry(op_name, operand)
        output_result(self.calc_result())

    def command_remove_history_entry(self):
        """comad remove history entry"""
        history_entry_id = get_history_entry_id()
        self.history_list.remove_history_entry(history_entry_id)

    def command_clear_history(self):
        """command clear history"""
        return self.history_list.clear_history()

    def command_show_history(self):
        """command show history"""
        output_list(self.history_list)

    def command_invalid(self):
        """command invalid"""
        output_invalid_command()

    async def command_save_history(self):
        """command save history"""
        await self.history_list.save_history()

    async def command_load_history(self):
        """command load history"""
        await self.history_list.load_history()

    def calc_result(self):
        """calc result"""
        result = 0
        for entry in self.history_list:
            result = math_ops[entry.op_name](result, entry.op_value)
        return result

    def is_math_op(self, op_name):
        """is math op"""
        return op_name in math_ops
