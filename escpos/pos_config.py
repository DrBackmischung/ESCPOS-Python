_disable_printing = False

def set_disable_printing(value: bool):
    global _disable_printing
    _disable_printing = value

def is_printing_disabled() -> bool:
    return _disable_printing
