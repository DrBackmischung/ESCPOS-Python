from escpos.pos_component import POSComponent
from escpos.constants import POSCommand
from escpos.pos_text import POSTextBuilder
from escpos.constants import POSPrintStyle, POSTextAlignment
from escpos.pos_linefeed import POSLineFeed

class POSDocument(POSComponent):
    def __init__(self):
        self.components = []

    def add_component(self, component: POSComponent):
        self.components.append(component)

    def add_line_feed(self, count: int = 1):
        self.components.append(POSLineFeed(count))

    def to_bytes(self) -> bytes:
        buffer = bytearray()

        # Padding hack
        filler = POSTextBuilder("").set_style(
            POSPrintStyle.BOLD, POSPrintStyle.DOUBLE_WIDTH
        ).set_alignment(
            POSTextAlignment.CENTER
        ).build().to_bytes()

        for _ in range(4):
            buffer += filler

        buffer += bytes([POSCommand.ESC, POSCommand.PAGE_MODE])
        buffer += bytes([POSCommand.ESC, POSCommand.PRINTER_RESET])
        buffer += bytes([POSCommand.GS, POSCommand.STATUS_REQUEST, 1])
        buffer += bytes([POSCommand.ESC, POSCommand.UNIDIRECTIONAL_MODE, 1])
        buffer += bytes([POSCommand.ESC, POSCommand.PRINT_PAGE_MODE])

        for comp in self.components:
            buffer += comp.to_bytes()

        buffer += bytes([POSCommand.ESC, POSCommand.PRINTER_RESET])

        return bytes(buffer)
