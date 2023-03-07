

from abc import ABC, abstractmethod

class HistoryStorage(ABC):
    
    @abstractmethod
    def load(self, history_list):
        ...

    @abstractmethod
    def save(self, history_list):
        ...