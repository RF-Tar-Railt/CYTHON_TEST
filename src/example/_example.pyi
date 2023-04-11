def split(text: str, separates: tuple[str, ...], crlf: bool = True) -> list[str]:
    """Split text into lines, optionally removing empty lines and/or CRLF."""
    ...

def split_once(text: str, separates: tuple[str, ...], crlf: bool = True) -> tuple[str, str]:
    """Split text into two parts, optionally removing CRLF."""
    ...