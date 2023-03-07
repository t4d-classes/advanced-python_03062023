from calc_app.user_entry import get_operand, get_history_entry_id


class Calculator:
    
    __math_ops = {
        "add": lambda a,b: a + b,
        "subtract": lambda a,b: a - b,
        "multiply": lambda a,b: a * b,
        "divide": lambda a,b: a / b,
        "exponent": lambda a,b: a ** b,
    }    

    def __init__(self, history_list):
        self.__history_list = history_list

    def command_calc(self, op_name):
        op_value = get_operand()
        self.__history_list.add_history_entry(op_name, op_value)
        print(self.calc_result())

    def command_remove_history_entry(self):
        history_entry_id = get_history_entry_id()
        self.__history_list.remove_history_entry(history_entry_id)

    def command_clear_history(self):
        self.__history_list.clear_history()

    def command_show_history(self):
        self.__history_list.show_history()

    def command_load_history(self):
        self.__history_list.load_history()

    def command_save_history(self):
        self.__history_list.save_history()

    def command_invalid(self):
        print("Invalid Command, Try Again")

    def calc_result(self):
        result = 0
        for entry in self.__history_list:
            result = self.__math_ops[entry.op_name](result, entry.op_value)
        return result
    
    def is_calc_command(self, command):
        return command in self.__math_ops.keys()



