""" history module """

# from typing import cast

class HistoryEntry:
    """ history entry dictionary """
    def __init__(self, history_entry_id: int, command: str, operand: float):
        self.history_entry_id = history_entry_id
        self.command = command
        self.operand = operand

    def __repr__(self) -> str:
        return (
            f"Id: {self.history_entry_id}"
            f", Command: {self.command}"
            f", Operand: {self.operand}"
        )

class History:
    """ history class"""

    history: list[HistoryEntry]

    def __init__(self) -> None:
        # self.history = cast(list[HistoryEntry], [])
        self.history = []

    def __get_next_id(self) -> int:
        """ get next id """
        if len(self.history) == 0:
            return 1
        ids = [ entry.history_entry_id for entry in self.history]
        return max(ids) + 1

    def append_entry(self, command_name: str, operand: float) -> None:
        """ append a history entry"""
        self.history.append(
            HistoryEntry(self.__get_next_id(), command_name, operand))

    def remove_entry(self, entry_id: int) -> None:
        """ remove a history entry by id """
        for entry in self.history:
            if entry.history_entry_id == entry_id:
                self.history.remove(entry)

    def clear_entries(self) -> None:
        """ clear history entries """
        self.history = []





