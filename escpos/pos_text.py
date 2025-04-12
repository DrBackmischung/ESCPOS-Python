from src.pos_component import POSComponent
from src.constants import POSCommand, POSPrintStyle, POSTextAlignment

class POSText(POSComponent):
    def __init__(self, builder):
        self.text = builder.text
        self.styles = builder.styles or []
        self.alignment = builder.alignment or POSTextAlignment.LEFT

    def to_bytes(self) -> bytes:
        buffer = bytearray()

        buffer += bytes([POSCommand.ESC, POSCommand.ALIGNMENT, self.alignment])

        for style in self.styles:
            buffer += bytes([POSCommand.ESC, POSCommand.STYLE_MODE, style])

        buffer += self.text.encode("ascii", errors="replace")
        buffer += bytes([POSCommand.LINE_FEED])

        buffer += bytes([POSCommand.ESC, POSCommand.STYLE_MODE, POSPrintStyle.NONE])

        return bytes(buffer)


class POSTextBuilder:
    def __init__(self, text: str):
        self.text = text
        self.styles = []
        self.alignment = POSTextAlignment.LEFT

    def set_style(self, *styles):
        self.styles = styles
        return self

    def set_alignment(self, alignment: int):
        self.alignment = alignment
        return self

    def build(self) -> POSText:
        return POSText(self)
