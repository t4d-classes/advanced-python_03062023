""" use output module """


def output_result(result: float) -> None:
    """ output calc app current result """
    print(f"Result: {result}")

def output_list(data: list[str]) -> None:
    """ output list item """
    for item in data:
        print(item)

def output_unknown_command() -> None:
    """ output the calc app command is unknown """
    print("unknown command, please try again")
