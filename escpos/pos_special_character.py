def _b(val):
    return val if isinstance(val, bytes) else str(val).encode("ascii")

POS_SPECIAL_CHARACTER = {
    "USD": bytes([0x24]),          # Dollar $
    "EUR": _b("EUR"),
    "GBP": bytes([0x9C]),          # Pound £
    "JPY": bytes([0x9D]),          # Yen ¥
    "CHF": _b("CHF"),
    "CNY": bytes([0x9D]),

    "INR": _b("INR"),
    "RUB": _b("RUB"),
    "BRL": _b("R$"),
    "ZAR": _b("R"),
    "HKD": _b("HK$"),
    "PLN": _b("zl"),
    "DKK": _b("DKK"),
    "NOK": _b("NOK"),
    "SEK": _b("SEK"),
    "ISK": _b("ISK"),
    "FOK": _b("kr"),
    "AUD": _b("A$"),
    "BSD": _b("B$"),
    "BBD": _b("Bds$"),
    "BZD": _b("BZ$"),
    "BMD": _b("Ber$"),
    "BND": _b("B$"),
    "CAD": _b("C$"),
    "KYD": _b("CI$"),
    "XCD": _b("EC$"),
    "FJD": _b("FJ$"),
    "GYD": _b("G$"),
    "JMD": _b("J$"),
    "KID": _b("$"),
    "LRD": _b("L$"),
    "NAD": _b("N$"),
    "NZD": _b("$NZ"),
    "SGD": _b("S$"),
    "SBD": _b("SI$"),
    "SRD": _b("SRD"),
    "TWD": _b("NT$"),
    "TTD": _b("TT$"),
    "TVD": _b("TV$"),
    "USD_ALT": _b("US$"),
    "ARS": _b("Arg$"),
    "CLP": _b("Ch$"),
    "COP": _b("Col$"),
    "CUP": _b("Cu$"),
    "DOP": _b("RD$"),
    "MXN": _b("Mex$"),
    "UYU": _b("$U"),
}

def get_special_char_buffer(key: str) -> bytes | None:
    return POS_SPECIAL_CHARACTER.get(key.upper())
