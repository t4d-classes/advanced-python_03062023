
class HistoryEntry:
    
    def __init__(self, id, op_name, op_value):
        self.id = id
        self.op_name = op_name
        self.op_value = op_value

    def __repr__(self):
        return  f"[id: {self.id}, name: {self.op_name}, value: {self.op_value}]"

class HistoryList:

  def __init__(self, history_storage):
      self.__history = []
      self.__current_iter = None
      self.__history_storage = history_storage

  def show_history(self):
      print(self.__history)

  def clear_history(self):
      self.clear()

  def __get_next_id(self):
      next_id = 1
      if self.__history:
          next_id = max([ entry.id for entry in self.__history ]) + 1
      return next_id

  def add_history_entry(self, op_name, op_value):
      self.__history.append(
          HistoryEntry(self.__get_next_id(), op_name, op_value))

  def remove_history_entry(self, history_entry_id):
      for entry in self.__history:
          if entry.id == history_entry_id:
              self.__history.remove(entry)
              break
          
  def get_history(self):
      return self.__history
  
  def __iter__(self):
      self.__current_iter = iter(self.__history)
      return self.__current_iter

  def __next__(self):
      return next(self.__current_iter)  

  def load_history(self):
      self.__history_storage.load(self)

  def save_history(self):
      self.__history_storage.save(self)

  def replace_history(self, history):
      self.__history = history
