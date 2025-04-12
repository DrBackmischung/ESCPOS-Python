# escpos-python

A **pure Python 3** library for printing **ESC/POS receipts**, **barcodes**, and **QR codes** directly via the operating system print spooler.  
Works on **macOS**, **Linux**, and **Windows** using `lp` or `print` system commands.

---

## 🚀 Features

✅ ESC/POS command generation  
✅ Text formatting (bold, underline, alignments, double width/height)  
✅ Barcodes (EAN13, Code128, and more)  
✅ QR codes (size, error correction)  
✅ Cross-platform printing (no C extensions)  
✅ Mock printer for testing

---

## 📦 Installation

```bash
pip install escpos-python
```

> Or build from source using `flit` or `twine`

---

## 🖨️ Usage Example

```python
from escpos import (
    POSPrinter,
    POSReceiptBuilder,
    POSTextBuilder,
    POSPrintStyle,
    POSTextAlignment,
    POSBarcodeBuilder,
    POSBarcodeType,
    POSQRCodeBuilder,
    POSQRCodeSize,
    POSQRCodeErrorCorrection
)

printer = POSPrinter("Your_Printer_Name")

receipt = (
    POSReceiptBuilder()
    .set_title("ESC/POS PYTHON DEMO")
    .add_component(POSTextBuilder("Left").set_alignment(POSTextAlignment.LEFT).build())
    .add_component(POSTextBuilder("Center").set_alignment(POSTextAlignment.CENTER).build())
    .add_component(POSTextBuilder("Right").set_alignment(POSTextAlignment.RIGHT).build())
    .add_component(POSTextBuilder("Bold").set_style(POSPrintStyle.BOLD).build())
    .add_item("Item A", 3.5)
    .add_item("Item B", 5.0)
    .add_component(
        POSBarcodeBuilder("123456789012")
        .set_type(POSBarcodeType.JAN13_EAN13)
        .build()
    )
    .add_component(
        POSQRCodeBuilder("https://example.com")
        .set_size(POSQRCodeSize.LARGE)
        .set_error_correction(POSQRCodeErrorCorrection.HIGH)
        .build()
    )
    .set_footer("Thank you!")
    .build()
)

printer.print(receipt)
```

---

## 🖨️ How to Find Printer Names

### macOS / Linux
```bash
lpstat -p
```

### Windows (PowerShell)
```powershell
Get-Printer | Select Name
```

---

## 🧪 Testing with a Mock Printer

```python
from escpos import POSPrinterMock, POSReceiptBuilder, POSTextBuilder

mock = POSPrinterMock()
receipt = (
    POSReceiptBuilder()
    .set_title("Test Receipt")
    .add_component(POSTextBuilder("Line 1").build())
    .build()
)

mock.print(receipt)
print("Printed buffers:", len(mock.get_printed_data()))
```

---

## 📣 Feature Request?

This repository is only for **bug reports and maintenance** related to the language-specific implementation.

Please open all **feature requests, enhancements, and cross-language discussions** in the **central repository**:  

👉 [DrBackmischung/ESCPOS](https://github.com/DrBackmischung/ESCPOS/issues)

---

## 📜 License

MIT
