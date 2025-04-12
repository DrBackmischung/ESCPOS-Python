from abc import ABC, abstractmethod

class POSPrinterInterface(ABC):
    @abstractmethod
    def print(self, document):
        pass
