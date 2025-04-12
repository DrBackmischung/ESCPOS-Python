import platform
import subprocess
from tempfile import NamedTemporaryFile
from typing import Optional

from escpos.pos_printer_interface import POSPrinterInterface
from escpos.pos_config import is_printing_disabled


class POSPrinter(POSPrinterInterface):
    def __init__(self, printer_name: str):
        self.printer_name = printer_name

    def print(self, document):
        if is_printing_disabled():
            print("[ESC/POS] Printing is disabled (test mode).")
            return

        data = document.to_bytes()

        with NamedTemporaryFile(delete=False) as temp:
            temp.write(data)
            temp.flush()

            command = self._build_command(temp.name)
            if not command:
                print(f"[ESC/POS] Unsupported OS: {platform.system()}")
                return

            try:
                subprocess.run(command, shell=True, check=True)
                print(f"[ESC/POS] Printed using printer: {self.printer_name}")
            except subprocess.CalledProcessError as e:
                print(f"[ESC/POS] Printing failed: {e}")

    def _build_command(self, file_path: str) -> Optional[str]:
        system = platform.system()
        if system == "Windows":
            return f'print /D:"{self.printer_name}" "{file_path}"'
        elif system in ["Linux", "Darwin"]:
            return f'lp -d "{self.printer_name}" -o raw "{file_path}"'
        return None
