from escpos.pos_printer_interface import POSPrinterInterface

class POSPrinterMock(POSPrinterInterface):
    def __init__(self):
        self.buffer = []

    def print(self, document):
        data = document.to_bytes()
        self.buffer.append(data)
        print(f"[MockPrinter] Captured {len(data)} bytes")

    def get_printed_data(self):
        return self.buffer

    def clear_printed_data(self):
        self.buffer.clear()
