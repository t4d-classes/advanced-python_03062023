import jsonpickle

from calc_app.history_storage import HistoryStorage

class HistoryFileStorage(HistoryStorage):
    
    def load(self, history_list):
        with open("history.json", "r", encoding="UTF-8") as f:
            history_entry_list = jsonpickle.decode(f.read())
            history_list.replace_history(history_entry_list)
            

    def save(self, history_list):
        with open("history.json", "w", encoding="UTF-8") as f:
            f.write(jsonpickle.encode(list(history_list)))

