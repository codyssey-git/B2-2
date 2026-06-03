def is_blank(value: str | None) -> bool:
    if value is None:
        return True

    return value.strip() == ""