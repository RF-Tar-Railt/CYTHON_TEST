def split(text: str, separates: tuple[str, ...] | None = None, crlf: bool = True) -> list[str]:
    """Split text into lines, optionally removing empty lines and/or CRLF."""
    ...