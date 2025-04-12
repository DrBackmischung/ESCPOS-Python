from escpos.pos_component import POSComponent
from escpos.constants import POSCommand, POSQRCodeSize, POSQRCodeErrorCorrection

class POSQRCode(POSComponent):
    def __init__(self, builder):
        self.data = builder.data
        self.size = builder.size or POSQRCodeSize.MEDIUM
        self.error_correction = builder.error_correction or POSQRCodeErrorCorrection.MEDIUM

    def to_bytes(self) -> bytes:
        buffer = bytearray()

        data_bytes = self.data.encode("ascii")
        data_len = len(data_bytes) + 3
        pL = data_len % 256
        pH = data_len // 256

        # Select model
        buffer += bytes([POSCommand.GS, 0x28, 0x6B, 4, 0, 49, 65, 50, 0])
        # Set size
        buffer += bytes([POSCommand.GS, 0x28, 0x6B, 3, 0, 49, 67, self.size])
        # Set error correction
        buffer += bytes([POSCommand.GS, 0x28, 0x6B, 3, 0, 49, 69, self.error_correction])
        # Store data
        buffer += bytes([POSCommand.GS, 0x28, 0x6B, pL, pH, 49, 80, 48])
        buffer += data_bytes
        # Print QR
        buffer += bytes([POSCommand.GS, 0x28, 0x6B, 3, 0, 49, 81, 48])
        buffer += bytes([POSCommand.LINE_FEED])

        return bytes(buffer)


class POSQRCodeBuilder:
    def __init__(self, data: str):
        self.data = data
        self.size = POSQRCodeSize.MEDIUM
        self.error_correction = POSQRCodeErrorCorrection.MEDIUM

    def set_size(self, size: int):
        self.size = size
        return self

    def set_error_correction(self, ec: int):
        self.error_correction = ec
        return self

    def build(self) -> POSQRCode:
        return POSQRCode(self)
