
def add(a,b):
    return a+b


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


def get_command():
    return input("Enter a command:")

def get_operand():
    return float(input("Please enter an operand:"))

def get_history_entry_id(prompt = None):
    if prompt:
        return int(input(prompt))
    else:
        return int(input("Please enter the history entry id: "))
    
def command_show_history(history):
    print(history)

def command_clear_history(history_list):
    # global history
    # history = []
    history_list.clear()

def get_next_id(history):
    next_id = 1
    if history:
        next_id = max([ entry["id"] for entry in history ]) + 1
    return next_id

def command_add_history_entry(history, entry_id, op_name, op_value):
    history.append({
        "id": entry_id,
        "opName": op_name,
        "opValue": op_value
    })

def command_remove_history_entry(history):
    history_entry_id = get_history_entry_id()
    
    for entry in history:
        if entry["id"] == history_entry_id:
            history.remove(entry)
            break

calc_commands = ["add", "subtract", "multiply", "divide", "exponent"]

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
            command_remove_history_entry(history)
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

