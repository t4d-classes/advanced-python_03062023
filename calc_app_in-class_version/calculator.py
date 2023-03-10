

from calc_app.user_input import (
    get_operand, get_history_entry_id
)
from calc_app.user_output import (
    output_result, output_list, output_invalid_command
)

math_ops = {
    "add": lambda a,b: a + b,
    "subtract": lambda a,b: a - b,
    "multiply": lambda a,b: a * b,
    "divide": lambda a,b: a / b,
    "exponent": lambda a,b: a ** b
}

class Calculator:

    def __init__(self, history_list):
        self.__history_list = history_list
    
    def command_calc(self, op_name):
        operand = get_operand()
        self.__history_list.append_history_entry(op_name, operand)
        output_result(self.calc_result())

    def command_remove_history_entry(self):
        history_entry_id = get_history_entry_id()
        self.__history_list.remove_history_entry(history_entry_id)

    def command_clear_history(self):
        return self.__history_list.clear()

    def command_show_history(self):
        output_list(self.__history_list)

    def command_invalid(self):           
        output_invalid_command()

    def command_save_history(self):
        self.__history_list.save()

    def command_load_history(self):
        self.__history_list.load()

    def calc_result(self):
        result = 0
        for entry in self.__history_list:
            result = math_ops[entry.op_name](result, entry.op_value)
        return result

    def is_math_op(self, op_name):
        return op_name in math_ops    
