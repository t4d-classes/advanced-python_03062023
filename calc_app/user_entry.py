def get_command():
    return input("Enter a command:")

def get_operand():
    return float(input("Please enter an operand:"))

def get_history_entry_id(prompt = None):
    if prompt:
        return int(input(prompt))
    else:
        return int(input("Please enter the history entry id: "))