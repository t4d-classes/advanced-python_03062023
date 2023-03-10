""" history file storage module """

import aiofiles
import jsonpickle
from calc_app.history_storage import HistoryStorage


class HistoryFileStorage(HistoryStorage):
    """history file storage"""

    async def load(self):
        async with aiofiles.open(
            "history.json", "r", encoding="UTF-8"
        ) as history_file:
            return jsonpickle.decode(await history_file.read())

    async def save(self, history_entries):
        async with aiofiles.open(
            "history.json", "w", encoding="UTF-8"
        ) as history_file:
            await history_file.write(jsonpickle.encode(history_entries))
