class POSCommand:
    ESC = 0x1B
    GS = 0x1D

    INIT = 0x40
    STYLE_MODE = 0x21
    ALIGNMENT = 0x61
    LINE_FEED = 0x0A
    FEED_LINES = 0x64
    PRINT_AND_FEED = 0x4A

    # Barcode
    BARCODE_PRINT = 0x6B
    SET_BARCODE_HEIGHT = 0x68
    SET_BAR_WIDTH = 0x77
    SET_BAR_LABEL_POSITION = 0x48
    SET_BAR_LABEL_FONT = 0x66

    # QR Code
    QR_MODEL = 0x31
    QR_SIZE = 0x43
    QR_ERROR_CORRECTION = 0x45
    QR_STORE = 0x50
    QR_PRINT = 0x51

    # Page mode & control
    PAGE_MODE = 0x4C
    PRINT_PAGE_MODE = 0x46
    PRINTER_RESET = 0x40
    STATUS_REQUEST = 0x72
    UNIDIRECTIONAL_MODE = 0x55

    # Cutter
    @staticmethod
    def full_cut() -> bytes:
        return bytes([0x1B, 0x56, 0x00])

    @staticmethod
    def partial_cut() -> bytes:
        return bytes([0x1B, 0x56, 0x01])


class POSPrintStyle:
    NONE = 0
    FONT_B = 1
    BOLD = 8
    DOUBLE_HEIGHT = 16
    DOUBLE_WIDTH = 32
    UNDERLINE = 128


class POSTextAlignment:
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class POSBarcodeType:
    UPC_A = 0x41
    UPC_E = 0x42
    JAN13_EAN13 = 0x43
    JAN8_EAN8 = 0x44
    CODE39 = 0x45
    ITF = 0x46
    CODABAR_NW_7 = 0x47
    CODE93 = 0x48
    CODE128 = 0x49


class POSBarcodeWidth:
    THINNEST = 2
    THIN = 3
    DEFAULT = 4
    THICK = 5
    THICKEST = 6


class POSQRCodeSize:
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    EXTRA_LARGE = 5


class POSQRCodeErrorCorrection:
    LOW = 48
    MEDIUM = 49
    QUARTILE = 50
    HIGH = 51
