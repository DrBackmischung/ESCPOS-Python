from escpos.pos_component import POSComponent
from escpos.constants import POSCommand

class POSLineFeed(POSComponent):
    def __init__(self, count: int = 1):
        self.count = count

    def to_bytes(self) -> bytes:
        return bytes([POSCommand.LINE_FEED] * self.count)
