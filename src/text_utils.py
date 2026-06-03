def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace in the given string.

    Example:
        normalize_whitespace("  hello   world  ") -> "hello world"
    """
    return " ".join(text.split())


def to_uppercase(text: str) -> str:
    """
    Convert the given string to uppercase.

    Example:
        to_uppercase("hello") -> "HELLO"
    """
    return text.upper()


def to_lowercase(text: str) -> str:
    """
    Convert the given string to lowercase.

    Example:
        to_lowercase("HELLO") -> "hello"
    """
    return text.lower()