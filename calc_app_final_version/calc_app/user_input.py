""" user input module """


def get_command():
    """get command"""
    return input("Enter a command:")


def get_operand():
    """get operand"""
    return float(input("Please enter an operand:"))


def get_history_entry_id():
    """get history entry id"""
    return int(input("Enter a history entry id to remove: "))
