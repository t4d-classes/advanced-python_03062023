math_ops = {
    "add": lambda a,b: a + b,
    "subtract": lambda a,b: a - b,
    "multiply": lambda a,b: a * b,
    "divide": lambda a,b: a / b,
    "exponent": lambda a,b: a ** b,
}

def calc_result(history):
    result = 0
    for entry in history:
        # op_value = entry["opValue"]
        # op_name = entry["opName"]
        # op_func = math_ops[op_name]
        # result = op_func(result, op_value)
        result = math_ops[entry["opName"]](result, entry["opValue"])
    return result
    


calc_commands = ["add", "subtract", "multiply", "divide", "exponent"]
