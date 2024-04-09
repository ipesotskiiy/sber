import re
from typing import List

LEN_FIRST_PART: int = 4
LEN_SECOND_PART: int = 5


def number_validation(numbers: str, len_part: int) -> str:
    if not numbers.isdigit():
        numbers: str = re.sub(r'\D', '', numbers)

    if len(numbers) != len_part:
        needed_count_zero: int = len_part - len(numbers)
        zeros: str = '0' * needed_count_zero
        return f'{zeros}{numbers}'
    return numbers


def get_good_number(special_number: str) -> str:
    first_part, second_part = special_number.split('\\')
    return f'{number_validation(first_part, LEN_FIRST_PART)}\\{number_validation(second_part, LEN_SECOND_PART)}'


def get_special_numbers(string_with_special_numbers: str) -> str:
    parts: List[str] = string_with_special_numbers.split()
    good_numbers: List[str] = []
    for part in parts:
        if "\\" in part:
            good_number = get_good_number(part)
            good_numbers.append(good_number)
    return "\n".join(good_numbers)


string: str = input(r'Введите строку: ')

print(get_special_numbers(string))