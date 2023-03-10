""" history list module """


class HistoryEntry:
    """history entry class"""

    def __init__(self, op_id, op_name, op_value):
        self.op_id = op_id
        self.op_name = op_name
        self.op_value = op_value

    def __repr__(self):
        return (
            f"id: {self.op_id}, name: {self.op_name}, value: {self.op_value}"
        )


class HistoryList:
    """history list class"""

    def __init__(self, history_storage):
        self.__history = []
        self.__current_iter = None
        self.__history_storage = history_storage

    def __get_next_id(self):
        next_op_id = 1
        if self.__history:
            next_op_id = max([entry.op_id for entry in self.__history]) + 1
        return next_op_id

    def append_history_entry(self, op_name, op_value):
        """append history entry"""
        self.__history.append(
            HistoryEntry(self.__get_next_id(), op_name, op_value)
        )

    def remove_history_entry(self, entry_id):
        """remove history entry"""
        for entry in self.__history:
            if entry.op_id == entry_id:
                self.__history.remove(entry)
                break

    def clear_history(self):
        """clear history entries"""
        self.__history = []

    async def save_history(self):
        """save history entries to storage"""
        await self.__history_storage.save(self.__history)

    async def load_history(self):
        """load history entries from storage"""
        self.__history = await self.__history_storage.load()

    def __iter__(self):
        self.__current_iter = iter(self.__history)
        return self.__current_iter

    def __next__(self):
        return next(self.__current_iter)
