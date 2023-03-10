""" user output module"""


def output_result(result):
    """output result"""
    print(f"Result: {result}")


def output_list(data):
    """output list"""
    for item in data:
        print(item)


def output_invalid_command():
    """output invalid command"""
    print("Invalid Command, Try Again.")
