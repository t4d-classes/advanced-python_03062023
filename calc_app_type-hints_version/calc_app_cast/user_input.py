""" user input module """

def input_command() -> str:
    """ input calc app command """
    return input("Enter a command > ")

def input_operand() -> float:
    """ input operand value """
    return float(input("Please enter an operand: "))

def input_entry_id() -> int:
    """ input history entry id """
    return int(input("Please the id of the history entry to remove: "))
