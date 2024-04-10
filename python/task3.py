from typing import List


def get_max_concatenated_number(numbers: List[str]) -> int:
    numbers.sort(key=lambda x: x*10, reverse=True)
    return int(''.join(numbers))


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
