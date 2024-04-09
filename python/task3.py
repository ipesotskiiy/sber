from typing import List


def get_max_concatenated_number(numbers: List[str]) -> int:

    return int(''.join(sorted(numbers, reverse=True)))


numbers: List[str] = []
while True:
    new_string = input('Введите число для конкатенации, отправьте пустую строку, если хотите получить результат: ')
    if not new_string:
        break
    if not new_string.isdigit():
        print('Введите строку состоящую только из цифр')
        continue
    numbers.append(new_string)

print(get_max_concatenated_number(numbers))
