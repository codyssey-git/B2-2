"""데이터 처리를 위한 유틸리티 함수 모음입니다."""


def calculate_average(numbers):
    """숫자 리스트의 평균을 계산합니다.

    Args:
        numbers (list[int | float]): 평균을 계산할 숫자 리스트

    Returns:
        float: 숫자 리스트의 평균값

    Raises:
        ValueError: 빈 리스트가 전달된 경우
        TypeError: 숫자가 아닌 값이 포함된 경우
    """
    if not numbers:
        raise ValueError("빈 리스트의 평균은 계산할 수 없습니다.")

    for number in numbers:
        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise TypeError("리스트에는 숫자만 포함되어야 합니다.")

    return sum(numbers) / len(numbers)