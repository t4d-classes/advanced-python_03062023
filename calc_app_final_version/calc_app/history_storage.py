""" history storage module """

from abc import ABC, abstractmethod


class HistoryStorage(ABC):
    """history storage abstract class"""

    @abstractmethod
    async def load(self):
        """load history entries from storage"""

    @abstractmethod
    async def save(self, history_entries):
        """save history entries to storage"""
