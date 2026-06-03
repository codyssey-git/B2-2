"""
값이 비어 있는지 확인합니다.

None, 빈 문자열, 공백만 있는 문자열을 빈값으로 판단합니다.

Example:
    is_blank(None) -> True
    is_blank("") -> True
    is_blank("   ") -> True
    is_blank("hello") -> False
"""

def is_blank(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip() == ""