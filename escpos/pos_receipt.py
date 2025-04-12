from escpos.pos_document import POSDocument
from escpos.pos_text import POSTextBuilder
from escpos.constants import POSPrintStyle, POSTextAlignment

class POSReceipt(POSDocument):
    pass

class POSReceiptBuilder:
    def __init__(self):
        self.receipt = POSReceipt()

    def set_title(self, title: str):
        self.receipt.add_component(
            POSTextBuilder(title)
            .set_style(POSPrintStyle.BOLD, POSPrintStyle.DOUBLE_HEIGHT)
            .set_alignment(POSTextAlignment.CENTER)
            .build()
        )
        return self

    def add_item(self, name: str, price: float):
        line = f"{name.ljust(20)} {format(price, '.2f').rjust(10)}"
        self.receipt.add_component(POSTextBuilder(line).build())
        return self

    def add_item_styled(self, name: str, price: float, *styles):
        line = f"{name.ljust(20)} {format(price, '.2f').rjust(10)}"
        self.receipt.add_component(
            POSTextBuilder(line).set_style(*styles).build()
        )
        return self

    def set_footer(self, footer: str):
        self.receipt.add_component(
            POSTextBuilder(footer)
            .set_style(POSPrintStyle.UNDERLINE)
            .set_alignment(POSTextAlignment.CENTER)
            .build()
        )
        self.receipt.add_line_feed(2)
        return self

    def add_component(self, component):
        self.receipt.add_component(component)
        return self

    def add_feed(self, count=1):
        self.receipt.add_line_feed(count)
        return self

    def build(self):
        self.receipt.add_line_feed(3)
        return self.receipt
