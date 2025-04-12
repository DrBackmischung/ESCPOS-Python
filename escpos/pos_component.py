from abc import ABC, abstractmethod

class POSComponent(ABC):
    @abstractmethod
    def to_bytes(self) -> bytes:
        """Convert the component to ESC/POS bytes."""
        pass
