from src.pos_component import POSComponent
from src.constants import POSCommand, POSBarcodeType, POSBarcodeWidth

class POSBarcode(POSComponent):
    def __init__(self, builder):
        self.data = builder.data
        self.type = builder.type or POSBarcodeType.CODE128
        self.width = builder.width or POSBarcodeWidth.DEFAULT

    def to_bytes(self) -> bytes:
        buffer = bytearray()

        # Set barcode width
        buffer += bytes([POSCommand.GS, POSCommand.SET_BAR_WIDTH, self.width])

        data_bytes = self.data.encode("ascii")
        buffer += bytes([
            POSCommand.GS,
            POSCommand.BARCODE_PRINT,
            self.type,
            len(data_bytes)
        ])
        buffer += data_bytes
        buffer += bytes([POSCommand.LINE_FEED])

        return bytes(buffer)


class POSBarcodeBuilder:
    def __init__(self, data: str):
        self.data = data
        self.type = POSBarcodeType.CODE128
        self.width = POSBarcodeWidth.DEFAULT

    def set_type(self, type_code: int):
        self.type = type_code
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def build(self) -> POSBarcode:
        return POSBarcode(self)
