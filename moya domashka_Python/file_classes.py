from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def append(self, data):
        pass


