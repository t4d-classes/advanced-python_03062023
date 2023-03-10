import aiofiles
import jsonpickle

from calc_app.history_storage import HistoryStorage

class HistoryFileStorage(HistoryStorage):

    async def load(self, history_list):
        async with aiofiles.open("history.json", "r") as f:
            await

            history_entry_list = jsonpickle.decode(f.read())
            history_list.replace_history(history_entry_list)

    async def save(self, history_list):
        async with aiofiles.open("history.json", "w") as f:
            f.write(jsonpickle.encode(list(history_list))) 