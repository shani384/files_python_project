# services/front/src/front/domain/services.py
from dataclasses import dataclass

@dataclass
class ProcessFileCommand:
    filename: str
    text: str


def build_process_command(filename: str, raw_bytes: bytes) -> ProcessFileCommand:
    if not raw_bytes:
        raise ValueError("Empty file")

    try:
        text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("Invalid format (UTF-8)")

    return ProcessFileCommand(filename=filename, text=text)
